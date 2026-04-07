# Mezcal Sacrificio — Website Redesign

Website prototype for [mezcalsacrificio.com](https://mezcalsacrificio.com) — artisanal mezcal from Tlacolula, Oaxaca.

## Handoff — TODO for Team

### UX/UI Lead — Age Verification
- Design and implement age gate modal before launch
- Current site's age gate for reference: https://mezcalsacrificio.com
- Must block scroll while modal is visible (`body overflow: hidden`)
- Store verification in `localStorage('age-verified')`
- Redirect underage users to https://responsibility.org
- Placeholder comment in `direction-b.html` where the age gate should go

### Tech Team — Store Locator
- Connect the existing store locator component from mezcalsacrificio.com
- Button is ready: `<button data-testid="button-find-store" id="button-find-store" aria-haspopup="dialog">`
- Match the current site's dialog/modal behavior
- The button already has the map pin SVG icon and correct aria attributes

### Tech Team — Email Capture → Database + Mailchimp
- Form is ready: `<form id="email-capture-form" data-integration="supabase+mailchimp">`
- Input field: `<input id="email-input" name="email" type="email">`
- Connect to:
  1. **Supabase** table `subscribers` (or Google Sheets as fallback)
  2. **Mailchimp** list via API for automated email campaigns
- Show success message on 200 response
- Current form has `onsubmit="event.preventDefault()"` — replace with API call

## Preview

**Run locally:**
```bash
python main.py
# Open http://localhost:5000
```

**Deploy on Replit:**
1. Import from this GitHub repo
2. Click Run
3. Share the Replit URL

## Pages

| Page | File | Description |
|------|------|-------------|
| Homepage | `direction-b.html` | Dark heritage theme — hero, products, process, cocktails, email capture, footer |
| Joven | `product-joven.html` | 100% Espadin, 40% ABV — tasting notes, awards, cocktail pairings |
| Reposado | `product-reposado.html` | 100% Espadin, 40% ABV — 3 months French oak |
| Tobalá | `product-tobala.html` | Wild agave, 45% ABV — one plant per bottle |
| Añejo | `product-anejo.html` | Espadin + Barril, 45% ABV — aged 1 year |
| Process | `process.html` | 4-step production process + innovation section |

## Features

- **Bilingual** — EN/ES translations on all pages (press **L** to toggle, or use the language pill)
- **Scroll snap** — full-viewport section paging on desktop
- **Real assets** — bottle photos, cocktail images, agave field hero, SVG logo
- **Responsive** — desktop, tablet, mobile breakpoints
- **Product pages** — click any bottle on homepage to see full details
- **Find My Closest Store** — button matches original site's component (`data-testid="button-find-store"`)

## Sections (Homepage)

1. **Hero** — Agave field background, headline, dual CTAs
2. **Awards Bar** — Scrolling marquee (94pts Wine Enthusiast, Best Value, Top 100, Double Gold SFWSC)
3. **Products** — 4-column grid with bottle images, tasting notes, discover links → product pages
4. **Process** — 4-step overview with numbered circles, links to process.html
5. **Cocktails** — 4 cards (Paloma, Old Fashioned, Margarita, Smoked Sour) with real photos
6. **Email Capture** — Newsletter signup + Total Wine & Find My Closest Store CTAs
7. **Footer** — 4-column layout (Explore, Find Us, Connect) + legal

## Brand

- **Company:** Destileria Sacrificio S.A. de C.V.
- **Brands:** Mezcal Sacrificio (this site), Mezcal Akul
- **Distributor:** Mexcor (Texas & Florida)
- **Primary Retailer:** Total Wine & More — 254 stores, 29 states
- **Maestro Mezcalero:** Eric Adalid Hernández Cortés (4th generation)

## Tech

- Static HTML/CSS/JS — no framework, no build step
- Google Fonts: Playfair Display, DM Sans, Cormorant Garamond
- Python `http.server` for local/Replit serving
- Playwright used for visual QA during development

## Assets

All in `assets/`:
- `logo.svg` — brand logo
- `hero-bg.webp` — agave field hero background
- `joven.png`, `reposado.png`, `tobala.png`, `anejo.png` — bottle photos
- `cocktail-paloma.webp`, `cocktail-old-fashioned.webp`, `cocktail-margarita.webp`, `cocktail-smoked-sour.webp` — cocktail photos
- `process-sowing.webp` — process page hero
