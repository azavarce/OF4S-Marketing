# Install & Setup — of4s-blog-post skill

For Andres. This sets up the marketing manager so she can create on-brand OF4S
project blog posts as unpublished Odoo drafts, herself, from her own Claude
account.

---

## What this skill does

She gives Claude her project notes (bullet points) and a Google Drive link to the
photos. Claude:
1. Collects the facts via a checklist.
2. Reads and classifies the Drive photos into slots and confirms the mapping.
3. Drafts the copy in the OF4S brand voice.
4. Assembles the full v3-design post with a **filename-labeled placeholder at
   every image slot**.
5. Creates the post in Odoo as a **DRAFT** (`is_published=false`) on the "Explore
   Our Projects" blog.
6. Hands her a review link + an image checklist.

She reviews in Odoo, clicks each placeholder to upload the named photo, and
publishes when happy. **The skill never publishes.**

---

## Install

Copy the whole `of4s-blog-post/` folder into her Claude skills directory:

```
~/.claude/skills/of4s-blog-post/
├── SKILL.md
├── ANATOMY.md
├── VOICE.md
├── template.html
└── INSTALL.md
```

The folder is self-contained — she does not need the OF4S_Brain repo. All five
files must travel together (SKILL.md reads ANATOMY.md, VOICE.md, and
template.html as companions).

---

## Prerequisites on her Claude account

Both connections must be present, or the skill stops at preflight and tells her to
ask you:

1. **OF4S Odoo MCP** — an MCP server pointed at the OF4S store's Odoo, with
   **write access** (tools like `odoo_create`, `odoo_write`, `odoo_search_read`,
   `run_readonly_query`, `odoo_execute`). This is the OF4S website Odoo, not the
   accounting/JK instance.
2. **Google Drive** access — so Claude can read the project photo folder she
   links (search + read/download file content).

---

## How she invokes it

- `/of4s-blog-post`, or
- just ask: *"Let's make a blog post for the [Client] project."*

Claude walks her through intake, image mapping, a summary, and creates the draft.

---

## Images — how it works today

- **Default = filename-labeled placeholders.** The post is built complete (all
  copy, structure, CTA) with a visible "REPLACE WITH IMAGE → filename" marker at
  each photo slot. In Odoo's blog editor she clicks each placeholder and uploads
  the named photo. This is reliable and needs no heavy upload.
- **Image-size guidance:** have her export **web-sized** images (ideally
  < ~300 KB each) before uploading in Odoo — faster and lighter on the instance.
- **Optional auto-upload:** if she asks, Claude can upload web-sized images
  directly to Odoo (public `ir.attachment`, one at a time, with back-off). This
  is the one part with a technical limit today: full-size photos are heavy and
  can fail, so the reliable path is the placeholder + manual upload.

---

## Known limitation & future option

**Limitation:** pushing image bytes through the tools is the weak point — heavy
files fail. That's why placeholders (manual upload in Odoo) are the default.

**Future option:** an **n8n Drive → Odoo image sync** — watch the project Drive
folder, resize to web dimensions, and create the public `ir.attachment` records
automatically, so the skill can drop real `/web/image/<id>` URLs and the whole
thing is hands-off. Worth building once the blog cadence justifies it.

---

## Load safety (important)

The OF4S Odoo is small and business-critical. The skill is written to serialize
every Odoo call, upload images one at a time (only on the optional path), and
back off on any timeout/429. Do not modify it to parallelize Odoo work.
