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

## Active project — 2026 Wholesale Seating Catalog

A 15-page trade/wholesale seating catalog, built on the v3 design system. **Status: approved cover/back-cover/Aley page, ready for more content changes.** Picking this up in a new session? Read this whole section first — it's the running history so you don't redo settled decisions.

**Files:** `collateral/of4s-wholesale-seating-catalog-2026.html` (source of truth) + matching `.pdf` (generated from it, never hand-edited). Product photos live alongside as `*-crop.png` (already cropped to their alpha bbox — see tooling below).

**Branch:** `claude/new-design-system-48y9mp` on `azavarce/OF4S-Marketing`, pushed after every round. If a fresh session's local checkout looks behind or the catalog files are missing, that's a stale/reset container, not lost work — `git fetch origin claude/new-design-system-48y9mp` and `git reset --hard origin/claude/new-design-system-48y9mp` before doing anything else. Never assume the file is gone; check the remote first.

**Page structure (15 pages, in order):** Cover · TOC · Sidon–Gray · Sidon–Black · Aley · Calico · Calico–All-Gray · Gibran · Gibran–Specifications · Programs · Warranty · Terms · Care · RMA · Back Cover. Every time a page is added/removed, grep and update **both** the `.page-num` footer on every page and the TOC `<li>`/`<span class="pg">` entries — this has bitten us before.

**Locked design decisions — don't re-litigate without the user asking:**
- **Cover**: navy background, `cover-bg.png` chair cutout bottom-right (bleeds off right+bottom edges, `right:-70px; bottom:-46px; width:800px`), title-block anchored at `bottom:235px` (raised from an earlier `84px` specifically so the chair's armrest clears "dealer-direct." instead of cutting across it). This exact layout was matched against a user-supplied reference image — don't move it back down.
- **Back cover**: navy, `haley 2 v blk-crop.png` chair photo (440px, drop-shadow filter) + radial-gradient floor shadow for depth.
- **Aley page (page 5), the 3 chairs**: sizes are tuned so High-Back/Mid-Back/Visitor share one base/wheel width (High-Back `max-width:90%;max-height:87%`, Mid-Back & Visitor `max-width:82%;max-height:82%` on the `<img>`). Vertically the frames use `align-items:flex-end` + `margin-bottom:8px` on each `<img>`, so all three chair bases sit flush on the same floor line (matches the vendor reference photos, where the chairs fill their frame edge-to-edge with the base near the bottom). An earlier round had used `flex-start` + `margin-top:20px` instead, reportedly to avoid a "misaligned-floor oblique look" from a prior `flex-end` attempt — that concern did not reproduce when re-tested (2026-08-31), so `flex-end` is the current locked choice. If asked to touch these chairs again, re-derive from the actual rendered `.chair-frame`/`img` bounding boxes (see tooling) and re-screenshot before committing, rather than guessing percentages.
- **Sidon SKUs**: color code is `GRY` (not `GY` or `DGY`) — page 3 is Gray, page 4 is Black.
- **Calico All-Gray (page 7) and Gibran Specifications (page 9)**: both use the `.spec-sheet`/`.spec-grid`/`.spec-row` two-column key/value component for full technical specs.

**Tooling (persisted in the repo, not scratchpad — safe across container resets):** `collateral/tools/print.js` (regenerate the PDF — `cd collateral/ && node tools/print.js`, must run from inside `collateral/` since paths/image srcs are relative), `collateral/tools/pdfshot_page.js` (screenshot one PDF page for visual QA — `node tools/pdfshot_page.js <pageNum> <outPath.png>`, runnable from anywhere), `collateral/tools/crop_products.py` (crops a raw product PNG to its alpha-channel bbox + 6% padding — every source photo from Drive only used ~45–65% of its own canvas before this).

**Workflow discipline for this file specifically:**
1. For any cover-level/major-visual change: draft in a scratch HTML copy first, screenshot it, compare against any reference the user gave, get it right visually *before* touching the real file.
2. After every edit to the real HTML: regenerate the PDF and screenshot the affected page(s) — never declare a visual change done without looking at the rendered result.
3. Only touch what was asked. This user has repeatedly called out unintended side effects — re-read the request narrowly.
4. After each round: commit with a descriptive message, `git push -u origin claude/new-design-system-48y9mp`, then send the updated `.html` and `.pdf` to the user with a plain-language summary of what changed.
5. The `impeccable` design-review hook will flag Schibsted Grotesk/Geist as "overused fonts," the cover's dark navy as "dark-glow," and the inherited numbered section markers/em-dashes — these are established false positives for this project (locked brand fonts, brand-mandated navy treatment, inherited catalog conventions). Note them as reviewed, don't change the design to satisfy the hook.

**Separate, not blocking:** there's an in-progress side task helping the user manually populate a Canva Brand Kit ("OF4S New") with this design system's colors/fonts/voice/graphics/icons/components/chart-colors — Canva's API has no write access to Brand Kit contents, so everything was handed to the user as copy-paste text/files, not automated. Unrelated to the catalog; only relevant if the user brings up Canva again.

---

## Prerequisites (connections — set up by Andres, not in this repo)

This repo provides the *instructions and reference*; it does not provide the live connections. The Claude environment needs:

- **OF4S Odoo** connection with permission to **create** and **read** records (to create the draft post and, optionally, upload images). It should NOT have write/delete/execute or access to the accounting Odoo — least privilege.
- **Google Drive** access to read the project-photos folder.

If either is missing, tell the user to ask Andres to connect it — do not proceed without them.
