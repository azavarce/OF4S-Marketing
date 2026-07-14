# OF4S Design System — Claude Code Guide

The complete, **decided** OF4S design system. All explorations are resolved; what's in this folder is final. Use it as the source of truth for anything you build for Office Furniture 4 Sale.

## How to use with Claude Code

1. Drop this folder into (or next to) your target repo.
2. Point Claude Code at this file first, then `CLAUDE.md` (project rules, traps, decision log).
3. For any task: read `tokens.css` + the relevant topic page(s), then build using only tokens.

## The decisions (all locked, 2026-07)

- **Logo**: the OF4S shorthand — Schibsted Grotesk 700, natural letter tracking, the "4" in navy-500 on light / navy-300 on dark. All versions (horizontal lockup, captioned, favicon/app tiles, text marks) on `logo-type.html`.
- **Display font**: Schibsted Grotesk. Sans: Geist. Mono: Geist Mono.
- **Direction**: A — "Editorial Modern" (`directions.html`).
- **Accent**: navy only for structure — navy-600 on light, navy-300 on dark. **Brass is garnish ONLY**: tiny mono details (ratings, stats, key numbers) — brass-700 on light, brass-400 on dark. Never eyebrows, headings, links, buttons, or fills.
- **No italics** — anywhere — except inside `blockquote`, `.testimonial`, or `.quote`. The `em` mannerism in headings = accent color, upright.
- Background is warm paper (`--of4s-paper-50`), never white. White is for raised cards.

## Files

- `CLAUDE.md` — project rules, known CSS traps, decision log. **Read before writing code.**
- `tokens.css` — canonical colors / type / spacing / radii / shadows / motion. The only place values are defined.
- `shared.css` — page chrome, responsive shell (single 960px breakpoint), scroll-hint affordance.
- `sidebar.jsx`, `scroll-hint.js` — shared chrome for the system site itself.
- Topic pages: `index.html` (overview), `logo-type.html` (logo + type), `color.html` (palette + accent-in-use demos), `typography.html`, `components.html`, `imagery.html`, `iconography.html`, `directions.html` (the chosen direction).
- Applied templates: `presentation.html`, `proposal.html`, `collateral.html` (letterhead, cards, email sig), `social.html`.
- `netlify.toml` — deploy config.

## Things you can ask Claude Code to do

- "Build a landing page / pricing page / email template using this design system."
- "Convert this system into a React/Vue component library."
- "Build a sales one-pager from the proposal.html layout."
- "Audit this page against the system and flag drift."

## Not included

Logo SVG/PNG exports, photography, product shots, customer logos, testimonials. Use captioned placeholders until real assets exist.
