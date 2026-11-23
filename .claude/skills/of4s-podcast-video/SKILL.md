---
name: of4s-podcast-video
description: Edit an OF4S client podcast into a YouTube full episode and vertical short clips (Instagram Reels, TikTok, YouTube Shorts) using the rules Joanne approved on the EPGD Law podcast. Use for any OF4S podcast / interview / testimonial video edit: picking clip topics, writing the cut script, hooks, framing, captions, animations, music, SFX, end card, YouTube intro/chapters/captions, QA and client review.
---

# OF4S Podcast Video Playbook

Everything below was decided with Joanne (OF4S marketing) while editing the EPGD Law podcast (Eric Gros-Dubois x George Dargham, Nov 2026). Follow it from the first edit so she does not have to repeat feedback. `TECH.md` in this folder has the build recipe. **`assets/` holds the exact sounds, music, end cards, fonts and approved animation templates from the EPGD videos — use these by default (catalogue in `assets/README.md`); only look for new music/SFX when Joanne asks or the mood needs something different.**

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
