# Instagram — Client Testimonial Cover

Reusable layout for the client-testimonial post/reel cover. Same layout every time; only the photo, name, title, and company change.

- **File:** `template.html` — 1080×1080, built on `design-system/tokens.css`.
- **Photo slot:** `.photo` — full-bleed client photo, `background-size: cover`, vertical anchor `center 20%` (keeps faces in frame for portrait crops). Swap the placeholder for `background-image: url('...')`.
- **Scrim:** navy gradient (`--of4s-navy-950` base) rising from the bottom so white type stays legible over any photo, without flattening the whole image.
- **Quote mark:** display-font `"` in `--of4s-navy-300`, top-left — signals "testimonial" at a glance in a grid view.
- **Copy block, bottom-anchored:**
  - Eyebrow: `CLIENT STORY` — mono caps, `--of4s-navy-300`.
  - Name: Schibsted Grotesk 500, 44px, white.
  - Title · Company: mono caps, `--of4s-paper-200` for the title, `--of4s-navy-300` for the company name.
- **No logo** — per brand direction, the grayscale/branded logo is intentionally omitted so the grid doesn't feel crowded when several of these run in sequence. The quote mark + navy accent + mono voice is enough to read as OF4S without a lockup.

## To produce a new cover

1. Duplicate `template.html`.
2. Drop the client photo in and point `.photo`'s `background-image` at it.
3. Replace `Client Name`, `Title`, and `Company Name` with the real values (never invent these — pull from what the user provides).
4. Export at 1080×1080 (or 1080×1350 for a reel cover crop — extend `.cover` height and keep the content block bottom-anchored).
