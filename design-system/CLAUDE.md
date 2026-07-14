# OF4S Design System — Project Notes

Persistent memory for this project. Read this before making changes so we don't repeat past bugs.

## Architecture

- **Pages**: `index.html` (cover) + topic pages (`color.html`, `typography.html`, `components.html`, `imagery.html`, `iconography.html`, `logo.html`, `collateral.html`, `proposal.html`, `social.html`, `presentation.html`, `directions.html`).
- **Shared chrome**: `sidebar.jsx` renders the left nav and the page footer. Every topic page mounts `<DSSidebar current="<page>" />` and `<DSFooter />` after loading React + Babel.
- **Design tokens**: `tokens.css` (colors, fonts, radii, shadows). Do not invent new tokens; reuse what's there.
- **Shared styles**: `shared.css` — page header chrome, sidebar styles, responsive shell, AND the mobile breakpoint rules that affect every topic page.
- **Cache busting**: `shared.css` is referenced as `shared.css?v=N`. Bump `N` on every page that loads it whenever you edit shared.css, otherwise verifier/users get stale CSS.
- **Scroll affordance**: `scroll-hint.js` is the shared overflow-detection script. It toggles `[data-overflow]` and `[data-at-end]` on `.scroll-hint` wrappers; the CSS in shared.css renders the right-edge fade + brass chevron.

## Mobile breakpoint

The single mobile breakpoint is `@media (max-width: 960px)` in shared.css. There's a secondary `@media (max-width: 600px)` for type-only tweaks. Don't add page-level mobile breakpoints in inline `<style>` blocks unless you really mean it — global rules in shared.css usually already cover the case.

## Known traps — DO NOT redo these

### 1. `zoom: calc(...)` with a length value silently fails

`shared.css` has rules like `.lh { zoom: calc((100cqw - 32px) / 612); }` and `.page { zoom: calc((100cqw - 24px) / 816); }`. These get parsed as **empty rules** in the browser — `zoom` accepts a unitless number, and `(length - length) / number` evaluates to a length, so the declaration is dropped.

**Implication**: do not rely on `zoom` to shrink letter-sized artifacts (letterhead 612×792, proposal page 816×1056) on mobile. Instead, give the wrapper `overflow-x: auto` so the artifact stays full-size and scrolls horizontally. Both `proposal.html` (`.doc-stage`) and `collateral.html` `.stage:has(> .lh, ...)` rule include `overflow-x: auto !important`.

If you ever want real shrink-to-fit, use `transform: scale()` with a wrapper that reserves the scaled height — not `zoom`.

### 2. `:has()` combined with `::after` is parser-fragile

The rule `.scroll-hint:has(> .doc-stage)::after { ... }` was silently dropped from `document.styleSheets` despite parsing fine on disk and `CSS.supports()` reporting true. Verifier caught the rule was never applied.

**Fix pattern**: use a flat modifier class instead. We use `.scroll-hint--paper-200` to override the fade color on proposal/collateral, applied directly to the wrapper. Never combine `:has()` with a pseudo-element in the same selector.

### 3. CSS specificity: surface backgrounds vs. variant backgrounds

In `directions.html` Direction C, `.C-wrap .surface { background: var(--C-cream) }` outranked `.C-social { background: var(--C-sage-deep) }` because the descendant selector beat the single-class one. Result: cream-on-cream unreadable text.

**Rule**: when a variant needs to break out of a wrapper's surface background, the override selector MUST match the wrapper's specificity or higher (`.C-wrap .C-social { background: ... }`).

### 4. Cache busting is mandatory after shared.css edits

Every page that loads shared.css needs the `?v=N` bumped. Currently at `v=12`. The verifier will catch stale-cache misses, but it wastes a round-trip — bump on the same edit.

### 5. Inline `<style>` order matters

Inline `<style>` blocks come AFTER `<link rel="stylesheet" href="shared.css">`, so inline rules win on equal specificity. When inline page styles set `width: 612px` and shared.css mobile rules try to override sizing — the inline can win unless wrapped in `@media`. If you need a mobile override, scope it with `@media (max-width: 960px)` in the inline block, OR set the property in shared.css with `!important`.

### 6. `flex-shrink: 0` on artifacts

`.lh`, `.email-sig`, `.bc` all have `flex-shrink: 0` (set in shared.css line ~627) so flex parents don't squeeze them down. Important for keeping artifacts at print dimensions.

### 7. The `:has()` selector for stage scrolling

The mobile rule `.stage:has(> .lh, > .bc, > .email-sig, > div > .lh, > div > .bc, > div > .email-sig)` keys off direct or one-level-nested children. If you change the DOM structure of collateral to wrap `.lh` in another div, this rule stops matching. Re-test mobile after any structural change.

### 8. Garnish class loses to contextual paragraph rules (Odoo reskin, 2026-07-11)

`.of4s-hm3 .garnish` (0,2,0) LOSES color/font-size to `.of4s-hm3 .row-text p` (0,2,1) — the shipped
proof line rendered grey 16px until a higher-specificity override (`.row-text p.garnish`) was added.
Whenever `.garnish` is placed inside a container that styles its `p` descendants, add the contextual
override. Verify with getComputedStyle (expect rgb(142,106,48) on light), not with rule-presence greps.

## Visual system reminders

- **Type**: Display = Schibsted Grotesk (--of4s-font-display); Sans = Geist; Mono = Geist Mono. Fraunces is RETIRED (2026-07). The accent-word em in display headings (styled navy, not italic serif) is the brand mannerism — used sparingly.
- **Color**: Brass = GARNISH ONLY (see Decisions). Accent work is done by the navy scale: navy-600 on light, navy-300 on dark, navy-500 for the logo "4". New tokens: --of4s-navy-300 #8fa9c7, --of4s-navy-100 #dde5ee.
- **Spacing**: 4/8/12/16/24/32/48/64/96 px. Don't invent values.
- **Radius**: `--of4s-radius-sm/md/lg` only.
- **Mono caps**: small mono labels with `letter-spacing: 0.1em` to `0.22em` and `text-transform: uppercase` are the eyebrow voice across the system.

## Decisions (2026-07)

- **Direction A ("Editorial Modern") chosen.** B and C removed from `directions.html`; compare table removed.
- **No italics EXCEPT testimonials/quotes.** shared.css forces `em, i { font-style: normal; }`; the only sanctioned exception is content inside `blockquote`, `.testimonial`, or `.quote`. The em mannerism in headings = accent color, never italic.
- **Display font DECIDED (2026-07): Schibsted Grotesk (T2).** Rolled through tokens.css + all pages. Logo = OF4S shorthand in Schibsted Grotesk 700. Rejected: Fraunces, Bricolage Grotesque.
- **Accent color DECIDED (2026-07): A1 — navy + brass garnish.** Navy does ALL structural accent work (navy-600 light / navy-300 dark). Brass is garnish ONLY: tiny mono details (ratings, stats, key numbers) — brass-700 on light, brass-400 on dark. Never eyebrows/headings/links/buttons/fills. A2 terracotta and A3 brass-secondary archived (color-accents.html deleted; A1 demos folded into color.html).
- `logo.html` and `logo-options.html` DELETED (old marks). Nav: single "Logo & Type" entry → logo-type.html.

## Logo

- **Decided 2026-07**: the logo is Option 5 "OF4S shorthand" in Schibsted Grotesk 700 (T2 on `logo-type.html`) — letters at natural tracking (no extra gap between OF / 4 / S), the "4" in navy-500 on light / navy-300 on dark. Chair-4 (T2) is a secondary playful mark only.
- Logo versions & uses (horizontal lockup, favicon, avatar, email sig) documented on `logo-type.html`. The horizontal lockup (mark + full-name mono caption) is the sanctioned wide version for letterheads/covers.

## Deploy

Netlify config is in `netlify.toml`. The `of4s-deploy/` folder is the staging directory for bundled output. To prep a deploy:

1. Bump `shared.css?v=N` if needed.
2. Verify cache buster matches in every page that loads shared.css.
3. Zip the project root or push the relevant files to the deploy folder.

## Asset review pane

User-facing deliverables (pages, etc.) are registered in the asset manifest. Support files (CSS, JS, JSX) should NOT be registered.
