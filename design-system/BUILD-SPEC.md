# OF4S v2 — Marketing Build Spec (distilled from the topic pages)

**Generated 2026-07-10** by full read of directions/components/typography/color/logo-type/imagery/iconography + shared.css.
Use WITH `DELTA.md` (what changed vs v1) and `tokens.css` (values). This file is the component vocabulary for building
marketing pages — you should not need to open the HTML topic pages for routine builds.

## Rulings on internal contradictions (RESOLVED — do not relitigate)

The zip's pages contain a few stale spots from earlier exploration rounds. Resolutions, applied throughout this spec:

1. directions.html still labels type as "Fraunces" in two attr tables → **Schibsted Grotesk** (its own CSS + every other page agree; Fraunces retired).
2. color.html's "Navy Accent" swatch spec block shows brass-400 print values (#C9A474 / Pantone 465 C) → the swatch itself is **navy-300 #8FA9C7**; tokens.css governs.
3. Hero CTA: directions mock shows a mono-caps pill; components.html `.btn` is 4px-radius Geist sentence-case → **components.html is the canonical UI library**; use `.btn btn-primary btn-lg` for hero CTAs.
4. Wordmark weight 500 in older nav mocks → **locked at 700** (logo-type.html + system CLAUDE.md).
5. `em` accent navy-800 in doc-site chrome → marketing surfaces use **navy-600 on light / navy-300 on dark**.
6. Dark sections: stone-900 vs navy → **navy-900/800 for brand/marketing dark sections**; stone-900 is deck/doc-site flavor.
7. Duotone placeholder still brass-tinted → written recipe governs: **B&W → shadows navy-800, highlights navy-300**.
8. Button icon size: **16px in default .btn** (shipped CSS); 20px acceptable in btn-lg.
9. GAP in source: no `:focus-visible` ring exists → adopt `:focus-visible { outline: 2px solid var(--of4s-navy-800); outline-offset: 2px; }` (derived from the input focus recipe; navy-300 on dark).

---

## 1. Direction A vocabulary — "Editorial Modern"

Magazine-editorial: giant light-weight Schibsted display headlines with one navy accent word, mono uppercase eyebrows, generous whitespace, warm paper surfaces, dark sections for weight. "Confident, warm, magazine-like."

**Homepage hero (the reference mock, `.A-hero` in directions.html):**
- Light hero on `--of4s-paper-50`, min-height 520px, `padding: 56px 64px`, `display:grid; grid-template-columns: 1.5fr 1fr; gap: 64px; align-items: end` — headline bottom-left, body copy + CTA bottom-right (asymmetric, baseline-anchored).
- Hero H1: `font-family: Schibsted Grotesk; font-weight:300; font-size:96px; line-height:0.92; letter-spacing:-0.035em; color: var(--of4s-stone-900)`; `em { font-style:normal; color: var(--of4s-navy-600); font-weight:400 }`.
- Eyebrow above headline: mono 11px / 0.22em / uppercase / navy-600; margin-bottom:20px — e.g. "SOUTH FLORIDA · SINCE 2008".
- Body: 15px/1.6 stone-700; max-width:320px.
- Hero CTA: `.btn btn-primary btn-lg` (per ruling 3).
- Section rhythm: sections `padding: 64px 80px` (up to 96px for feature moments), separated by `border-bottom: var(--of4s-border-thin)` (1px rgba(15,29,51,0.1)). Mobile (≤960px): 36–40px 20px.
- Signature moves: dark navy panels for stats/weight; huge display numbers (weight 300, up to 180px, ls -0.04em); `1.2fr 1fr` / `1.5fr 1fr` asymmetric grids; thin hairline dividers above meta rows; navy-100 (#DDE5EE) callout panels; core message "Local. Modern. Easy."

## 2. Headings

Display = `var(--of4s-font-display)` ('Schibsted Grotesk', 'Geist', sans-serif). Sentence case always. Line-height compresses as size grows.

| Level | Size/LH | Weight | Tracking |
|---|---|---|---|
| 7XL hero | 112 / 0.95 | 300 | -0.025em (hero mock -0.03 to -0.035em) |
| 6XL | 84 / 1.0 | 300–400 | -0.025em |
| 5XL | 64 / 1.05 | 400 | -0.025em |
| 4XL | 48 / 1.1 | 400 | -0.025em |
| 3XL section | 36 / 1.2 | 500 | -0.02em |
| 2XL sub | 28 / 1.3 | 500 | -0.02em |
| Card title | 18–24 / ~1.2 | 500 | -0.015em |

Lede = Geist 400 22px/1.4 or 18px/1.55; body = Geist 16px/1.6; small 14px/1.55.

**Accent-word `em` mannerism** — one word per headline, upright, never italic:
```css
h1 em, h2 em { font-style: normal; color: var(--of4s-navy-600); }   /* on light */
.dark h1 em, .dark h2 em { color: var(--of4s-navy-300); }           /* on dark */
/* when heading is weight 300, em steps up to 400 */
```

**Eyebrow:**
```css
.eyebrow { font-family: var(--of4s-font-mono); font-size: 11px; letter-spacing: 0.22em;
  text-transform: uppercase; color: var(--of4s-navy-600); margin-bottom: 16px; }
/* dark bg: color: var(--of4s-navy-300). Small card caps: 10px / 0.15–0.18em. */
/* Neutral/quiet labels (captions, table heads): same recipe, stone-500 (light) / stone-400 (dark). */
/* Eyebrows are NEVER brass. */
```

## 3. Buttons (components.html — canonical)

```css
.btn { display: inline-flex; align-items: center; gap: 8px;
  font-family: var(--of4s-font-sans); font-weight: 500; font-size: 14px;
  line-height: 1; padding: 12px 20px; border-radius: var(--of4s-radius-md); /* 4px */
  border: 1px solid transparent; letter-spacing: 0.01em;
  transition: all var(--of4s-dur-fast) var(--of4s-ease); }
.btn-primary   { background: var(--of4s-navy-800); color: var(--of4s-paper-50); }
.btn-primary:hover { background: var(--of4s-navy-900); }
.btn-secondary { background: white; color: var(--of4s-navy-800); border-color: var(--of4s-stone-400); }
.btn-secondary:hover { background: var(--of4s-paper-100); border-color: var(--of4s-stone-600); }
.btn-ghost     { background: transparent; color: var(--of4s-navy-800); padding: 12px 8px; }
.btn-ghost:hover { color: var(--of4s-navy-600); }
.btn-accent    { background: var(--of4s-navy-300); color: var(--of4s-stone-900); }  /* THE emphasis moment only */
.btn-accent:hover { background: var(--of4s-navy-500); }
.btn-sm { padding: 8px 14px; font-size: 13px; }
.btn-lg { padding: 16px 28px; font-size: 16px; }   /* hero CTAs */
.btn svg { width:16px; height:16px; stroke:currentColor; stroke-width:1.5; fill:none; stroke-linecap:round; stroke-linejoin:round; }
```
Always sentence case. On-dark: primary inverts (`background: paper-50; color: navy-900`); secondary becomes a text link.
Text-link: `color: navy-600; text-decoration: underline; text-underline-offset: 3px; font: 500 14px sans` (navy-300 on dark).

## 4. Cards & surfaces

- Base card: `background: white; border: var(--of4s-border-thin); border-radius: var(--of4s-radius-lg); overflow: hidden`.
- Surface hierarchy: page = paper-50; section bands / photo backdrops = paper-100; cards on either = white.
- Hover-raise (product card): `transition: box-shadow/transform var(--of4s-dur-base) var(--of4s-ease)` → hover `box-shadow: var(--of4s-shadow-lg); transform: translateY(-2px)`.
- Product card anatomy: 4/3 photo (bg paper-100) → body padding 20px → SKU mono 11px stone-500 ls 0.08em + badges → name display 500 18px → vendor 13px stone-600 → price row w/ top hairline (price display 500 22px; unit sans 12px stone-500).
- Dark callout: `background: navy-800; color: paper-100; radius-lg; padding: 32px;` `strong { color: navy-300; font-weight: 500 }`.
- Light callout: `background: navy-100; color: navy-800` (AAA pair).

## 5. Forms

```css
.field-label { font-family: var(--of4s-font-mono); font-size: 10px; letter-spacing: 0.15em;
  text-transform: uppercase; color: var(--of4s-stone-600); }  /* 6px gap to input */
.input, .select, .textarea { font-family: var(--of4s-font-sans); font-size: 14px; padding: 12px 14px;
  border: 1px solid var(--of4s-paper-300); border-radius: var(--of4s-radius-md);
  background: white; color: var(--of4s-stone-900); }
.input:focus { outline: none; border-color: var(--of4s-navy-800); box-shadow: 0 0 0 3px rgba(21,39,63,0.08); }
.input.error { border-color: var(--of4s-danger); }
.input::placeholder { color: var(--of4s-stone-400); }
.help { font-size: 12px; color: var(--of4s-stone-500); }  .help.error { color: var(--of4s-danger); }
```
Form card: white, border-thin, radius-lg, padding 32px, max-width 540px; h3 display 500 22px; lede 14px stone-600;
rows gap 16px; actions row `margin-top:24px; padding-top:24px; border-top: var(--of4s-border-thin)`.
Checkbox 18×18 navy-800; radio 18px circle navy-800 dot; toggle 40×22 pill navy-800 on.

## 6. Logo ("OF4S" shorthand — locked)

```css
.logo { display:inline-flex; align-items:center; color: var(--of4s-navy-800);
        font-family: var(--of4s-font-display); font-weight: 700;
        letter-spacing: -0.03em; line-height: 0.9; }
.logo .four { color: var(--of4s-navy-500); }        /* #466489 on light */
.logo.on-dark { color: var(--of4s-paper-50); }
.logo.on-dark .four { color: var(--of4s-navy-300); }
```
Markup: `OF<span class="four">4</span>S`. Nav size ~22px; cover size 52–68px.

Horizontal lockup (web nav / letterhead / covers): mark + 1px vertical rule + stacked mono caption, gap 18px:
```css
.lockup-h .rule { width:1px; align-self:stretch; background: rgba(15,29,51,0.18); } /* dark: rgba(255,255,255,0.25) */
.lockup-h .fullname { font-family: var(--of4s-font-mono); font-size:11px; letter-spacing:0.26em;
  text-transform:uppercase; color: var(--of4s-stone-600); line-height:1.9; }        /* dark: paper-200 */
```
Caption exactly: `OFFICE FURNITURE<br/>4 SALE`.
Favicon/tile: navy-800 square (radius 5px @32 / 9px @56), "OF4S" Schibsted 700 (11px @32 / 18px @56, ls -0.03em), paper-50 with 4 in navy-300.
URL style: mono 14px stone-700, the `4` navy-600 weight 600 → of4s.com.
No SVG/PNG exports exist yet — render in live text/CSS on the web.

## 7. Stats / numbers (the ONLY sanctioned brass)

```css
.stat-card { background: var(--of4s-navy-800); color: var(--of4s-paper-50);
  border-radius: var(--of4s-radius-lg); padding: 32px; }
.stat-card .label { font:500 10px var(--of4s-font-mono); letter-spacing:0.18em;
  text-transform:uppercase; color: var(--of4s-navy-300); margin-bottom:16px; }
.stat-card .value { font-family: var(--of4s-font-display); font-weight:300; font-size:64px;
  letter-spacing:-0.025em; line-height:0.95; }
.stat-card .value em { font-style:normal; color: var(--of4s-navy-300); font-weight:400; } /* the unit: 24<em>hrs</em> */
.stat-card .desc { font-size:13px; color: var(--of4s-paper-200); margin-top:12px; max-width:240px; line-height:1.55; }
```
Oversized proof number: display 300, up to 180px, ls -0.04em, lh 0.85, unit em navy-600 (light) / navy-300 (dark).

**Brass garnish** — tiny mono proof lines only (`4.9 rating · 2,400 installs · est. 2009`):
```css
.garnish { font-family: var(--of4s-font-mono); font-size:11px; letter-spacing:0.14em;
  text-transform:uppercase; color: var(--of4s-brass-700); }   /* dark: brass-400 */
```
Never eyebrows/headings/links/buttons/fills.

## 8. Imagery

- Aspect ratios: 4/3 install shots & product cards; 16/10 editorial frames. SKU shots on paper-100, 3/4 angle, soft top light.
- Radius: radius-md (4px) standalone; 0 when flush inside a bordered card (card clips).
- No borders on photos; NO overlay/scrim tricks — compose type beside negative space.
- Duotone (sparing; hero/social/dividers): B&W → shadows navy-800 #15273F, highlights navy-300 #8FA9C7.
- Placeholders: paper-200 bg + repeating 135deg navy-tint stripes + mono label. Never stock photos.
- Content: real installs, natural light, eye-level, one subject per frame.

## 9. Iconography

24×24 grid, 2px keyline padding, stroke-only (no fills), round caps/joins, geometric.
Stroke: 1px @16 (inline) · 1.5px @20/@24 · 2px @32+. In buttons: 16px (ruling 8).
```css
svg.icon { width:24px; height:24px; stroke:currentColor; stroke-width:1.5; fill:none;
  stroke-linecap:round; stroke-linejoin:round; } /* viewBox="0 0 24 24" */
```
Library paths live in iconography.html (product/process/UI sets) — copy inline.
Don'ts: no mixed libraries, no fills, no emoji, no circle backgrounds.

## 10. Dark/navy sections

Marketing dark = **navy-900 #0F1D33 / navy-800 #15273F** (ruling 6).
On dark: headings paper-50; body paper-200; quiet labels stone-400/paper-200; eyebrows + em accents + links navy-300;
brass garnish brass-400; logo "4" navy-300; primary button inverts paper-50/navy-900.
Contrast-approved pairs: navy-800↔paper-50 13.7:1 AAA; navy-300 on stone-900 6.9:1 AA; navy-800 on navy-100 11.0:1 AAA.

## 11. Tables / badges / chips / nav / stepper

```css
.badge { display:inline-flex; align-items:center; gap:6px; padding:4px 10px;
  border-radius: var(--of4s-radius-pill); font:500 10px var(--of4s-font-mono);
  letter-spacing:0.1em; text-transform:uppercase; }
.badge .dot { width:6px; height:6px; border-radius:50%; background:currentColor; }
.badge.in-stock  { background: rgba(90,122,79,0.12);  color: var(--of4s-success); }
.badge.lead-time { background: rgba(184,137,90,0.18); color: var(--of4s-navy-800); }
.badge.backorder { background: rgba(156,58,48,0.12);  color: var(--of4s-danger); }
.badge.new       { background: var(--of4s-navy-800);  color: var(--of4s-paper-50); }
.badge.partner   { background: var(--of4s-navy-100);  color: var(--of4s-navy-800); }
```
Chip: navy-100 bg / navy-800 text, mono 10px 0.1em uppercase, pill.
Table: white, border-thin, radius-lg, overflow hidden; th mono 500 10px/0.15em uppercase stone-500 on paper-100,
padding 14px 20px; td 14px, border-top thin; numeric cells mono; row hover paper-50.
Top nav: white bar, padding 16px 24px, border-bottom thin; links Geist 14px stone-700,
active `color: navy-800; border-bottom: 2px solid navy-300`; wordmark left; `.btn-primary .btn-sm` "Get a quote" right.
Stepper (Discover→Install): 28px numbered circles (paper-200/stone-600 → current navy-800/white → done success/✓),
label mono 9px/0.15em stone-500 over 500 14px, 1px paper-300 connector.

## 12. Global/reusable rules

```css
/* Italics ban — include verbatim on every page */
em, i { font-style: normal; }
blockquote em, blockquote i, .testimonial em, .testimonial i, .quote em, .quote i,
blockquote.testimonial, .testimonial, .quote { font-style: italic; }

::selection { background: var(--of4s-navy-800); color: var(--of4s-paper-50); }
:focus-visible { outline: 2px solid var(--of4s-navy-800); outline-offset: 2px; } /* navy-300 on dark (ruling 9) */
```
Breakpoints: single mobile breakpoint `@media (max-width: 960px)` (grids → 1 col, sections → 36px 20px);
`@media (max-width: 600px)` type-only shrink.
Section divider rhythm: `border-bottom: var(--of4s-border-thin)` between full-bleed sections.
Scroll-hint pattern (mobile horizontal scroll): `.scroll-hint` wrapper + `.scroll-x { overflow-x:auto; scrollbar-width:none }`,
right-edge 44px fade to surface color + navy-300 chevron circle; flat modifier classes, never `:has()`+pseudo-element.
