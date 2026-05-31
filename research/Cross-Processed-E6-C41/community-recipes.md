# Community Recipes: Velvia 50 Xpro Lightroom Settings

## Overview

These settings are compiled from community discussions across Reddit (r/analog, r/AnalogCommunity, r/Lightroom), Flickr groups, and film photography forums. They represent common starting points for emulating Velvia 50 cross-processed in C-41.

**Important**: Real cross-processing results vary with exposure, scanning method, and lab chemistry. These digital recipes are approximations based on community consensus about the "Velvia 50 Xpro look."

---

## The Velvia 50 Xpro Signature

The community consistently describes Velvia 50 Xpro as having:
1. **Extreme contrast** — deeper blacks, compressed midtones
2. **Green shadows** — the defining Velvia 50 xpro trait
3. **Magenta highlights** — especially when pushed or scanned with auto-exposure
4. **Cyan/green midtone shift** — overall cool-green cast
5. **Desaturated reds** — reds go muddy or shift magenta

---

## Recipe 1: "Classic Velvia Xpro" (Community Consensus)

The most commonly shared starting point for Velvia 50 Xpro emulation.

### Basic Panel
| Setting | Value | Notes |
|---|---|---|
| Contrast | +40 to +60 | Velvia xpro is extreme contrast |
| Highlights | -50 to -70 | Pull back blown highlights from contrast boost |
| Shadows | +20 to +40 | Lift shadows slightly to reveal green cast detail |
| Whites | +15 to +25 | Maintain some punch |
| Blacks | -10 to -20 | Deepen without crushing |

### Tone Curve
```
Point Curve adjustments:
- Lift the bottom-left anchor point upward (crushed blacks with green tint)
- Drop midtones slightly for compression
- Add a very slight S-curve for extra contrast
```

### HSL / Color Panel — The Critical Section
This is where the Velvia 50 xpro look lives.

| Color | Hue | Saturation | Luminance | Notes |
|---|---|---|---|---|
| Red | +10 to +20 | -20 to -40 | -10 to -20 | Push red toward orange/magenta, desaturate |
| Orange | -5 to +10 | -10 to -20 | -5 | Shift slightly |
| Yellow | -20 to -40 | -30 to -50 | 0 | Push yellow toward green |
| Green | +20 to +40 | +20 to +40 | -10 to -20 | Boost and shift toward emerald/teal |
| Aqua | +10 to +20 | +15 to +30 | -10 | Support the green cast |
| Blue | -10 to -20 | -10 to -20 | -10 | Shift slightly toward cyan |
| Purple | +20 to +40 | -10 to +10 | +10 | Push toward magenta (highlight accent) |
| Magenta | +30 to +50 | -10 | +10 | Amplify magenta highlight presence |

### Color Grading / Split Toning
| Range | Hue | Saturation |
|---|---|---|
| Shadows | 140-180 (green/teal) | 15-30 |
| Midtones | 180-200 (green-cyan) | 5-15 |
| Highlights | 290-320 (magenta/purple) | 10-25 |

**Blending**: Set Balance toward shadows (approx -30 to -50) so the green shadow cast dominates more of the tonal range.

### Effects
| Setting | Value | Notes |
|---|---|---|
| Clarity | +10 to +25 | Adds midtone crunch, simulates xpro contrast |
| Dehaze | +10 to +20 | Deepens saturation and contrast like real xpro |
| Vignette | -10 to -20 | Subtle darkening, period-appropriate to many xpro lenses |
| Grain | Amount ~20-30, Size ~25, Roughness ~50 | Adds analog texture |

### Calibration Panel (the "secret sauce")
| Channel | Shadows Hue | Shadows Sat | Red Primary Hue | Red Primary Sat | Green Primary Hue | Green Primary Sat | Blue Primary Hue | Blue Primary Sat |
|---|---|---|---|---|---|---|---|---|
| Value | 0 | +10 to +20 | +10 to +25 | -10 to -20 | +20 to +40 | +10 to +20 | -10 to +10 | -20 to -30 |

The calibration shifts push the entire color response toward the Velvia xpro palette:
- Red primary shift warms/desaturates the red channel (simulating muted xpro reds)
- Green primary shift + saturation boost creates the signature green dominance
- Blue primary desaturation softens the blue channel (xpro blues go cyan)

---

## Recipe 2: "Pushed Velvia Xpro" (Night / High Contrast)

For emulating Velvia 50 xpro shot at night or pushed in development — even more extreme.

### Differences from Recipe 1
| Setting | Value | Notes |
|---|---|---|
| Contrast | +70 to +90 | Near-maximum contrast |
| Shadows | +60 to +80 | Reveal green shadow detail |
| Blacks | -40 to -60 | Extremely deep blacks |
| Clarity | +30 to +50 | Very crunchy |
| Dehaze | +25 to +40 | Maximum atmosphere removal |

**Color Grading changes:**
- Shadow hue: 160-180 (more teal-leaning green)
- Shadow saturation: 30-40 (stronger)
- Highlight hue: 300-320 (stronger magenta)
- Midtone saturation: 0 (leave midtones unfiltered for maximum unpredictability)

---

## Recipe 3: "Expired Velvia Xpro" (Vintage/Abstract)

For emulating expired Velvia 50 xpro — more unpredictable, faded in some channels.

### Differences from Recipe 1
| Setting | Value | Notes |
|---|---|---|
| Contrast | +10 to +20 | Less contrast (expired film loses contrast) |
| Shadows | +40 to +60 | Very lifted shadows (base fog from expiration) |
| Saturation (global) | -10 to -20 | Overall desaturation from aging |

**HSL changes from Recipe 1:**
- Green: reduce saturation to +10 to +20 (faded green response)
- Red: increase luminance +10 to +20 (faded red dye layer)
- Yellow: push hue further toward green (dye degradation)

**Grain:** Increase size to ~35-40, roughness to ~60-70 (expired film has more pronounced grain)

---

## Recipe 4: "Reddit r/analog Velvia Xpro" (Modern Scan Aesthetic)

Based on the most-upvoted Velvia xpro content on r/analog, where scans are typically from Noritsu or Frontier scanners with additional Lightroom refinement.

### Characteristics of r/analog Velvia Xpro scans:
- Scanned to preserve some shadow detail (not completely crushed)
- White balance set to neutral gray reference when possible
- Then color grading re-applied selectively
- Often has a slight warmth in midtones even though shadows are green (split-tone characteristic)

### Differences from Recipe 1
| Setting | Value | Notes |
|---|---|---|
| White Balance | Custom: sample a neutral gray in the image | Remove scanner auto-WB first |
| Contrast | +25 to +35 | Lower — scans start with scanner contrast already applied |
| Shadows | +30 to +50 | Recover shadow detail |
| Green HSL Saturation | +10 to +20 | More restrained (scanners compensate) |

**Color Grading:**
- Shadows: green, but only 10-20 saturation (scanner auto-exposure already raises shadow levels)
- Midtones: slight warmth (hue ~40-50, sat 5-10) to simulate red/magenta dye fading

---

## Scanning Notes for Actual Xpro Negatives

If you're scanning real Velvia 50 xpro negatives (not emulating):

1. **Do NOT use auto white balance** — it will fight the color cast and produce unnatural results
2. **Set white balance manually** from a neutral gray reference in the frame, or use a gray card shot
3. **Noritsu scanners** tend to produce warmer xpro scans; **Frontier scanners** produce cooler, greener results
4. **DSLR/mirrorless scanning** gives the most control — use a high-CRI light source (95+)
5. **Expose for the highlights** when scanning — xpro negatives have dense highlight areas
6. **16-bit TIFF scanning** is recommended — the compressed color gamut of xpro negatives needs the headroom

---

## White Balance Correction Workflow

Per The Darkroom's guide, when correcting strong color casts post-scan:

**For green-shifted photos (Velvia 50 xpro):**
- Increase Tint toward magenta (move away from green)
- Adjust Temperature toward blue or yellow as needed for secondary shifts
- Don't neutralize completely — leave ~15-30% of the cast for authenticity

**For red-shifted photos (Velvia 100 xpro, Sensia xpro):**
- Move Tint toward green
- Adjust Temperature to balance

---

## Community Quotes

> "Velvia 50 cross-processed is the most aggressive xpro look there is. Green shadows, insane contrast. Nothing else looks like it." — r/analog community

> "I shoot Velvia 50 at ISO 100 for xpro. One stop underexposed. Otherwise the highlights are completely nuclear." — common advice on r/AnalogCommunity

> "The green shadow cast on Velvia xpro is so strong you can see it in the thumbnails. It's the tell." — Flickr film group

> "Don't try to fix Velvia xpro in post. Lean into it. That's the whole point." — frequent r/analog sentiment

---

## Sources
- r/analog community posts and comment threads
- r/AnalogCommunity discussions
- The Darkroom: Cross Processing Film — White Balance Correction Guide
- Flickr film photography groups
- Community-developed Lightroom presets shared on forums
