"""Voice repair used on the Martinez-Cid podcast (Nov 2026). Run this on DAY 1, before any edit.

The master audio (George's camera, a mix of both lav mics) was CLIPPED: flat tops at full scale, worst on the
guest's loud lines. Joanne heard it as the voice "breaking". What fixed it, in order:

  1. check_clipping(master)                     -> list of heavily clipped stretches (clipped samples per second)
  2. declip(master, out)                        -> whole-file repair: -6 dB headroom + ffmpeg adeclip (rebuilds flat tops)
  3. camera_track(cam_mov, fit, t0, t1)         -> the OTHER camera's copy of the same mics (recorded ~19 dB lower, never
                                                   clipped), resampled onto master time with the measured clock drift
  4. patch(timeline, start, end, offset, ...)   -> for the worst stretches only: splice the camera copy in, tone-matched
                                                   (+4.5 dB above 3 kHz), gently compressed (not limited), level-matched,
                                                   30 ms equal-power crossfades at quiet points

Joanne preferred the declipped master overall (step 2) and the camera patch only where step 2 is not enough
(e.g. the "office furniture for less... for sale" crosstalk: 1,330 clipped samples/s). Always confirm the patched
section by transcribing the finished file, and check the true peak (<= -1 dBTP).

Measured on Martinez-Cid: client-camera time = master + (1.65329710e-05 * t + 4.86620626)  (0.4 ms residual).
Re-measure for every new shoot with fit_drift().
"""
import subprocess, numpy as np
from scipy.io import wavfile
from scipy.signal import correlate, butter, sosfilt

SR = 48000


def check_clipping(master_wav, per_second_threshold=300):
    sr, a = wavfile.read(master_wav)
    x = np.abs(a.astype(np.float32) / (32768 if a.dtype == np.int16 else 1)) > 0.99
    if x.ndim > 1: x = x.any(1)
    per = [int(x[int(t*sr):int((t+1)*sr)].sum()) for t in range(int(len(x)/sr))]
    st = []
    for t, c in enumerate(per):
        if c > per_second_threshold:
            if st and t - st[-1][1] <= 2: st[-1][1] = t + 1
            else: st.append([t, t + 1])
    return [(a_, b_, max(per[a_:b_])) for a_, b_ in st], per


def declip(master_wav, out_wav):
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', master_wav, '-af',
                    'volume=-6dB,adeclip=threshold=1:hsize=1000:method=s', '-c:a', 'pcm_f32le', out_wav], check=True)


def fit_drift(master, cam, probes, approx_offset, win=4.0):
    """master, cam: mono float arrays at SR. Returns (slope, intercept): cam_time = t + slope*t + intercept."""
    pts = []
    for t in probes:
        x = master[int(t*SR):int((t+win)*SR)]; w = int(0.08*SR); o = approx_offset
        y = cam[int((t+o)*SR)-w:int((t+o)*SR)+len(x)+w]
        if len(y) < len(x)+2*w: continue
        cc = correlate(y, x, mode='valid'); k = int(np.argmax(cc))
        nc = cc[k]/np.sqrt((x**2).sum()*(y[k:k+len(x)]**2).sum()+1e-12)
        if nc > 0.4: pts.append((t+win/2, o+(k-w)/SR))
    P = np.array(pts); return tuple(np.polyfit(P[:, 0], P[:, 1], 1))


def camera_track(cam_mov, fit, t0, t1, channel=1):
    """The other camera's audio for master time t0..t1, resampled onto master time (drift-corrected)."""
    slope, icpt = fit; f = lambda t: slope*t + icpt
    cs = t0 + f(t0) - 0.5
    raw = np.frombuffer(subprocess.run(['ffmpeg', '-v', 'error', '-ss', f'{cs:.4f}', '-t', f'{t1-t0+1:.3f}', '-i', cam_mov, '-vn',
                        '-af', f'pan=mono|c0=c{channel}', '-ar', str(SR), '-f', 'f32le', '-'], capture_output=True).stdout, np.float32)
    t = np.arange(int((t1-t0)*SR))/SR + t0
    return np.interp((t + f(t) - cs)*SR, np.arange(len(raw)), raw).astype(np.float32)


def patch(timeline, a0, a1, offset, cam, cam_t0, master_dc, ref_after=(None, None)):
    """Replace timeline[a0:a1] (seconds, in the edit's own time) with the camera copy.
    offset: master_time = edit_time + offset for this stretch (one continuous take).
    cam: camera_track() output starting at master time cam_t0.  master_dc: declipped master (for level/scale)."""
    y = timeline.astype(np.float32)
    # tone match + scale to the edit's level
    hp = sosfilt(butter(2, 3000, 'hp', fs=SR, output='sos'), cam); c = cam + hp*(10**(4.5/20)-1)
    ref = master_dc[int((a0+offset-1.5)*SR):int((a0+offset-0.5)*SR)]
    sc = np.std(y[int((a0-1.5)*SR):int((a0-0.5)*SR)]) / (np.std(ref)+1e-9)
    pad = int(0.5*SR); i0c = int((a0+offset-cam_t0)*SR); n = int((a1-a0)*SR)
    ext = c[i0c-pad:i0c+n+pad] * sc * np.std(ref)/(np.std(c[i0c-pad:i0c+pad])+1e-9)
    pk = np.abs(ext).max()
    p = subprocess.run(['ffmpeg', '-v', 'error', '-f', 'f32le', '-ar', str(SR), '-ac', '1', '-i', '-', '-af',
                        'acompressor=threshold=0.12:ratio=4:attack=4:release=90:knee=4:makeup=1', '-f', 'f32le', '-'],
                       input=(ext/pk*0.9).astype(np.float32).tobytes(), capture_output=True)
    seg = np.frombuffer(p.stdout, np.float32)[:len(ext)]*pk/0.9; seg = seg[pad:pad+n]
    r0, r1 = ref_after
    if r0 is not None:   # match the loudness of the lines right after the patch
        seg *= np.sqrt(np.mean(y[int(r0*SR):int(r1*SR)]**2))/np.sqrt(np.mean(seg**2))*10**(0.7/20)
    XF = int(0.03*SR); fi = np.sin(np.linspace(0, np.pi/2, XF)); fo = np.cos(np.linspace(0, np.pi/2, XF))
    i0 = int(a0*SR); i1 = i0+len(seg); out = y.copy()
    out[i0:i0+XF] = y[i0:i0+XF]*fo + seg[:XF]*fi
    out[i0+XF:i1-XF] = seg[XF:-XF]
    out[i1-XF:i1] = seg[-XF:]*fo + y[i1-XF:i1]*fi
    return out


def quiet_point(y, t0, t1):
    """Quietest 10 ms point between t0 and t1 (put splices and cuts there)."""
    n = int(0.01*SR); ts = np.arange(t0, t1, 0.01)
    v = [20*np.log10(np.sqrt(np.mean(y[int(t*SR):int(t*SR)+n]**2))+1e-9) for t in ts]
    return float(ts[int(np.argmin(v))])
