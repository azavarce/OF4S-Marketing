# Re-render only the opening seconds of the body with the new "IN THIS EPISODE" box, splice onto the existing body.
import runpy, sys, subprocess, os
sys.argv=['x','plan']
S='/tmp/claude-0/-home-user-OF4S-Marketing/915db505-5c90-5c27-94f4-cf4a8187b153/scratchpad'
g=runpy.run_path(S+'/yt2/yt2_build.py'); R=g['R']; FPS=g['FPS']; SHOWF=g['SHOWF']; BODY=g['BODY']; ENC=g['ENC']
# splice point = first keyframe of the existing body after the name tags; everything after it is copied untouched (no re-encode)
kf=subprocess.run(['ffprobe','-v','error','-select_streams','v','-skip_frame','nokey','-show_entries','frame=pts_time','-of','csv=p=0','-read_intervals','%+60',R+'/body.mp4'],capture_output=True,text=True).stdout.split()
K=next(round(float(x.strip(','))*FPS) for x in kf if x.strip(',') and round(float(x.strip(','))*FPS)>=SHOWF+30)
parts=[]; H=0
for i,(s,e,l,zz) in enumerate(BODY):
    p,n=g['piece'](f"b{i:04d}",s,e,l,zz); parts.append(p); H+=n
    if H>=K: break
print('splice at frame',K)
open(R+'/h_list.txt','w').write(''.join(f"file '{p}'\n" for p in parts))
subprocess.run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',R+'/h_list.txt','-c','copy',R+'/head_raw.mp4'],check=True)
pp=subprocess.Popen(['ffmpeg','-v','error','-y','-i',R+'/head_raw.mp4','-f','rawvideo','-pix_fmt','rgba','-s','1920x1080','-r','30','-i','-','-filter_complex','[1:v]setpts=PTS-STARTPTS[o];[0:v][o]overlay=0:0:eof_action=pass:format=auto[v]','-map','[v]','-frames:v',str(K)]+ENC+[R+'/head.mp4'],stdin=subprocess.PIPE)
for fi in range(SHOWF): pp.stdin.write(g['showcase'](fi/FPS).tobytes())
pp.stdin.close(); pp.wait()
subprocess.run(['ffmpeg','-v','error','-y','-i',R+'/body.mp4','-map','0:v','-c','copy','-f','segment','-segment_frames',str(K),'-reset_timestamps','1',R+'/sg%03d.mp4'],check=True)
os.replace(R+'/sg001.mp4',R+'/tail.mp4'); os.remove(R+'/sg000.mp4')
print('tail frames',g['nfr'](R+'/tail.mp4'),'expected',g['BODY_F']-K)
open(R+'/ht.txt','w').write(f"file '{R}/head.mp4'\nfile '{R}/tail.mp4'\n")
subprocess.run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',R+'/ht.txt','-c','copy',R+'/body_new.mp4'],check=True)
n=g['nfr'](R+'/body_new.mp4'); print('frames',n,'expected',g['BODY_F'])
assert n==g['BODY_F']
os.replace(R+'/body_new.mp4',R+'/body.mp4')
for f in ['head_raw.mp4','head.mp4','tail.mp4']+[os.path.basename(p) for p in parts]: os.remove(os.path.join(R,f))
