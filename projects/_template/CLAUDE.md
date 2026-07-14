# Project: <NAME>

> Scaffold for a new OF4S marketing project. Copy this folder to
> `projects/<your-project>/`, then fill in the placeholders with Claude. Delete
> this quote block when done. This layers on top of the root `CLAUDE.md` — the
> root hard rules (design system is locked, never invent facts, etc.) still
> apply.

## What this project is

<One or two sentences: what are we making, for whom, and where does it end up?
e.g. "A monthly OF4S Instagram carousel promoting a featured product line,
delivered as ready-to-post images + captions.">

## How Claude should behave here

<The mode Claude is in for this project. Tone, how proactive, what to draft vs.
ask for, what to hand back. e.g. "Draft 3 caption options; never post to
Instagram directly; always show the layout before generating final images.">

## Inputs — the checklist to collect

<The facts Claude should gather from the user before starting. e.g.>
- <Item 1>
- <Item 2>
- <Item 3>

## Output — what "done" looks like

<The deliverable format and where it goes. e.g. "1080×1350 PNGs in this folder +
a captions.md; nothing published — the user posts it.">

## Design system

Pull all colors, type, logo, and components from the root `design-system/`
(read-only source of truth). Reading order: `design-system/HANDOFF.md` →
`DELTA.md` → `BUILD-SPEC.md`; `tokens.css` has the color/type tokens; the
`*.html` files are live references. Never modify `design-system/`.

## Hard rules for this project

1. <Project-specific rule, e.g. "Never publish — hand the finished asset to the
   user to post.">
2. <e.g. "Brass is garnish only; navy does structural accent work.">
3. <Add as needed.>
