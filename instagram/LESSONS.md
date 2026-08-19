# Instagram design assets — lessons learned

Notes from building the client-testimonial cover (2026-07-23), kept general so they apply to the *next* Instagram design too, not just testimonials. Read this before starting a new Instagram asset in a fresh session.

## Legibility & sizing

- **Grid thumbnails shrink text far more than "looks fine" at full 1080px size.** When feedback is "I can't read this," don't nudge the font size up a few px — jump it up meaningfully (we went 13px → 20px → still unreadable → pulled it out as its own 46px bold line before it actually worked). Assume any label needs to be bigger and bolder than intuition says.
- **Don't bury the most important word in a small mono-caps eyebrow line.** If one phrase has to read first even at thumbnail scale (e.g. what kind of post this is), give it its own visual weight and position — don't nest it as a secondary detail inside a bigger text block.
- **A container is allowed to grow to fit bigger text.** Don't treat an existing box's size as fixed when the client asks for larger type — resize the box around the type, not the other way around.

## Matching the brand's shape language

- This design system is sharp-edged (rectangular cards, no rounded pill/badge shapes elsewhere in the system). When a "make X stand out" problem is tempting to solve with a pill/badge, check the existing shape vocabulary first — here, a big plain-text line fit better than a badge and the client explicitly rejected the pill once they saw it next to everything else.
- Ornamental marks (quote marks, icons) are cheap to add but shouldn't be precious — when the client says "remove it," just remove it. Simpler often reads cleaner, especially at small size.
- When an element needs to move relative to a container (e.g. "put the label above the box, outside of it"), restructure the DOM so both pieces share one wrapper anchored at a single position, instead of hand-computing independent pixel offsets for two separately-positioned elements. Much easier to keep them locked together through the next round of edits.

## Reel-cover math (reusable for any future 9:16 cover)

- Instagram's profile grid only shows the **center 1080×1350 (4:5) crop** of a 1080×1920 Reel cover — 285px is cropped off the top and bottom in grid view. Anything that needs to read on the grid (not just when the reel is opened) must stay inside that band, with some buffer margin (we used 40px).
- Build a togglable dashed safe-zone guide overlay (`.safe-guide`, toggled via a body class) to check photo/text placement before exporting — never present in the actual export.
- Verify with an actual rendered screenshot against the guide, not just the CSS math on paper.

## Technical gotchas

- **`aspect-ratio` breaks if a fixed `height` is also set alongside `max-width: 100%`.** On a narrow viewport the width shrinks but the fixed height doesn't, distorting the shape. Set `width` + `max-width: 100%` + `aspect-ratio`, and leave `height` to compute automatically.
- **The Artifact preview only bundles the single HTML file you publish** — sibling image files and relative CSS links (like a photo in the same folder, or `../../design-system/tokens.css`) will NOT resolve there, even though they work fine in the actual repo. For an Artifact preview specifically, inline the image as a base64 data URI and inline the CSS. For everything else, **always confirm the real deliverable with an actual exported PNG**, not the Artifact preview.
- **PNG export recipe:** Playwright is preinstalled globally at `/opt/node22/lib/node_modules/playwright`; launch Chromium with `executablePath: '/opt/pw-browsers/chromium'`. Import it as `import playwright from 'playwright'; const { chromium } = playwright;` — a plain named import (`import { chromium } from 'playwright'`) fails here. Screenshot the specific element (`page.$('.cover').screenshot(...)`), not the full page, to get exact native pixel dimensions without the staging-page padding.
- **Google Drive `download_file_content` on a photo returns a huge base64 blob** that overflows the context window and gets saved to a tool-results `.txt` file instead. Don't try to read that file directly — extract the image with a small Python script (`json.load` the file, `base64.b64decode` the `content` field, write the bytes to a `.png`/`.jpg`).

## Process

- Never invent testimonial content (name, title, company, quote) — always wait for the real values from the user.
- When the user gives visual feedback ("still can't read it," "move it here"), re-render and send the actual PNG back rather than describing the change — confirms the fix landed and surfaces problems (like the Artifact-preview image bug) immediately.
- Keep the feed (1:1) and reel (9:16) variants structurally identical (same class names, same CSS logic) so a style change can be copy-pasted between them instead of re-derived — drift between the two was the main source of repeated edits this session.
