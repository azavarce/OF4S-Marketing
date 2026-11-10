# Asset kit: the exact sounds, music, end cards, fonts and animations from the EPGD (Eric) videos

Folder layout matches the builder code. In `reference/build_reel_example.py`, set `A = <this skill>/assets/audio` and the `sfx/`, `sfx_new/` and `music/` paths resolve as they are.

## Sound effects (`audio/sfx`, `audio/sfx_new`)
| File | Used for | Level / timing used on EPGD |
|---|---|---|
| `sfx_new/justsomesounds-click-sound-432501.mp3` | Soft click when a **gold caption keyword** pops; checklist lines | 0.30 x voice peak, 0.10 s before the pop (snapped to voice onset −1 frame) |
| `sfx/swoosh05.mp3` | **Card entry** (every floating card) | 0.18 x voice peak, 0.20 s before the card |
| `sfx/pop.mp3` | **Beats inside a card** (numbers, rows, icons popping in) | 0.24 x voice peak, 0.07 s before each pop |
| `sfx/swooshriser.mp3` | **Riser into the black beat** (story-reel hooks) | starts 1.8 s before the black, peak on the black, VL−6 LUFS |
| `sfx_new/black_kumizhi-huge-cinematic-reverb-impact-506132.mp3` | **Cinematic impact on the black screen** | on the black frame, VL−3 LUFS, 1.6 s fade |
| `sfx/whoosh_ds.mp3` | **Logo end card** whoosh in | 0.22 x voice peak, 0.9 s before the end card |
| `sfx/snap.mp3` | Sharp beat (strike-through, stamp landing) | like pop |
| `sfx/ping1.mp3` | Logo/sign reveal (EPGD sign in Reel 2) | light, once |
| `sfx/thud.mp3` | **Funny moments only** (the "Dentist" stamp in Reel 7) | never on serious beats |

There is **no chime** on the OF4S logo card. Joanne removed it, so it is not included.

## Music (`audio/music`): all Pixabay
Content ID registered tracks need the License Certificate (Joanne already has the certificates for the ones marked ✔ in the EPGD Drive folder). See SKILL.md §8.

| File | Role / mood | Used in | Content ID |
|---|---|---|---|
| `nastelbom-motivation-motivation-cinematic-617063.mp3` | **Hook build**. Its hit at **33.25 s** is placed on the black beat | Hooks of Reels 1, 2, 4, 5, 6, 7, 8, 10 | Registered ✔ |
| `nastelbom-motivation-motivation-background-617070.mp3` | Calm bed. Use only the **opening phrase** (start 1.325 s, loop 8.889 s), because later parts build too much | Reel 1 bed | Registered ✔ |
| `atlasaudio-background-smooth-512254.mp3` | Steady advice bed | Reels 2, 3, 5 | Registered ✔ |
| `velariomusic-upbeat-chill-613805.mp3` | Warm and light, for **testimonials** | Reels 8, 9 (Joanne's pick) | Registered ✔ |
| `audiocoffee-sad-dramatic-background-music-short-548325.mp3` | Serious legal story | Reel 6 | Registered ✔ |
| `premiummusicodyssey-broken-halo-446240.mp3` | Dramatic story bed | Reel 7 | Not registered |
| `nastelbom-news-news-music-629329.mp3` | Newsy, serious | Reel 10 | Registered ✔ |
| `cut_nastelbom-cinematic-drive.mp3` | **"Badass"** driving bed (16–33.5 s cut of 617063) | Reel 4 (Joanne picked C) | Registered (617063) ✔ |
| `audioatlant-revolution-epic-action-cinematic-trailer-short-1-494839.mp3` | **Trailer / YouTube cold open**. Hits at ~18.3 s and ~29.7 s; the final hit lands on the title card | YouTube cold open, trailer | Registered ✔ |
| `bombinsound-podcast-music-intro-ridingx27-617282.mp3`, `bombin_16s.mp3`, `bombin_logo.mp3`, `bombinsound-...-logo-version-...-617274.mp3` | **Podcast title / showcase / end-screen** music, ducks under the conversation | YouTube full episode | Not registered (safe for YouTube) |

Bed levels used: 16–21 dB under the voice (`BEDDB`), +4 dB under the hook. It must stay audible.

## Transitions (built in code, see TECH.md)
- **Black beat ("rewind")**: 18 frames (0.6 s) of black between the hook and the story. Riser + impact play on it, and the hook-music hit lands on it.
- **Hard cut hook**: no black. The music beat lands on the guest's first word (Reel 3).
- **Zoom steps**: switch between `C` → `Ct` → `Cz` crops on key lines. Never smooth zooms.
- **Split screen** `S`: host top, guest bottom, navy seam (#15273f, 6 px), no zoom inside.
- **Cutaway**: host listening (`Gt`) to cover camera drift or a jump.
- Cards fade in and out over 0.14 s (alpha) and enter with the `IN` flip-up.

## Ready-made renders (`rendered/`)
- `of4s_endcard_vertical.mp4`: the **OF4S logo end card** for every reel (1080x1920, navy gradient, navy-300 rule, officefurniture4sale.com). Use the first 78 frames (~2.6 s).
- `of4s_endscreen_16x9.mp4`: the YouTube end screen.

## HyperFrames sources (`hyperframes/`)
- `logoend/`, `end169/`: sources for the two end cards above (edit them only if the brand changes).
- `ytshow/`: the YouTube **split-screen showcase** (name tags + "IN THIS EPISODE" topics). It still has the EPGD names, titles and topics, so replace them for each new client.
- `cards/<name>/index.html`: **every card Joanne approved**, as a style library. To reuse one, copy the folder, add `assets/` (copy `cards/_shared_assets/*` into it), change the text and the timings, and run `npx hyperframes render --format mov -o <name>.mov`.
  - Money/number comparisons: `r6money` (LOSE $250,000 vs SPEND $1,500), `r7score`, `r7math1/2`, `r7price`, `r8time` (2 h → 30 min)
  - Checklists (no background, green checks, one line at a time): `r9check`, `r10check`, `r4skills`, `r4needs`
  - Maps: `r7slider` (Florida outline), `r2map` (route + radar pulse)
  - Icons with ✕/✓: `r8school`, `r6contract`, `r7dentist` (stamp + thud), `r6bill`
  - Count-ups and grids: `r9sixteen` (floor plan filling in), `r10pages` (page stack + counter), `r8clerks` (people row)
  - Definitions / badges: `r10prose`, `r9years`, `r7years`, `r2card`, `r4who`
  - Strike-through chips: `r8jobs`
  - Photo cards (4:3 floating): `r3photo`, `r2miamiov` (photos not included; ask the client for theirs)
- `card_scripts/`: the generator (`gen_r7_with_HEAD_template.py` holds the shared HTML/GSAP template with `IN`/`OUT`/`POP`) and the per-reel card definitions (`cards8/9/10.py`).

**Rejected, so not included:** "FULL OF NONSENSE" stamp, "2018 / fully furnished", "It's been great" check, "Still in demand" list, stop sign, cartoon calendar, "SEARCHING…" label, logo chime.

## Fonts (`fonts/`)
Schibsted Grotesk 400–900 (captions use **700**, never 800/900) and Geist 400/500 (URL, name-tag titles).
