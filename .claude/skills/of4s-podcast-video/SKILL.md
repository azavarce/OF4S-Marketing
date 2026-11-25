---
name: of4s-podcast-video
description: Edit an OF4S client podcast into a YouTube full episode and vertical short clips (Instagram Reels, TikTok, YouTube Shorts) using the rules Joanne approved on the EPGD Law and Martínez-Cid Law podcasts, with the saved tools in reference/. Use for any OF4S podcast / interview / testimonial video edit: audio check and repair, clip topics, cut script, hooks, framing, captions, photos, music, SFX, end card, YouTube intro/chapters/captions, the Video Desk editor, the final quality gate and client review.
---

# OF4S Podcast Video Playbook

Everything below was decided with Joanne (OF4S marketing) while editing the EPGD Law podcast (Eric Gros-Dubois x George Dargham, Nov 2026). Follow it from the first edit so she does not have to repeat feedback. `TECH.md` in this folder has the build recipe. **`assets/` holds the exact sounds, music, end cards, fonts and approved animation templates from the EPGD videos — use these by default (catalogue in `assets/README.md`); only look for new music/SFX when Joanne asks or the mood needs something different.**

Updated after the Martínez-Cid Law podcast (Nov 2026): **§17** lessons, **§18** the 3-day workflow, **§19** the final gate every file must pass before it is sent (zero mistakes, professional), **§20** the shoot checklist for George. The working tools are in `reference/martinezcid/`.

---

## 1. How to work with Joanne (process rules)

1. **Send the script before you edit.** For every reel: list the exact lines in order (speaker, quote), mark what is kept / cut, and get her OK. Do not render first and ask later.
2. **Do not apply big changes without her OK.** Proposals first; build after she says go.
3. **Apply ALL changes for a reel in one pass** — cuts, transitions, captions, animations and their sounds, music. She should never have to repeat a note.
4. **Send finished videos one by one**, as each finishes, with a short list of what changed. Re-check the frames yourself before sending.
5. **Never invent facts, quotes or numbers.** Only words the speakers actually say. A text hook or title card is fine if it is clearly a question/title, never presented as a quote.
6. **Verify who is speaking** before attributing a line (check the video: whose mouth moves). Do not guess.
7. **Keep old versions** (save as v2, v3…) when making a new one; never overwrite the only copy of something she approved.
8. **Long renders:** tell her roughly how long, and say so if something failed. Watch the disk (clean old drafts/intermediates, never final deliverables).
9. **Never paste API keys or secrets in chat.**

## 2. Intake for a new podcast

Collect before editing:
- Raw camera files for each person (each angle), the clean audio, and the names + exact titles of everyone on camera (e.g. "Founding Partner, EPGD Business Law"; "CEO, OfficeFurniture4Sale").
- How the client's firm/company name must be written on screen.
- Any photos/logos she wants to use (client logo, office photos). Ask; do not pull random images.
- Make a word-level transcript (forced alignment) of every source so every cut lands between words.

Then propose a **topic list** for reels (one idea per reel), each with a 1-line why. Skip topics that are generic, inside-history, or not useful to business owners (she rejected "leadership: make more mistakes" and "how they met"). Remove topics she doesn't like without arguing.

## 3. Cutting rules

- **Never clip a word.** Check the waveform at each cut: end after the last syllable fades, start before the first one. If two words run together with no gap, keep both rather than clip one.
- Cut pauses, stutters, "you know"/filler restarts and false starts, but keep natural rhythm. Cut crew talk/outtakes.
- Cut the interviewer's filler reactions ("OK", "Right", "Wow") unless they add something; keep a short reaction ("That's insane") when it lands.
- Don't repeat a line that is already in the hook immediately after it; a repeat later in the story is OK.
- Drop lines that **answer a different question** than the one shown (e.g. a question about the company answered with an unrelated point — move that to its own reel).
- Boring details out (financing terms, percentages down, banker names) unless she asks; keep strong concrete numbers that matter to the viewer (e.g. "$250,000 vs $1,500", "16 offices").
- Story must make sense on its own: give **context for why** before the advice (e.g. his own experience → the lesson). If a reel "doesn't make sense", fix the order (story first, then advice) rather than adding effects.
- Target lengths: reels ~35–60 s (up to ~1:50 for a strong story), trailer 20–25 s.

## 4. Hooks

- **Advice reels:** open on the strongest line (or the host's question when it is short and specific to business owners). A broad or off-target question (e.g. "is it a challenge to law firms like yours?") is a weak opener — start with the guest instead.
- **Story reels:** 2–3 short lines as a build-up → **0.6 s black screen** ("rewind") with a cinematic hit → story starts from the beginning.
- Hook lines must be the guest's real words. If the best hook is an idea he never says, use an **on-screen text question** (e.g. "Wrote your contract with ChatGPT?"), clearly a title, not a quote.
- Testimonials can skip the hook and open on the host's question.
- No transition effects inside the hook.

## 5. Framing & camera (vertical 1080x1920)

- Use the **highest-resolution original** of each camera (4K), not proxies.
- **Straighten** tilted cameras (measure the tilt; we used −3°).
- Frame **tighter, with less desk clutter**; keep the full head in frame, with the head in the upper part of the frame but **not cut** and not pushed into the bottom half. Measure head position per time range — people shift during a long recording — and re-frame each range so the head sits at the same height in every shot.
- Hook shots may be slightly more zoomed than the body.
- When the speaker leans out of frame (e.g. reaching for a document), use a wider crop for those shots rather than cutting him off.
- **No camera movement visible.** Check every shot for camera drift/pan (measure on a static background area, not on the person). Cover drifting moments with a cutaway of the other person listening.
- **Never show the host looking down** (except the very opening). No auto face-crop.
- Split screen (host top / guest bottom, navy seam) is good for reactions and for exchanges; no zoom inside split screens.
- One framing per line; zoom steps (not smooth zooms) only on key lines.
- **Lighting / exposure (check on day 1, before any edit).** Pull stills of both cameras (faces, skin, background) and check the exposure. If the footage is dark, correct it so faces look **bright, natural and well lit**: lift exposure, shadows and midtones gently; keep skin tones natural and warm; keep real blacks (no washed-out grey look); don't add visible noise or blow out highlights and windows. **Match both cameras** to each other and to the look of the earlier OF4S podcasts. Use **one correction per camera for the whole podcast** (same on every reel and the YouTube episode). Check a contact sheet of every shot before rendering, and again on each finished file. With the first delivery, send one **before/after still** of the correction.
  - **Settings already approved (start from these, then adjust to the new footage):** iPhone footage is HDR: always convert HDR to SDR first (`zscale … tonemap=hable:desat=0 … bt709`), or it looks flat/grey.
    - **EPGD Law** (`reference/build_reel_example.py`): guest camera `colorchannelmixer=rr=1.049:gg=1.057:bb=1.110,eq=saturation=1.153`; George's camera matched to it with `lutrgb` per-channel levels (`GGo`).
    - **Martínez-Cid** (`reference/martinezcid/reel_builder.py`, `youtube_builder.py`): `eq=brightness=0.015` after the tonemap; on Joanne's own cuts `eq=brightness=0.035:contrast=1.04:saturation=1.08` and a `lutrgb` match for the other camera (`finish_her_cut.py`).
    - These are per-shoot values, not one fixed preset: measure face brightness/skin colour on stills of both cameras, compare with an approved EPGD/Martínez-Cid still, and set the values so they match.

## 6. Captions

- Font: **Schibsted Grotesk Bold/SemiBold** (never ExtraBold/Black). White. **No outline/stroke ever**; soft dark shadow only.
- Base 64 px; **keywords in gold #F6B560 at ~1.6x**, max width 70% of the frame. Use **two-tier** (small line over BIG gold line) only on key phrases/numbers. No dark boxes behind words.
- 2–3 words per caption chunk; sentence case; correct spelling of names/brands.
- Position: lower third, block centred ~62% height, bottom ≤ 70%. Stay inside IG/TikTok safe zones (top 220, bottom 480, left 60, right 140 px). **Never cover faces.** In split screens, sit on the seam.
- Captions **pause while an animation card is up**; a caption already showing ends when the card starts.
- **Brand spelling:** always "OfficeFurniture4Sale" (one word, with 4) in captions and SRTs. The generic phrase "office furniture" stays lowercase.
- A soft click plays only when a gold keyword pops, snapped to the actual voice onset (−1 frame).

## 7. Animations / cards

- **Only where they add something.** No literal "illustrate the word" animations (rejected: a "FULL OF NONSENSE" stamp, a "2018 / fully furnished" card, an "It's been great" check, a "Still in demand" list, a stop sign, a cartoon calendar). Fewer is better; zero is fine.
- Style: **floating cards over the speakers in the lower part of the frame, below the faces** (not full screen). Paper card (#faf8f4), navy text (#15273f), Schibsted Grotesk; red #d64545 for losses/✕, green #2fb36a for wins/✓.
- **Checklists: NO background at all** — white text with soft shadow, green check icons, lines appear **one at a time** as he says each item.
- Everything is timed to the exact word (number pops on the number, ✕ on "no", etc.). Each card gets its own subtle sounds (swoosh in, pop/click on beats).
- Photos as **4:3 floating cards**, not full screen.
- Maps/diagrams: clean, on-brand; no extra labels that state the obvious (rejected "SEARCHING…").
- Keep enough padding inside pills/badges so text never touches the edge.

## 8. Music & sound effects

- Music stays **low under the voices** but must be **audible** (a bed nobody can hear is a bug). Under the hook it can be a few dB louder.
- **Two tracks per reel** when it helps: a cinematic build under the hook whose **hit lands on the black screen**, then a bed under the conversation.
- Match the mood and pace: advice reels → steady/serious (no motivational "building" music); testimonials → warm/light; serious legal stories → dramatic; "badass" energy when she asks for it. When she doesn't like a track, send **3 short (20 s) previews (A/B/C)** and let her pick.
- SFX: soft click on gold keywords; swoosh on card entries; pops on card beats; riser + cinematic impact into the black beat. **The "thud" is only for funny moments.** No chime/ding on the OF4S logo card.
- **LICENSING (standing rule):** every time you use a NEW music track, check its Pixabay page for **"Content ID Registered"**. If registered, **remind Joanne to log in to Pixabay and download that track's License Certificate** (.txt, from the "Download" dropdown on the track page) and keep it with the videos. Only Content ID tracks have certificates. Prefer non-registered tracks for the YouTube full episode. Claims are disputed in YouTube Studio → Checks → Dispute → License → paste certificate.
  - **Non-registered tracks can still be claimed by third parties.** Example: BombinSound #490524 was claimed by HAAWK on the EPGD YouTube episode. In that case there is no certificate, so dispute with **License** and paste the Pixabay track URL + https://pixabay.com/service/license-summary/ as the rationale. Never appeal a rejected dispute (that risks a strike); mute or replace the segment instead.

## 9. Branding & end card

- Design system v3 (`design-system/`): navy-800 #15273f, navy-900 #0f1d33, navy-700 #1e3554, navy-300 #8fa9c7, navy-100 #dde5ee, paper-50 #faf8f4; Schibsted Grotesk display, Geist body.
- Every reel ends on the **OF4S logo end card** (navy gradient, navy-300 rule, Geist URL officefurniture4sale.com), ~2.6 s, with a whoosh in and no chime.
- Name tags: navy box, navy-300 accent bar, name in Schibsted, title in Geist.
- **Guest NAME CARD (approved, use exactly this whenever Joanne asks for a "name card"):** run `reference/namecard.py in.mp4 out.mp4 "<Name>" "<Title, Company>"`. Spec, 1080x1920:
  - Centred navy box (#15273f at ~92% opacity), corner radius 28, soft drop shadow. Height 196; width = longest line + 55 px padding each side. Top edge at **y = 1490**, which leaves a gap between the captions and the card for the Instagram link sticker.
  - Two lines only: **name** in Schibsted Grotesk 700, 74 px, white; **title + company** in Geist 500, 38 px, navy-100 (e.g. "Founding Partner, EPGD Business Law").
  - **No "Episode N" label.**
  - Visible from the **first frame** (no fade-in), held to 3.4 s, then a 0.35 s fade-out.
  - Don't change the size or position unless she asks.

## 10. YouTube full episode

- 16:9, side-by-side two-shot + singles, all pauses/crew talk removed; same colour fixes as the reels.
- **Trailer-style cold open (~20–30 s):** 7–9 of the strongest lines that warn business owners about mistakes, mixing topics; white captions in the reel style with gold keywords; trailer music with a big hit mid-way and the final hit on the title card. Joanne picks/reorders the lines — offer a numbered list of candidate sentences.
- Title card (~3 s) hard-cuts in on the music hit.
- **Split-screen showcase** of host + guest (~5 s): navy divider, name tags slide in, then an "IN THIS EPISODE" band with 3–4 topics popping in one by one; podcast title music starts here and ducks under the conversation.
- Don't repeat name tags right after the showcase.
- Deliver **chapters (.txt)** and a **captions file (.srt)** for upload (do not burn captions into the whole episode). End screen ~20 s.

## 11. QA before sending anything

**Run the full §19 gate on every file.** The list below is the minimum.

- [ ] Every cut: no clipped word at start/end (waveform + listen points).
- [ ] Heads uncut, consistent height, no desk clutter, nobody looking down, no camera drift.
- [ ] Captions: correct words/spelling/brand, inside safe zones, no face covered, paused under cards.
- [ ] Cards land on the right words; card text has padding; no unnecessary card.
- [ ] Music audible but under the voice; hit lands on the black; no clash; logo card silent except whoosh.
- [ ] New music tracks → Content ID checked → certificate reminder given.
- [ ] Contact sheet of frames reviewed before sending.

## 12. Client review email (short)

> Subject: Podcast videos for your review
>
> Hi [Name],
>
> Thank you again for joining George on the podcast!
>
> In the folder below you'll find the full video, plus short clips we've put together for Instagram, TikTok and YouTube Shorts. We'll be choosing which ones to post from these, so not all of them will necessarily go live.
>
> [Google Drive link]
>
> Please take a look and let us know if there's anything you'd like changed, or anything you'd prefer we not post.
>
> Thank you!
>
> Best,
> Joanne

Share the Drive folder with the client's email as Viewer/Commenter; keep only the videos to review inside it (sharing a subfolder does not expose the parent).

**Follow-up if the client hasn't replied** (keep it polite and calm — never an ultimatum, never "otherwise we'll go ahead"; give a soft date a couple of days out, not "tomorrow"):

> Hi [Name],
>
> I hope you're doing well! I just wanted to follow up on the podcast videos I sent over last week.
>
> We're aiming to start sharing the clips by [Thursday], so please let us know before then if there's anything you'd like changed or would prefer we not post.
>
> Here's the folder again for easy access:
> [Google Drive link]
>
> Thank you!
>
> Best,
> Joanne

Reply on the original email thread. Joanne prefers short, plain sign-offs ("Thank you!", "Thanks again.") over gushy ones.

## 13. Quality bar — mistakes Joanne has already caught (check EVERY one before sending)

**Cuts & hooks**
- **Never clip a word, including at the end of a line** ("…I don't fully *trust*", "What's your *niche*?"). After building, **transcribe the rendered output around every cut** and confirm the first and last word of each segment are complete. Waveform alone is not enough.
- Never cut **inside a sentence** to save time (e.g. removing "super pro-employer state and a" from "Florida is a super pro-employer state and a pro non-compete state"). Use the whole sentence or a different line.
- **Pause cuts are smooth:** same framing on both sides (soft cut / short crossfade), **no zoom in or out** at a pause cut. Zoom steps are only for new lines.
- **Hooks with judgment, not by formula.** The black-screen "rewind" is only for a real story with a build-up. If the host's question is the natural opener ("What's your niche?", "Corporations by law are required to…"), **start with the host's question** and keep it whole. Ask yourself: does a stranger understand the first 3 seconds?
- **Every trailer/hook line must make sense on its own.** No lines with an unexplained "he" or "it" ("Now he can do it on his own using ChatGPT", "You can't afford not to have it"). Add a context line before a story line when needed (e.g. "Florida is a pro non-compete state" before the non-compete story).
- **Nothing extreme or misleading** out of context (rejected: "ChatGPT is making up cases that don't exist"). Host lines in a guest trailer must connect to what the guest says, or drop them.

**Framing**
- **Don't over-zoom the host** (George). Head and shoulders, with some chest visible, like the guest framing. Check a still of every shot.
- Keep the head at the same height across neighbouring shots. No empty wall above the head, no head cut at the top.

**Music**
- **Match the music to the content of each reel**, not to the series. Success stories and "getting clients results" → confident/uplifting, **never sad**. Sad/dramatic only for a genuinely bad-outcome story. When unsure, send A/B/C previews before rendering.
- In trailers/montages, **never carry over music from a reel's audio** (clips cut from finished reels bring their bed with them; use the raw camera audio).

**Captions**
- Centred (x = 540) and inside the safe zone, verified by measuring the rendered overlay, not by eye.
- Captions/text must **never overlap photo cards**; raise the caption above the cards while they're up.
- No lone one-word caption chunks (merge them); no double spaces.

**Covers (Instagram)**
- Approved style: **split screen** (George top, guest bottom, navy seam), title on the **guest's half**, left-aligned, white line + gold line, **subtle navy shade**, **no logo**, both faces inside the 3:4 grid crop (y 240–1680). Text may touch the top of the guest's head slightly.
- Use frames where both people look **engaged, not frowning**, with mouths closed or mid-natural-expression. Use a **different frame for each reel**.
- Title = a short title, **not a fake quote**. Avoid leading with numbers unless she asks. Don't change the text size unless asked.
- When she dislikes a frame, offer 3 alternatives side by side.

**YouTube thumbnail**
- 1280x720. Host and guest **cut out, large, at the edges, facing each other**, placed symmetrically (same distance from each edge so lighting/shadow is even). **Dark moody background** (blurred OF4S install photo, darkened) with edge vignette. Brightened faces.
- **3–5 words stacked in the centre**, one word in a **gold box with navy text**. Thumbnail text complements the title, doesn't repeat it. Nothing in the bottom-right corner (timestamp).
- No reaching arms or limbs touching the other person — pick frames with arms crossed or close to the body.

**Language & legal**
- Never call a lawyer (or any guest) an "expert", "specialist" or "the best" in captions, titles, covers or posts (Florida Bar rules). Use their actual title.
- No outcome claims a guest didn't make ("cost him $250,000" when he said "put $250,000 a year at risk").
- Get the guest's OK on the YouTube title/thumbnail before publishing.

## 14. Captions across a series (Instagram, LinkedIn: George's page and the OF4S page)

Several clips from the same episode go out over a few weeks, so **captions must not sound repetitive**:
- Before writing a caption, **look at the captions already posted for that episode** (ask Joanne or check this thread) and don't reuse the same hook structure, the same credit phrase or the same CTA.
- Rotate hooks: a question / the guest's own line / a turning point / a surprising fact / a short lesson.
- Rotate how the guest is credited. Say "my friend and client" at most once per episode. Otherwise use "Eric Gros-Dubois of EPGD Business Law", "Eric", "our first guest", etc.
- Rotate CTAs: "Watch the full episode: [link]" / "Full conversation here: [link]" / "Hear the rest of the story: [link]" / "The whole episode is up: [link]" / Instagram: "Watch the full story at the link in bio."
- Rotate hashtags slightly per post (keep 2–3 core tags, swap the topic tags).
- Each caption says what **this** clip is about, not a summary of the whole episode (the full-episode post already did that).
- George's page = his voice (short, upbeat, personal). OF4S page = brand voice, more official. Never post the same clip on both pages on the same day.

## 15. Outside producer's feedback (on EPGD Reel 1 "networking" + George's series trailer)

Reel 1 was the earliest edit and used the most B-roll; later reels already used much less. These rules apply to every edit from now on:

**Audio**
- **No distorted / saturated voice.** The producer heard the voice "breaking" in Reel 1 and in George's trailer. Every build: check the source WAV for clipped samples (flat tops near 0 dBFS) and the output for distortion; use a **true-peak limiter at about −1 dBTP**, not a hard limiter pushing into distortion; if the source itself clipped, use a declipper or pick a cleaner take. Listen to the loudest lines on headphones before sending.
- **No people talking over each other.** Cut overlaps so only one voice is heard at a time; drop a line rather than keep crosstalk. Lines where the audio isn't clear are cut.

**Transitions**
- **No plain black screen.** A black frame after the hook reads as empty to a viewer. For a story-reel "rewind" beat, use a quick hard cut or a ~0.5 s **OF4S logo flash** (navy, like the end card) instead of black.

**B-roll & animations**
- **No AI-looking or generic stock B-roll** (rejected: unclear "billboards" shot, a "free networking group" of random people, one dressed like a farmer). If B-roll is used at all, it must be **from OF4S's world**: real OF4S installs, the showroom, the team, the client's office. When in doubt, stay on the speaker.
- **No literal "illustrate the sentence" animations** (rejected: an empty chair with a question mark for "imaginary boss").
- When showing a room/space (e.g. "invited to be on the board"), **use a real OF4S install photo**. That's a chance to show the work.
- Diagrams that explain an idea (the word-of-mouth diagram) are good; give them enough screen time to read (slightly longer).

**Set & filming (pass these to George before each shoot)**
- **Clean, spotless set.** "You sell furniture, it has to be impeccable." Clear the desk of cards, pens, remotes, old calculators, cups. Frame to show good furniture and hide clutter; in edits, crop tighter or blur/cover clutter that's left in.
- Shoot at the client's office when it's OF4S furniture, and **make the furniture look great**. It's free proof of OF4S's work.
- **George shouldn't read questions on camera.** Keep them on the table out of frame, glance down briefly, and look at the guest while asking.
- Avoid talking over the guest during recording (leave a beat before reacting).

## 16. Transitions (approved Nov 2026, replaces the black "rewind" beat)

- **Never a black screen** between hook and story.
- **Default transition = the WHIP** (Joanne's choice): 0.3 s horizontal slide with motion blur (`xfade=slideleft` + horizontal blur) and a soft whoosh (`whoosh_ds.mp3`), the music hit in the middle of the whip.
  - **Breathing room:** the speaker finishes his last word, holds on screen **0.2 s**, then the whip starts. The next speaker starts talking **0.1 s after** he's fully on screen. Keep ~0.4 s of extra footage before his first word so his lips stay in sync. The whoosh never overlaps a word.
  - Voices are never blended across the whip.
- The white flash was shown as an alternative; use it **only if Joanne asks**.
- **Words are never cut at a transition.** Find the real silence before the first word and after the last word on the waveform (10 ms steps). If two words run together with no gap (e.g. "And you…"), keep both. After rendering, **transcribe the finished file** and confirm every word is complete before sending. Always build from the original camera audio, never by cutting a finished reel (its mixed music hides the gaps between words).
- **Animations and effects must never be literal or gimmicky** (the producer's feedback): no illustrating the sentence (empty chair for "imaginary boss", stamps, random icons), no AI-looking stock. Only add a card/diagram when it **explains** something (numbers, a comparison, a process, a checklist), or a **real OF4S photo** when a space is mentioned. When in doubt, stay on the speaker.
- Reference build: Reel 8 hook → George's question, rebuilt from the raw 4K cameras (Eric 539.00–544.02 in "Shot 2 Client.MOV", George 499.95–501.52 + 502.36–505.98, George video offset −3.25 s).

## 17. Lessons from the Martínez-Cid Law podcast (Nov 2026)

Tools for everything below are in `reference/martinezcid/` (see its README). Start from them; don't rebuild.

**Sound: check it before anything else**
- Run `audio_repair.check_clipping` on the master on day 1. Martínez-Cid's master (George's camera) was **clipped**; Joanne heard it as the voice "breaking", worst on the guest's loud lines.
- Default fix: **declip the whole master** (−6 dB headroom + `adeclip`). Where it is still bad (hundreds of clipped samples per second, crosstalk), **patch those seconds with the other camera's copy** of the mics: drift-corrected, tone-matched (+4.5 dB above 3 kHz), gently compressed (never a hard limiter), level-matched, 30 ms crossfades. Joanne rejected the camera copy for a whole video (a bit duller) but loved it as a patch.
- **Pause cuts never dip to silence**: 40 ms equal-power crossfade between the two takes.
- Final mix: −14 LUFS, limiter set low enough that the **true peak is ≤ −1 dBTP** after AAC (check with `ebur128=peak=true`).
- **Joanne's own exported cuts can carry the clipped audio** (her 04 "Client GPT" export was loud and broken). Rebuild their voice from the clean master with `her_cut_clean_voice.py` and confirm the words are identical.

**Cuts**
- A word's ending runs past where the waveform looks done (the "-st" of "trust", "-che" of "niche", "-tion" of "retention"). End a line 0.15–0.25 s after the visible end, at the next real silence, then **transcribe the finished file** and read every first and last word.
- The transcriber **invents words at clip starts** ("And", "So", "Thank you", "Microsoft"). Check against the waveform before believing it, and fix captions by hand.
- Remove stutters ("I, I represent", "there was, there was a", "what what what"), "you know", "um", throat noise and coughs. Keep emphatic repeats ("really, really", "It's odd. It's odd.").
- Never leave a lone word of the next speaker in a caption ("…or the oddest? I").

**Framing**
- **One locked frame per camera for the whole reel.** Re-centering per piece made the frame jump in/right/left inside one sentence, and Joanne hated it. No zoom steps at pause cuts.
- YouTube: George framed like the guest (head and shoulders, not over-zoomed), **both heads at the same height** (about 15% from the top), no empty wall above the guest.
- YouTube camera follows the speaker via `speaker_detect.py` (voice classifier, 96% vs the checked script). Turns under 2 s → two-shot. George's framing only changes at a camera switch.

**Structure & content choices Joanne made**
- Hooks only when they serve the story. Often **George's question is the opener** ("What would you say was the craziest case…", "Corporations by law are required…", "Tell me the type of clients…"). Her employees reel: no hook at all ("it makes the video longer").
- Cold open: no line starts with "And"; a punch line gets a short pause before and after; no line that needs context; she removed "My niche is the weird" in the end.
- Name tags on YouTube: **big text** (52 px name / 30 px title at 1920 wide), long boxes, ~9 s on screen. Topic wording: **send 3–4 options before rendering** (she rejected "Money vs. vibes" and "Keeping great people"; chose "Starting his own firm × Hiring the right people × AI and the courts").
- Client names a guest drops on camera (e.g. a former head of state) stay out unless Joanne/the guest OKs it.

**Music & SFX**
- Match the mood of each video: mysterious/investigative for "craziest case" (not sad piano), upbeat for success stories. Offer A/B(/C) versions of the same edit when unsure.
- **Duck the music (−5 dB) once the host's question ends** and the guest starts answering.
- Click sound for cards and photos (no bubble pop, no snap). Whip: soft `swoosh05` only (she disliked whoosh + impact on the whip).
- Testimonial with captions + photos only: no music unless she asks.

**Photos & captions**
- Real OF4S install photos from the client's blog post (Odoo `blog.post`), matched to what's said (chairs → conference table, "war room" → conference room, standing desks → office desk). Click sound on each. **Captions move above a photo card** while it's up; never hidden.
- Quotes in captions get quote marks ("“Brevity is the soul of wit”"). "err on the side of" is spelled *err*.

## 18. Fast workflow: one podcast in 3 days

| Day | Claude | Joanne |
|---|---|---|
| Before the shoot | Send George the shoot checklist (§20) | Forward it |
| 1 | Download sources; **audio check + repair**; transcript (+ filler-aware transcript); speaker detection; head tracks; **lighting/exposure check + correction (§5)**; propose 8–10 clip topics as **one script document** (exact lines in order, hooks/openers, A/B/C music per clip, YouTube cold-open candidates, topic wording options) | Approve or adjust everything in one pass |
| 2 | Build all reels + the YouTube episode with the saved tools, in one pass each; run the §19 gate on every file; upload previews to the **Video Desk** (`reference/martinezcid/video_desk.html`, one project doc per video) | — |
| 3 | Render final versions from her Video Desk edits/notes; upload full quality to Drive | Review in the Video Desk: fix small things herself, leave notes for bigger ones, mark ready |

Efficiency rules: one 4K render at a time (parallel 4K jobs ran out of memory); keep ≥10 GB disk free; keep the YouTube episode in sections and change the intro with `youtube_intro_splice.py` (keyframe cut, no full re-encode); don't re-transcribe an unchanged body (shift the old SRT/chapters instead). Review copies < 380 MB (2.4 Mbps); full masters go to Drive.

**Every fix goes into this skill, the same day.** Anything Claude fixes, whether Joanne asked for it or not (a setting, a workaround, a tool limit, a bug in a script), is written here with the values and the script it lives in, at the time of the fix, and pushed. Before closing a podcast, go through every builder script once more and make sure no setting lives only in code. See §21.

**How to talk to Joanne**: short bullets plus **one table** (# / video / version / what changed / what I need from you). Files named `<Client>_<##>_<Topic>_v<N>.mp4`; the number never changes, only vN. When she asks a question mid-render, answer first. If her message is ambiguous ("try"), state the reading and act on it.

**Her CapCut cuts**: useful when she has already chosen the lines (it replaces the script step). Ask for exports with the **original audio untouched** (no auto-enhance/volume boost/noise reduction), highest quality, and no captions or music; or her cut points. Her audio still gets mapped to the clean master.

## 19. Final gate: zero mistakes, professional (run on EVERY file before sending)

Nothing goes to Joanne until every line passes. If one fails, fix it first; never send "known issues".
- [ ] **Words**: transcript of the finished file read start to end; every first/last word at every cut complete; no stray word from a cut neighbour; no filler/stutter/cough she asked to remove.
- [ ] **Captions**: spelling, names and brand exact (Martínez-Cid, OfficeFurniture4Sale, OF4S); punctuation/capitals right; no caption over a face or photo; gold words are the right ones; nothing on black/transition frames.
- [ ] **Sound**: no clipping/breaking on the loudest lines (listen points + clipped-sample count), pause cuts smooth, true peak ≤ −1 dBTP, music under the voice and ducked after the question, SFX are the approved ones.
- [ ] **Picture**: contact sheet of 8–10 frames: locked framing, same head height, no empty wall, no green/black flashes (check transitions frame by frame), lighting: faces bright and natural, no dark or washed-out shots, both cameras matching, end card present.
- [ ] **Content**: every rule in §13–§17 and every note she gave for this video in this round — tick them off one by one against her message.
- [ ] **Delivery**: correct name/version, file plays to the end, size < 380 MB, previous version kept.

## 20. Shoot checklist for George (send before every recording)
- **Audio**: set mic/receiver gain so the loudest laugh peaks around −12 dB (Martínez-Cid clipped and broke the voice). Record a **backup** (second camera or a 32-bit float recorder) with both lavs.
- Spotless table and room; show OF4S furniture, hide clutter, cards, cups.
- Don't read questions on camera; glance at notes off frame and look at the guest. Leave a beat before reacting (no talking over the guest).
- Both cameras at eye level, steady; guest framed with headroom; same white balance; **enough light on both faces** (add a soft light if the room is dim; footage that is too dark has to be brightened in the edit); record 10 s of room silence at the start.
- Get the guest's exact name spelling and title on camera or in writing.

## 21. Fixes Claude made on its own (keep adding; never only in code)

| Problem | Fix (use it from the start next time) | Where |
|---|---|---|
| Footage too dark / flat (iPhone HDR) | HDR→SDR tonemap, then the approved grade; match both cameras (§5) | §5, builders |
| Clipped master voice ("breaking") | Declip day 1; patch worst seconds with the other camera's audio (§17) | `audio_repair.py` |
| Green edge on the whip | Render the `xfade` + blur in RGB (`format=gbrp`), not yuv | `reel_builder_hook_whip.py` |
| Frames lost when cutting the YouTube body with `-ss … -c copy` | Cut at a keyframe with the segment muxer (`-f segment -segment_frames K`), join with stream copy, check the frame count | `youtube_intro_splice.py` |
| Out of memory with two 4K renders | One 4K render at a time; long renders as tracked background jobs (a plain `&` job died) | — |
| Duplicate / broken renders after a worker restart | Fail-fast render queue: one job, stop on the first error, check each output's frame count | — |
| Disk full | Delete finished reels' intermediates and old masters; keep ≥10 GB free | TECH.md §1 |
| Captions hidden under photo cards | Photo cards keep captions, placed above the photo; captions off only on non-photo cards | `finish_her_cut.py` |
| Drive upload from a session capped at 10 MB | Big files: send in chat with SendUserFile (≤400 MB) and Joanne saves them to Drive | — |
| Full-quality YouTube over 400 MB | HQ copy: HEVC two-pass ~2480 kbps (≈378 MB for ~20 min); review copy 2.4 Mbps H.264 | — |
| Scheduled sessions have no Drive/Gmail connector | Put the Drive file IDs in the task prompt; download with curl `drive.usercontent.google.com/download?id=<ID>&export=download&confirm=t`; deliver in that session's chat | — |
| Brand on a cup / product in shot | Track the logo box every frame (OpenCV tracker, re-checked with template match), smooth the box over ~0.5 s, soft `gblur` (sigma ~20) inside a feathered mask a little bigger than the logo; only the branded item; check every frame where it appears (no saved script yet: save it when built) | — |
