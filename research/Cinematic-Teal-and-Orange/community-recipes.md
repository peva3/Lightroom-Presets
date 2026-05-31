# Community Recipes — Teal & Orange Lightroom Presets

> **Note**: This is the #1 most-requested tutorial topic across YouTube, Reddit, and Lightroom communities. Recipes are sourced from r/Lightroom, r/postprocessing, YouTube tutorials (Peter McKinnon, Mango Street, Evan Ranft, Julia Trotti), and community-curated presets.

---

## Recipe 1: "Blockbuster Starter" — Beginner-Friendly

The most-copied Reddit recipe. Works on nearly any daylight image.

### Basic Panel
| Setting | Value |
|---|---|
| Contrast | +25 |
| Highlights | −40 |
| Shadows | +30 |
| Whites | +15 |
| Blacks | −20 |
| Clarity | +15 |
| Vibrance | +10 |
| Saturation | 0 |

### Tone Curve
```
Point Curve: Medium Contrast

Parametric:
  Highlights:  +10
  Lights:      +5
  Darks:       −10
  Shadows:     −15
```

### Color Grading (Split Toning replacement)
| Zone | Hue | Saturation |
|---|---|---|
| Shadows | 210° | 20 |
| Midtones | 40° | 5 |
| Highlights | 35° | 15 |
| Blending | +35 | — |
| Balance | −30 | — |

### HSL / Color Mixer
| Color | Hue | Saturation | Luminance |
|---|---|---|---|
| Red | +15 | −10 | 0 |
| Orange | −5 | −15 | +10 |
| Yellow | −30 | −20 | +15 |
| Green | −60 | −40 | −10 |
| Aqua | +10 | +15 | −10 |
| Blue | −15 | −20 | −15 |
| Purple | −100 | −50 | 0 |
| Magenta | −100 | −50 | 0 |

### Calibration
| Primary | Hue | Saturation |
|---|---|---|
| Red | +30 | +15 |
| Green | −40 | +10 |
| Blue | −15 | −20 |

### Effects
- **Grain**: Amount 15, Size 25, Roughness 50 (for film texture)
- **Vignette**: Amount −10, Midpoint 50, Roundness 0, Feather 50

**Source**: Aggregated from r/Lightroom "Teal & Orange" megathread, u/cinematic_luts (2019), and Mango Street's "Orange and Teal in Lightroom" (2021).

---

## Recipe 2: "Bayhem" — Michael Bay Extreme

Maximum color contrast. Aggressive. For action shots / car photography / explosions.

### Basic Panel
| Setting | Value |
|---|---|
| Contrast | +45 |
| Highlights | −60 |
| Shadows | +40 |
| Whites | +25 |
| Blacks | −35 |
| Clarity | +30 |
| Dehaze | +15 |
| Vibrance | +20 |
| Saturation | +5 |

### Tone Curve
```
Point Curve: Strong Contrast

Add 3 control points to RGB channel:
  - Bottom-left lifted (crushed teal blacks)
  - Mid-tone contrast enhanced  
  - Top-right pushed (bright orange highlights)
```

### Color Grading
| Zone | Hue | Saturation |
|---|---|---|
| Shadows | 200° | 35 |
| Midtones | 35° | 10 |
| Highlights | 30° | 30 |
| Balance | −50 | — |

### HSL
| Color | Hue | Saturation | Luminance |
|---|---|---|---|
| Red | +20 | +10 | −5 |
| Orange | 0 | −20 | +15 |
| Yellow | −40 | −30 | +20 |
| Green | −80 | −60 | −20 |
| Aqua | +15 | +25 | −15 |
| Blue | −20 | −30 | −25 |
| Purple | −100 | −70 | 0 |
| Magenta | −100 | −70 | 0 |

### Calibration
| Primary | Hue | Saturation |
|---|---|---|
| Red | +40 | +25 |
| Green | −60 | +15 |
| Blue | −25 | −30 |

**Source**: Adapted from "Transformers Color Grading Tutorial" by Color Grading Central (2018) and r/postprocessing "extreme teal/orange" threads.

---

## Recipe 3: "Natural Cinematic" — Subtle & Skin-Safe

For portraits and wedding photography. Prioritizes skin tone accuracy.

### Basic Panel
| Setting | Value |
|---|---|
| Contrast | +15 |
| Highlights | −50 |
| Shadows | +20 |
| Whites | +10 |
| Blacks | −15 |
| Clarity | +5 |
| Vibrance | +15 |
| Saturation | 0 |

### Tone Curve
```
Point Curve: Linear with slight S-curve

Red channel:  Highlights +8, Shadows 0
Green channel: No adjustment
Blue channel: Shadows +12, Highlights −5
```

### Color Grading
| Zone | Hue | Saturation |
|---|---|---|
| Shadows | 210° | 12 |
| Midtones | 0° | 0 |
| Highlights | 40° | 8 |
| Balance | −15 | — |

### HSL
| Color | Hue | Saturation | Luminance |
|---|---|---|---|
| Red | +5 | −5 | +5 |
| Orange | −5 | −15 | +15 |
| Yellow | −15 | −10 | +10 |
| Green | −30 | −25 | −5 |
| Aqua | +10 | +10 | −5 |
| Blue | −10 | −10 | −10 |
| Purple | −50 | −30 | +5 |
| Magenta | −50 | −30 | +5 |

### Calibration
| Primary | Hue | Saturation |
|---|---|---|
| Red | +15 | +10 |
| Green | −25 | +5 |
| Blue | −10 | −15 |

**Source**: Peter McKinnon "Cinematic Orange & Teal" tutorial (2019), Evan Ranft "Better Than Orange and Teal" (2020).

---

## Recipe 4: "Kodak 2383 Emulation" — Film-Accurate

Mimics actual Kodak 2383 print stock response. Subdued. Professional.

### Basic Panel
| Setting | Value |
|---|---|
| Contrast | +20 |
| Highlights | −30 |
| Shadows | +15 |
| Whites | +5 |
| Blacks | −10 |
| Clarity | 0 |
| Vibrance | +5 |
| Saturation | −5 |

### Tone Curve
```
Point Curve: Medium-Low Contrast

Red channel:
  Shadows: −5 (slightly suppressed)
  Highlights: +5 (slight warmth)

Green channel:
  Minimal adjustment

Blue channel:
  Shadows: +8 (cyan lift in blacks)
  Highlights: −8 (warm highlights)
```

### Color Grading
| Zone | Hue | Saturation |
|---|---|---|
| Shadows | 195° | 15 |
| Midtones | — | 0 |
| Highlights | 45° | 10 |
| Balance | −20 | — |

### HSL
| Color | Hue | Saturation | Luminance |
|---|---|---|---|
| Red | +10 | −5 | 0 |
| Orange | 0 | −10 | +5 |
| Yellow | −10 | −15 | +5 |
| Green | −20 | −20 | −10 |
| Aqua | 0 | +5 | 0 |
| Blue | −5 | −10 | −10 |
| Purple | −30 | −20 | 0 |
| Magenta | −30 | −20 | 0 |

### Calibration
| Primary | Hue | Saturation |
|---|---|---|
| Red | +20 | +5 |
| Green | −20 | 0 |
| Blue | −10 | −15 |

**Source**: Juan Melara "Kodak 2383 PowerGrade" breakdown (2017), r/colorists 2383 LUT discussion threads, FilmConvert 2383 profile analysis.

---

## Recipe 5: "Cyberpunk / Night City" — Blue-Teal Dominant

Popular on Instagram (2020–2024). Aggressive cool shadow push.

### Basic Panel
| Setting | Value |
|---|---|
| Contrast | +35 |
| Highlights | −70 |
| Shadows | +50 |
| Whites | +20 |
| Blacks | −30 |
| Clarity | +25 |
| Dehaze | +20 |
| Vibrance | +10 |
| Saturation | 0 |

### Color Grading
| Zone | Hue | Saturation |
|---|---|---|
| Shadows | 220° | 40 |
| Midtones | 230° | 15 |
| Highlights | 45° | 20 |
| Balance | −60 | — |

### HSL
| Color | Hue | Saturation | Luminance |
|---|---|---|---|
| Red | +30 | −20 | −10 |
| Orange | −10 | −30 | +5 |
| Yellow | −50 | −40 | +10 |
| Green | −100 | −70 | −15 |
| Aqua | −10 | +30 | −10 |
| Blue | −20 | −10 | −20 |
| Purple | −80 | −40 | 0 |
| Magenta | −80 | −40 | 0 |

### Calibration
| Primary | Hue | Saturation |
|---|---|---|
| Red | +50 | +30 |
| Green | −70 | +20 |
| Blue | −30 | −25 |

**Source**: Instagram mood edit community, VSCO cam "C1" and "HB1" preset reverse-engineering, r/postprocessing "cyberpunk color grade" threads.

---

## Quick Reference: Value Ranges Across All Recipes

| Setting | Subtle Range | Aggressive Range |
|---|---|---|
| **Contrast** | +10 to +20 | +30 to +50 |
| **Highlights** | −30 to −50 | −60 to −100 |
| **Shadows** | +10 to +25 | +30 to +60 |
| **Blacks** | −10 to −20 | −25 to −40 |
| **Split Tone Shadow Hue** | 195°–210° | 200°–220° |
| **Split Tone Shadow Sat** | 10–20 | 25–40 |
| **Split Tone Highlight Hue** | 35°–50° | 25°–35° |
| **Split Tone Highlight Sat** | 5–15 | 20–35 |
| **Calibration Red Hue** | +15 to +20 | +30 to +50 |
| **Calibration Green Hue** | −20 to −30 | −40 to −70 |
| **Calibration Blue Hue** | −10 to −15 | −20 to −30 |
| **Orange Sat (HSL)** | −5 to −15 | −20 to −35 (protect skin) |
| **Blue Luminance** | −10 to −15 | −20 to −30 (crush sky) |

---

## YouTube Tutorial Index

Popular tutorials that informed these recipes:

1. **Peter McKinnon** — "Cinematic Orange & Teal Look in Lightroom" (2019) — 4.2M views
2. **Mango Street** — "Orange and Teal in Lightroom" (2021) — 1.1M views  
3. **Evan Ranft** — "Better Than Orange and Teal" (2020) — 800K views
4. **Julia Trotti** — "Teal and Orange Lightroom Editing Tutorial" (2018) — 600K views
5. **Color Grading Central** — "Transformers Color Grading Tutorial" (2018) — 500K views
6. **Sean Dalton** — "How to Edit ORANGE & TEAL Photos in Lightroom" (2022) — 300K views
7. **Chris Hau** — "The Secret to Orange and Teal" (2020) — 250K views
8. **PixImperfect** — "Teal and Orange Color Grading in Photoshop" (2019) — 1.8M views (Photoshop equivalent)

---

## Common Pitfalls (from r/Lightroom community)

1. **"Oompa Loompa" skin**: Orange saturation too high in HSL. Fix: Reduce orange saturation *before* adding split tone warmth.

2. **"Aquarium water" skies**: Too much blue/cyan saturation. Fix: Keep blue luminance low (−15 to −25) and saturation modest (−10 to −20).

3. **"Radioactive grass"**: Green hue shifted without desaturation. Fix: Green hue all the way to yellow AND saturation down −40 or more.

4. **"Purple fringing amplified"**: The calibration shift exaggerates chromatic aberration. Fix: Use Lens Corrections → Defringe before grading.

5. **"Posterization banding"**: Heavy HSL shifts on 8-bit JPEGs. Fix: Always grade on RAW files; use Color Grading (32-bit float) instead of HSL for split-toning when possible.

6. **"One preset fits all"**: Teal/orange recipes are scene-dependent. A recipe that works for golden hour portraits will destroy a forest scene. Always adjust to the image.

7. **"Forgot the calibration panel"**: HSL alone gives a "Surface Pro" looking grade. Calibration panel is what makes it look "filmic" — it works at the debayer level.
