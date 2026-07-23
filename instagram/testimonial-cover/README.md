# Instagram — Client Testimonial Cover

Reusable layout for the client-testimonial post/reel cover. Same layout every time; only the photo, name, title, and company change.

Two variants, same visual language:

- **`template.html`** — 1080×1080 feed post.
- **`reel-template.html`** — 1080×1920 Reel cover. Instagram's profile grid only shows the **center 1080×1350 (4:5) crop** of a Reel cover — 285px is cropped off the top and 285px off the bottom. The face and the text panel are kept inside that center band so the cover still reads correctly from the grid, not just when the Reel is opened.

Both built on `design-system/tokens.css`.

## Shared anatomy

- **Photo slot:** `.photo` — full-bleed client photo, `background-size: cover`. Swap the placeholder for `background-image: url('...')`.
  - Feed (1:1): anchor `center 20%`.
  - Reel (9:16): anchor `center 24%` (roughly upper-middle third) so the face sits inside the 4:5 grid-safe zone — check with the guide (below) and adjust per photo.
- **Scrim:** a light navy lift over the top of the photo so it doesn't compete with the panel.
- **Text panel:** a solid navy card (`rgba(10,22,40,0.94)`) with a thin `--of4s-navy-300` top rule — this is the shape that defines the copy area, not a soft fade. No pill/badge shapes anywhere — the system is sharp-edged, so the panel itself (and the guide rule) is the only "shape" used.
  - **Kicker** (`.kicker`, top of the panel): the quote mark + `TESTIMONIAL`, side by side — mono, weight 700, 28px, `--of4s-navy-300`. This is the word that has to read first, even at a shrunk grid thumbnail, so it runs large and bold rather than as a small mono-caps eyebrow (an earlier, smaller version wasn't legible — don't shrink this back down). A standalone pill badge floating on the photo was also tried and rejected — the shape read as off-brand and disconnected from the rest of the panel; keep the kicker inside the panel, above the name.
  - Name: Schibsted Grotesk 500, 66px, white.
  - Title · Company: mono caps 500, 24px — `--of4s-paper-200` for the title, `--of4s-navy-300` for the company.
- **No logo** — per brand direction, the grayscale/branded logo is intentionally omitted so the grid doesn't feel crowded when several of these run in sequence. The kicker + navy accent + mono voice is enough to read as OF4S without a lockup.

## Reel cover — grid-safe math

Canvas is 1080×1920. The grid crop is centered, so:

- Crop-safe top: `(1920 − 1350) / 2 = 285px`
- Crop-safe bottom: `1920 − 285 = 1635px`

The text panel is floated up off the true bottom edge (`bottom: 325px`, i.e. the 285px crop plus a 40px buffer) instead of flush at `bottom: 0`, so it lands inside `[285, 1635]` with margin. **Don't reset this to `bottom: 0` on the reel variant** — that would push the name/title below the grid-visible area.

`reel-template.html` has a `.safe-guide` overlay (dashed lines at the crop boundaries) toggled by adding `show-guide` to `<body>` — useful for checking a new photo's framing before exporting, never present in the final export.

## To produce a new cover

1. Duplicate `template.html` (feed) and/or `reel-template.html` (reel).
2. Drop the client photo in and point `.photo`'s `background-image` at it. For the reel variant, toggle `show-guide` and confirm the face sits inside the dashed lines before finalizing.
3. Replace `Client Name`, `Title`, and `Company Name` with the real values (never invent these — pull from what the user provides).
4. Export each `.cover` element at its native size: 1080×1080 for the feed post, 1080×1920 for the reel cover (with the guide switched off).
