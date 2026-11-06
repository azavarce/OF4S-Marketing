---
name: of4s-podcast-video
description: Edit an OF4S client podcast into a YouTube full episode and vertical short clips (Instagram Reels, TikTok, YouTube Shorts) using the rules Joanne approved on the EPGD Law podcast. Use for any OF4S podcast / interview / testimonial video edit: picking clip topics, writing the cut script, hooks, framing, captions, animations, music, SFX, end card, YouTube intro/chapters/captions, QA and client review.
---

# OF4S Podcast Video Playbook

Everything below was decided with Joanne (OF4S marketing) while editing the EPGD Law podcast (Eric Gros-Dubois x George Dargham, Nov 2026). Follow it from the first edit so she does not have to repeat feedback. `TECH.md` in this folder has the build recipe.

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

## 9. Branding & end card

- Design system v3 (`design-system/`): navy-800 #15273f, navy-900 #0f1d33, navy-700 #1e3554, navy-300 #8fa9c7, navy-100 #dde5ee, paper-50 #faf8f4; Schibsted Grotesk display, Geist body.
- Every reel ends on the **OF4S logo end card** (navy gradient, navy-300 rule, Geist URL officefurniture4sale.com), ~2.6 s, with a whoosh in and no chime.
- Name tags: navy box, navy-300 accent bar, name in Schibsted, title in Geist.

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
