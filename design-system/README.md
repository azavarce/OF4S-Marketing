# OF4S Design System — Netlify Deploy

A self-contained static site. No build step required.

## Quickest deploy (30 seconds)

1. Go to **https://app.netlify.com/drop**
2. Drag this entire folder onto the drop zone
3. Done — Netlify gives you a public URL

## Git-based deploy

1. Push this folder to a GitHub/GitLab/Bitbucket repo
2. In Netlify: **Add new site → Import from Git** → pick the repo
3. Build settings auto-fill from `netlify.toml`:
   - Build command: *(none)*
   - Publish directory: `.`
4. Deploy

## Custom domain

Netlify dashboard → **Domain management → Add custom domain**.
HTTPS is automatic via Let's Encrypt.

## What's in the box

- `index.html` — overview / system entry
- `directions.html` — 3 brand directions (A / B / C)
- `logo.html`, `color.html`, `typography.html`, `iconography.html`, `imagery.html` — foundations
- `components.html` — UI library
- `presentation.html`, `proposal.html`, `collateral.html`, `social.html` — templates
- `shared.css`, `tokens.css`, `sidebar.jsx` — shared chrome

Mobile-friendly: sidebar collapses to a hamburger drawer below 960px.

— OF4S · v1.0 · April 2026
