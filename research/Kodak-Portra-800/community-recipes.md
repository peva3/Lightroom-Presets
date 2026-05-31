# Kodak Portra 800 - Community Recipes & Lightroom Settings

This document compiles known community approaches to emulating Portra 800 in Lightroom. Community recipes are less documented than for Portra 400, but general techniques share common patterns.

## General Community Approach (Consensus)

### Typical Base Adjustments
These are community-consensus starting points derived from general Portra 800 discussions, forum posts, and YouTube tutorials:

### Tone Curve
- **Lifted blacks** (raise the black point on the tone curve ~5-10%)
- **Compressed highlights** (pull highlight endpoint down slightly, ~5% from top)
- Create a gentle S-curve for contrast while maintaining film-like roll-off
- The characteristic curves from the datasheet show a long linear region with smooth shoulder in highlights

### Basic Panel
- **Exposure**: +0.10 to +0.30 (slight overexposure emulates popular Portra shooting style)
- **Contrast**: -10 to -20 (compensate for tone curve adjustments)
- **Highlights**: -45 to -70 (Portra has exceptional highlight retention)
- **Shadows**: +30 to +50 (lift shadows for that film latitude look)
- **Whites**: -10 to -20 (soften brightest points)
- **Blacks**: -15 to -25 (add depth while keeping lifted blacks via curve)

### Color Temperature/Tint
- **Temp**: +5 to +15 (warm the image - Portra 800 is warmer than Portra 400)
- **Tint**: +3 to +8 toward magenta (Portra has a slight magenta bias in shadows per Mastin Labs observation)

### HSL Panel Adjustments
Based on known Portra color characteristics:

**Hue**
- Red: 0 to +10 (push reds slightly toward orange)
- Orange: -3 to +5
- Yellow: -10 to -20 (warm yellows toward orange for Kodak warmth)
- Green: -15 to -30 (desaturate/neutralize greens - key Portra characteristic)
- Aqua: 0 to +10
- Blue: -5 to -15 (push blues slightly toward cyan for cool Portra shadows)
- Purple: 0
- Magenta: 0

**Saturation**
- Red: -10 to -20
- Orange: -5 to -15
- Yellow: -15 to -25
- Green: -20 to -40 (strong green desaturation is a key Portra trait)
- Aqua: -10 to -25
- Blue: -5 to -15
- Purple: -10 to -20
- Magenta: -10 to -20

**Luminance**
- Red: +10 to +20 (brighten skin tones slightly)
- Orange: +15 to +30 (brighten skin for that creamy Portra look)
- Yellow: +5 to +15
- Green: 0 to +10
- Aqua: 0
- Blue: -10 to -20 (darken blues for deeper skies)
- Purple: 0
- Magenta: 0

### Split Toning (Color Grading)
- **Highlights**: Warm/yellow-gold bias (Hue ~45-55, Saturation ~5-10)
- **Shadows**: Subtle cool/blue-magenta (Hue ~230-250, Saturation ~5-15)
  - Mastin Labs notes "purple shifts in the shadows" for Portra 800 pushed looks
- **Balance**: Shifted toward highlights (+40 to +60)

### Grain
- **Amount**: 25-45 (Portra 800 has visible but pleasing grain)
- **Size**: 35-45 (larger than 400 speed films)
- **Roughness**: 45-55 (organic, textured feel)
- Grain should be more pronounced in shadows/dark areas

### Calibration Panel
- **Shadows Tint**: +2 to +8 (green direction - common for Kodak emulation)
- **Red Primary Hue**: -5 to +5
- **Red Primary Saturation**: 0 to +10
- **Green Primary Hue**: +5 to +15
- **Green Primary Saturation**: -5 to +5
- **Blue Primary Hue**: -5 to -15
- **Blue Primary Saturation**: -5 to +5

## Pushed Portra 800 (EI 1600/3200) Emulation

### EI 1600 (Push +1)
- **Exposure**: +0.20 to +0.50 (overexpose slightly for pushed look)
- **Contrast**: +15 to +30 (pushed film has more contrast)
- **Highlights**: -50 to -60
- **Shadows**: +20 to +35
- **Blacks**: -20 to -30 (deeper blacks with push)
- **Grain Amount**: 40-55 (increased with push)
- **Grain Size**: 40-50
- Color shifts more dramatic - increased warmth
- Green desaturation slightly less aggressive

### EI 3200 (Push +2)
- **Exposure**: +0.30 to +0.70
- **Contrast**: +25 to +40 (highest contrast of all variants)
- **Highlights**: -40 to -55
- **Shadows**: +15 to +25
- **Blacks**: -25 to -35
- **Grain Amount**: 50-70 (most grain)
- **Grain Size**: 45-55
- **Grain Roughness**: 50-65
- Strong color shifts - purple/magenta in shadows prominent
- Blues become more saturated/contrasty
- Skin tones may shift warmer; may need orange luminance boost to compensate

## YouTube/Forum Community Notes

### Common Keywords for Portra 800 Looks:
- "Moody but natural"
- "Golden hour glow"
- "Creamy skin with bite"
- "Shadow details preserved"
- "Contrasty but not harsh"
- "Rich saturation without being cartoonish"

### Shooting Recommendations for Best Emulation:
- Capture slightly overexposed RAW files (+1/3 to +1 stop) to emulate the common practice of overexposing Portra 800
- Shoot in flat/natural lighting for most authentic film look
- Avoid heavy shadow crushing in-camera - Portra 800 retains exceptional shadow detail
- White balance slightly warm in-camera (~5500K-6000K for daylight)
- Use lower contrast picture profiles in-camera for more latitude in post

### Regions Where Portra 800 Diverges from Portra 400 Emulation:
- More aggressive green desaturation
- Warmer overall color balance (~200-400K warmer)
- Noticeably more grain (often the biggest differentiator)
- Higher contrast curve
- More purple/magenta in shadow tones
- Red-orange tones are richer
- Blue handling: Portra 800 blues are deeper but less cyan than Portra 400

## Note on Available Community Data

Portra 800 community recipes are significantly less documented than Portra 400. Most "Portra 800" preset recipes found online are actually Portra 400 recipes with added grain and warmth. True Portra 800 emulation should account for:
1. The different spectral sensitivity of the higher-speed emulsion
2. More pronounced warm bias
3. Heavier grain structure
4. Higher native contrast
5. The Vision3-era color science (different from the 2006-reformulated 160/400)
