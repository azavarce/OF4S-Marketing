# Project: Blog — "Explore Our Projects"

Claude's behavior when working in `projects/blog/`. This layers on top of the
root `CLAUDE.md`; the root hard rules still apply.

## What this project is

Client case-study / project-story posts for the OF4S **"Explore Our Projects"**
blog, created as **unpublished drafts in Odoo** for a human to review, drop
photos into, and publish.

## How to work

**Use the `of4s-blog-post` skill** — `.claude/skills/of4s-blog-post/SKILL.md`.
Follow it exactly. In short it:

1. Collects project facts as a friendly checklist (client, type, city/state,
   spaces, furniture partners, stats, short notes per story section, an optional
   client quote, the salesperson/designer name, the Vimeo video ID).
2. Reads and classifies the project photos from a **Google Drive folder** the
   user provides, then confirms the mapping.
3. Drafts the copy in the **OF4S brand voice**
   (`.claude/skills/of4s-blog-post/VOICE.md`) from the user's bullet notes.
4. Assembles the post to the standardized **anatomy**
   (`.claude/skills/of4s-blog-post/ANATOMY.md`), with a filename-labeled
   placeholder at every image slot.
5. Creates the post in Odoo as an **UNPUBLISHED DRAFT**.

The reusable template lives in Odoo as **"TEMPLATE — OF4S Project Post (copy
me)"** (unpublished); `.claude/skills/of4s-blog-post/template.html` mirrors it.

## Hard rules for this project

1. **Drafts only — never publish.** A person reviews in Odoo, adds photos, and
   clicks Publish.
2. **Protect the Odoo instance.** Serialize every Odoo call (never in parallel),
   upload images one at a time, verify lightly. The moment any call times out or
   returns 429 / "too many requests," **STOP and wait — do NOT retry.**
3. **Never invent facts.** Client names, numbers, quotes, spaces, and partners
   come only from the user or a verified source. Placeholders stay placeholders
   until filled with real info.
4. **Zero `<h1>` in blog content** — the post title is the page heading. One
   upright navy `<em>` accent word per `<h2>`.
5. **Use the homepage grayscale partner logos** (color on hover), never the
   white-background versions.

## Changing the skill

The `of4s-blog-post` skill is change-protected: any edit to it requires the
user's explicit confirmation (the guard hook will ask). Don't refactor it as a
side effect of a blog task — only touch it when the user has clearly asked to
change the skill and confirmed.

## Local files

This folder is a fine place for working notes, drafts, and photo checklists for
a post in progress. The published artifact itself lives in Odoo, not here.
