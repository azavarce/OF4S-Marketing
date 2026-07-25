# OF4S Design System v3 — Start Here

This zip is the complete, **decided** design system for Office Furniture 4 Sale
(OF4S), a commercial office furniture dealer in South Florida. It's packaged so
you can hand it to Claude (claude.ai chat or Claude Cowork) and generate
on-brand marketing content and assets. Everything in here is final — there are
no open explorations to choose between.

---

## Setting it up with Claude

### Option A — Claude chat (claude.ai)

1. Create a **Project** in claude.ai (Projects keep files and instructions
   attached to every conversation).
2. Upload these files to the project's knowledge:
   - `HANDOFF.md`, `CLAUDE.md`, `DELTA.md`, `BUILD-SPEC.md` (the system docs)
   - `tokens.css` (every color / font / spacing value)
   - `VOICE.md` (how OF4S copy should read)
   - Any topic pages relevant to your work (`color.html`, `typography.html`,
     `components.html`, etc.) — Claude reads HTML fine.
3. Paste the block below into the project's **custom instructions**.

> You are creating marketing assets and content for Office Furniture 4 Sale
> (OF4S), a commercial office furniture dealer in South Florida. The OF4S v3
> design system files in this project are the ONLY source of truth for colors,
> type, logo, components, and voice. Before producing anything, read HANDOFF.md,
> then tokens.css, then the topic file closest to the task. Write all copy in
> the voice defined in VOICE.md. Never invent facts — client names, numbers,
> quotes, and partners come only from what I provide. Key locked rules: display
> font Schibsted Grotesk, body Geist, mono Geist Mono; navy is the only
> structural accent (navy-600 on light, navy-300 on dark); brass is garnish
> ONLY for tiny mono numbers/stats, never headings, links, buttons, or fills;
> no italics anywhere except inside quotes/testimonials; backgrounds are warm
> paper (#faf9f7-ish paper-50), never pure white except raised cards.

### Option B — Claude Cowork

1. Unzip this folder somewhere Claude can reach (your working folder).
2. Point Claude at the folder and say: *"Read START-HERE.md and HANDOFF.md in
   this folder before doing anything — this is the OF4S design system, the
   source of truth for everything you make for OF4S."*
3. Claude will pick up `tokens.css` and the topic pages as needed per task.

---

## Reading order (for Claude)

1. `HANDOFF.md` — the decisions, all locked (2026-07)
2. `CLAUDE.md` — project rules, known CSS traps, decision log
3. `tokens.css` — the only place color/type/spacing values are defined
4. `VOICE.md` — how OF4S prose should sound
5. The topic page closest to the task (see file map below)

`DELTA.md` and `BUILD-SPEC.md` are deeper reference — what changed from v2 and
the full build spec.

---

## The non-negotiables (short version)

- **Type**: Schibsted Grotesk (display) / Geist (body) / Geist Mono (mono).
  Loaded from Google Fonts / Vercel in the HTML pages.
- **Logo**: the "OF4S" shorthand in Schibsted Grotesk 700, natural tracking,
  the "4" in navy-500 on light / navy-300 on dark. Versions on `logo-type.html`.
- **Accent**: navy does ALL structural accent work — navy-600 on light,
  navy-300 on dark. **Brass is garnish only**: tiny mono details (ratings,
  stats, key numbers) — brass-700 on light, brass-400 on dark. Brass is never
  used for eyebrows, headings, links, buttons, or background fills.
- **No italics** — anywhere — except inside `blockquote`, `.testimonial`, or
  `.quote`. The `<em>` accent word in headings renders as navy, upright.
- **Backgrounds**: warm paper (`--of4s-paper-50`), never white. White is
  reserved for raised cards.
- **Spacing**: 4/8/12/16/24/32/48/64/96 px only. Radii: the three tokens in
  `tokens.css`. Don't invent values.
- **Eyebrow voice**: small mono caps labels, letter-spacing 0.1–0.22em.
- **Copy voice**: consultative and warm, plainly competent, first-person
  plural "we", no hype adjectives, active voice, never invent facts. Full
  guide in `VOICE.md`.
- **Blog-specific**: never an `<h1>` inside post content (the post title is
  the page heading); one navy `<em>` accent word per `<h2>`.

---

## File map

| File | What it is |
|---|---|
| `START-HERE.md` | This guide |
| `HANDOFF.md` | The locked decisions — read first |
| `CLAUDE.md` | Working rules, CSS traps, decision log |
| `DELTA.md` | What changed v2 → v3 |
| `BUILD-SPEC.md` | Full build specification |
| `VOICE.md` | Brand voice / copywriting guide |
| `tokens.css` | Canonical colors, fonts, spacing, radii, shadows, motion |
| `index.html` | System overview (open in a browser to see it live) |
| `logo-type.html` | Logo versions + typography in use |
| `color.html` | Palette + accent-in-use demos |
| `typography.html` | Type scale and rules |
| `components.html` | UI component library |
| `imagery.html` / `iconography.html` | Photo treatment + icon style |
| `directions.html` | The chosen direction, "Editorial Modern" |
| `presentation.html`, `proposal.html`, `collateral.html`, `social.html` | Applied templates (decks, proposals, letterhead/cards/email sig, social) |
| `assets/logo/` | Logo files — vector SVGs (outlined, no font needed) + transparent PNGs of the primary mark and horizontal lockup in light/dark versions, plus favicon/app tiles. See `assets/logo/README.md` for which file goes where |
| `shared.css`, `sidebar.jsx`, `scroll-hint.js`, `netlify.toml`, `index-print.html`, `README.md` | Chrome/deploy for the system site itself — ignore for content work |

Tip: every `.html` page opens directly in a browser (no build step), so the
person can *see* the system, not just read about it.

---

## Not included

Photography, product shots, customer logos, and testimonials. Use captioned
placeholders until real assets are supplied. Fonts load from Google Fonts /
CDN inside the HTML pages. (Logo files ARE included — see `assets/logo/`.)

---

## Guardrails for whoever uses this

- Claude should **never invent facts** — client names, stats, quotes, spaces,
  and furniture partners come only from you.
- Anything destined for the OF4S website or blog goes through a human review
  before publishing. Nothing goes public automatically.

*Packaged from the OF4S-Marketing repo (`design-system/` + the brand voice
guide), July 2026.*
