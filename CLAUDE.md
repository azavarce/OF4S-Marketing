# OF4S Marketing — Claude Working Instructions

This repository is the **OF4S marketing toolkit for Claude** — the home base for
creating OF4S-branded marketing assets of every kind: blog posts, Instagram
sets, email campaigns, flyers, and other collateral. Blog posts were the first
job and are still a big one, but this repo is now organized to support the full
marketing role.

**Company:** Office Furniture 4 Sale (OF4S) — commercial office furniture dealer,
South Florida.
**Design system:** v3 — Schibsted Grotesk display / Geist body / Geist Mono;
navy structural accent; brass only on mono garnish numbers. See `design-system/`.

---

## How this repo is organized

- **`projects/`** — one subfolder per marketing project, where the actual work
  lives. **Each project folder has its own `CLAUDE.md`** that defines how Claude
  should behave for that project — its checklist, output format, and rules.
  Working inside a project folder puts Claude in that project's mode. See
  `projects/README.md`.
- **`design-system/`** — the canonical, **locked** OF4S v3 design system (tokens,
  brand voice, components, specs). The shared brand source of truth every project
  draws from. Reference it; never change it.
- **`.claude/skills/`** — the reusable skills Claude runs (e.g. `of4s-blog-post`).
- **`CLAUDE.md`** (this file) — repo-wide instructions Claude reads on open.

### Starting a project

To create a new asset, work in its project folder — e.g. **"Create a new blog
post"** uses `projects/blog/`. To spin up a **new** kind of project (Instagram,
email, flyer…), say so and Claude will copy `projects/_template/` to a new
`projects/<name>/` and fill in that project's `CLAUDE.md` with you. Behavior for
each project is shaped as it's built — it doesn't all have to be defined up front.

---

## Design system (for any OF4S-branded asset)

`design-system/` is the canonical OF4S v3 design system. Use it as the source of
truth for colors, type, logo, and components when building any asset. Reading
order: `design-system/HANDOFF.md` → `DELTA.md` → `BUILD-SPEC.md`; `tokens.css`
holds the color/type tokens; the `*.html` files are live component/typography/
color references.

---

## Hard rules (never break these)

1. **The design system is LOCKED.** Never modify anything under
   `design-system/` — it is the brand source of truth. A guard hook
   (`.claude/hooks/guard.mjs`) blocks edits to it. Reading it is expected;
   changing it is not. If a design-system change is ever genuinely needed, it
   has to be done deliberately, outside the normal agent flow.
2. **Changing the blog-creation skill needs explicit authorization.** Edits to
   `.claude/skills/of4s-blog-post/` (and to the guard/settings that protect it)
   are gated: the guard hook will **ask you to confirm** first. Only proceed
   when you've clearly asked to change the skill and said yes. Don't touch it as
   a side effect of another task.
3. **Never invent facts.** Client names, numbers, quotes, spaces, and partners
   come only from what the user provides or from verified sources. Placeholders
   stay as placeholders until filled with real information.
4. **Publishing is a human's call.** Nothing goes public automatically — Claude
   drafts and hands off; a person reviews and publishes. (Blog posts are created
   as **unpublished Odoo drafts**; other assets are handed back for the user to
   post/send.)
5. **Protect the Odoo instance — it is a live, fragile, business-critical
   database.** Serialize every Odoo call (never in parallel), upload images one
   at a time, verify lightly, and **the moment any call times out or returns
   429 / "too many requests," STOP and wait — do NOT retry.** Retrying is what
   causes outages.

Project folders may add their own hard rules on top of these — read the
project's `CLAUDE.md` when working inside it.

---

## Prerequisites (connections — set up by Andres, not in this repo)

This repo provides the *instructions and reference*; it does not provide the live
connections. Depending on the project, the Claude environment may need:

- **OF4S Odoo** connection with permission to **create** and **read** records (to
  create draft blog posts and, optionally, upload images). It should NOT have
  write/delete/execute or access to the accounting Odoo — least privilege.
- **Google Drive** access to read project-photo folders.
- Other connectors as new project types call for them.

If a needed connection is missing, tell the user to ask Andres to connect it —
do not proceed without it.
