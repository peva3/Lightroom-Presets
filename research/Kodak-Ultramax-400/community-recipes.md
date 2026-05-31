# Kodak Ultramax 400 — Community Lightroom Recipes & Settings

Compiled from Reddit (r/AnalogCommunity, r/postprocessing, r/analog), photography forums, YouTube creators, and preset makers.

---

## Recipe 1: "Budget Portra" Base Look (from r/postprocessing)

Source: Reddit user Laetheralus93 — "Kodak HybridMax" (a blend of Ultramax, Portra, and Gold characteristics)

### Profile
- Adobe Color or Camera Standard profile
- Profile strength: 100%

### Basic Panel
- Contrast: +15 to +25
- Highlights: -20 to -35
- Shadows: +10 to +20
- Whites: +5 to +10
- Blacks: -10 to -20
- Clarity: -5 (slight softening to emulate film)
- Vibrance: +10 to +15
- Saturation: -5 (compensate for vibrance boost)

### Tone Curve
```
Point Curve: Medium Contrast or Custom S-curve
- Lift black point slightly (+5, 0 to 5, 0)
- Pull highlight point down slightly (95, 95 to 95, 90)
- Add slight concavity in shadows (flattened shadows)
```

### HSL Adjustments
| Color | Hue | Saturation | Luminance |
|-------|-----|------------|-----------|
| Red | +5 | +15 | -5 |
| Orange | -5 | +20 | -3 |
| Yellow | -10 | +15 | -5 |
| Green | -15 | -5 | -10 |
| Aqua | -5 | -10 | +5 |
| Blue | 0 | -5 | -10 |
| Purple | +5 | -10 | +5 |
| Magenta | +5 | -5 | 0 |

### Color Grading
- **Highlights**: Hue 45° (warm yellow-gold), Saturation 15–20
- **Midtones**: Hue 35° (warm), Saturation 5–10
- **Shadows**: Hue 200° (teal-blue), Saturation 10–15
- **Blending**: 60
- **Balance**: +20 (shift toward warm highlights)

### Calibration
- Red Primary: Hue +10, Saturation +15
- Green Primary: Hue -5, Saturation 0
- Blue Primary: Hue -15, Saturation +10

### Grain
- Amount: 25–35
- Size: 30–35
- Roughness: 50–60

---

## Recipe 2: "Golden Hour in a Can" (from YouTube creator, approximated)

### Basic Panel
- Temperature: +8 to +12 (warm)
- Tint: +2 to +5 (slight magenta to balance green)
- Exposure: +0.15 to +0.30
- Contrast: +20
- Highlights: -30
- Shadows: +15
- Whites: +10
- Blacks: -15
- Vibrance: +15
- Saturation: -5

### Tone Curve
- RGB Point Curve: Strong Contrast
- Red channel: Slightly lift highlights (warm highlight roll-off)
- Blue channel: Lower shadow point slightly (cooler shadows)

### HSL
| Color | Hue | Sat | Lum |
|-------|-----|-----|-----|
| Red | +8 | +20 | -3 |
| Orange | -3 | +25 | -5 |
| Yellow | -12 | +10 | -8 |
| Green | -20 | -10 | -15 |
| Aqua | -10 | -10 | +5 |
| Blue | +5 | -10 | -15 |
| Purple | 0 | -15 | +5 |
| Magenta | +5 | -10 | 0 |

### Color Grading
- Highlights: Hue 40, Sat 20
- Midtones: Hue 40, Sat 8
- Shadows: Hue 210, Sat 10
- Blending: 50

---

## Recipe 3: General Community Consensus (aggregated from Reddit threads)

### Key themes from community discussion:

1. **White Balance**: Most shooters describe Ultramax as having a **warm golden cast** in daylight, but **cooler than Gold 200**. Target 5400–5800K with +5 to +10 tint toward magenta.

2. **Contrast**: Universally described as **punchy and contrasty**. Significantly more contrast than Portra 400. Strong S-curve with lifted blacks (filmic shadow behavior).

3. **Saturation**: High saturation, especially in **reds, oranges, and yellows**. Some labs reduce saturation in scanning. Blues described as vivid but with darker luminance.

4. **Shadows**: Described as having a **cool/teal tendency** — multiple users mention "slightly green shadows" or "teal in the lows."

5. **Skin tones**: "UltraMax tends to make people look yellow" — one Reddit user (epandrsn). Skin tones described as less flattering than Portra; warmer and more saturated.

6. **Grain**: Noticeable grain, especially compared to Portra 400. At box speed, grain is visible in midtones and skies. On half-frame cameras, grain is "very noticeable."

7. **Overexposure behavior**: At +1 to +3 stops over, Ultramax holds color well (per alchemycolor's ColorChecker tests). At +4 stops, colors begin shifting. Underexposure amplifies grain significantly.

8. **Vs Fuji 400**: Users note they are "almost interchangeable" though some prefer Ultramax for warm tones, Fuji for green/blue scenes.

### Additional tips from community:
- **Scanning matters**: Lab scans on Fuji SP3000 / Noritsu HS-1800 can dramatically alter the look. Frontier scans tend to amplify film stock "characteristics."
- **NLP (Negative Lab Pro)**: Many home scanners report Ultramax converts easily in NLP with minimal tweaking — described as having a "relatively neutral" color profile as a negative.
- **Best use cases**: Sunny days, golden hour, flash photography, travel, everyday snapshots. Less ideal for portraits where skin tones are critical.

---

## Recipe 4: "Everyday Ultramax" Quick Mobile Preset (Lightroom Mobile)

### Light
- Exposure: +0.15
- Contrast: +20
- Highlights: -25
- Shadows: +15
- Whites: +10
- Blacks: -15

### Color
- Temp: +10
- Tint: +4
- Vibrance: +12
- Saturation: -3

### Effects
- Texture: -10
- Clarity: -8
- Dehaze: +5
- Vignette: -5

### Detail
- Sharpening: 30
- Noise Reduction: 10
- Grain: Amount 30, Size 25, Roughness 50

---

## Known Preset Packs Including Ultramax 400

| Pack Name | Creator | Platform | Notes |
|-----------|---------|----------|-------|
| Film Emulations (HybridMax) | Laetheralus93 (Reddit) | Lightroom profiles | Custom profile + LR adjustments, hybrid of UltraMax/Portra/Gold |
| Alchemy Color Film Emulation | alchemycolor.com | Lightroom/Resolve | Research-grade emulation based on color chart analysis |
| VSCO Film Pack (discontinued) | VSCO | Lightroom (legacy) | Included Ultramax via their "Kodak Gold" variants; no longer sold |
| RNI All Films 5 | Really Nice Images | Lightroom/Capture One | Includes Ultramax 400 in their "Consumer Films" category |
| Mastin Labs Kodak Everyday | Mastin Labs | Lightroom/Capture One | Includes Gold and Ultramax-inspired profiles |
| Filmborn (discontinued) | Mastin Labs | iOS | Previously had Ultramax profile |
| The Archetype Process | TAP | Lightroom | Kodak Pro Pack — closest match is their Gold profile |
| CineGrain | CineGrain | LUTs/video | Has Ultramax film grain scans |

---

## Notes on Preset Accuracy

Community consensus is strong that **no single slider recipe works universally** — the scanning/inversion method dramatically affects the final look. A proper emulation requires:
1. A calibrated **camera profile** (color response mapping)
2. A **tone curve** matching the film's characteristic curve
3. **HSL/grading** adjustments for the color cast
4. **Grain overlay** matching the actual grain structure

For Lightroom-only approaches, the recipes above provide a starting point that should be tuned per image.
