# OF4S Blog Post — Anatomy (v3 design system)

This is the canonical structure and EXACT component markup for an OF4S project
blog post. Build the `content` HTML from these components, in this order, using
the real project facts and images. Copy the markup verbatim and fill only the
`[bracketed]` placeholders.

---

## Global rules (non-negotiable)

1. **Zero `<h1>` in content.** The post title (the `name` field on `blog.post`)
   is the page H1. Every section heading in the body starts at `<h2>`.
2. **Exactly ONE upright-navy `<em>` accent word per `<h2>`.** The skin renders
   the `<em>` upright and navy (it is NOT italic here). Pick one meaningful word
   per heading and wrap only that word.
3. **Italics only inside `<blockquote>`.** Nowhere else.
3a. **Bold a few key phrases in every body paragraph and bullet list**, `<strong>`
   only — never `<u>`, never italics for emphasis. In each `<p>` or `<li>`, wrap
   the one phrase that carries the fact or benefit (a number, a capability, a
   timeframe) — e.g. `<li><strong>Sizing the open workstation floor</strong> for
   the current team, with room to add seats as it grows</li>` or `<p>...gave them
   room to weigh in <strong>before a single piece was ordered</strong>.</p>`.
   Roughly one bolded phrase per sentence/bullet — enough to make the section
   skimmable, not so much that bolding stops meaning anything. Apply this to
   EVERY text-heavy section (Discovery, Design & layout planning, What we helped
   design & furnish, The installation, The final results), not just Discovery.
4. **Images: filename-labeled placeholders by default.** Uploading photos to
   Odoo is heavy and unreliable, so the DEFAULT build puts a visible, self-
   explanatory placeholder at every image slot (see "Image slots" below). Only
   use a real `<img src="/web/image/<id>">` when the photo was actually uploaded
   to this Odoo (owned images only — never hotlink external or `-redirect` URLs).
5. **Components are DIRECT children of `.of4s-blog`.** `.of4s-sec` wraps ONLY the
   eyebrow `<p class="of4s-eyebrow">` + the `<h2>`. Body paragraphs, lists,
   figures, galleries, pairs, quote bands, the video block, and stat strips are
   SIBLINGS that come AFTER the `.of4s-sec` block — never nested inside it.
   Nesting a wide block inside `.of4s-sec` breaks the full-width centering.
6. **Wrap the whole thing** in the stylesheet link + `.of4s-blog` div (below),
   and keep the partner-strip `<style>` block ONCE near the top.

---

## Cover / banner image (set this in Odoo, not in the content HTML)

Every post needs a **Cover image** set in Odoo's post settings — it is used BOTH
as the card thumbnail on the "Explore Our Projects" blog list AND as the wide
banner at the top of the opened post.

- Pick a strong **LANDSCAPE** hero photo (a finished-space or on-site shot that
  reads well wide).
- It must survive two crops: a small list thumbnail AND a wide top banner.
  **Avoid portrait or awkward-crop images** — pick one that crops well wide with
  the subject roughly centered.
- Always confirm the cover-photo choice with the marketing manager before
  creating the draft (see SKILL.md intake).

---

## Image slots — the placeholder pattern (DEFAULT)

Every figure below shows an `<img src="[/web/image/…]">`. In the **default build**
you do NOT have uploaded images — instead you replace each `<img>` with a
**filename-labeled placeholder box** so the marketing manager can see exactly
which photo to drop into which slot in Odoo's editor. The placeholder must render
as a clear "upload me" marker, never a broken image.

**Placeholder markup — use this in place of every `<img>`:**

```html
<span class="of4s-imgslot" style="display:block;border:2px dashed #b0b7c3;border-radius:10px;padding:1.6em 1em;text-align:center;background:#f4f6f9;color:#3a4353;font-family:Arial,Helvetica,sans-serif;line-height:1.4;">
  <span style="display:block;font-weight:700;letter-spacing:.06em;font-size:.85em;">⬆ REPLACE WITH IMAGE</span>
  <span style="display:block;font-size:1.15em;font-weight:700;margin-top:.35em;">[EXACT-SOURCE-FILENAME]</span>
  <span style="display:block;font-size:.85em;margin-top:.25em;">Slot: [classification, e.g. Salesperson at work · first photo]</span>
  <span style="display:block;font-size:.8em;margin-top:.25em;color:#6b7480;">Caption: [intended figcaption text]</span>
</span>
```

Rules for placeholders:
- Keep the surrounding figure structure exactly (`of4s-wide`, `of4s-gallery`,
  `of4s-pair`) — only the `<img>` is swapped for the placeholder `<span>`.
- Show the **exact source filename** from her Drive folder (e.g. `DSC_0591.webp`),
  the slot classification, and the intended caption.
- Keep the real `<figcaption>` on the figure as normal (below the placeholder).
- When a photo IS uploaded (optional path), use the real `<img src="/web/image/<id>">`
  instead of the placeholder for that one slot.
- The **partner-logo strip and the 3D video are NOT placeholders** — the partner
  logos are stable homepage assets (`/web/image/<id>`) and the video is a Vimeo
  ID she gives you. Fill those with real values, not upload boxes.

The finished draft must be fully readable and reviewable with placeholders in
place: all text, structure, and the CTA complete, so her only remaining Odoo task
is swapping each named placeholder for its photo.

---

## Component order (build ALL of these, in this order)

1. Standfirst
2. Client logo (optional, **110px, readable**)
3. Snapshot (4 fixed fields)
4. Credibility strip (FIXED — 4.7 / 20+ / 25M+)
5. **Salesperson-at-work `of4s-wide` — the FIRST content photo**
6. Discovery
7. Design & layout planning (text + **optional 2D/3D plan `of4s-pair`, ABOVE the
   video** + **3D autoplay video**)
8. What we helped design & furnish (head + intro + space list)
9. **Render-vs-installed `of4s-pair`** — signature OF4S element, directly under
   the closing sentence of §8
10. (Optional) per-space mini-sections/galleries — see "Breaking out per-space
    galleries" below
11. The installation (gallery)
12. **Delivery-summary band** (`of4s-band`, factual, one line) — right before
    The final results
13. The final results (gallery + optional quote band)
14. Project stats strip
15. **Furniture-partner logo strip** — at the very end, after the stats, right
    before the CTA
16. CTA (FIXED)

---

## Root wrapper + partner-strip style

```html
<link rel="stylesheet" href="/web/content/35837/of4s-blog-v3.css"><div class="of4s-blog">
<style>
.of4s-blog .of4s-partners{display:flex;justify-content:center;align-items:center;gap:40px;flex-wrap:wrap;margin-top:16px}
.of4s-blog .of4s-partners img{height:40px;width:auto;object-fit:contain;filter:grayscale(1);opacity:0.75;transition:filter .2s ease,opacity .2s ease}
.of4s-blog .of4s-partners img:hover{filter:grayscale(0);opacity:1}
</style>
  <!-- all components here, as direct children -->
</div>
```

The skin lives at CSS attachment `35837` (`of4s-blog-v3.css`). Keep this link and
the `.of4s-blog` wrapper on every post. The `<style>` block powers the partner
strip (§8); keep it ONCE near the top — it rides inside the post content and
survives the blog sanitizer (do NOT move partner CSS to a shared view or CSS
attachment).

---

## 1 · Standfirst

Mono-caps eyebrow (`Project story · [Type] · [City, ST]`) + a 2–3 sentence lede.

```html
<div class="of4s-standfirst">
  <p class="of4s-eyebrow">Project story · [Type] · [City, ST]</p>
  <p class="of4s-lede">[2–3 confident, warm sentences: who the client is, what they set out to build, and OF4S's role — design, furnish, install.]</p>
</div>
```

## 2 · Client logo (optional)

Centered, owned `/web/image` only. Omit the block if there is no clean logo. The
final size depends on each company's logo, but it MUST be **large enough to
READ** — `max-height:110px` is the readable default; keep `width:auto`.

```html
<div style="text-align:center;margin:0 auto 2.5em;">
  <img src="[/web/image/…]" alt="[Client] logo" style="border:none;border-radius:0;max-height:110px;width:auto;">
</div>
```

## 3 · Snapshot — 4 FIXED fields, this order

Keep exactly these four fields, in this order. Do not add, remove, or rename.

- **Client** = client name
- **Type** = industry / sector (Law firm, Food distribution, School, …)
- **Spaces** = comma list of spaces furnished
- **Furniture Partners** = the manufacturers (AIS, Global, Narbutas, …)

```html
<dl class="of4s-snapshot">
  <div><dt>Client</dt><dd>[Client name]</dd></div>
  <div><dt>Type</dt><dd>[Industry/sector]</dd></div>
  <div><dt>Spaces</dt><dd>[Spaces furnished, comma list]</dd></div>
  <div><dt>Furniture Partners</dt><dd>[Manufacturers, comma list]</dd></div>
</dl>
```

## 4 · Credibility strip — FIXED, verbatim

Identical on every post. Do NOT edit these numbers or labels.

```html
<div class="of4s-stats">
  <div><h3>4.7</h3><p>Google rating</p></div>
  <div><h3>20+</h3><p>Years in business</p></div>
  <div><h3>25M+</h3><p>Sq ft furnished</p></div>
</div>
```

## 5 · Salesperson-at-work — the FIRST content photo

The very first photo the reader sees, right after the credibility strip. It MUST
be a **real photo of the OF4S salesperson/designer working on THIS project** —
on-site, at the CET screen, or walking the space with the client — NOT a finished
room. Full-width `of4s-wide`. The caption names them.

```html
<figure class="of4s-wide">
  <img src="[/web/image/…]" alt="[Salesperson name] on-site with the [Client] team">
  <figcaption>On-site with the client · [Salesperson / designer name]</figcaption>
</figure>
```

## 6 · Discovery

`.of4s-sec` (eyebrow + h2) followed by 1–2 body paragraphs as siblings.

```html
<div class="of4s-sec">
  <p class="of4s-eyebrow">Discovery</p>
  <h2>[Heading with one <em>accent</em> word]</h2>
</div>
<p>[What the client had and needed; who we sat down with; the cultural and operational requirements uncovered.]</p>
<p>[Optional second paragraph: departments, headcount, growth plans, the brief that came out of discovery.]</p>
```

## 7 · Design & layout planning

Text on how the plan came together (CET Designer, real-time iteration), then —
if you have BOTH a 2D floor plan AND a 3D plan/layout render — an `of4s-pair`
showing them side by side, **ABOVE** the video, then the project's **3D
walkthrough VIDEO** as an autoplay background (muted, looping, no controls —
same as the South Florida Donor Network post).

Paste the project's Vimeo **VIDEO ID (numbers only)** in place of `[VIMEO_ID]`.
Delete the video block if there is no 3D video. If there's only a 2D plan (no
matching 3D plan), use a single `of4s-wide` figure for it instead of a pair.

```html
<div class="of4s-sec">
  <p class="of4s-eyebrow">Design &amp; layout planning</p>
  <h2>[Heading with one <em>accent</em> word]</h2>
</div>
<p>[How the plan came together: CET Designer, real-time iteration, how feedback turned into layouts.]</p>
<div class="of4s-pair">
  <figure><img src="[/web/image/…]" alt="[Client] 2D floor plan"><figcaption>The 2D plan</figcaption></figure>
  <figure><img src="[/web/image/…]" alt="[Client] 3D plan"><figcaption>The 3D plan</figcaption></figure>
</div>
<div class="of4s-wide" style="aspect-ratio: 16 / 9;"><iframe src="//player.vimeo.com/video/[VIMEO_ID]?autoplay=1&amp;muted=1&amp;autopause=0&amp;controls=0&amp;loop=1" style="width:100%;height:100%;border:0;border-radius:8px;" frameborder="0" allowfullscreen="allowfullscreen"></iframe></div>
```

> Note: the `[VIMEO_ID]` placeholder's square brackets get URL-encoded by Odoo's
> sanitizer (`%5BVIMEO_ID%5D`) — harmless. A real numeric ID has no brackets, so
> the stored URL stays clean.

### If the client's video lives on YouTube instead of Vimeo

Some projects only have a YouTube video. Use this iframe pattern instead — the
query string minimizes YouTube's on-page branding (no controls/related
videos/keyboard, muted autoplay loop):

```html
<div class="of4s-wide" style="aspect-ratio: 16 / 9;"><iframe src="https://www.youtube.com/embed/[YOUTUBE_ID]?autoplay=1&amp;mute=1&amp;controls=0&amp;loop=1&amp;playlist=[YOUTUBE_ID]&amp;modestbranding=1&amp;rel=0&amp;iv_load_policy=3&amp;fs=0&amp;disablekb=1&amp;playsinline=1" style="width:100%;height:100%;border:0;border-radius:8px;" frameborder="0" allow="autoplay" allowfullscreen="allowfullscreen"></iframe></div>
```

`playlist=[YOUTUBE_ID]` (same ID repeated) is required for `loop=1` to work on a
single video. **Keep the source video's true aspect ratio** — don't force a crop
to 16:9 if the source is natively 4:3 or another ratio; check with the YouTube
oEmbed API (`https://www.youtube.com/oembed?url=...&format=json`) if unsure, and
set `aspect-ratio` on the wrapper to match rather than cropping content off.

## 8 · What we helped design & furnish

Body paragraph (optionally a `<ul>` of spaces) closing on a summary sentence
(e.g. "The result is an office with one shared identity from the lobby to the
last conference room."). The **furniture-partner logo strip does NOT go here**
— it now goes at the very end of the post, after the project stats and right
before the CTA (see §15). This section is just the intro text; the
render-vs-installed pair (§9) comes immediately after it.

```html
<div class="of4s-sec">
  <p class="of4s-eyebrow">What we helped design &amp; furnish</p>
  <h2>[Heading with one <em>accent</em> word]</h2>
</div>
<p>[Turnkey scope: the spaces furnished and how one consistent palette tied them together.]</p>
<ul>
  <li>[Space one]</li>
  <li>[Space two]</li>
  <li>[Space three]</li>
</ul>
<p>[Closing summary sentence for this section.]</p>
```

## 9 · Render-vs-installed pair — SIGNATURE OF4S element

Whenever you have a **3D render AND a photo of that SAME area already installed**,
pair them here: render on the left, the finished reality on the right. This is a
signature OF4S move — Andres loves it. Keep both captions exactly as below. Place
it **directly after §8's closing sentence** — before any per-space galleries.
Omit only if there is no render + matching installed photo.

```html
<div class="of4s-pair">
  <figure><img src="[/web/image/…]" alt="[Client] 3D render of the space"><figcaption>The 3D render</figcaption></figure>
  <figure><img src="[/web/image/…]" alt="[Client] the same space installed"><figcaption>The finished space</figcaption></figure>
</div>
```

### Breaking out per-space galleries (optional, for projects with many photos)

When there are enough categorized photos to justify it, instead of one combined
gallery under §8, give each named space its own mini `of4s-sec` (eyebrow + `<h2>`
with one `<em>` accent word) + gallery, right after the render-vs-installed pair
— e.g. Collaborative area, Lounge, Executive offices, Open workstations, Private
offices, Conference rooms, Lobby.

**Order them so two visually-similar spaces never sit back to back** — e.g. put
Collaborative area before Lounge (not after) if their photos read similarly, so
the reader isn't looking at two near-identical rooms in a row. Use judgment on
which spaces "read similarly" per project; when unsure, ask the marketing
manager which order she'd prefer.

## 10 · The installation

Body paragraph + install gallery.

```html
<div class="of4s-sec">
  <p class="of4s-eyebrow">The installation</p>
  <h2>[Heading with one <em>accent</em> word]</h2>
</div>
<p>[Our in-house team: delivery, placement to the approved plan, on schedule, minimal disruption.]</p>
<div class="of4s-gallery">
  <figure><img src="[/web/image/…]" alt="[alt]"><figcaption>[caption]</figcaption></figure>
  <figure><img src="[/web/image/…]" alt="[alt]"><figcaption>[caption]</figcaption></figure>
  <figure><img src="[/web/image/…]" alt="[alt]"><figcaption>[caption]</figcaption></figure>
</div>
```

## 11a · Delivery-summary band — RECOMMENDED, right before Final Results

A short, one-line **factual** summary of the delivery outcome, in a blue
`of4s-band`, placed right before "The final results" heading — e.g. "Both
floors delivered on time, fully furnished and ready for the team and their
clients." This is DIFFERENT from the client-quote band in §11 (below): this one
is written by you from verified project facts (schedule, phasing, readiness),
never a real quote, and never invented numbers not already given. Add it to
every post — it's now the standard, not optional. Omit only if you don't have
enough verified facts to summarize honestly.

```html
<div class="of4s-band">
  <p class="of4s-eyebrow">The result</p>
  <blockquote>[One factual sentence: delivered on schedule / through phased installation / ready for the team from day one — using only verified facts already in the post.]</blockquote>
</div>
```

## 11 · The final results

Body paragraph + a gallery of the finished space. The dark `of4s-band` CLIENT
QUOTE at the end is OPTIONAL — use a real client or team line, or omit the band
entirely. (This is separate from the delivery-summary band in §11a above, which
now precedes this section by default.)

```html
<div class="of4s-sec">
  <p class="of4s-eyebrow">The final results</p>
  <h2>[Heading with one <em>accent</em> word]</h2>
</div>
<p>[The finished office: what it reflects about the client's culture, how it works and feels now, the outcome delivered.]</p>
<div class="of4s-gallery">
  <figure><img src="[/web/image/…]" alt="[alt]"><figcaption>[caption]</figcaption></figure>
  <figure><img src="[/web/image/…]" alt="[alt]"><figcaption>[caption]</figcaption></figure>
  <figure><img src="[/web/image/…]" alt="[alt]"><figcaption>[caption]</figcaption></figure>
</div>
<div class="of4s-band">
  <p class="of4s-eyebrow">[label, e.g. In their words]</p>
  <blockquote>[A real client or team quote.]</blockquote>
  <p class="of4s-band-attr">[Name, Title, Client]</p>
</div>
```

## 12 · Project stats strip

2–3 proof numbers for THIS project. Frame lead time as "Weeks, order to install",
never "X-week install". Edit numbers per project. Use only real numbers from her
notes — do not invent.

```html
<div class="of4s-stats">
  <div><h3>[15,000]</h3><p>Square feet</p></div>
  <div><h3>[10]</h3><p>Weeks, order to install</p></div>
  <div><h3>[84]</h3><p>Workstations</p></div>
</div>
```

## 12a · Furniture-partner logo strip — end of post, before CTA

Place the partner-logo strip here, at the very end (after the stats, right
before the CTA) — NOT earlier in the post. Use ONLY the manufacturers actually
used on THIS project. These are the HOMEPAGE grayscale logos (color on hover) —
the standard. **Do NOT use white-background logo versions.** Available assets:

| Manufacturer | src | Manufacturer | src |
|---|---|---|---|
| AIS | `/web/image/6446` | OM Seating | `/web/image/6452` |
| Global Furniture Group | `/web/image/6448` | COE | `/web/image/6453` |
| Narbutas | `/web/image/6447` | OFGO | `/web/image/6454` |
| Enwork | `/web/image/6449` | Byrne | `/web/image/6455` |
| Corp Design | `/web/image/6451` | School Specialty | `/web/image/6456` |
| SitOnIt | `/web/image/6439` | 9to5 | `/web/image/6450` |

```html
<div style="text-align:center;margin:2.5em auto;">
  <p class="of4s-eyebrow" style="text-align:center;">Furniture partners on this project</p>
  <div class="of4s-partners">
    <img src="/web/image/6446" alt="AIS">
    <img src="/web/image/6448" alt="Global Furniture Group">
    <img src="/web/image/6447" alt="Narbutas">
    <!-- …only the manufacturers used on THIS project… -->
  </div>
</div>
```

## 13 · End-of-post CTA — FIXED & REQUIRED, verbatim

Keep the copy, the `/request-a-free-quote` link, and the `tel:` number exactly
as-is. "within the hour" is canon.

```html
<div class="of4s-blog-cta">
  <p class="of4s-eyebrow">Start your project</p>
  <h2>Ready to plan <em>your</em> office?</h2>
  <p>Tell us about your space. We call back, usually within the hour, and a free 3D plan of your office follows.</p>
  <div class="of4s-cta-actions">
    <a class="of4s-cta-btn" href="/request-a-free-quote">Request a Free Quote</a>
    <a class="of4s-cta-tel" href="tel:+13058893364">(305) 889-3364</a>
  </div>
</div>
```

---

## Standard section eyebrows (use these labels)

- `Discovery`
- `Design & layout planning`  (write the `&` as `&amp;` in HTML)
- `What we helped design & furnish`  (`&amp;`)
- `The installation`
- `The final results`
- `Start your project`

---

## Figure/slot reference

| Slot | Component | Notes |
|---|---|---|
| Cover / banner | Odoo post setting | LANDSCAPE hero; reads as list thumbnail AND top banner. Not in content HTML. |
| Client logo | logo block | Optional, centered, ~110px tall — big enough to READ. |
| Salesperson at work | `of4s-wide` (§5) | FIRST content photo. Person working on THIS project, NOT a room. Caption names them. |
| 3D project video | `of4s-wide` iframe (§7) | Autoplay background, muted/looping/no controls. Vimeo by default (ID only); use the YouTube pattern in §7 if that's where the client's video lives, keeping its true aspect ratio. |
| 2D + 3D plan | `of4s-pair` (§7) | Optional, ABOVE the video. Single `of4s-wide` if only a 2D plan exists. |
| Render vs installed | `of4s-pair` (§9) | SIGNATURE element: same area, render + the finished reality. Directly after §8's closing sentence. |
| Furnished-space photos | `of4s-gallery` (§8/§9 breakout) | Renders and/or installed shots; break into per-space mini-sections for projects with many photos — order so similar-looking spaces aren't adjacent. |
| Installation photos | `of4s-gallery` (§10) | The install in progress. |
| Delivery-summary band | `of4s-band` (§11a) | One factual line, before Final Results. Standard, not optional. |
| Final-result photos | `of4s-gallery` (§11) | The finished space. |
| Furniture partners | `of4s-partners` strip (§12a) | Homepage grayscale logos; ONLY manufacturers used on this project; never white-bg versions. At the END of the post, right before the CTA. |

If a slot has no suitable photo, omit that figure gracefully (or ask the user).
Never leave a broken/empty `<img>`.
