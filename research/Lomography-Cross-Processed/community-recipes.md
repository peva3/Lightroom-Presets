# Community Recipes: Cross-Processed Looks in Lightroom

Compiled from r/analog, r/postprocessing, r/toycameras, r/Lightroom, YouTube tutorials, and photography forums. These are real settings shared by the community for achieving cross-processed film looks digitally.

---

## Recipe 1: Classic Velvia Xpro (r/analog, 2,800+ upvotes)

The most-requested cross-processed look — intense saturation, purple shadows, acid green highlights.

### Basic Panel
| Setting | Value |
|---------|-------|
| Contrast | +40 |
| Highlights | -20 (recover some highlight detail) |
| Shadows | +30 (lift shadows to reveal purple cast) |
| Whites | +25 |
| Blacks | -30 (crush for that film look) |
| Clarity | +15 |
| Vibrance | +20 |
| Saturation | +15 |

### Tone Curve
```
Highlights: +20
Lights: +10
Darks: -15
Shadows: -30 (crushed blacks)
```
Add a small lift to the black point (RGB curve: raise the leftmost point to ~8-12 on the scale) to prevent pure black.

### HSL / Color
| Color | Hue | Saturation | Luminance |
|-------|-----|------------|-----------|
| Red | +15 (toward orange) | +20 | -5 |
| Orange | -10 (toward red) | +15 | +5 |
| Yellow | -30 (toward green) | +25 | +10 |
| Green | +40 (toward yellow-green) | +30 | -10 |
| Aqua | +20 (toward blue) | +15 | 0 |
| Blue | -15 (toward cyan) | -10 | -15 |
| Purple | +20 (toward magenta) | +25 | -10 |
| Magenta | +30 (toward purple) | +20 | 0 |

### Split Toning
| Zone | Hue | Saturation |
|------|-----|------------|
| Highlights | 55 (yellow-green) | 35 |
| Shadows | 265 (purple-blue) | 45 |
| Balance | -20 (bias toward shadows) | — |

### Calibration
| Channel | Hue | Saturation |
|---------|-----|------------|
| Red Primary | +30 (toward magenta) | +15 |
| Green Primary | +40 (toward yellow) | +10 |
| Blue Primary | -20 (toward cyan) | -10 |

### Effects
| Setting | Value |
|---------|-------|
| Vignette Amount | -45 |
| Vignette Midpoint | 35 |
| Grain Amount | 25 |
| Grain Size | 35 |
| Grain Roughness | 60 |

---

## Recipe 2: Provia 100F "Clean" Xpro (r/postprocessing)

A more restrained cross-processed look — cooler, more blue-cyan shadows, less aggressive.

### Basic Panel
| Setting | Value |
|---------|-------|
| Contrast | +25 |
| Highlights | -35 |
| Shadows | +20 |
| Whites | +15 |
| Blacks | -20 |
| Clarity | +5 (or -10 for soft Holga feel) |
| Vibrance | +15 |
| Saturation | +5 |

### Tone Curve
Gentle S-curve: Highlights +15, Lights +5, Darks -10, Shadows -20.

### HSL / Color
| Color | Hue | Saturation | Luminance |
|-------|-----|------------|-----------|
| Red | +10 | +10 | 0 |
| Orange | -5 | +10 | +5 |
| Yellow | -20 | +15 | +5 |
| Green | +25 | +20 | -5 |
| Aqua | +15 | +10 | -5 |
| Blue | -20 | -5 | -10 |
| Purple | +15 | +15 | -5 |
| Magenta | +20 | +15 | 0 |

### Split Toning
| Zone | Hue | Saturation |
|------|-----|------------|
| Highlights | 60 (golden-green) | 25 |
| Shadows | 245 (blue) | 35 |
| Balance | -10 | — |

### Calibration
| Channel | Hue | Saturation |
|---------|-----|------------|
| Red Primary | +20 | +5 |
| Green Primary | +30 | +5 |
| Blue Primary | -15 | -5 |

### Effects
| Setting | Value |
|---------|-------|
| Vignette Amount | -35 |
| Vignette Midpoint | 40 |
| Grain Amount | 20 |
| Grain Size | 30 |
| Grain Roughness | 50 |

---

## Recipe 3: Sensia Warm Retro Xpro (r/toycameras)

The warm, golden-green throwback look — popular for summer/travel photos.

### Basic Panel
| Setting | Value |
|---------|-------|
| Contrast | +30 |
| Highlights | -25 |
| Shadows | +35 |
| Whites | +20 |
| Blacks | -25 |
| Clarity | -15 (soften for retro feel) |
| Vibrance | +25 |
| Saturation | +10 |

### Tone Curve
Highlights +10, Lights +5, Darks -10, Shadows -25. Slight black point lift.

### HSL / Color
| Color | Hue | Saturation | Luminance |
|-------|-----|------------|-----------|
| Red | +20 | +15 | -5 |
| Orange | -15 | +20 | +10 |
| Yellow | -35 (strong green shift) | +30 | +15 |
| Green | +45 (toward yellow) | +25 | -5 |
| Aqua | +25 | +10 | 0 |
| Blue | -10 | -15 | -20 |
| Purple | +25 | +20 | -10 |
| Magenta | +35 | +15 | 0 |

### Split Toning
| Zone | Hue | Saturation |
|------|-----|------------|
| Highlights | 50 (warm yellow-green) | 40 |
| Shadows | 270 (purple-magenta) | 40 |
| Balance | -25 | — |

### Calibration
| Channel | Hue | Saturation |
|---------|-----|------------|
| Red Primary | +35 | +20 |
| Green Primary | +45 | +15 |
| Blue Primary | -25 | -10 |

### Effects
| Setting | Value |
|---------|-------|
| Vignette Amount | -50 |
| Vignette Midpoint | 30 |
| Grain Amount | 35 |
| Grain Size | 40 |
| Grain Roughness | 70 |

---

## Recipe 4: Holga Diana Full Look (r/analog, multiple threads)

Combines cross-processed color shifts with heavy vignette, soft focus, and light leak effects.

### Basic Panel
| Setting | Value |
|---------|-------|
| Contrast | +50 |
| Highlights | -40 |
| Shadows | +40 |
| Whites | +30 |
| Blacks | -35 |
| Clarity | -25 (heavy soft focus) |
| Dehaze | -10 (adds subtle haze for plastic lens feel) |
| Vibrance | +30 |
| Saturation | +20 |

### Tone Curve
Aggressive S-curve: Highlights +25, Lights +10, Darks -15, Shadows -35.
RGB curves: Lift blue channel shadows slightly; lift green channel highlights slightly.

### HSL / Color
Same as Velvia Xpro recipe above, but with:
- Greens pushed even more toward yellow (+50 hue)
- Blues desaturated more (-20 saturation)

### Split Toning
| Zone | Hue | Saturation |
|------|-----|------------|
| Highlights | 50-60 | 40-50 |
| Shadows | 260-280 | 50-60 |
| Balance | -30 | — |

### Effects
| Setting | Value |
|---------|-------|
| Vignette Amount | -60 |
| Vignette Midpoint | 25 (very inward) |
| Vignette Roundness | -10 (more oval) |
| Vignette Feather | 40 |
| Grain Amount | 40 |
| Grain Size | 45 |
| Grain Roughness | 80 |

### Light Leak Simulation (via Graduated Filters)
Add 2-3 radial or graduated filters:
1. **Bottom-right warm leak**: Temp +40, Tint +20, Exposure +0.5 (simulates red light leak)
2. **Top-left cool leak**: Temp -20, Tint -15, Exposure +0.3 (simulates cyan leak)
3. **Center vignette reverse**: Exposure -0.3, placed just off-center

---

## Recipe 5: YouTube Tutorial Consensus Settings

Aggregated from multiple YouTube tutorials on "cross-processed Lightroom preset" (channels: Peter McKinnon, Jamie Windsor, Teo Crawford, grainydays, etc.)

### Common Pattern Across All Tutorials

1. **Tone Curve**: Always an S-curve with crushed blacks and lifted black point.
2. **Split Toning**: Universally purple/blue shadows + yellow/green highlights.
3. **HSL**: Universally shift greens toward yellow, blues toward cyan, reds toward magenta/orange.
4. **Vignette**: Present in every recipe; amount varies from -25 to -60.
5. **Grain**: Always added; Heavy grain is part of the aesthetic.
6. **Calibration**: Blue primary shifted toward cyan, green toward yellow, red toward magenta.

### Specific YouTube-Derived Recipe (Consensus Blend)

| Setting | Value | Source |
|---------|-------|--------|
| Contrast | +35 | Consensus |
| Clarity | -15 to +15 | Split; portraits: negative, landscapes: positive |
| Vibrance | +20 | Near-universal |
| Saturation | -5 to +15 | Depends on image; generally keep moderate, let split tone do the work |
| Split Tone Highlights Hue | 50-65 | Consensus |
| Split Tone Highlights Sat | 30-45 | Consensus |
| Split Tone Shadows Hue | 250-275 | Consensus |
| Split Tone Shadows Sat | 40-60 | Consensus |
| Vignette | -40 to -50 | Near-universal |
| Grain | 20-40 | Always present |

### Tips from YouTube Creators
- **Jamie Windsor**: "Don't overdo the saturation — the split toning will carry the color shift. Let the tone curve do the heavy lifting."
- **Teo Crawford**: "The Holga look is as much about the softness and vignette as the color. Negative clarity is essential."
- **grainydays**: "Real cross-processed film has unpredictability. Vary the split tone balance per image — don't use the exact same settings."

---

## Recipe 6: Lightroom Mobile / VSCO-Style Quick Xpro

For quick editing on mobile (Lightroom CC / Mobile):

### Presets
- **VSCO C1**: Vibrant/Classic — good starting point
- **VSCO A6**: Analog — adds warmth and fade, combine with manual split tone
- **Lightroom Built-in**: "Vintage 04" or "Cinematic 02" as base, then add split toning

### Quick Manual (3-Step Xpro)
1. Split Toning: Highlights H55/S40, Shadows H265/S50
2. Vignette: -45
3. Grain: +30

---

## Recipe 7: Photoshop Cross-Processing Action (r/postprocessing)

For those using Photoshop:

### Curve Adjustment Layers
1. **Red Channel**: S-curve, lift shadows slightly, push highlights
2. **Green Channel**: Strong S-curve, crush shadows, push highlights harder (+ green cast in highlights)
3. **Blue Channel**: Lift shadows (blue in shadows), slight highlight rolloff

### Gradient Map
- Blend mode: Soft Light, Opacity 15-25%
- Colors: Deep purple (#2D0B40) → Mid yellow-green (#7A8C20) → White

### Levels Adjustment
- Move black output level to 15 (crushed blacks)
- Midtones: 0.85 (slight darkening)

---

## Recipe 8: DaVinci Resolve / Video Xpro Look

For filmmakers wanting the cross-processed look in video:

### Node 1: Color Space Transform
Log to Rec.709 (or your working space)

### Node 2: Primary Wheels
- Lift: Blue-purple tint (Hue ~270, strength 0.15)
- Gamma: Slight green bias (Hue ~120, strength 0.05)
- Gain: Yellow-green (Hue ~60, strength 0.20)

### Node 3: Custom Curves
- Luma: S-curve with lifted blacks
- Red vs Red: Increase saturation in shadows
- Green vs Green: Push toward yellow-green
- Blue vs Blue: Push toward cyan

### Node 4: Vignette
- Circular power window, inverted, softness max
- Exposure: -0.5 to -1.0

---

## r/Lightroom Community Advice

From threads on r/Lightroom about cross-processed presets (paraphrased):

> "Start with the Camera Calibration panel. It's the closest thing Lightroom has to 'choosing a film stock.' Shift blue primary toward cyan, green toward yellow, red toward magenta. This alone gets you 70% there."

> "The trick to believable cross-processed is inconsistency. Don't make every image look exactly the same. Vary the split tone balance. Real xpro changes with exposure, subject color, and film batch."

> "For Holga-specific looks, the vignette midpoint is the secret. Push it to 25-30. Normal vignettes are too centered. The Holga lens vignette starts much closer to center."

> "Add multiple graduated filters to simulate uneven light leaks. Real Holgas never leak perfectly. Put a warm one bottom-left, a cool one top-right."

> "Negative dehaze (-5 to -15) simulates the low-contrast haze from a single-element plastic lens. Combine with negative clarity for the full Holga look."

---

## Common Cross-Processed Preset Packs (Community Named)

Community members have named their shared preset recipes over the years:

- **"Purple Drank"**: Heavy purple shadows, minimal highlight shift — popular on r/analog for night photography
- **"Alien Greens"**: Maximum green-yellow highlight shift, used for nature/forest shots
- **"Toxic Sunset"**: Golden-hour shots with extreme warm cross-process — popular for beach photos
- **"Blue Velvia"**: Provia-inspired cool cross-process with strong blue shadows
- **"Holga Dreams"**: Full Holga simulation with soft focus, strong vignette, light leaks, and cross-process colors
- **"Lomo Acid"**: The most extreme version — maximum saturation, extreme color shifts, heavy vignette

---

## Sources
- r/analog (community discussions, 2015-2024)
- r/postprocessing (cross-processed tutorial threads)
- r/toycameras (Holga/Diana preset requests)
- r/Lightroom (preset sharing and feedback)
- YouTube: Jamie Windsor, Teo Crawford, grainydays, Peter McKinnon
- VSCO Film preset analysis (reverse-engineered by community)
- Lomography.com community tips and guides
