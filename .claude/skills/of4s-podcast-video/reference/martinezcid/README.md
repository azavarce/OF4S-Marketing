# Martínez-Cid tools (Nov 2026): start the next podcast from these

These are the working scripts behind the Martínez-Cid Law deliverables (8 reels, 1 testimonial, YouTube v7). They use hard-coded paths from that session (`S = .../scratchpad`). On a new podcast, **copy them into the session's scratchpad, change the paths, source file names and time ranges, and run**: do not rebuild tools from scratch.

| File | What it does | Notes |
|---|---|---|
| `audio_repair.py` | Clipping check, declip, other-camera patch for the worst seconds | **Run on day 1.** See SKILL.md §17 Sound |
| `speaker_detect.py` | Who is speaking every 0.1 s (voice classifier trained on the checked script turns) | 96% agreement on Martínez-Cid. Short turns (<2 s) → two-shot |
| `filler_cuts.py` | Finds "um/uh", stutters ("I, I", "what what") and false starts; keeps a cut only where the waveform has a real gap | Uses a filler-aware transcript (initial_prompt with "Um, uh") |
| `reel_builder.py` + `reel_config_example.json` | Vertical reel from the raw 4K cameras: one **locked** frame per camera, captions from the reel's own audio, gold keywords, clicks, music, OF4S end card, 40 ms crossfades at pause cuts | One reel per config key. Optional whip if the config has a `K` segment |
| `reel_builder_hook_whip.py` | Story reel with hook → **whip** (0.3 s slide + blur, 0.2 s hold, soft swoosh) → story | Whip rendered in RGB (yuv caused a green edge) |
| `finish_her_cut.py` | Finishes Joanne's own exported cuts: captions, gold keywords, photo cards (captions sit above them), click on photos, music or none, end card | Config in `cfg.json`, camera switches in `shotmap.json` |
| `her_cut_xfade.py` | Re-cuts her export with pause tightening, 1.1x speed and crossfaded audio | |
| `her_cut_clean_voice.py` | Rebuilds the voice of her export from the clean master (maps every 0.1 s, finds her internal edits, ±60 s search) | Verify: per-second match ≥ 0.9 and words identical |
| `youtube_builder.py` | 16:9 full episode: cold open (no line starts with "And"), title card, name tags + IN THIS EPISODE, speaker-following camera, filler cuts, chapters, SRT | Steps: `video compose audio mux srt` |
| `youtube_intro_splice.py` | Changes the intro/name tags **without re-rendering the whole episode**: re-renders the opening, cuts the old body at a keyframe with the segment muxer (frame-exact), joins with stream copy | Minutes instead of ~45 min |
| `youtube_coldopen_captions.py` | Cold-open captions transcribed clip by clip (one pass over joined clips invents "and"s) | |
| `video_desk.html` | The **Video Desk** editor artifact page (db + assets): Joanne edits captions, photos, cuts, music, notes; Claude reads `projects/<id>` and renders | Live: https://claude.ai/artifact/CujoraBYwtKc9PsBEqNUJ2 |
