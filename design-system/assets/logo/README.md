# OF4S Logo Exports

Generated from the v3 spec on `logo-type.html` — "OF4S" in Schibsted Grotesk
700, letter-spacing -0.03em, the "4" in navy-500 on light / navy-300 on dark.
SVGs are true vectors with the letters converted to outlines, so they render
identically everywhere with no font installed. PNGs have transparent
backgrounds except the tiles (navy fill is part of the tile).

| File | Use for |
|---|---|
| `of4s-mark.svg` / `.png` | Primary mark, on light/paper backgrounds — the default |
| `of4s-mark-ondark.svg` / `.png` | Primary mark, on navy/dark surfaces |
| `of4s-lockup.svg` / `.png` | Horizontal lockup (mark + full company name) — letterhead, proposal covers, web nav, on light |
| `of4s-lockup-ondark.svg` / `.png` | Horizontal lockup on navy/dark surfaces |
| `of4s-tile.svg`, `of4s-tile-512.png` | App icon / avatar master |
| `of4s-tile-180.png` | Apple touch icon |
| `of4s-tile-32.png` | Favicon |

Rules (from the system):

- Pick the `-ondark` version on navy or any dark surface — never recolor by hand.
- Don't stretch, re-track, re-space, or restyle the letters; the "4" is the
  only colored letter.
- Minimum clear space: leave at least the height of the "S" around the mark.
- The captioned vertical version and the `of4s.com` text mark exist only as
  live HTML on `logo-type.html`; use those pages as reference if you need them.
