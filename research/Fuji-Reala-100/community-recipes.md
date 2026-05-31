# Fuji Reala 100 — Community Lightroom Recipes & Emulation

## Summary

No widely published Reala-specific Lightroom preset recipe was found in community forums. This is likely because:
1. Reala was discontinued ~2013, before the peak of the "film preset" era
2. Its neutral look is inherently harder to market as a preset than warm/"vintage" looks
3. VSCO Film (the dominant film preset pack of the 2010s) included Reala in their Fuji packs, but VSCO discontinued Lightroom preset sales

However, community discussion provides clear guidance for emulating Reala.

## Community-Recommended Approach

### From r/AnalogCommunity (2026 Thread, 162 comments)

The most relevant thread was a user who shot Fuji films exclusively, took a decade off, and returned to find all their favorites discontinued. Key excerpts:

> *"I miss four-layer color. I don't understand why everyone's so excited about 'warmth'."*

> *"Are Ektar and Pro-Image 100 kinda my only options at this point?"*

**Community consensus:** Pro-Image 100 is the closest currently-produced film to Reala's neutral color palette, though it lacks the 4th layer.

### General Film Emulation Approach (r/AnalogCommunity)

From a detailed thread on creating film presets:

1. **White balance approach**: Users recommend making a preset based on the unexposed film base color (the orange mask between frames). Scan the unexposed border neutral and create a white balance preset. This gets "75% of the way there."

2. **Tone curve method**: Manual RGB tone curve adjustment is preferred over auto-levels, as auto-balancing strips the film's unique color signature.

3. **RNI Films presets** are frequently cited as the most accurate film emulation presets available.

### From r/postprocessing and r/AnalogCommunity

A user working on film emulation described their process:
- Start with calibrated film scans as reference
- Study how film handles tonality, dynamic range, highlight/shadow roll-off
- Use custom Lightroom profiles (not just presets) for color accuracy
- Recommended resource: demystify-color.com for understanding color grading

## Recommended Settings for Reala Emulation (Synthesized)

Based on Reala's known characteristics and general color grading principles:

### Basic Panel
- **White Balance**: Neutral ~5200-5500K (daylight balanced, no warm shift)
- **Tint**: Approximately -2 to -5 (slight green shift to counter most digital sensors' magenta bias)
- **Exposure**: As shot
- **Contrast**: -5 to -10 (Reala has moderate, not high contrast)
- **Highlights**: -15 to -25 (preserve highlight detail like film)
- **Shadows**: +10 to +20 (open up shadows for film-like shadow detail)
- **Whites**: 0
- **Blacks**: -5 to -10

### Tone Curve
- **Point Curve**: Medium contrast or custom S-curve with gentle roll-off
- Reala has a more linear midtone response than Kodak films — avoid heavy S-curves
- Lift the black point slightly (+5-10 RGB points) for film-like "open" shadows

### HSL / Color
- **Red Hue**: -5 (pull reds slightly toward true red, away from orange)
- **Orange Hue**: -5 to -10 (skin tone correction — move orange toward true orange, away from yellow)
- **Yellow Hue**: -5
- **Green Hue**: +5 to +10 (greens should be accurate, not yellow-green)
- **Aqua/Blue**: Minimal adjustment — the 4th layer handled cyan separation naturally
- **Blue Saturation**: -5 to -10 (Reala blues are clean, not punchy)
- **Green Saturation**: +5 (greens are well-rendered)

### Color Grading
- **Shadows**: Add very subtle cool/blue (Hue ~225, Sat ~5-10) — Reala shadows tend slightly cool
- **Midtones**: Neutral — no warmth added
- **Highlights**: Slightly cool (matching Reala's neutral-to-cool white balance)

### Detail
- **Sharpening**: Amount 25-40, Radius 1.0, Detail 25 (fine grain film renders as smooth detail)
- **Noise Reduction**: Minimal — Reala grain is fine and pleasing

### Calibration
- **Red Primary**: Hue +5, Sat -10 (tame red-channel warmth)
- **Green Primary**: Hue +10, Sat +5 (boost green separation)
- **Blue Primary**: Hue -5, Sat -10 (clean, not over-saturated blues)

## Key Differentiation from Other Film Emulations

What makes *Reala* different from:
- **Portra preset**: Remove warmth, increase green accuracy, cooler shadows
- **Ektar preset**: Reduce contrast, reduce saturation, finer grain
- **Fuji Superia preset**: Finer grain, more neutral color, less "consumer" saturation
- **Kodak Gold preset**: Dramatically cooler, remove yellow-gold cast, neutral skin tones

## Source Threads

- "Flexible everyday color film recs for a Portra hater?" — r/AnalogCommunity, May 2026 (162 comments)
- "Confusion regarding colour correcting film scans" — r/AnalogCommunity (Fuji Reala 100 scanning discussion)
- "Do any of you keep film stock presets in Lightroom?" — r/AnalogCommunity
- "Creating Kodak Fun Saver Preset in Lightroom" — r/AnalogCommunity
- "After months of tweaking and testing, I think I finally nailed the film look" — r/postprocessing
- "Working on a Kodachrome Lightroom Emulation Preset" — r/postprocessing

*Note: Settings above are synthesized from community knowledge of Reala's characteristics, not from a verified published recipe. Users should calibrate against actual Reala scans.*
