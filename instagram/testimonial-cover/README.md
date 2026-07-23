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
- **Scrim:** a light navy lift over the top of the photo so it doesn't compete with the elements below.
- **`.foot`:** a bottom-anchored wrapper holding the tag and the navy box as two stacked, separate pieces (not nested) — this is what lets the tag sit outside the box while both still move together as one group for the reel's grid-safe offset.
  - **Tag** (`.tag`, on the photo, directly above the box): the quote mark (flipped with `transform: scaleX(-1)`, so it reads as a closing rather than opening mark) + `CLIENT TESTIMONIAL`, side by side — mono, weight 800, 36px, white with a text-shadow, sitting on its own small gradient rather than a pill/badge. This is the phrase that has to read first, even at a shrunk grid thumbnail, so it's oversized and outside the box rather than squeezed inside it as a small eyebrow (two earlier, smaller-and/or-boxed versions weren't legible or didn't match the brand's sharp-edged shapes — don't reintroduce a pill, and don't shrink this back down).
  - **Box** (`.content`, directly under the tag): solid navy card (`rgba(10,22,40,0.94)`) with a thin `--of4s-navy-300` top rule.
    - Name: Schibsted Grotesk 500, 66px, white.
    - Title · Company: mono caps 500, 24px — `--of4s-paper-200` for the title, `--of4s-navy-300` for the company.
- **No logo** — per brand direction, the grayscale/branded logo is intentionally omitted so the grid doesn't feel crowded when several of these run in sequence. The tag + navy accent + mono voice is enough to read as OF4S without a lockup.

## Reel cover — grid-safe math

Canvas is 1080×1920. The grid crop is centered, so:

- Crop-safe top: `(1920 − 1350) / 2 = 285px`
- Crop-safe bottom: `1920 − 285 = 1635px`

`.foot` (tag + box together) is floated up off the true bottom edge (`bottom: 325px`, i.e. the 285px crop plus a 40px buffer) instead of flush at `bottom: 0`, so the whole group lands inside `[285, 1635]` with margin. **Don't reset this to `bottom: 0` on the reel variant** — that would push the tag and name/title below the grid-visible area.

`reel-template.html` has a `.safe-guide` overlay (dashed lines at the crop boundaries) toggled by adding `show-guide` to `<body>` — useful for checking a new photo's framing before exporting, never present in the final export.

## To produce a new cover

1. Duplicate `template.html` (feed) and/or `reel-template.html` (reel).
2. Drop the client photo in and point `.photo`'s `background-image` at it. For the reel variant, toggle `show-guide` and confirm the face sits inside the dashed lines before finalizing.
3. Replace `Client Name`, `Title`, and `Company Name` with the real values (never invent these — pull from what the user provides).
4. Export each `.cover` element at its native size: 1080×1080 for the feed post, 1080×1920 for the reel cover (with the guide switched off).
