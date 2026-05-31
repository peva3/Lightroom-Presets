# Kodak Portra 160 — Community Recipes

> Settings gathered from Reddit r/analog, r/Lightroom, r/postprocessing, photography forums, and YouTube.  
> These are starting points — every image needs per-scene adjustment.

---

## Recipe 1: "Portra 160 Base" — Soft Daylight Portrait

**Source:** r/postprocessing, r/Lightroom, multiple threads (2017–2025)

```
Tone Curve (Parametric):
  Highlights:  −15
  Lights:      +10
  Darks:       +25
  Shadows:     +30

Tone Curve (Point):
  Lift black point to output ~8 (soft black)
  Very gentle S-curve — no hard knee

Basic Panel:
  Contrast:    −10 to −20
  Exposure:    +0.30 to +0.70 (expose to the right)
  Whites:      −10
  Blacks:      +15 to +25 (lifted blacks)

HSL / Color:
  Hue:         Orange +5, Yellow +3, Green +8 (toward cool green), Aqua −5
  Saturation:  Red −10, Orange −5, Yellow −5, Green −15, Blue −10, Purple −20
  Luminance:   Orange +15 (skin glow), Green −5 (depth), Blue −10

Calibration:
  Red Primary:    Hue +5, Sat −10
  Green Primary:  Hue −10, Sat −10
  Blue Primary:   Hue −5, Sat −10

Grain:
  Amount:     15–25
  Size:       20–25
  Roughness:  40–50

Camera Profile: Adobe Standard or Camera Neutral
```

---

## Recipe 2: VSCO Film 06 — Portra 160+ (The Gold Standard)

**Source:** r/Lightroom, multiple threads referencing VSCO 06 (discontinued)

The VSCO Portra 160+ preset was widely considered the most accurate Portra 160 emulation. Key characteristics reverse-engineered by the community:

```
Profile:       VSCO Portra 160+ (custom camera profile, not just preset)
Tone:          Flat S-curve, lifted shadows, slight highlight compression
White Balance: +3 toward yellow-green (cooler than Portra 400 which is +5 warm)
Contrast:      −15 to −25 (ultra-soft)
Saturation:    −5 to −15 (muted, pastel-like)
Split Toning:  Highlights: 0 saturated, 50 hue (subtle warmth)
               Shadows:     5 saturation, 210 hue (cool blue, barely there)

Known VSCO Cam equivalents:
  A1 = Kodak Portra 160+ (+1 Tint)
```

**Community consensus:** VSCO 06 Portra 160 presets remain the benchmark. Users who lost access after laptop theft / OS upgrade consistently seek replacements from Mastin Labs, RNI, or Color Precision.

---

## Recipe 3: The "Jonathan Canlas" Portra Look

**Source:** r/analog, r/postprocessing threads referencing Jonathan Canlas Photography

Canlas's signature Portra 160/400 look (shot on Pentax 67 / RZ67, often +1 stop overexposed):

```
Exposure:     +1.0 stop in-camera (or +0.7 to +1.0 in LR)
Contrast:     Very soft — achieved via lifted black point in curves, NOT the contrast slider
S-curve:      Steep in midtones for punch, but soft landing at both ends
               — Blacks lifted to ~5-8% (never pure black)
               — Whites capped at ~92-95% (never blown)
Color:        Very low blue presence — blue channel desaturated and warmed
              Greens: muted but still distinguishable
              Reds: warm but not saturated, leaning toward coral/orange
Skin:         "Pastel-flawless" — achieved via overexposure + orange luminance boost
Grain:        Medium format grain simulation (light, fine)

Key insight from Canlas analysis:
  "He doesn't use much blue tones...
   highlight/shadow toning going on...
   contrast always feels very soft and gentle"
```

---

## Recipe 4: AndP FilmStyles Portra 160

**Source:** r/postprocessing, andpfilmstyles.com blog (2023)

AndP FilmStyles offers a Portra 160 simulation praised for:
- Soft midtone contrast with natural roll-off
- Cooler white balance than most Portra emulations
- Subdued greens (closer to real Portra 160 rather than the warmer "internet Portra" look)
- Subtle grain matching 35mm and 120 formats

**Key settings shared on their blog:**
```
Base Profile: Adobe Standard → modified per-camera
Tone Curve: Gentle S-curve with lifted blacks
HSL emphasis: Reduce Blue saturation, shift Aqua toward Green
Calibration: Cooler blue primary (+ hue, − sat)
```

---

## Recipe 5: Alex Ruskman Portra 160 Presets

**Source:** r/postprocessing (2023 thread), Gumroad

Alex Ruskman's 200+ XMP file pack includes Portra 160, 400, and 800. Community feedback:
- "Super velvety" — particularly praised for Portra 160 emulation
- Better than Mastin Labs according to some users
- Priced at ~$20 for the full 200+ XMP pack
- Available on Gumroad: `alexruskman.gumroad.com`

---

## Recipe 6: The DIY Approach — Rebuilding Portra 160 from Scratch

**Source:** r/postprocessing, multiple deep-dive threads on film emulation technique

### Step 1: White Balance
Portra 160 is daylight-balanced at 5500K. Start at 5200–5500K, tint −3 to +2 (slightly toward green for the cooler Portra 160 feel).

### Step 2: Tone Response
The single most important element. Use a **point curve** (not parametric):
```
→ Pull the black point up (blacks → dark gray, ~RGB 15,15,15)
→ Pull white point down slightly (~RGB 242,242,242)
→ Create a very gradual S-curve through the midtones
→ Add a second inflection point in the upper quarter for highlight roll-off
```
The "soft contrast with preserved detail" is a combination of lifted blacks + rolled-off highlights + boosted midtone micro-contrast.

### Step 3: Color
```
HSL Panel:
  Red:       Hue +2, Sat −15, Lum +5     → coral/pastel reds
  Orange:    Hue +5, Sat −10, Lum +15     → glowing skin
  Yellow:    Hue +3, Sat −10, Lum 0       → muted warm tones
  Green:     Hue +8, Sat −20, Lum −5      → cooler, subdued greens
  Aqua:      Hue −5, Sat −15, Lum 0       → pull toward teal
  Blue:      Hue 0, Sat −15, Lum −10      → muted sky
  Purple:    Hue 0, Sat −20, Lum 0
  Magenta:   Hue 0, Sat −10, Lum 0

Calibration:
  Red Primary:   Hue +5, Saturation −10
  Green Primary: Hue −10, Saturation −10
  Blue Primary:  Hue −5, Saturation −10
```

### Step 4: Grain
Portra 160 has RMS ~4. In Lightroom:
```
Grain Amount: 15–20 (35mm) / 8–12 (120) / Off (4×5)
Grain Size:   20–25
Roughness:    40–50 (smoother grain character)
```

### Step 5: Lens Correction
Portra 160 has natural vignetting from lens + scanning. Add subtle vignette (−5 to −10) if desired, but many clean scans have minimal vignette.

---

## Community-Shared Slider Positions (Aggregated Average)

From threads where users posted actual LR settings for Portra 160 emulation:

| Slider | Average Value | Range |
|--------|--------------|-------|
| Exposure | +0.50 | +0.20 to +1.00 |
| Contrast | −15 | −5 to −30 |
| Highlights | −25 | −10 to −40 |
| Shadows | +30 | +15 to +50 |
| Whites | −10 | 0 to −20 |
| Blacks | +20 | +10 to +35 |
| Clarity | −5 | −15 to +5 |
| Vibrance | −5 | −10 to +5 |
| Saturation | −10 | −5 to −20 |
| Temp | 5200K | 5000–5500 |
| Tint | +3 | 0 to +8 |

---

## Important Community Caveats

1. **No single preset works across all lighting.** Portra 160 looks dramatically different in golden hour vs. overcast vs. studio flash. Most users recommend at least 2–3 variants (direct sun, shade, strobe).
2. **The "internet Portra" look is often Portra 400, not 160.** The warm, saturated, high-contrast "Portra look" on Instagram/Flickr is predominantly Portra 400. Portra 160 is cooler, softer, and more muted.
3. **Scanner matters more than the preset.** Frontier scans lean cool/cyan; Noritsu scans lean warm/magenta. This can shift the entire baseline — a preset made from Noritsu scans needs adjustment for Frontier, and vice versa.
4. **Overexposure is key.** Nearly every community recipe emphasizes shooting Portra 160 at ISO 100–125 (or boosting exposure +0.3 to +1.0 in LR) for the signature pastel skin look.
5. **"Faded blacks" technique:** The lifted black point via point curve (NOT the Blacks slider) is the single most-recommended technique for achieving the soft Portra 160 contrast without making images look "dull."
