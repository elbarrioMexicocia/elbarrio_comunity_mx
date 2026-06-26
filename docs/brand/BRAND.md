# El Barrio — Brand Guidance

> Economía local en tiempo real.

---

## 1. Brand identity

### Name
**El Barrio** — always written as two words, capital E, capital B. Never "el barrio", never "ElBarrio", never abbreviated.

### Tagline
*Economía local en tiempo real* — use in full on splash screens, onboarding, and marketing. For compact UI contexts (header subtitle, app store listing) use *Economía local*.

### Personality
El Barrio is the digital extension of a real neighborhood. The voice is warm and direct — it speaks like a trusted neighbor, not a corporation. Four core traits:

| Trait | What it means in practice |
|---|---|
| **Cercana** | First names, informal tone, Spanish-first. "Doña Carmen", not "Vendor #142". |
| **Inmediata** | Distances in km, countdowns in hours, live pulse visible at all times. |
| **Confiable** | Ratings always visible. No hidden fees. No vague copy. |
| **Humana** | Real people, real food, real services. Emojis are allowed — they humanize. |

---

## 2. Color palette

### Primary colors

| Name | Hex | Role |
|---|---|---|
| Cyan Barrio | `#00C8F0` | Primary action, links, active states, interactive accents |
| Verde Local | `#00E87A` | Live indicator, prices, success states |

These two colors always appear together as a gradient on CTAs and key UI elements: `linear-gradient(135deg, #00C8F0, #00E87A)`.

### Dark surface system

| Name | Hex | Role |
|---|---|---|
| Noche Urbana | `#0F1117` | Page background |
| Asfalto | `#1C1E27` | Card / surface background |
| Concreto | `#2A2D3A` | Borders, dividers |
| Borde activo | `#353847` | Hover borders |

### Text

| Name | Hex | Role |
|---|---|---|
| Texto principal | `#E8E8EC` | Body, headings |
| Texto secundario | `#9A9BA8` | Subtitles, descriptions, labels |
| Texto terciario | `#5A5C6B` | Placeholders, disabled states, hints |

### Category colors

Used for map markers, filter chips, and category badges. Always pair with the matching dark background.

| Category | Hex | Background tint |
|---|---|---|
| Comida | `#FF6B35` | `rgba(255,107,53,0.1)` |
| Servicios | `#4ECDC4` | `rgba(78,205,196,0.1)` |
| Refacciones | `#F9C74F` | `rgba(249,199,79,0.1)` |
| Clases | `#A78BFA` | `rgba(167,139,250,0.1)` |
| Busco ayuda | `#FF6B9D` | `rgba(255,107,157,0.1)` |

### Color usage rules

- **Never** use the gradient on text — only on solid fills (buttons, avatar backgrounds, top accents).
- **Never** put white or `#E8E8EC` text on a cyan/green surface — use `#0F1117` (near-black) instead.
- On colored category badges, use the 800-level (darkest) shade of the same hue for text.
- Glow effects are allowed only on the map center indicator and the live pulse dot. Nowhere else.

---

## 3. Typography

### Typefaces
El Barrio uses the system font stack — no external font dependency required.

```
font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
```

On platforms where Inter is available, prefer it for display headings.

### Type scale

| Role | Size | Weight | Letter spacing |
|---|---|---|---|
| App name / hero | 20–28px | 600 | −0.03em |
| Section heading | 15–16px | 600 | −0.01em |
| Card title | 14px | 600 | 0 |
| Body / description | 13px | 400 | 0 |
| UI label (uppercase) | 10–11px | 500 | +0.06em |
| Caption / hint | 11–12px | 400 | 0 |

### Writing rules

- **Sentence case everywhere.** Never title case on labels or buttons ("Anunciar en 5 km", not "Anunciar En 5 Km").
- **Active verbs on actions.** "Contactar ahora", "Anunciar tu oferta", not "Enviar" or "Submit".
- **Specific over vague.** "28 personas cerca · 5 km" not "personas cerca de ti".
- **Spanish-first.** All UI copy is in Spanish. Error messages, empty states, and toasts too.

---

## 4. Logo

### Construction
The logo consists of two elements: the **icon** and the **wordmark**.

**Icon** — A filled circle (location dot) centered inside a dashed circle (radio/reach). Represents a person broadcasting within their neighborhood. The icon sits in a rounded square container (`border-radius: 9px`) filled with the primary gradient.

```
Icon container: 36×36px, border-radius 9px
Background: linear-gradient(135deg, #00C8F0, #00E87A)
Inner SVG: 20×20px viewBox 0 0 20 20
  - Solid circle: cx=10, cy=10, r=3, fill=#0F1117
  - Dashed ring: cx=10, cy=10, r=8, stroke=#0F1117, stroke-width=1.5, stroke-dasharray="2.5 2"
```

**Wordmark** — "El Barrio", 20px, weight 600, letter-spacing −0.03em. Paired with the subtitle "Economía local" at 10px, weight 500, uppercase, letter-spacing +0.07em, color `#5A5C6B`.

### Variants

| Variant | When to use |
|---|---|
| Dark (default) | App header, dark backgrounds |
| Light | Light marketing backgrounds |
| Gradient lockup | Social media, splash screens, app icons |
| Icon only | Favicon, app icon, small contexts (< 24px) |

### Clear space
Maintain clear space of at least **1× the icon height** around the full lockup on all sides.

### Don'ts
- Don't rotate or skew the logo.
- Don't change the gradient direction.
- Don't place the logo on a busy photographic background without a backdrop.
- Don't use the wordmark without the icon except in inline text references.

---

## 5. Components

### Cards
All cards in El Barrio share the same base:

```css
background: #1C1E27;
border: 1px solid #2A2D3A;
border-radius: 12px;
padding: 1rem;
```

Offer cards add a **2px gradient accent** on the top edge:

```css
/* ::before pseudo-element */
height: 2px;
background: linear-gradient(90deg, #00C8F0, #00E87A);
```

On hover, cards lift slightly and the border gets a cyan tint:

```css
border-color: rgba(0, 200, 240, 0.4);
transform: translateY(-3px);
box-shadow: 0 10px 24px rgba(0, 200, 240, 0.1);
```

### Buttons

**Primary (CTA)** — gradient fill, dark text, full-width inside cards.
```css
background: linear-gradient(135deg, #00C8F0, #00E87A);
color: #0F1117;
border-radius: 8px;
padding: 8–13px 12–16px;
font-weight: 600;
```

**Secondary / outline** — transparent background, border `#2A2D3A`, text `#9A9BA8`.

**Hover state** — `translateY(-2px)` + `box-shadow: 0 8px 20px rgba(0,200,240,0.25)`.

### Live indicator
The live pill is always visible in the header when the user has active neighbors nearby.

```css
background: rgba(0, 232, 122, 0.08);
border: 1px solid rgba(0, 232, 122, 0.3);
color: #00E87A;
border-radius: 20px;
padding: 6px 12px;
font-size: 12px;
```

The pulse dot animates between `opacity: 1 / scale(1)` and `opacity: 0.4 / scale(1.3)` over 1.8s.

### Distance badges
Small inline badges on offer cards showing proximity:

```css
background: rgba(0, 200, 240, 0.08);
border: 1px solid rgba(0, 200, 240, 0.2);
color: #00C8F0;
border-radius: 10px;
padding: 3px 8px;
font-size: 11px;
```

### Filter chips
Default state: `background: #1C1E27`, `border: 1px solid #2A2D3A`, `color: #9A9BA8`.
Active state: gradient fill (`#00C8F0 → #00E87A`), `color: #0F1117`, no border.

Category chips include a 7px colored dot matching the category color.

---

## 6. Spacing & layout

```
Base unit: 8px
Container max-width: 1000px, horizontal padding 1rem (16px)

Spacing scale:
  xs   4px
  sm   8px
  md   12px
  lg   16px
  xl   24px
  2xl  32px

Border radius:
  sm   8px   (inputs, buttons, badges)
  md   10px  (stat cards)
  lg   12px  (offer cards, main cards)
  xl   20px  (pills, chips)

Grid:
  Offer cards: repeat(auto-fill, minmax(270px, 1fr)), gap 12px
  Stat cards:  repeat(auto-fit, minmax(110px, 1fr)), gap 10px
```

---

## 7. Motion

Keep animations purposeful and subtle. El Barrio is a live app — motion should communicate activity, not distract.

| Element | Animation |
|---|---|
| Live pulse dot | `opacity + scale`, 1.8s ease-in-out, infinite |
| Card hover | `translateY(-3px)` + border/shadow change, 0.2s |
| Button hover | `translateY(-2px)` + glow shadow, 0.2s |
| Button press | `scale(0.98)`, 0.15s |
| Tab switch | Instant — no transition on tab content |

**Respect `prefers-reduced-motion`** — disable the pulse animation and all transforms for users who have it enabled.

```css
@media (prefers-reduced-motion: reduce) {
  .pulse-dot { animation: none; }
  .offer-card:hover, .broadcast-btn:hover { transform: none; }
}
```

---

## 8. Voice & tone examples

| Context | ✅ Do | ❌ Don't |
|---|---|---|
| Empty state | "Sin ofertas en esta categoría" | "No results found" |
| CTA button | "Contactar ahora" | "Submit" / "Send" |
| Broadcast action | "Anunciar en 5 km a la redonda" | "Post listing" |
| Error | "Por favor completa oferta y precio" | "Required fields missing" |
| Success toast | "¡Anuncio enviado! Visible por 3 horas" | "Success" |
| Distance | "0.8 km" | "Nearby" |
| Live status | "28 personas cerca · 5 km" | "Users online: 28" |

---

## 9. CSS variables reference

Add this to your root stylesheet:

```css
:root {
  /* Brand */
  --eb-cyan:        #00C8F0;
  --eb-green:       #00E87A;
  --eb-gradient:    linear-gradient(135deg, #00C8F0, #00E87A);

  /* Surfaces */
  --eb-bg:          #0F1117;
  --eb-surface:     #1C1E27;
  --eb-surface2:    #22252F;
  --eb-border:      #2A2D3A;
  --eb-border2:     #353847;

  /* Text */
  --eb-text:        #E8E8EC;
  --eb-text2:       #9A9BA8;
  --eb-text3:       #5A5C6B;

  /* Categories */
  --eb-food:        #FF6B35;
  --eb-service:     #4ECDC4;
  --eb-item:        #F9C74F;
  --eb-class:       #A78BFA;
  --eb-request:     #FF6B9D;

  /* Spacing */
  --eb-radius-sm:   8px;
  --eb-radius-md:   10px;
  --eb-radius-lg:   12px;
  --eb-radius-pill: 20px;
}
```
