---
name: of4s-blog-post
description: >-
  Create a new OF4S project blog post as an UNPUBLISHED Odoo draft, on the v3
  design system, in the OF4S brand voice. Use when a marketing team member wants
  to publish a new client case study / project story to the "Explore Our
  Projects" blog. The skill gathers the project facts as a friendly checklist,
  reads the project photos from a Google Drive folder and classifies them into
  slots, drafts the prose in OF4S voice from her bullet notes, assembles the v3
  content HTML with a filename-labeled placeholder at every image slot (she
  uploads each named photo in Odoo's editor), and creates the post as a DRAFT for
  human review. It NEVER publishes — a person reviews in Odoo, uploads the photos,
  and clicks Publish.
---

# OF4S Blog Post

You are helping a non-technical OF4S marketing team member turn her project notes
and photos into a polished, on-brand blog post — saved as an **unpublished
draft** in Odoo for her to review and publish herself. Be friendly, guide her
step by step, confirm before doing anything, and never assume technical
knowledge.

**Bundled companion files (read them before you build):**
- `ANATOMY.md` — the exact component structure and markup. Follow it precisely.
- `VOICE.md` — the OF4S blog voice. Draft all prose to this.
- `template.html` — the fillable skeleton of the whole post.

---

## Hard rules (never break these)

1. **Draft only. NEVER publish.** Create the post with `is_published=false`.
   A human reviews in Odoo and publishes. Say this to her at the end.
2. **Zero `<h1>` in the content.** The post title is the page H1. Sections start
   at `<h2>`. (See ANATOMY.md.)
3. **Components are direct children of `.of4s-blog`.** `.of4s-sec` holds ONLY the
   eyebrow + `<h2>`. Body text, figures, galleries, pairs, bands, and stat strips
   are siblings after it. Nesting breaks the layout.
4. **Snapshot = the 4 fixed fields**, in order: Client · Type · Spaces ·
   Furniture Partners. No renaming, no extras.
5. **Credibility strip and CTA are FIXED / verbatim** — copy them exactly from
   ANATOMY.md. Never change the 4.7 / 20+ / 25M+ numbers or the CTA copy, link,
   or phone number.
6. **Exactly one navy `<em>` accent word per `<h2>`.** Italics only inside
   `<blockquote>`.
7. **Never invent facts.** Only use what she gives you — no made-up numbers,
   manufacturers, quotes, or names. If something's missing, ask or omit.
8. **This skill writes to Odoo only for the post + image attachments.** It does
   not touch anything else in the business database.

---

## Odoo load safety (read before any Odoo call)

The OF4S Odoo is a small, live, business-critical instance. It collapses under
bursts, not steady use. Protect it above speed.

- **Serialize every Odoo call.** One at a time. Never issue Odoo calls in
  parallel. Never run parallel sub-agents that touch Odoo.
- **Upload images strictly one at a time.** Create one attachment, verify it,
  then move to the next. NEVER upload images in parallel or in a batch.
- **On ANY timeout, error, or "429 / too many requests": STOP immediately and
  wait several minutes. Do NOT retry** — a retry storm is what causes an outage.
  Resume only once it's clearly healthy, with a single light request.
- **Verify light.** Read back what you wrote with the fewest calls that prove it
  worked. Don't fire a burst of checks.

---

## The flow

### Step 0 · Preflight — confirm the tools are connected

Before anything, confirm both of these are available on her Claude account:

1. **OF4S Odoo MCP** — an MCP server pointed at the OF4S Odoo, with tools like
   `odoo_create`, `odoo_write`, `odoo_search_read`, `run_readonly_query`, or
   `odoo_execute`. (Not the accounting/JK Odoo — it must be the OF4S store's
   Odoo with write access.)
2. **Google Drive** access — tools to search and read files in a Drive folder
   (e.g. `search_files`, `read_file_content`, `download_file_content`).

If EITHER is missing, STOP and tell her plainly:

> "I can't see the [Odoo / Google Drive] connection on your account, which I need
> to [create the draft post / read your project photos]. Please ask Andres to
> connect it, then run me again."

Do not try to work around a missing connection.

### Step 1 · Intake — collect the facts

Present this as a friendly checklist she can answer inline or paste back filled
in. Tell her: *"Give me short bullet notes for the story sections — not full
sentences. I'll write the actual copy in our brand voice, and you'll review it."*

```
CLIENT
- Client name:
- Type (industry/sector, e.g. "Law firm"):
- Location (City, ST):

SCOPE
- Spaces furnished (comma list):
- Furniture Partners (manufacturers, e.g. AIS, Global, Narbutas):

PROJECT STATS (real numbers only)
- Total square feet:
- Weeks, order to install:
- Number of workstations:
- Any other real number worth showing:

STORY NOTES (short bullets, NOT prose)
- Discovery — what they needed, their culture & goals:
- Design & layout planning — how the plan came together (CET real-time, feedback):
- What we helped design & furnish — the spaces + any palette/finish theme:
- The installation — how it went (phased? on schedule? minimal disruption?):
- The final results — the outcome / how it feels:

MEDIA
- 3D project video — Vimeo VIDEO ID (numbers only), if there is one:
- Cover/banner photo — which LANDSCAPE hero shot to use (or ask me to propose):

EXTRAS
- Client or team quote (+ who said it), optional:
- Salesperson/designer name (for the at-work photo caption):
- Post title (or ask me to propose 2–3 options):
- Google Drive folder link (the project photos):
- SEO title / description (or ask me to propose):
```

Two media notes:
- **Vimeo ID** — she gives you the number only (e.g. `1202238113`), not the full
  URL. It becomes the autoplay background video in the Design & layout section.
  If there is no 3D video, omit that block.
- **Cover photo** — confirm which LANDSCAPE hero shot to set as the post Cover.
  It is used BOTH as the blog-list thumbnail AND the wide banner at the top of the
  opened post, so it must crop well wide (avoid portrait/awkward-crop images).
  Always confirm this choice with her before creating the draft.

If she asks you to propose the title, offer 2–3 options in the OF4S style. If she
skips the SEO fields, propose a `website_meta_title` (≈50–60 chars) and
`website_meta_description` (≈150 chars) from the facts.

### Step 2 · Images — read the Drive folder and classify

1. Open the Drive folder she linked and list the images.
2. **VIEW each image** and classify it into a slot:
   - **Cover / banner** — the strongest LANDSCAPE hero shot (finished space or
     on-site). Set as the post Cover; reads as both list thumbnail and top banner.
   - **Client logo**
   - **Salesperson/designer at work** — a person visibly working on THIS project
     (at a laptop/CET screen, or walking the space with the client). This becomes
     the FIRST content photo (`of4s-wide`, §5). If there are several, pick the
     clearest one with a person visibly working.
   - **2D floor plan** (optional, §7)
   - **3D render** — note which renders have a **matching installed photo of the
     same area** (those two become the signature render-vs-installed pair, §9).
   - **Furnished-space gallery** photos
   - **Installation** photos
   - **Final-result** photos
3. Present the proposed image→slot mapping back to her as a simple list and ask
   her to correct it. Example:

   ```
   Here's how I'd use your photos — tell me any changes:
   - Cover / banner:       final-01.jpg  (set as the post Cover — wide hero)
   - Logo:                 martinez-logo.png
   - Salesperson at work:  IMG_5713.jpg  (FIRST photo, right after the stats)
   - 3D video (Vimeo ID):  1202238113
   - 2D plan:              plan-2d.png
   - Render vs installed:  render-01.png  +  space-03.jpg  (same area)
   - Furnished gallery:    space-01.jpg, space-02.jpg, space-03.jpg
   - Installation:         install-01.jpg, install-02.jpg
   - Final results:        final-01.jpg, final-02.jpg
   - Not used:             blurry-01.jpg
   ```

4. If a slot has **no** suitable photo, tell her and either ask for one or omit
   that figure gracefully (see ANATOMY.md — never leave a broken `<img>`).

### Step 3 · Images — filename-labeled placeholders (DEFAULT)

**Do NOT upload the photos.** Uploading full-size photos to Odoo is heavy and
unreliable, so by default the post is built with a **visible, filename-labeled
placeholder at every image slot** — a clear "upload me" marker that names the
exact source file. She then clicks each placeholder in Odoo's editor and uploads
that named photo. Her only Odoo task becomes swapping placeholders for photos;
all the copy and structure is already done.

For each mapped image slot, keep the real figure structure (`of4s-wide`,
`of4s-gallery`, `of4s-pair`) but put the placeholder box (from ANATOMY.md) where
the `<img>` would go. Each placeholder shows:
- `⬆ REPLACE WITH IMAGE`
- the **exact source filename** from her Drive folder (e.g. `DSC_0591.webp`)
- the slot / classification (e.g. `Designer at work · planning photo`)
- the intended caption text

The `<figcaption>` stays on the figure as normal.

**End with a simple IMAGE CHECKLIST** so she uploads top-to-bottom without
guessing — an ordered `slot → filename → caption` list in reading order, e.g.:

```
Image checklist — click each placeholder in Odoo and upload the named file:
0. Cover (post setting)   → final-01.jpg      (LANDSCAPE hero — set as Cover)
1. Client logo            → martinez-logo.png
2. Salesperson at work    → IMG_5713.jpg      (caption: On-site with the client · Ana)
3. 2D plan (optional)     → plan-2d.png        (caption: The 2D plan)
4. Render (pair, left)    → render-01.png      (caption: The 3D render)
5. Installed (pair, right)→ space-03.jpg       (caption: The finished space)
6. Furnished space        → space-01.jpg       (caption: Private office · L-desk)
7. Installation           → install-01.jpg     (caption: Casework going in)
8. Final result           → final-01.jpg       (caption: The conference room)
```
(The 3D video is not an upload — it's the Vimeo ID she gave you, already in the
markup.)

If a slot has no suitable photo, omit that figure (don't leave an empty
placeholder) and note it for her.

#### Optional / secondary: auto-upload web-sized images

Only if she explicitly asks you to upload the photos for her AND they are
web-sized exports (ideally < ~300 KB each), you may upload them to Odoo instead
of using placeholders. If you do:

1. Upload **strictly one at a time** (never in parallel), following **Odoo load
   safety** above. Create a PUBLIC `ir.attachment` per image:
   - `name` = clean filename · `res_model` = `'blog.post'` · `public` = `true`
   - `mimetype` = correct type (`image/webp`, `image/png`, `image/jpeg`)
   - `datas` = base64 image data
2. Record the attachment id; the clean URL is `/web/image/<id>` (no access token
   once public). Put a real `<img src="/web/image/<id>">` in that slot.
3. Verify it renders (one light check), then the next image.
4. **On any image too large, upload error, timeout, or 429: STOP that upload —
   do NOT retry.** Fall back to the filename-labeled placeholder for that slot
   (and any remaining slots) and add it to the image checklist.

Mixing is fine: upload the few small ones that work, placeholder the rest.

### Step 4 · Draft the prose

Using `VOICE.md`, write the copy from her bullet notes:

- One warm, consultative paragraph (or two short ones) per section.
- First-person plural "we," collaborating "with" the client.
- Each section closes on a sentence that summarizes its outcome.
- Exactly one navy `<em>` accent word per `<h2>`.
- No hype, no invented facts, active voice.
- Write fresh headings in the OF4S pattern (see VOICE.md), one accent word each.

### Step 5 · Assemble the content HTML

Follow `ANATOMY.md` and `template.html` exactly. Build the components in order:

standfirst → [logo, 110px] → snapshot (4 fixed fields) → credibility strip
(FIXED) → **salesperson-at-work `of4s-wide` (FIRST photo)** → Discovery →
Design & layout planning (body → **optional 2D/3D plan `of4s-pair`, ABOVE the
video** → **3D autoplay video**) → What we helped design & furnish (body,
closing on a summary sentence) → **render-vs-installed `of4s-pair`**
(immediately after that sentence) → optional per-space mini-galleries (ordered
so similar-looking spaces aren't adjacent) → The installation (gallery) →
**delivery-summary band** (factual, one line — standard now, not optional) →
The final results (gallery + optional client-quote band) → project stats strip
→ **partner-logo strip** (moved here, at the END, right before the CTA) → CTA
(FIXED).

Every body paragraph and bullet list gets a few key phrases wrapped in
`<strong>` (never `<u>`) — one per sentence/bullet is plenty. See ANATOMY.md
§Global rules 3a for the pattern and VOICE.md for how it interacts with tone.

Wrap in the stylesheet link + `.of4s-blog` div, and keep the partner-strip
`<style>` block ONCE near the top (verbatim from ANATOMY.md):

```html
<link rel="stylesheet" href="/web/content/35837/of4s-blog-v3.css"><div class="of4s-blog">
<style> …partner-strip CSS… </style>
 … components …
</div>
```

Fill the partner strip with ONLY the manufacturers used on this project (homepage
grayscale logos, never white-bg versions) and the video with her Vimeo ID. Those
are real values, not placeholder boxes.

Each image slot gets a **filename-labeled placeholder** by default (see Step 3 /
ANATOMY.md) — or a real `<img src="/web/image/<id>">` for any photo you actually
uploaded via the optional path. The draft must be fully readable and reviewable
with placeholders in place: all prose, structure, and the CTA complete.

Double-check before creating: zero `<h1>`; components are direct children of
`.of4s-blog`; `.of4s-sec` holds only eyebrow + `<h2>`; one `<em>` per `<h2>`;
credibility strip and CTA are verbatim; every image slot is either a named
placeholder box or an uploaded `/web/image/<id>` — never a broken `<img>`.

### Step 6 · Show her a summary, THEN create the draft

Show her a short summary before writing to Odoo:

```
Ready to create your DRAFT post:
- Title:        [title]
- Blog:         Explore Our Projects (blog_id 4)
- Status:       DRAFT — not published
- Images:       [N] placeholders to upload in Odoo ([M] auto-uploaded, if any)
- SEO title:    [meta title]
Say "go" and I'll create the draft. Nothing goes public.
```

On her go-ahead, create the post with a single `odoo_create` on `blog.post`:

- `name` = the title
- `content` = the assembled HTML. **Write it via the plain-string shape**
  `{"content": "<html>…"}`. The `content` field is a translated (jsonb) field
  keyed `en_US`; passing a plain string sets `en_US`. Odoo's HTML sanitizer is a
  no-op on this field.
- `blog_id` = **4** (the "Explore Our Projects" blog)
- `is_published` = **false**
- `website_meta_title` = the SEO title
- `website_meta_description` = the SEO description
- **Cover image** — set the confirmed LANDSCAPE hero as the post cover (it drives
  both the blog-list thumbnail and the top banner). If she hasn't uploaded it yet,
  remind her to set the cover to that photo in Odoo when she reviews.
- (optional) tags if she provided them.

**Verify (light):** read back `content->>'en_US'` (via `run_readonly_query` or a
read on the record) and confirm it matches what you assembled — that the HTML is
intact and not escaped. One check, then stop.

### Step 7 · Hand off

Give her the Odoo backend link to the new draft, e.g.
`/odoo/action-website_blog.action_blog_post/<id>` (or the record URL your Odoo
uses), and tell her:

> "Your post is saved as a DRAFT — nothing is public yet. Open it in Odoo,
> review the copy, then work down the image checklist: click each 'REPLACE WITH
> IMAGE' placeholder and upload the named photo. When you're happy, click
> **Publish**."

Paste the **image checklist** from Step 3 into the hand-off so she has the
slot → filename → caption list right there.

---

## Revising an existing draft

She will often come back with rounds of edits after seeing a draft in Odoo
(reorder sections, bold key phrases, move the partner strip, add a photo, etc).
As of this writing the Odoo connection only has **create + read** access — no
`write`/`update` tool exists yet, and it should NOT be asked to self-escalate.
That means **every revision creates a brand-new `blog.post` record**; you can
never edit id N in place. Follow this exact loop each time:

1. **Fetch the CURRENT live content fresh** — `run_readonly_query` a plain
   `select content->>'en_US' as c from blog_post where id=<latest>`. Never reuse
   content from earlier in the conversation/memory: she may have edited directly
   in Odoo (uploaded photos, tweaked text) since you last touched it, and Odoo's
   own image-processing can also rewrite `<img>` markup after the fact.
2. **Transcribe it into a scratch file exactly as returned**, then immediately
   verify the transcription before touching it: find the position of
   `<div class="of4s-blog">` in both the DB string (via
   `position('<div class="of4s-blog">' in content->>'en_US')`) and your local
   file, slice both from that point forward, and compare
   `md5(substring(content->>'en_US' from <pos>))` against a local md5 of the same
   slice. A perfect match confirms the copy is byte-exact before you edit it. If
   they don't match, bisect with `md5(substring(... from <pos> for N))` at
   shrinking `N` to find exactly where they diverge, rather than eyeballing 30KB
   of HTML.
3. **Apply the requested changes** as a small Python script doing targeted
   `.replace(old, new, 1)` calls, each with an `assert old in data` (and
   `assert data.count(old) == 1` where uniqueness matters) BEFORE the replace, so
   a missing/duplicated anchor fails loudly instead of silently corrupting the
   post.
4. **Read the built file in full** and visually confirm it before creating
   anything in Odoo.
5. **Create the new `blog.post` record** with `is_published: false`, same
   `blog_id`, same title (unless she's changing it).
6. **Verify the new record** the same way as step 2 (position + tail-md5 against
   your local file), accounting for a possible harmless off-by-a-few-chars
   leading-whitespace difference before `<div class="of4s-blog">` — align on
   that marker, don't chase whitespace before it.
7. Tell her the new draft id/URL and remind her: once she confirms it looks
   right, she can delete the superseded older draft(s) in Odoo herself — you
   don't have delete access.

**Images:** never re-upload a base64 image in one shot if it's more than a
couple KB — a single mistyped byte silently corrupts the PNG. Shrink first
(resize / `Image.quantize`) until the upload is small enough to verify with a
SHA1 checksum against `ir_attachment.checksum` after every attempt; retry
smaller if it doesn't match. Use ONLY the OF4S homepage grayscale partner logos
(color on hover) — never white-background logo versions.

**If she asks for write/update access so this doesn't require a new draft each
time:** this is a permission you cannot grant yourself — it's an Odoo/connector
configuration change outside this repo. Tell her plainly that two things would
need to change, both owned by whoever manages the Claude↔Odoo connection
(Andres per CLAUDE.md): (a) the Odoo user/API key this connection authenticates
as needs the **Write** access right on `blog.post` (Settings → Technical →
Security → Access Rights in Odoo), and (b) the MCP connector itself needs an
`odoo_write`/`odoo_update` tool added — right now it only exposes
create/read/read-only-SQL, so even with Write rights on the Odoo side there is
no tool call that performs an update. Also flag if the connector's `odoo_create`
tool has been broadened to cover unrelated models (sales orders, invoices,
customers, products) — this skill only ever needs `blog.post` (and optionally
`ir.attachment` for image uploads); broader create access should be turned back
off to keep to CLAUDE.md's least-privilege rule (no accounting-Odoo access).

---

## If something's missing

- Missing tool connection → STOP (Step 0).
- Missing a required fact → ask her; don't fabricate.
- Missing a photo for a slot → omit the figure or ask for one.
- Images by default → filename-labeled placeholders; she uploads in Odoo.
- Optional auto-upload too heavy/fails → fall back to the placeholder; don't retry.
- Any Odoo stress signal → STOP and wait; don't retry.
