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
6. **Blog image attachments are PUBLIC and untied from any one post.** Upload (or convert) each image `ir.attachment` to `public=true` with **`res_id=0`** (no `res_id` pointing at a specific draft). Deleting a post cascade-deletes the attachments linked to it by `res_id` — which silently wipes those photos out of *every other* draft/post that shares them. This caused real data loss on the UMusic post. Note: when a human uploads a photo through Odoo's editor it lands as `public=false` tied to that post's `res_id`, so after uploads, convert them to public/`res_id=0`.
7. **Never delete a post/record without human approval AND a safety check.** Before deleting a superseded draft, confirm that every attachment still tied to it (`res_model='blog.post'`, `res_id=<that draft>`) is NOT referenced by the live/published post's content. Delete one at a time, serialized, and re-verify the live post's images after each.

---

## Operational lessons (learned building the UMusic post)

Hard-won, cross-cutting gotchas. Read these before revising an existing post or touching attachments.

- **Editing an existing draft = `odoo_write` on `blog.post` `content`** (don't rebuild the post). The field is jsonb keyed `en_US`; pass a plain string. **Verify byte-exactly:** compute the md5 of your intended HTML locally and compare it to `md5(content->>'en_US')` from the DB after writing. For large content, first pull the current value into a file (a `run_readonly_query` that repeats the column enough that the result is saved to a file), hash-verify it, transform it there, then write — never hand-retype 15–40 KB of HTML into a tool call.
- **Real images must be plain, borderless `<img>`.** The dashed-border placeholder box is build-time ONLY. Once a photo fills a slot, the `<img>` must be a **direct child of the `<figure>`** (matching the published South Florida Donor Network post, `blog.post` id 18): `<img src="/web/image/<id>" alt="…">`. If the `<img>` stays nested inside the placeholder `<span>` wrapper, the `.of4s-pair` / `.of4s-gallery` equal-sizing rules (`object-fit:cover` on a direct-child img) don't apply and paired render-vs-installed images render at different sizes.
- **The click-to-enlarge lightbox is a website view, not post content.** It lives in `ir.ui.view` `website.of4s_blog_v3_lightbox` (a generic view **plus** a per-website copy — keep both in sync). It auto-makes every `.of4s-blog img` zoomable **except** images whose `src` contains `logo` or that carry a `data-no-zoom` attribute — so give logo files a name containing "logo" (or add `data-no-zoom`) to keep logos from being clickable. Two production failure modes seen: (a) if its `t-if` includes `blog.blog` it also loads on the "Explore Our Projects" **listing** page, where there is no `.of4s-blog` wrapper, so its close button never wires up and a stuck full-screen overlay traps the visitor — keep it scoped to **`blog.post` only**; (b) the website builder can re-save the overlay in an `open` state with an image baked in, showing an un-closeable full-screen image on load — the overlay markup must start hidden (`class="of4s-lb"`, never `of4s-lb open`). Editing this view is **outside** the normal blog scope and needs explicit human authorization.

---

## Prerequisites (connections — set up by Andres, not in this repo)

This repo provides the *instructions and reference*; it does not provide the live connections. The Claude environment needs:

- **OF4S Odoo** connection pointed at the OF4S store's Odoo (NOT the accounting/JK Odoo), with permission to **create, read, AND update (`odoo_write`)** — update is needed to revise a draft and fix images in place without rebuilding the post. Access must be **limited to the `blog.post` and `ir.attachment` models** (plus read-only SQL for verification). If the connection also exposes `sale.order`, `account.move`, `purchase.order`, `res.partner`, or other business models, it is **too broad** — flag it to Andres and do not use them. `unlink`/delete: only with explicit per-action human approval. (Editing website views — e.g. the blog lightbox — is outside this scope and needs separate, explicit authorization.)
- **Google Drive** access to read the project-photos folder.

If either is missing, tell the user to ask Andres to connect it — do not proceed without them.
