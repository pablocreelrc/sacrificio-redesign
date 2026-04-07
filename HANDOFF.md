# Mezcal Sacrificio — Website Redesign Handoff

**Date:** April 7, 2026
**Project Lead:** Pablo Creel
**Repo:** https://github.com/pablocreelrc/sacrificio-redesign
**Current Site:** https://mezcalsacrificio.com
**Design Theme:** Dark Heritage (gold + cream on dark)

---

## What's Built

A complete prototype of the redesigned mezcalsacrificio.com with 7 pages, bilingual support (EN/ES), responsive design, and real brand assets.

### Pages

| Page | File | Description |
|------|------|-------------|
| **Homepage** | `direction-b.html` | Hero → Awards → Products → Process → Cocktails → Email/Footer |
| **Joven** | `product-joven.html` | 100% Espadin, 40% ABV, awards, tasting notes |
| **Reposado** | `product-reposado.html` | 100% Espadin, 3 months French oak, best seller |
| **Tobalá** | `product-tobala.html` | Wild agave, 45% ABV, one plant per bottle |
| **Añejo** | `product-anejo.html` | Espadin + Barril, aged 1 year, 96pts SFWSC |
| **Process** | `process.html` | 4 production steps + innovation section |
| **Entry** | `index.html` | Redirects to direction-b.html + EN/ES toggle |

### Features Already Working
- Bilingual EN/ES with `data-en`/`data-es` attributes on all text
- Responsive: desktop (1440px), laptop (1024px), tablet (768px), mobile (375px)
- Product cards click through to individual product pages
- Process CTA links to process.html
- Real cocktail photos from live site
- Real bottle images (WebP compressed, 83-88% smaller than PNGs)
- Scroll snap (proximity) on desktop, disabled on mobile
- Awards marquee animation
- Nav darkens on scroll with backdrop blur
- "Buy Now" links to Total Wine search
- "Find My Closest Store" button ready with original site's data attributes

---

## Tasks for Team

### 1. UX/UI Lead — Age Verification Gate

**Priority:** Must-have before launch
**Reference:** Current site's age gate at mezcalsacrificio.com

**Requirements:**
- Full-screen modal on first visit
- Logo centered, "Verify Your Age" headline
- "Yes, I am 21+" button → dismiss modal, set `localStorage('age-verified', 'true')`
- "No, I am not" button → redirect to https://responsibility.org
- Must block page scroll while modal is visible (`document.body.style.overflow = 'hidden'`)
- Skip modal on return visits (check localStorage)
- Must work on mobile — buttons should stack, text should be readable
- Bilingual: support EN/ES toggle

**Where in code:** Search for `<!-- TODO: Age Gate -->` in `direction-b.html` (line ~1131)

**Design notes:**
- Dark background (#0A0A0A), gold headline (#C9A84C), cream text
- Match the brand's "classic-contemporary" personality — not clinical
- Consider a subtle agave field background at very low opacity

---

### 2. Tech Team — Store Locator Connection

**Priority:** Must-have before launch
**Reference:** Current store locator at mezcalsacrificio.com (click "Find My Closest Store")

**What's ready:**
```html
<button class="btn-ghost-gold find-store-btn"
        data-testid="button-find-store"
        id="button-find-store"
        type="button"
        aria-haspopup="dialog"
        aria-expanded="false"
        data-state="closed">
  <svg><!-- map pin icon --></svg>
  Find My Closest Store
</button>
```

**Requirements:**
- Connect to the same store locator dialog/modal used on the current site
- The button already has matching `data-testid`, `aria-haspopup`, and `data-state` attributes
- Should open a modal with ZIP code search → nearest Total Wine locations
- Store data: 254 stores across 29 states (Texas and Florida primary)
- Must work on mobile

**Aesthetic improvements from current site:**
- Use the dark theme colors (#0A0A0A bg, #C9A84C gold accents, #F5F0E8 cream text)
- Match the card styling from the product grid (rounded corners, gold border on hover)
- Map integration (Google Maps or Mapbox) with dark map theme

---

### 3. Tech Team — Email Capture → Database + Mailchimp

**Priority:** Must-have before launch

**What's ready:**
```html
<form id="email-capture-form" data-integration="supabase+mailchimp">
  <input type="email" id="email-input" name="email" required>
  <button type="submit" id="email-submit">Subscribe</button>
</form>
```

**Requirements:**

**Step 1 — Database (choose one):**
- **Supabase:** Create table `subscribers` with columns: `id`, `email`, `language` (en/es), `source` (homepage), `created_at`
- **Google Sheets:** Alternative if Supabase is not set up. Sheet with same columns.

**Step 2 — Mailchimp:**
- POST email to Mailchimp list via API on successful database write
- Use the "Sacrificio Circle" list/audience
- Tag subscribers with `website-redesign` and language preference

**Step 3 — UX:**
- On success (200): Replace form with "Thank you! You're in the circle." message
- On error: Show "Something went wrong. Please try again." below the form
- Disable button during API call to prevent double-submit

**Step 4 — Privacy:**
- Disclaimer text is already in place: "By subscribing, you confirm you are 21+ and agree to our Privacy Policy."
- Ensure GDPR/CAN-SPAM compliance

---

### 4. UX/UI Lead + Tech — Scroll Snap Improvement

**Priority:** Nice-to-have (improve before launch)
**Current state:** `scroll-snap-type: y proximity` on desktop, disabled on mobile

**Known issues:**
- Snap can feel janky when sections are taller than viewport (products section especially)
- Awards marquee bar between hero and products can interrupt the snap flow
- Nav click scroll positioning doesn't always align perfectly with snap points
- On some browsers, scroll snap fights with smooth scroll from nav link clicks

**Options to consider:**
1. **Remove scroll snap entirely** — let the page scroll naturally. Use IntersectionObserver to highlight the active nav link instead. Simplest fix.
2. **Switch to JS-based scroll** — use a library like Lenis (https://lenis.darkroom.engineering/) for smooth, controlled scrolling that works with snap
3. **Keep snap but tweak** — change from `proximity` to `mandatory` only on sections that are exactly 100vh, skip sections that overflow
4. **Scroll-driven animations** — instead of snap, use CSS `animation-timeline: scroll()` for parallax-like effects as sections enter view

**Recommendation:** Option 1 (remove snap, natural scroll) is safest for launch. Add Lenis in v2 for premium feel.

**Where in code:** Search for `scroll-snap-type` in `direction-b.html` CSS

---

## Design System Reference

### Colors
| Token | Hex | Usage |
|-------|-----|-------|
| Dark BG | `#0A0A0A` | Body, sections |
| Dark Card | `#161616` | Cards, elevated surfaces |
| Gold | `#C9A84C` | Headlines, CTAs, accents |
| Cream | `#F5F0E8` | Body text, nav links |
| Muted | `rgba(245,240,232,0.6)` | Secondary text |
| Red (Joven) | `#C41E2A` | SKU accent |
| Navy (Añejo) | `#2B3A67` | SKU accent |

### Typography
| Style | Font | Size | Usage |
|-------|------|------|-------|
| Display | Playfair Display Bold | 42-76px | Headlines |
| Body | DM Sans Regular | 14-18px | Body text |
| Accent | Cormorant Garamond | 20-26px | Quotes |
| UI | DM Sans Bold | 11-14px | Buttons, nav, labels |

### Assets
All in `assets/`:
- `logo.svg` — SVG logo (use `filter: brightness(0) invert(1)` for white on dark)
- `hero-bg.webp` — Agave field hero (also used as subtle bg on Products, Process, Cocktails)
- `joven.webp`, `reposado.webp`, `tobala.webp`, `anejo.webp` — Bottle images (WebP, ~100-130KB each)
- `cocktail-paloma.webp`, `cocktail-old-fashioned.webp`, `cocktail-margarita.webp`, `cocktail-smoked-sour.webp` — Cocktail photos
- `process-sowing.webp` — Process page hero

### Bilingual Pattern
All translatable text uses `data-en` and `data-es` attributes:
```html
<h2 data-en="Our Mezcal" data-es="Nuestro Mezcal">Our Mezcal</h2>
```
JS listener switches text via `postMessage` from the parent `index.html`.

---

## How to Run

```bash
# Clone
git clone https://github.com/pablocreelrc/sacrificio-redesign.git
cd sacrificio-redesign

# Run locally
python main.py
# Open http://localhost:5000

# Or deploy on Replit — import from GitHub URL, click Run
```

---

## File Structure

```
sacrificio-redesign/
├── index.html              # Entry point (redirects to direction-b.html + EN/ES pill)
├── direction-b.html        # Main homepage (dark theme)
├── direction-a.html        # Light theme variant (archived, not used)
├── product-joven.html      # Product page — Joven
├── product-reposado.html   # Product page — Reposado
├── product-tobala.html     # Product page — Tobalá
├── product-anejo.html      # Product page — Añejo
├── process.html            # Process page — 4 steps + innovation
├── main.py                 # Python server (reads PORT from env)
├── .replit                 # Replit config
├── README.md               # Setup instructions
├── HANDOFF.md              # This document
└── assets/
    ├── logo.svg
    ├── hero-bg.webp
    ├── joven.webp
    ├── reposado.webp
    ├── tobala.webp
    ├── anejo.webp
    ├── cocktail-paloma.webp
    ├── cocktail-old-fashioned.webp
    ├── cocktail-margarita.webp
    ├── cocktail-smoked-sour.webp
    └── process-sowing.webp
```

---

## Future Improvements (Post-Launch)

- **Our Story page** — Eric's story is the brand's #1 differentiator. Needs a dedicated page with full narrative, timeline, photos
- **Cocktail recipe pages** — individual recipe pages with ingredients, steps, video
- **Blog/Journal** — SEO content (mezcal vs tequila, agave guide, tasting guides)
- **Awards showcase** — dedicated page with timeline and badge gallery
- **Instagram feed** — embed @mezcalsacrificio
- **Product schema** — JSON-LD for Google rich snippets
- **Analytics** — preserve existing GTM (GTM-N5CBBTBV), Google Ads (AW-17600837888), Meta Pixel (830242789673792)
