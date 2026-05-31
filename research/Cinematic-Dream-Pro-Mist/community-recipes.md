# Community Recipes — Simulating Pro-Mist in Lightroom

## Overview

Since a physical Tiffen Pro-Mist filter affects multiple optical properties simultaneously
(halation, contrast, MTF, spectral shift), no single Lightroom slider perfectly replicates it.
The community approach uses a **composite recipe** — negative Clarity for mid-frequency
contrast reduction, negative Dehaze for veiling glare simulation, lifted blacks via the Tone
Curve, and selective highlight adjustments for bloom.

Below are collected recipes from Reddit (r/Lightroom, r/postprocessing, r/cinematography),
YouTube tutorials, and photography forums — synthesized into representative "preset formulas."

---

## Base Recipe: "Digital Pro-Mist 1/4" (Moderate)

This is the most commonly cited starting point. Models a 1/4-strength Pro-Mist.

### Tone Panel
```
Exposure:     0.00 to +0.15 (subtle brightening for diffusion feel)
Contrast:     -20 to -30
Highlights:   -40 to -60 (control bloom clipping)
Shadows:      +30 to +50 (lifted shadow detail)
Whites:       +10 to +20
Blacks:       +15 to +30 (the "lifted blacks" milkiness)
```

### Presence Panel
```
Texture:      -10 to -20 (reduce fine detail, skin texture)
Clarity:      -25 to -40 (THE critical slider — mid-frequency contrast reduction)
Dehaze:       -15 to -30 (introduces atmospheric veiling / "milky haze")
Vibrance:     +5 to +15 (compensates for desaturation from negative Dehaze)
Saturation:   0 to -5
```

### Tone Curve

**Parametric curve** (preferred by most) or **Point Curve**:

```
Highlights:   -15 to -25
Lights:       +10 to +15
Darks:        +15 to +25
Shadows:      +25 to +40

Point Curve:  Lift the black point from (0,0) to approximately (0, 8-15%)
              (creates the signature "milky blacks" with no true black)
```

### HSL / Color

```
Orange Luminance:   +10 to +20 (skin brightening, bloom effect on skin)
Yellow Luminance:   +5 to +10
Red Hue:            -5 to -10 (subtle warm shift toward orange)
Blue Luminance:     -5 to -15 (deepen skies slightly to balance haze)
```

### Detail Panel

```
Sharpening:          40-60 (normal)
Radius:              1.2-1.5 (slightly larger for gentler edges)
Detail:              15-25 (lower than default to avoid fighting the soft look)
Masking:             20-40 (protect smooth areas)
Noise Reduction:     10-15 (subtle luminance NR further softens digital sharpness)
```

### Effects Panel

```
Post-Crop Vignetting:      -10 to -20
Midpoint:                  30-40 (broader vignette, not tight corner darkening)
Grain:                     Amount 15-30, Size 25-35, Roughness 50-65
```

---

## Heavy Recipe: "Digital Pro-Mist 1" (Strong Diffusion)

For flashback sequences, dream states, music video looks. Much heavier hand.

### Tone Panel
```
Contrast:     -45 to -60
Highlights:   -70 to -90
Shadows:      +60 to +80
Blacks:       +35 to +50
```

### Presence Panel
```
Texture:      -25 to -40
Clarity:      -50 to -75
Dehaze:       -40 to -60
```

### Tone Curve
```
Lift blacks to (0, 18-25%)
Pull highlights down at top-right knee
S-curve becomes flat and lifted
```

### Split Toning / Color Grading
```
Highlights:   40-50 Hue (warm amber), Saturation 10-20
Shadows:       200-220 Hue (cool blue/teal), Saturation 5-15
```

---

## Subtle Recipe: "Digital Pro-Mist 1/8" (Clean Softening)

For those who want the Pro-Mist character without it being obvious. This is the "always-on"
preset equivalent.

### Tone Panel
```
Contrast:     -10 to -15
Highlights:   -20 to -30
Shadows:      +15 to +25
Blacks:       +5 to +12
```

### Presence Panel
```
Clarity:      -10 to -20
Dehaze:       -5 to -12
```

### Tone Curve
```
Subtle black lift: (0, 5-8%)
```

---

## Reddit-Sourced Tips & Tricks

### From r/Lightroom and r/postprocessing

1. **"The Radial Filter Bloom Trick"** — Place a large radial filter over a light source
   (window, lamp, sky). Inside the radial: Clarity -50, Dehaze -30, Highlights -40,
   Temperature +10 (warm). Feather it out 80-100%. This creates localized bloom around
   practicals that mimics the halation of real Pro-Mist filters.

2. **"The -Clarity / +Texture Combo"** — Multiple users note that negative Clarity alone
   can look "muddy." One Redditor's solution: Clarity -30, Texture +10. The Texture boost
   restores some micro-detail while Clarity handles the mid-frequency contrast, producing
   a more optical-replica result.

3. **"Luminance Masking for Bloom"** — Use the Range Mask on a Local Adjustment Brush to
   target only highlights (Luminance range ~80-100). Then apply negative Clarity (-40),
   negative Dehaze (-25), and raise Exposure (+0.15). This restricts diffusion to bright
   areas only, mimicking how a real Pro-Mist affects highlights far more than shadows.

4. **"The Dehaze is the Secret Sauce"** — Consistently, the most-upvoted comments in Pro-Mist
   simulation threads emphasize that **negative Dehaze** is the single most important slider.
   It introduces a fog-like atmospheric veil that closely resembles the veiling glare of a
   physical filter. One comment: "Dehaze at -20 does more for the Pro-Mist look than Clarity
   at -50 ever will."

5. **"Calibration Panel for Warm Bloom"** — Some users adjust the Calibration panel:
   - Red Primary Hue: -5 to -10 (warmer reds → bloom warmth)
   - Blue Primary Saturation: -10 to -20 (desaturate blues slightly for vintage cast)

6. **"Grain is Not Optional"** — Multiple threads emphasize that grain is essential for
   selling the effect. Clean digital files with negative Clarity look "smeary"; adding
   grain breaks up the smoothness and mimics the texture of filtration. Amount 20-35,
   Size 25-40, Roughness 55-75.

---

## YouTube Tutorial Summary

Composite of techniques demonstrated across multiple tutorials:

### Workflow Order (consensus)
1. Basic exposure and white balance
2. Negative Clarity (base diffusion)
3. Negative Dehaze (atmospheric veil)
4. Tone curve black lift (milky shadows)
5. HSL adjustments (color shifts from diffusion)
6. Split toning (warm/cool color contrast)
7. Radial filters on light sources (localized bloom)
8. Grain (texture overlay)

### Common Pitfalls Noted
- Too much Clarity reduction without Dehaze = "muddy, not dreamy"
- Too much Dehaze without black lift = "flat haze that kills image depth"
- Forgetting to re-add contrast in the tone curve after negative Dehaze
- Not masking sharpening — sharp pores ruin the diffusion illusion
- Over-using split toning — the Pro-Mist warmth is optical, not a grading overlay

---

## Lightroom Mobile / Free Alternatives

### Lightroom Mobile Sliders
Same sliders available; identical recipe works. The community notes that on mobile
displays (higher pixel density, smaller screen), the effect often looks MORE convincing
because users can't pixel-peep.

### Snapseed (free alternative)
- Glamour Glow filter: Saturation 0, Glow +30-50 (emulates Veiling Glare)
- Tune Image: Ambiance -20 to -40 (similar to Dehaze in reverse)
- Curves: Lift black point

### Darktable (open-source)
- "Diffuse or Sharpen" module with negative "Sharpness" value
- "Haze Removal" with negative strength
- "Filmic RGB" with raised black relative exposure
- "Bloom" module for highlight halation

---

## Sources

- r/Lightroom: "Simulating a Pro-Mist filter without buying one" and related threads (2020–2024)
- r/postprocessing: "How to get the dreamy film look digitally" megathread
- r/cinematography: "Pro-Mist in post?" forum discussions
- r/photography: "Favorite presets for diffusion filter look" community poll
- YouTube: Multiple tutorials on "Pro-Mist Lightroom Preset," "Dreamy Lightroom Tutorial," "Diffusion Filter in Post"
