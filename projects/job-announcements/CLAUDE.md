# Project: Job Announcements

Claude's behavior when working in `projects/job-announcements/`. This layers on
top of the root `CLAUDE.md`; the root hard rules still apply (the design system
is locked, never invent facts, hand off for human review).

## What this project is

Corporate recruiting **e-flyers** for OF4S job openings — one portrait
**8.5" × 11" PNG at 300 DPI** (2550 × 3300 px) per role, ready for email and
job-board distribution. Clean, business-appropriate, strong hierarchy, generous
white space. No stock clip-art.

## How Claude should behave here

- Build the flyer as an HTML page rendered to PNG (see Pipeline). Design on the
  OF4S v3 system **exactly** — tokens, fonts, and the logo lockup.
- Draft the marketing microcopy (headline eyebrow, "About the Role" paragraph,
  the CTA line) in a confident, corporate-professional tone — but **never invent
  facts**. Titles, numbers, locations, responsibilities, comp details, and the
  apply address come only from what the user provides.
- Render, **look at the PNG**, and refine until it's clean and fits on one page
  without overflow. Then hand it back — this is a deliverable for the user to
  send out, not something Claude publishes anywhere.
- One new role = one new output PNG (and, if the layout differs, a copy of
  `flyer.html`). Keep `flyer.html` as the reusable base.

## Inputs — the checklist to collect

- **Header:** site URL (e.g. OfficeFurniture4Sale.com). "WE'RE HIRING" is the
  primary hook — big, not a small pill.
- **Job title** (the role, shown under the hook). Pick one word to carry the
  navy `<em>` accent.
- **Location**, **Job type** (Full-Time, etc.), **Total compensation** (headline
  figure, e.g. "$100K+") — the info bar.
- **About the Role** — a sentence or two of positioning.
- **Key Responsibilities** — bullet list (renders as balanced two columns).
- **Qualifications** — the headline requirement (e.g. "3–5 years") + one line.
- **Compensation Highlights** — the perks list for the callout box.
- **How to Apply** — the exact apply email / instructions.
- **Any footer note** (e.g. reporting cadence).
- **Hero photo** — subject + any specifics (e.g. "two women networking, 25–35").
  Ask if the user has their own brand photography; otherwise source stock (below)
  and treat it as a swappable placeholder.

## Output — what "done" looks like

- `output/<Role-Name>.png` — 2550 × 3300 px (8.5 × 11 @ 300 DPI). Current layout:
  a **full-bleed photo hero** under a navy brand gradient with the logo lockup on
  a top scrim and a large **"WE'RE HIRING"** hook + role over it; a navy info bar
  (Location · Job Type · Comp); then About, Key Responsibilities (2 cols),
  Qualifications + Compensation callout; a navy CTA band; and a footer note bar.
- Delivered to the user via file send. Nothing is posted or published by Claude.

## Imagery (hero photo)

The hero photo is the emotional hook — feature real people, on-brand and tasteful.

- **Prefer the user's own OF4S team/brand photography** when available.
- **Otherwise source free-license stock** (Unsplash). The website is auth-walled
  to `curl`, but the CDN works: `https://images.unsplash.com/photo-<id>?auto=format&fit=crop&w=2600&q=80`.
  Find valid photo IDs with WebSearch / WebFetch (unsplash.com/s/photos/<query>),
  **download and view candidates before choosing** (a Playwright contact sheet is
  quick), and pick for the brief's *physical* subject ("two women networking,
  25–35"), not the generic category. Save the winner to `assets/img/`.
- Integrate it as a full-bleed hero under the **navy gradient** (bright at the
  top so faces read, deep navy at the bottom so the white headline is legible) —
  this keeps any photo on-brand. Verify legibility on the rendered PNG.
- Stock people are **placeholders** — always tell the user it's a licensed stock
  image they can swap for real OF4S photography.

## Design system — apply exactly

Values are copied from `design-system/tokens.css` into the flyer's `:root` (same
hex). Pull colors/type/logo from the locked `design-system/` — **never edit it.**

- **Logo:** horizontal lockup — `OF` + navy-accent `4` + `S` in Schibsted
  Grotesk 700 (letter-spacing −0.03em), a 1px rule, then "OFFICE FURNITURE / 4
  SALE" in Geist Mono 0.26em caps. On navy, the `4` is navy-300. (Anatomy from
  `design-system/logo-type.html`.)
- **Type:** Schibsted Grotesk = display/headlines; Geist = body; Geist Mono =
  eyebrows/labels/URLs (uppercase, wide letter-spacing).
- **Color:** navy scale does all structural accent work; navy-100 for the
  callout tint. Brass is garnish only — avoid it here. Warm paper background.
- **Voice mannerism:** exactly one navy `<em>` accent word per big heading;
  `em` is color, never italic.

## Pipeline

Self-contained; no network needed at render time.

- `flyer.html` — the page, designed at 816 × 1056 px (8.5 × 11 @ 96 DPI).
- `assets/fonts/` — the brand woff2 files + `fonts.css` (localized Google Fonts
  for Schibsted Grotesk / Geist / Geist Mono, so the render is faithful offline).
- `assets/img/` — the hero photo (`hero-networking.jpg`) and any other imagery,
  referenced by relative path so the render stays offline.
- `render.mjs` — Playwright (global, `/opt/node22/.../playwright`, Chromium at
  `/opt/pw-browsers/chromium-1194/...`) renders `.page` at `deviceScaleFactor
  3.125` → a true 2550 × 3300 PNG in `output/`.

To build a new one: edit/copy `flyer.html` with the new role's content, set the
output filename in `render.mjs`, run `node render.mjs`, view the PNG, refine.

## Hard rules for this project

1. **Hand off, don't publish.** Deliver the PNG to the user; they distribute it.
2. **Never invent role facts** — titles, comp, responsibilities, apply address
   all come from the user.
3. **Never modify `design-system/`.** Reference it; copy token values in.
4. **Fit on one page** — check the rendered PNG for overflow before delivering.
