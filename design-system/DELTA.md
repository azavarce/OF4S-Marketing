# Design Delta — v1 (Fraunces/brass) → v2 (Schibsted Grotesk/navy)

## NAMING KEY (Andres's numbering — canonical, 2026-07-11)

- **v1** = the ORIGINAL website, before any design system (old homepage view 3868, parked at /home-old).
- **v2** = the FIRST design-system round (Fraunces/brass, views 5671-5749, live at / since the cutover).
- **v3** = the OWNER REBRAND (Schibsted/navy, `design_system_v2/` folder, /home-v3 reveal, views 5755-5762).

⚠️ Repo folder/doc names predate this key: the folder `design_system_v2/` and DELTA.md's "v1→v2"
refer to DESIGN SYSTEMS (old system → new system), i.e. Andres's v2 → v3. When talking to Andres,
always use HIS numbering above.

**Date:** 2026-07-10 · **Authority:** owner-directed rebrand, executed by Emma (Andres delegated — no sign-off gate on this doc; the reveal gate is the homepage itself)
**Sources:** `tokens.css`, `CLAUDE.md`, `HANDOFF.md` in this folder (v2, final, all decisions locked) vs. the shipped v1 token block (embedded per-page in views 5671–5749; canonical copy in view 5739 / `migration/home/view_a.xml`).

This is the spec every reskin edit follows. When this doc and the v2 source files disagree, the v2 source files win — update this doc.

---

## 1. What did NOT change (do not touch)

- **Neutrals — identical.** Warm paper + stone scales carry over 1:1:
  paper-50 `#faf8f4` · paper-100 `#f3efe7` · paper-200 `#e8e2d4` · paper-300 `#d6cfbe` · stone-400 `#a8a094` · stone-500 `#7a7468` · stone-600 `#555047` · stone-700 `#3a362f` · stone-900 `#1a1814`
- **Body font:** Geist. **Mono font:** Geist Mono. (Only the display font changes.)
- **Primary navy hex:** `#15273f` survives as navy-800 (v2 adds a full navy scale around it).
- **Semantic colors:** success `#5a7a4f`, danger `#9c3a30`, warning `#b8895a` — same.
- **Motion:** same easing `cubic-bezier(0.2,0.8,0.2,1)`, same 150/240ms durations (v2 adds 400ms slow).
- **Background rule:** warm paper, never pure white; white reserved for raised cards.
- **Mono-caps eyebrow as the label voice** (tracking 0.1–0.22em, uppercase) — the *mechanism* stays; its *color* changes (see §3).
- **Copy canon (unchanged, not a design matter):** "within the hour", tel:+13058893364, 1790 W 8th Ave, no em-dashes in body, cubicles ≠ benching.

## 2. Fonts

| Role | v1 | v2 |
|---|---|---|
| Display | **Fraunces** (serif, opsz 9–144, wght 300–600, italic em) | **Schibsted Grotesk** (wght 400–800) — Fraunces **RETIRED 2026-07** |
| Body | Geist | Geist (unchanged) |
| Mono | Geist Mono | Geist Mono (unchanged) |

Google Fonts href (v2): `family=Schibsted+Grotesk:wght@400;500;600;700;800&family=Geist:wght@300;400;500;600;700&family=Geist+Mono:wght@400;500`

Weight mapping for display headings: v1 Fraunces 300 (light, elegant) → v2 Schibsted Grotesk is a grotesque; use the weights shown in v2 typography.html (see BUILD-SPEC). Do not carry "weight 300 + italic em" habits over.

## 3. The accent revolution (biggest change)

**v1:** brass did all accent work — eyebrows, italic em-words, links, CTA pill, hero accents.
**v2:** **navy does ALL structural accent work. Brass is garnish ONLY.**

| Job | v1 | v2 light bg | v2 dark bg |
|---|---|---|---|
| Structural accent (em-words, links, active states) | brass-700 `#8e6a30` / brass-400 `#c9a474` | **navy-600 `#2d4a6e`** | **navy-300 `#8fa9c7`** |
| Eyebrows | brass-700 (light) / brass-400 (dark) | navy-600 | navy-300 |
| Chips/badges tint | brass-100 `#f0e6d4` | navy-100 `#dde5ee` | — |
| Tiny mono garnish: ratings, stats, key numbers ONLY | (brass everywhere) | brass-700 | brass-400 |

**Brass is NEVER:** eyebrows, headings, links, buttons, background fills. If in doubt → navy.
Brass tokens stay defined in tokens.css but are marked DEPRECATED for structural use.

New navy scale: 950 `#0a1628` · 900 `#0f1d33` · **800 `#15273f` (primary)** · 700 `#1e3554` · 600 `#2d4a6e` · 500 `#466489` · 300 `#8fa9c7` · 100 `#dde5ee`.

## 4. The italics ban (biggest mannerism change)

- **v1 signature:** ONE italic Fraunces `<em>` word per display heading, colored brass.
- **v2 rule:** **no italics anywhere** except inside `blockquote`, `.testimonial`, `.quote`. The heading `em` mannerism survives as an **upright, accent-colored word** — navy-600 on light, navy-300 on dark. v2 shared.css enforces `em, i { font-style: normal; }`.
- Reskin implication: every v1 heading (`h1/h2 em{font-style:italic;color:var(--br4|--br7)}`) becomes upright navy. Keep the one-accent-word-per-heading restraint.

## 5. Logo (all-new)

- v1: raster logo images (e.g. attachment-based imgs in header) + no codified mark.
- v2: **text mark "OF4S"** — Schibsted Grotesk **700**, natural tracking (no extra letter-spacing between OF/4/S), the **"4" in navy-500 `#466489` on light / navy-300 `#8fa9c7` on dark**. Horizontal lockup = mark + full-name mono caption. Favicon/app-tile and email-sig versions specced on `logo-type.html`.
- **No SVG/PNG exports exist yet** (explicitly "not included"). Web usage renders the mark in live text/CSS. Collateral needing raster exports is a follow-up.
- Chair-4 mark = secondary/playful only. Old marks deleted from the system.

## 6. Structure tokens (formalized, mostly compatible)

- **Type scale:** 12/14/16/18/22/28/36/48/64/84/112px (named xs→7xl). v1 used clamp() ad-hoc sizes — v2 scale is the reference; clamp() between adjacent steps is fine for fluid headings.
- **Spacing:** 4/8/12/16/24/32/48/64/96/128px. Don't invent values.
- **Radii:** sm 2 / md 4 / lg 8 / xl 14 / pill 999. (v1 used 4/6/8 ad-hoc — compatible.)
- **Shadows/borders:** now tokenized (`--of4s-shadow-sm/md/lg`, `--of4s-border-thin/medium/strong`) — all rgba(15,29,51,·) i.e. navy-tinted, matching v1's border color habit.
- Direction locked: **A — "Editorial Modern"** (B/C removed from the system).

## 7. Token NAMING migration (for the shared view)

v1 pages define short local aliases (`--st9, --p50, --br4, --nv8, --fd, --fs, --fm, --ez, --df, --db`) **duplicated inside every page's scoped CSS**. v2 canonical names are `--of4s-*`.

**Architecture (Andres-approved 2026-07-10):** one shared Odoo qweb view `website.of4s_ds_v2_tokens` defines the `--of4s-*` custom properties + the v2 Google-Fonts link, t-called by every reskinned page. Future rebrand = one edit. During reskin, per-page CSS is rewritten to reference `var(--of4s-…)` directly; the old local aliases retire page-by-page. **Never define token values inside a page again.**

## 8. Blast-radius inventory (what carries v1 today)

| Surface | v1 carrier | Reskin action |
|---|---|---|
| 26 migrated pages + legal/privacy (views 5671–5749) | per-page token block + Fraunces link + italic-em + brass | full reskin loop, page by page (homepage FIRST, reveal-only) |
| Old canon LPs (5613 /cubicle-lp-pt-v3, 5610 /quote-southflorida-v3, v1/v2 variants) | same | reskin after main queue; they're also ad landing pages — coordinate with live campaigns |
| Site chrome: header/footer (views 5745 `of4s_chrome_v2`, 5746 `of4s_header_brand_v2`, footer 4659) | logo image + brass accents | **other session's records** — logo swap + navy accents happen there; coordinate, don't collide |
| Blog: skin CSS (attachment 35412) + rebuilt posts + REBUILD-SPEC.md CSS appendix | Fraunces/brass | one-file skin swap + spec update; rebuilt posts carry inline vocab — audit |
| Thank-you shared CSS (view 5734) | v1 tokens | becomes a t-call consumer of the shared token view |
| Harness docs: migration/PROMPT.md, copy-loop/PROMPT.md, blog-loop specs, MEMORY.md, PRODUCT.md | hardcode Fraunces/brass rules | update BEFORE any loop session runs again (else they "fix" pages back to v1) |
| Odoo website settings: logo, favicon | old logo | new text-mark favicon/logo per logo-type.html |
| OG/social images, branded email templates (e.g. Paper Inspection) | old brand | follow-up queue, not blocking homepage reveal |

## 9. Rollout order (agreed)

1. ✅ v2 system ingested to repo (`design_system_v2/`), old handoff marked SUPERSEDED.
2. This DELTA + BUILD-SPEC (agent-distilled component vocabulary).
3. Shared token view `website.of4s_ds_v2_tokens` in Odoo.
4. **Homepage rebuilt on v2 at a parallel noindex URL — the reveal. STOP there** for Andres/George.
5. After approval: reskin loop over the remaining pages (new `reskin/` harness), chrome/logo coordination, blog skin, collateral.
