# Kodak Portra 400 — Community Lightroom Recipes

> Compiled from Reddit (r/Lightroom, r/postprocessing, r/analog), YouTube tutorials, forums, and community presets. This is NOT one "official" recipe — Portra 400 has many interpretations depending on scanner profile, exposure, and creative intent.

---

## Recipe Philosophy: The "Graded Scan" Problem

Every Portra 400 recipe depends on which scanner profile you're targeting:

- **Noritsu HS-1800**: Cooler, more magenta/cyan, higher contrast, punchy
- **Fujifilm Frontier SP-3000**: Warmer, greener shadows, lower contrast, more "filmic"
- **DSLR/Mirrorless scan** with Negative Lab Pro: Neutral starting point, highly variable

Most commercial presets (RNI, Mastin, VSCO) target the **Frontier** or **Noritsu** look.

---

## YouTube Tutorials (Most Referenced)

### Tone Fuentes — "How to Create the Kodak Portra 400/800 Look in Lightroom Classic"
- **Link**: `youtube.com/watch?v=TIZFooNHu94`
- **Cited extensively** on r/postprocessing
- Method: Create a Color Profile (not preset), warm tone curve with lifted blacks, desaturated greens
- Key adjustments:
  - Tone curve: S-curve with raised black point (blacks +15 to +30)
  - HSL: Green hue +10 toward yellow, Green saturation -15
  - Color grading: Warm highlights (golden), cool shadows (slight teal)
  - Calibration: Blue primary hue shifted toward cyan
- Reddit reception: Mixed. Some users say it's too yellow/warm.

### Jamie Windsor — "Portra" Preset Pack
- **Link**: `jamiewindsor.com/portra`
- Highly recommended on r/Lightroom
- Medium Format Stocks (Set #2) praised for Portra 400
- Profile-based (works across camera brands)

### Alex Ruskman — Film Emulation Presets
- Mentioned on r/Lightroom: "Alex Ruskman's Portra 800 (and 400)"
- Sold on Etsy / Gumroad
- LUT/profile-based approach

---

## Commercial Preset Rankings (from Reddit)

### Best Portra 400 Presets — r/Lightroom Consensus

| Rank | Product | Price | Format | Notes |
|------|---------|-------|--------|-------|
| **#1** | **RNI All Films 5** | $149 | Profiles | Most accurate colors, clips white/black points, shadow lift baked in |
| **#2** | **Caleb Salvadori Film Preset Collection** | ~$60 | Profiles | Narrower selection (~25 presets), very high quality, praised over RNI by some |
| **#3** | **Really Nice Images (RNI) Demo** | Free | Profiles | Free Portra 400 in trial, color accurate but whites can appear gray |
| **#4** | **Mastin Labs Portra Original** | $99 | Presets | Designed for batch wedding editing, strong look out of box |
| **#5** | **Color Precision** | ~$40 | Profiles | Noritsu-specific profile, needs highlight adjustment post-apply |
| **#6** | **VSCO Film 06** (discontinued) | n/a | Profiles | Still the benchmark for many old-timers, Portra 400+ and 400- variants |
| **#7** | **Jamie Windsor** | ~$15–25 | Profiles | Budget option, Portra in Essentials pack |
| **#8** | **Cobalt Image** | ~$60 each | Profiles | Very accurate, expensive per-stock, "not moody but clinical" |
| **#9** | **ANDP Film Styles** | ~$5 | LUT/Profile | Cheapest option, LUT-based, mentioned on r/postprocessing |
| **#10** | **Nik Collection / DxO FilmPack** | varies | Profiles | Integrated into workflow, mentioned as alternative |

### Key Reddit Threads:
- `r/Lightroom/comments/vx0a1y` — "Who makes the best Kodak Portra 400 Preset?" (16 upvotes, 21 comments)
- `r/Lightroom/comments/1q9x9vc` — "RNI vs Color Precision comparison" (screenshot comparison)
- `r/Lightroom/comments/1de4z6p` — "Film Style Preset Packs?" (21 upvotes, 19 comments)

---

## Community DIY Lightroom Recipes

### Recipe A: "The Classic Overexposed Portrait Look" (Noritsu-targeted)

From a r/postprocessing user who matched the "Find Lab / Carmencita Noritsu look":

```
Basic:
  Exposure: +0.30 to +0.70
  Contrast: -10 to -15
  Highlights: -40
  Shadows: +25
  Whites: -5
  Blacks: +15 (lifted blacks)

Tone Curve:
  Point curve: Mild S
  Blacks output: ~15 (RGB)
  Midtones: Slight bump

HSL / Color:
  Orange Hue: -3 (warmer skin)
  Orange Saturation: -5
  Orange Luminance: +15 (brighten skin)
  Yellow Hue: -8 (toward orange)
  Yellow Saturation: -10
  Green Hue: +15 (toward yellow, crucial "Portra green")
  Green Saturation: -20
  Aqua Saturation: -10
  Blue Hue: -5
  Blue Saturation: -15
  Blue Luminance: -10 (deeper skies)

Color Grading:
  Highlights: Warm (45° hue, 10-15 saturation)
  Midtones: Neutral or slightly warm
  Shadows: Cool (210° hue, 5-10 saturation)
  Blend: 50-70

Calibration:
  Red Primary: Hue +5, Sat -5
  Green Primary: Hue +15, Sat -10
  Blue Primary: Hue -10, Sat -5

Effects:
  Grain Amount: 20-30
  Grain Size: 25
  Roughness: 50
```

### Recipe B: "The YouTube Frontier Look" (Tone Fuentes-inspired)

```
Basic:
  Exposure: 0.00 (adjust per image)
  Contrast: -5
  Highlights: -70
  Shadows: +30
  Whites: 0
  Blacks: +20

Tone Curve:
  Raise black point (output ~20)
  S-curve for midtones

HSL:
  Orange Hue: +5
  Orange Saturation: -5
  Green Hue: +20
  Green Saturation: -25
  Blue Saturation: -10
  Blue Luminance: -15

Color Grading:
  Shadows: Cyan/Teal (190°, Sat 5)
  Highlights: Amber/Gold (40°, Sat 15)

Calibration:
  Red Primary: Hue +10
  Green Primary: Hue +15
  Blue Primary: Hue -15

Grain:
  Amount: 15-25
```

### Recipe C: "The Neutral/Natural Scan Look"

For those who want the film look without heavy color cast:

```
Basic:
  Exposure: +0.50 (overexposed Portra look)
  Contrast: 0
  Highlights: -50
  Shadows: +40
  Whites: 0
  Blacks: 0

Tone Curve:
  Lift blacks slightly (output 5-10)
  Very gentle S-curve

HSL:
  Green Hue: +10
  Green Saturation: -10
  Blue Saturation: -5

Calibration:
  Green Primary: Hue +5

Grain:
  Amount: 20
```

---

## Fujifilm In-Camera Recipe (Fuji X Weekly)

### Kodak Portra 400 v2 — for X-T3 / X-T30

From Fuji X Weekly (Ritchie Roesch), 2021-08-17:

```
Film Simulation: Classic Chrome
Dynamic Range: DR-Auto
Highlight: -1
Shadow: -1
Color: +2
Noise Reduction: -4
Sharpening: -2
Grain Effect: Strong
Color Chrome Effect: Strong
White Balance: Daylight, +2 Red & -6 Blue
ISO: Auto, up to ISO 6400
Exposure Compensation: +2/3 to +1 (typically)
```

**X100V / X-T4 / X-Trans IV version** is slightly different (also on Fuji X Weekly).

### User Feedback (from blog comments):
- "Really shines with front and side lit scenes, becomes very washed out shooting into the light — exactly how Portra behaves"
- "DR400 recommended in harsh sunlight for more film-like DR"

---

## Common Community Mistakes (from Reddit critiques)

1. **Too much yellow/orange** — Users often push warmth too far. Portra 400 is warm, but naturally — not Instagram-filter warm. Real Portra has cool shadow tones that balance the warmth.

2. **Over-lifting blacks** — Real Portra 400 (properly exposed/developed) does NOT have crushed or heavily lifted blacks. The "faded blacks" look is more characteristic of underexposed or expired film.

3. **Ignoring the scanner profile** — Applying a Noritsu-targeted preset to a Frontier scan (or vice versa) will look wrong. Noritsu profiles have already boosted contrast; Frontier profiles are flatter.

4. **Too much grain** — Portra 400 (especially 120 format) is surprisingly fine-grained. Adding heavy grain makes it look like 35mm pushed 2 stops, not the medium-format Portra look most seek.

5. **Wrong source image** — Users note that the scene matters: "editing an indoor photo of your cat is not the same as the typical cliché photo of a tennis court." Portra excels in certain conditions (golden hour, open shade, overcast).

6. **Preset ≠ Profile** — Presets just move sliders. Profiles (LUTs/ICC) remap color at a fundamental level. Users who just use presets on different camera brands report wildly different results. The recommendation on Reddit is consistently: use a **profile** as the base, then fine-tune with presets/sliders.

---

## YouTube Channels with Portra 400 Editing Content

- **Tone Fuentes** — Structured method for Portra 400/800 color profile creation
- **Jamie Windsor** — Film emulation presets for sale, deep dives into film aesthetics
- **Kyle McDougall** — Film photography focus; occasionally covers scanning/editing
- **Willem Verbeeck** — Film-centric; shows lab scans but not Lightroom recipes per se
- **GxAce (Jason Kummerfeldt)** — Film reviews with scanning notes
- **Matt Day** — Film/darkroom focus

---

*Compiled May 2026 from active Reddit threads, YouTube tutorials, and community forums. Settings are starting points — always adjust for your specific image, lighting, and camera.*
