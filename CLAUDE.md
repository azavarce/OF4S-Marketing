# OF4S Marketing — Claude Working Instructions

This repository is the **OF4S marketing toolkit for Claude**. When you (Claude) work in this repo, follow these instructions. The primary job today is **creating blog posts** for the OF4S "Explore Our Projects" blog; the design system here also supports building other OF4S-branded marketing assets over time.

**Company:** Office Furniture 4 Sale (OF4S) — commercial office furniture dealer, South Florida.
**Design system:** v3 — Schibsted Grotesk display / Geist body / Geist Mono; navy structural accent; brass only on mono garnish numbers. See `design-system/`.

---

## Primary task — create a blog post

To create a new project blog post, **use the `of4s-blog-post` skill** at `.claude/skills/of4s-blog-post/SKILL.md`. Follow it exactly. In short, it:

1. Collects the project facts from the user as a friendly checklist (client, type, spaces, furniture partners, project stats, short notes per story section, the Vimeo video ID, the designer/salesperson name).
2. Reads and classifies the project photos from a **Google Drive folder** the user provides, and confirms the mapping.
3. Drafts the copy in the **OF4S brand voice** (`.claude/skills/of4s-blog-post/VOICE.md`) from the user's notes.
4. Assembles the post to the standardized **anatomy** (`.claude/skills/of4s-blog-post/ANATOMY.md`) — intro, snapshot, credibility strip, the salesperson-at-work photo, Discovery, Design & Layout Planning (with the autoplay project video), What We Helped Design & Furnish (with the grayscale partner-logo strip), the render-vs-installed pair, Installation, Final Results, stats, and CTA — with a filename-labeled placeholder at each image slot.
5. Creates the post in Odoo as an **UNPUBLISHED DRAFT** for the user to review, drop the photos in, and publish.

The reusable, up-to-date template lives in Odoo as the post **"TEMPLATE — OF4S Project Post (copy me)"** (unpublished); `.claude/skills/of4s-blog-post/template.html` mirrors it.

---

## Design system (for any OF4S-branded asset)

`design-system/` is the canonical OF4S v3 design system — tokens, brand voice, components, and specs. Use it as the source of truth for colors, type, logo, and components when building any marketing asset. Reading order: `design-system/HANDOFF.md` → `DELTA.md` → `BUILD-SPEC.md`; `tokens.css` holds the color/type tokens; the `*.html` files are live component/typography/color references.

---

## Hard rules (never break these)

1. **Blog posts are created as DRAFTS — never publish automatically.** A human reviews the draft in Odoo, drops in the photos, and clicks Publish. Nothing goes public without a person.
2. **Protect the Odoo instance — it is a live, fragile, business-critical database.** Serialize every Odoo call (never in parallel), upload images one at a time, verify lightly, and **the moment any call times out or returns 429 / "too many requests," STOP and wait — do NOT retry.** Retrying is what causes outages.
3. **Never invent facts.** Client names, numbers, quotes, spaces, and partners come only from what the user provides or from verified sources. Placeholders stay as placeholders until filled with real information.
4. **Zero `<h1>` in blog content** — the post title is the page heading. One upright navy `<em>` accent word per `<h2>`.
5. **Use the homepage grayscale partner logos** (color on hover), never the white-background versions.

---

## Prerequisites (connections — set up by Andres, not in this repo)

This repo provides the *instructions and reference*; it does not provide the live connections. The Claude environment needs:

- **OF4S Odoo** connection with permission to **create** and **read** records (to create the draft post and, optionally, upload images). It should NOT have write/delete/execute or access to the accounting Odoo — least privilege.
- **Google Drive** access to read the project-photos folder.

If either is missing, tell the user to ask Andres to connect it — do not proceed without them.
