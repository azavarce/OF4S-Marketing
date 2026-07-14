# OF4S Marketing

Your Claude toolkit for creating OF4S marketing content — starting with **blog posts** for the "Explore Our Projects" blog. Open this repository in Claude, and Claude will do the heavy lifting; you review and publish.

---

## Create a new blog post

1. **Open this repo in Claude** (Claude Code).
2. Say: **"Create a new blog post."**
3. Claude will ask you for the project details — answer the checklist:
   - **Client name**, **Type** (their industry, e.g. "Law firm"), and **City, State**
   - **Spaces** you furnished and the **furniture partners** (manufacturers) used
   - **Project numbers:** total sq ft, weeks (order to install), number of workstations
   - **Short notes** (a few bullets each) for: Discovery, Design & Planning, the Spaces, the Installation, and the Final Result — Claude writes the polished copy from your notes
   - An optional **client quote** and who said it
   - The **salesperson/designer** name (for the planning photo caption)
   - The **Vimeo video ID** of the project walkthrough (just the number)
4. **Point Claude at a Google Drive folder** with the project photos. Claude looks at each photo, figures out what it is, and shows you the plan (which photo goes where). Correct it if needed.
5. Claude builds the whole post as a **DRAFT in Odoo** — all the copy, structure, and a labeled placeholder at each photo spot (e.g. "REPLACE WITH → `DSC_0591.webp`").
6. Claude gives you a **link and a photo checklist.** Open the draft in Odoo, swap each placeholder for its photo, pick a nice cover image, give it a final read — then click **Publish**.

**Nothing publishes automatically.** You always review and publish yourself.

---

## What's in here

- **`.claude/skills/of4s-blog-post/`** — the blog-post skill Claude follows (you don't need to open this).
- **`design-system/`** — the complete OF4S v3 design system (brand colors, type, logo, components). This is here so Claude can help you build *other* branded assets down the road, not just blog posts.
- **`CLAUDE.md`** — the instructions Claude reads automatically when you open the repo.

---

## One-time setup (ask Andres if it's not done)

For Claude to reach the blog, your Claude needs two connections turned on:

- **OF4S Odoo** — so Claude can create the draft post (create/read only — it can't delete or change anything else).
- **Google Drive** — so Claude can read your project-photos folder.

If Claude says a connection is missing, ask Andres to enable it.

---

## Tips

- **Photos:** put all the project photos for one post in a single Google Drive folder. Helpful filenames (e.g. `reception.jpg`, `3d-render.jpg`) make Claude's job easier, but it can also tell from the image itself.
- **Cover image:** pick a wide, attractive photo — it shows as both the thumbnail in the blog list and the banner at the top of the post.
- **The video** plays automatically in the background (muted, looping, no buttons) — just like the South Florida Donor Network post.
