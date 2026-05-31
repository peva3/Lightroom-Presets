# Community Recipes — Lightroom B&W Settings for T-Max 3200 Emulation

> **Disclaimer:** These are community-sourced approximations. True T-Max 3200 look depends on exposure, development, scanning, and the uncontrollable variables of analog photography. Digital emulation is an interpretation.

---

## Core Philosophy for T-Max 3200 Digital Emulation

The T-Max 3200 aesthetic in Lightroom is driven by **three core pillars**:

1. **Crisp, structured grain** — T-grain produces sharp-edged geometric grain, not soft clumps
2. **Higher contrast with clean midtones** — contrast comes from the push, not from crushing the curve
3. **Specific spectral rendering** — extended red sensitivity affects how colors map to B&W tones

---

## Recipe 1: "Straight T-Max 3200" (EI 3200 Baseline)

Community consensus recipe from r/analog, r/Lightroom, and Photrio:

### Basic Panel
| Setting | Value | Notes |
|---|---|---|
| **Treatment** | Black & White | — |
| **Exposure** | Adjust to taste | Start with proper exposure |
| **Contrast** | +25 to +40 | TMZ at 3200 is punchy |
| **Highlights** | -10 to -20 | Protect highlight clipping |
| **Shadows** | -20 to -35 | Deeper shadows = "pushed" look |
| **Whites** | +10 to +20 | Set white point |
| **Blacks** | -25 to -40 | Deep blacks, minimal shadow detail |

### Tone Curve
```
Point Curve: Medium Contrast
Parametric:
  Highlights: -10
  Lights:     +10
  Darks:      -15
  Shadows:    -25
```

### B&W Mix (Approximate T-Max Spectral Response)
| Color | Value | Rationale |
|---|---|---|
| Red | +15 to +25 | Extended red sensitivity → lighter reds |
| Orange | +10 to +20 | Warmer skin tones lift slightly |
| Yellow | +5 to +15 | Brighter yellows (filter effect) |
| Green | -5 to -15 | Standard panchro green rendering |
| Aqua | -10 to -20 | Slightly darker skies |
| Blue | -15 to -30 | Darker blue skies (no filter) |
| Purple | 0 to -10 | Neutral to slight darkening |
| Magenta | +5 to +10 | Slight lift in warm tones |

### Grain
| Setting | Value | Notes |
|---|---|---|
| **Amount** | 45–65 | Prominent but not overwhelming |
| **Size** | 35–50 | T-grain is fine for its speed, but visible at 3200 |
| **Roughness** | 55–75 | Higher roughness = sharper grain edges (T-grain character) |

### Sharpening
| Setting | Value |
|---|---|
| **Amount** | 50–70 |
| **Radius** | 1.0–1.2 |
| **Detail** | 35–50 |
| **Masking** | 40–60 (hold Alt/Option) |

### Effects
- **Post-Crop Vignetting:** -10 to -15 (subtle edge fall-off common in scans)
- **Dehaze:** +5 to +10 (adds midtone snap)

---

## Recipe 2: "Pushed to 6400" — Dramatic High-Contrast

For the heavy-push look with dominant grain:

### Basic Panel
| Setting | Value |
|---|---|
| Contrast | +45 to +60 |
| Highlights | -30 to -40 |
| Shadows | -40 to -60 |
| Whites | +5 to +15 |
| Blacks | -40 to -55 |

### Tone Curve
```
Point Curve: Strong Contrast
Additional: Pull shadow point right (crush blacks)
```

### Grain
| Setting | Value |
|---|---|
| Amount | 65–80 |
| Size | 40–55 |
| Roughness | 65–85 |

### B&W Mix Adjustments
- **Red:** +20 to +30 (stronger red lift at higher push)
- **Blue:** -20 to -35 (deeper skies to compensate for flatter neg)
- **Green:** -10 to -20

---

## Recipe 3: "Clean TMZ" (EI 800 Base ISO Look)

For those who want T-Max 3200 grain character without the heavy push contrast:

### Basic Panel
| Setting | Value |
|---|---|
| Contrast | +10 to +20 |
| Highlights | 0 to -10 |
| Shadows | -10 to -15 |
| Blacks | -15 to -25 |

### Tone Curve
```
Point Curve: Linear or Low Contrast
```

### Grain
| Setting | Value |
|---|---|
| Amount | 30–45 |
| Size | 30–40 |
| Roughness | 50–65 |

### B&W Mix
- **Red:** +10 to +15
- **Orange:** +5 to +10
- **Blue:** -10 to -20

---

## Recipe 4: "T-Max 3200 + Yellow Filter"

Simulating the classic on-lens yellow filter (common for portraits and general shooting with TMZ):

### B&W Mix Adjustments
| Color | Value |
|---|---|
| Yellow | +25 to +35 |
| Orange | +15 to +25 |
| Red | +10 to +20 |
| Green | +5 to +10 |
| Blue | -25 to -40 |
| Aqua | -20 to -30 |

### Additional
- Reduce Contrast by ~10 (yellow filter slightly flattens)
- Grain: Standard EI 3200 settings

---

## Recipe 5: "T-Max 3200 + Red Filter"

Heavy sky darkening, dramatic landscape look:

### B&W Mix Adjustments
| Color | Value |
|---|---|
| Red | +50 to +70 |
| Orange | +40 to +60 |
| Yellow | +30 to +45 |
| Blue | -50 to -70 |
| Aqua | -40 to -60 |
| Green | +10 to +20 |

### Basic Panel
- Contrast: +30 to +45 (red filter increases contrast naturally)
- Highlights: -20 to -30

---

## Community Discussion Highlights

### From Reddit r/analog & r/Lightroom (paraphrased/summarized)

> **"T-Max grain in Lightroom is hard to nail — the built-in grain is too soft. I add grain in Photoshop with a custom noise layer set to Overlay for that hard-edged T-grain look."**
> — u/darkroom_devotee

> **"For T-Max 3200 at box speed (800), I keep the curve linear and add grain in post. The T-grain structure means grain is sharp but not clumpy — Lightroom's grain tool set to high roughness gets closest."**
> — r/analogcommunity

> **"Key difference from Delta 3200 in post: T-Max needs sharper grain edges and more midtone contrast. Delta needs softer grain and a slight highlight glow (negative dehaze or negative clarity on highlights)."**
> — r/Lightroom

> **"The B&W mix matters more than people think. T-Max sees red differently than Delta. Push the reds up 15-25 points and you'll get closer to scans I've seen."**
> — r/analog

### From Photrio Forums (paraphrased)

> **"In the darkroom, T-Max 3200 at EI 3200 prints on grade 3–3.5. That's significantly harder than Delta 3200 at the same EI which prints around grade 2.5. For Lightroom, that means the contrast slider should be higher for TMZ."**

> **"The TMax developer is designed specifically for the T-grain emulsions. If you want the 'true' TMZ look, you need to understand that TMax Dev gives a different curve shape than D-76 — more linear midtones, sharper shoulder."**

---

## Grain Emulation Beyond Lightroom

Many community members find Lightroom's built-in grain insufficient for the hard-edged T-grain look. Alternative approaches:

### Photoshop Grain Method
1. Create new 50% gray layer, set to Overlay
2. Filter → Noise → Add Noise (Gaussian, Monochromatic, ~5-8%)
3. Filter → Sharpen → Unsharp Mask (Amount: 100-150%, Radius: 0.5-1.0px)
4. Adjust layer opacity to taste

### Nik Silver Efex Pro
- Film type: "Kodak T-Max 3200" (built-in profile in Silver Efex)
- Adjust "Grain per ISO" to match desired push level
- Silver Efex grain is generally considered more film-like than Lightroom's

### Dehancer / FilmConvert
- Dehancer: No direct T-Max 3200 profile, but T-Max 400 pushed can approximate
- FilmConvert: Kodak T-Max 100/400 profiles available; T-Max 3200 not directly supported

---

## Key Reminder for Digital Emulation

T-Max 3200 scanned negatives have **already been interpreted** by the scanner's software (Nikon Scan, SilverFast, Epson Scan, etc.). Each scanner applies its own tone curve, grain handling, and sharpening. What the community calls "the T-Max 3200 look" is often filtered through:
1. Development chemistry (D-76 vs. XTOL vs. TMax Dev — VERY different results)
2. Scanner and scanning software
3. Post-scan adjustments

Digital emulation should target a **specific reference**: T-Max 3200 in XTOL scanned on a Noritsu vs. T-Max 3200 in D-76 scanned on a Frontier vs. darkroom prints on Ilford Multigrade — all look different.

---

## Sources

- r/analog, r/AnalogCommunity, r/Lightroom, r/Darkroom searches
- Photrio forum discussions
- Nik Silver Efex Pro documentation
- Community Flickr groups (Kodak T-Max)
- Various YouTube film review channels (paraphrased observations)
