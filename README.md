# OF4S Marketing

Your Claude toolkit for creating OF4S marketing content — blog posts, Instagram
sets, email campaigns, flyers, and more. Open this repository in Claude, tell it
what you're making, and it does the heavy lifting on the OF4S v3 design system.
You review and publish.

---

## How it's organized

```
OF4S-Marketing/
├── projects/          ← your work, one folder per project
│   ├── blog/          ← the "Explore Our Projects" blog workflow
│   └── _template/     ← starting point for a new kind of project
├── design-system/     ← the OF4S v3 brand system (LOCKED — never edited)
├── .claude/           ← the skills + guardrails Claude uses (you don't open this)
├── CLAUDE.md          ← instructions Claude reads automatically
└── README.md          ← you are here
```

Each project folder has its **own instructions**, so Claude behaves differently
per project — a blog post, an email, and a flyer each get their own checklist and
rules. See `projects/README.md`.

---

## Create a blog post

1. **Open this repo in Claude.**
2. Say: **"Create a new blog post."**
3. Answer Claude's checklist — client name, type (industry), city/state; the
   spaces you furnished and furniture partners used; project numbers (sq ft,
   weeks, workstations); a few bullet notes for each story section; an optional
   client quote; the salesperson/designer name; and the Vimeo video ID.
4. **Point Claude at a Google Drive folder** with the project photos. It looks at
   each photo, figures out what it is, and shows you the plan. Correct it if
   needed.
5. Claude builds the whole post as a **DRAFT in Odoo** — copy, structure, and a
   labeled placeholder at each photo spot (e.g. "REPLACE WITH → `DSC_0591.webp`").
6. Claude gives you a **link and a photo checklist.** Open the draft in Odoo,
   swap each placeholder for its photo, pick a cover image, give it a final read
   — then click **Publish**.

**Nothing publishes automatically.** You always review and publish yourself.

---

## Start a different kind of project

Tell Claude, e.g. **"Set up a new Instagram project"** (or email campaign,
flyer…). Claude copies the `_template/` scaffold to a new project folder and
works with you to define how it should behave — what to collect, what to produce,
and the rules. You don't have to plan it all up front; it takes shape as you go.

---

## What's protected

- **The design system can't be changed.** `design-system/` is locked — Claude
  will refuse edits to it. Everything else builds *from* it. This keeps the brand
  consistent no matter what you're making.
- **The blog-creation skill is change-protected.** It rarely needs changing, so
  if you ever ask Claude to modify it, Claude will first check: *"You're asking
  me to change the blog-creation skill — are you sure?"* Say yes and it proceeds.
  This prevents accidental changes to the thing that builds your posts.

(Both are enforced by a guard in `.claude/`, not just by good intentions.)

---

## One-time setup (ask Andres if it's not done)

For Claude to reach the tools it needs, your Claude needs connections turned on:

- **OF4S Odoo** — so Claude can create draft blog posts (create/read only — it
  can't delete or change anything else).
- **Google Drive** — so Claude can read your project-photo folders.
- Other connectors as new project types need them.

If Claude says a connection is missing, ask Andres to enable it.

---

## Tips

- **Photos:** put all the photos for one post in a single Google Drive folder.
  Helpful filenames (e.g. `reception.jpg`, `3d-render.jpg`) make Claude's job
  easier, but it can also tell from the image itself.
- **Cover image:** pick a wide, attractive photo — it's both the blog-list
  thumbnail and the banner at the top of the post.
- **The video** plays automatically in the background (muted, looping, no
  buttons) — just like the South Florida Donor Network post.
