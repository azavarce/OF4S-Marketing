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

---

## Lessons from live posts (apply these from the start — don't wait to be corrected)

These came out of building and revising the Somos TV post against the live UMusic post as the reference. `ANATOMY.md` still documents an older single-gallery layout — until it's rewritten, follow the corrections below over that file where they conflict.

**Structure — one section per named space, not one lumped gallery.**
In "What we helped design & furnish," don't put every furnished-space photo in a single `of4s-gallery`. Give each space its own `of4s-sec` (eyebrow + `<h2>`, one fresh accent word) followed by its own gallery — exactly like UMusic's Collaborative area / Lounge / Executive offices / etc. If the client only gave 5 spaces but photos exist for a 6th (e.g. a "Collaborative area" folder that wasn't in the original scope), add that section and add the space to the snapshot too.

**Linked space list, with real page checks.**
The "What we helped design & furnish" intro is followed by a bulleted list of spaces, each `<a href="/...">` to its OF4S category page, bold+underlined, with a one-line description — copy UMusic's exact markup pattern. Before linking, check the live page list (`SELECT url FROM website_page`) — don't assume a page exists. Not every space has one (e.g. no `/filing`, `/storage`, or `/editing-rooms` page exists as of this writing); leave those bold but unlinked, or link to the closest real match only if the user confirms it's accurate (e.g. Editing Rooms → `/private-offices`, since editing-room furniture is private-office furniture).

**Multiple photos per space.**
Don't assume one photo per space. Ask how many photos exist for each space, or default to 3 placeholder slots per space with "photo N of 3 · delete this box if you have fewer, duplicate it if you have more" — not a single slot.

**Placeholders and real photos don't mix cleanly by default.**
When a real image is dropped into a placeholder `<span class="of4s-imgslot">`, the border/background CSS on that class still applies to the final photo unless the class is stripped down. Once photos are uploaded, immediately simplify `.of4s-imgslot` to `display:block` with no border/background/padding — don't leave dashed-box styling wrapping real photos. Odoo's editor auto-adds `of4s-zoomable` (click-to-enlarge) to uploaded images — nothing to do there.

**Captions must match what's actually in the photo — verify, don't assume from the section name.**
"Workstations going in" on an empty room, or "Space to seat the whole group" over a chairless conference room, are the kind of mismatches that get caught immediately by the client-facing user. If the photo's content isn't confirmed, write a caption that's true of any plausible framing (e.g. "The space, cleared and ready" / "Furniture being assembled on-site") rather than guessing specifics.

**Voice — don't overclaim beyond what's confirmed.**
Avoid absolute or judgment-laden phrasing not backed by the user's notes: not "wanted the new office to work harder than the old one," not "moving the whole operation at once," not "on schedule" unless the user said so. When a fact is fuzzy (a number, a timing claim), hedge honestly ("roughly 6,000 square feet") or ask, rather than asserting it.

**Full-content Odoo writes — verify photo count survives every edit.**
`blog.post.content` is replaced wholesale on every `odoo_write` — there's no partial patch. Before any text-only edit, fetch the live content, edit it locally, and run a diff check (`<img ` count unchanged, no unintended string still present) before writing back. Never reconstruct the HTML from memory once real photos are in it — always start from the live DB content.

**Filename-driven mapping works well — encourage it upfront.**
Ask the user to name their Drive photos by space (e.g. `Conference 1`, `Executive 1`) before sending the folder link. Claude cannot currently view Drive images directly (downloads return empty/unusable content in this environment) — filenames are the only reliable way to build accurate galleries without a slow back-and-forth.
