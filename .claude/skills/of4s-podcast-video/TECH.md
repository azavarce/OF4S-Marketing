# OF4S Podcast Video: Build Recipe (technical)

This is how the EPGD reels and YouTube episode were built. The working scripts are copied in `reference/`. They hard-code the old session's scratchpad path (`S=...`), so point `S` at the new session's scratchpad and change the file names. They are examples to adapt, not a finished tool.

## 0. Setup and housekeeping
- Tools: ffmpeg/ffprobe, Python (numpy, scipy, Pillow), faster-whisper for transcripts, HyperFrames (`npx hyperframes render`) for animated cards, and Chromium (pre-installed).
- Fonts: Schibsted Grotesk woff files (400–800, from the npm `@fontsource/schibsted-grotesk` package) and Geist. Use weight 700 for captions.
- Music and SFX come from Pixabay, saved to `audiodl/music` and `audiodl/sfx`. Log every track's page URL so you can check Content ID (SKILL.md §8).
- **Disk:** the session has a fixed allowance. Delete cached segment renders (`vNN.mp4`) and intermediates (`body.mp4`, `picture.mp4`, `mix*.wav`) of reels that are finished. Never delete final deliverables or the `.mov` card renders still in use.
- **Run HyperFrames renders one at a time** (use a queue script). If several run in parallel, Chrome fails to start.
- Never kill processes with `pkill -f <pattern>`, because it can match your own shell. Check `/proc/<pid>/cmdline` first.

## 1. Sources and transcripts
1. Use the 4K originals of each camera. Convert to constant frame rate if needed. Extract the clean audio as 48 kHz WAV (`long/a1.wav` and `long/a2.wav` per recording).
2. Find the camera sync offset against the clean audio by cross-correlation. On EPGD the George camera was `GOFF = -3.25 s`.
3. Transcribe with word timestamps: `python transcribe.py audio.wav large-v3 out.json` (see `reference/transcribe.py`). Then align so that every word has `[start, end, text]`.
4. Use the transcript to find lines, and check each one against the video to see who is talking (whose mouth moves).

## 2. Segment list (`segs_rN.json`)
One entry per kept line or shot (see `reference/segs_example.json`):
```json
{"name":"S1","st":365.55,"en":371.10,"lay":"C","opt":{"oy":-170},"w":[[365.59,365.71,"Then"], ...]}
```
- `st`/`en`: times in the source audio. Each must sit in a gap between words. Check the waveform there: the cut should be in silence, after the last syllable has faded.
- `lay` (layout):
  - `C`: guest single
  - `Ct`: guest, tighter
  - `Cz`: guest, hook zoom (with `z`)
  - `G`/`Gt`/`Gz`: host
  - `S`: split screen (host on top, guest below, navy seam)
  - `shot` picks the recording when there are several.
- `opt` (options):
  - `oy` / `dx` / `dy`: framing offsets
  - `cam` + `vt`: a cutaway that borrows video from another moment while the audio stays on `st`
- `nf = round((en-st)*30)`: each segment renders to exactly that many frames.

## 3. Framing (4K guest camera, vertical 1080x1920)
Filter chain `EC(dx,dy,oy)`:
1. `crop=1600:2400:480:600+oy`
2. `rotate=-3*PI/180`, which straightens the tilted camera
3. `crop=1040:1849`
4. `scale=1080:1920`
5. HDR→SDR tonemap (`zscale…tonemap=hable`), a colour match, and light unsharp

**Head-height rule:** measure the top of the head in the rotated 1600x2400 frame for each time range. Do this with a skin-row detector, or by eye on stills, about every 30 s, because people shift during a long recording. Then set `oy ≈ headtop − 370` so the head sits at the same height in every shot.

- If someone leans out of frame, use a wider crop for that shot.
- Use the tight crop (`Ct`) only where it doesn't cut the head.
- Check desk clutter at the bottom edge.

## 4. Camera drift check
`reference/camera_drift_check.py <t0> <t1>` phase-correlates a static background patch, frame against frame minus 9. Any run of frames with a shift of 0.8 px or more is reported as camera movement. Run it over every kept segment. Cover any movement with a host cutaway (`cam:'G'`) or move the cut.

## 5. Build steps (`build_rN.py video|compose|audio|mux`)
See `reference/build_reel_example.py`.

1. **video:** renders each segment frame-exact to `vNN.mp4`. The cache is checked by frame count only, so **delete the caches when the segment order or framing changes**. It also renders the logo end card (`ENDF=78` frames, about 2.6 s) and the optional black beat (`BLACKF=18`, 0.6 s, inserted at index `HOOK`). The concat must handle `BLACKF=0`:
   `order=(parts[:HOOK]+[black]+parts[HOOK:] if BLACKF else parts)+[end]`
2. **compose:** overlays the HyperFrames `.mov` cards (alpha, 0.14 s fades, list `BRN` = (file, start time)). It also pipes a PIL-drawn caption layer (RGBA) frame by frame.
3. **audio:**
   - Voice is cut sample-exact from the clean WAV, with 12 ms fades at each cut.
   - Music is set relative to the voice loudness (`VL`). For the bed, `BEDDB`=11–16 dB under the voice.
   - SFX are scaled to the voice peak.
   - The whole mix is normalised to **−14 LUFS**, then `alimiter` at 0.84.
4. **mux:** combines the H.264 video with AAC 192k audio, writes BT.709 colour tags, and uses `+faststart`. Save each version under a new name (`OUTNAME=..._v2.mp4`).

Music env switches used on EPGD:

| Switch | What it does |
|---|---|
| `BED=<file>` | Bed track. Add `BESTWIN=1` to use the steadiest window of the track. It auto-loops on the best repeat point. |
| `BEDDB`, `DROPDB` | Bed level and the extra drop once the story starts. |
| `HOOKCIN=1 HOOKBOOST=4` | Cinematic hook track whose hit lands on the black beat, plus a riser and an impact. |
| `HOOKM=<file> HOOKDB` | A separate driving track under the hook that hands off to the bed. |
| `BEDFROM0=1 HOOKUP=4` | Bed starts at 0 and plays a few dB louder under the hook (use when there is no black beat). |

Don't change voice levels unless she asks.

## 6. Captions (inside the builder)
- `HL` = per segment `[(tokens, small_line, big_line, 'tier'|'big'|'num')]`. These are the gold keywords; everything else is plain white in chunks of 2–3 words.
- Lone one-word chunks are merged into the next chunk. Captions use sentence case.
- `NOCAP` = card windows. Captions are removed while a card is up, and a caption already showing ends when the card starts.
- Gold pops are snapped to the real voice onset (a level detector on the WAV) minus 1 frame. The click SFX plays 0.10 s before the pop.
- Layout:
  - Lower third, block centred at 62% of the height, bottom no lower than 70%.
  - Maximum width 70%.
  - In split screens, sit on the seam (centred on y=960).
  - Shadow: 9 px Gaussian blur, black at alpha 170, offset 5 px. No stroke.
- Brand spelling: merge "office furniture 4 sale" into "OfficeFurniture4Sale" in captions, chapters and SRT (`_brand()` in `reference/yt_intro_example.py`).

## 7. Cards (HyperFrames)
- `reference/cards_gen_example.py` has the HTML `HEAD` template: 1080x1920, transparent background, GSAP, the paper `.card` class and the helpers `IN` (flip-up entry), `OUT` and `POP`.
- Each card is a dict `{D: duration, CSS, BODY, JS}` holding times **relative to the card start**. Get those times from the word timestamps.
- Write each reel's cards in its own `cardsN.py` (avoids quote-nesting errors). See `reference/cards_checklist_example.py` for the no-background checklist style.
- Render each card with `npx hyperframes render --format mov -o hf/<name>.mov` inside the card folder, one at a time. Place it with `BRN=[(file, segment_offset + delay)]`, then add matching `card(name, pops=…, clicks=…)` SFX in the audio step.
- Check a still of each card over the real frame: card text needs padding, faces must stay clear, and nothing may sit outside the safe zone.

## 8. YouTube episode
- `reference/yt_intro_example.py` covers the cold-open clip list (`CL`, in master times), the trailer captions, the title-card hit (`HIT_I`), the split-screen showcase with name tags and "IN THIS EPISODE", the chapters `.txt` and the SRT.
- `reference/yt_mix_example.py` mixes the trailer music, the hit and the podcast-title music, which ducks under the conversation.
- The main body is a 16:9 two-shot plus singles with all pauses and crew talk removed. Put the captions in an SRT file instead of burning them in.

## 9. QA tools
- **Contact sheet:** take one still per segment plus one at each card's mid-point (`ffmpeg -ss t -frames:v 1`), tile them and look at the sheet before sending.
- **Cut check:** for each cut, plot or print the RMS in 10 ms steps over ±150 ms. The level should be at the noise floor at the cut point.
- **Frame-count asserts:** every `vNN.mp4` must equal `nf`, and the picture must equal `TOTALF`. Audio length must equal `TOTALF*1600` samples.
