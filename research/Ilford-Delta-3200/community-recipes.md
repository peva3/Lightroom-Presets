# Community Recipes — Delta 3200 Emulation in Lightroom

> Compiled from r/analog, r/Lightroom, r/Darkroom, Photrio, 35mmc, and film photography forums.

---

## Overview of Available Emulation Presets

Several commercial preset packs include Delta 3200 emulations:

| Pack | Delta 3200 Coverage | Notes |
|------|---------------------|-------|
| **VSCO Film 01–07** | Delta 3200 included in Film 02 (B&W pack) | Industry standard; grain profiles are good |
| **Mastin Labs Ilford Pack** | Dedicated Delta 3200 preset | Curated tone curve; good highlight rolloff |
| **RNI All Films 5** | Ilford Delta 3200 profile included | Camera-profile based; very accurate grain |
| **Really Nice Images (RNI)** | Delta 3200 variant | Focused on scan-emulation aesthetic |
| **Caleb Salvadori** | B&W film presets (some Ilford) | More stylised than accurate |
| **PresetsHeaven / MikeyG** (free) | Ilford B&W pack | Older free pack; basic but usable start |

---

## Community-Shared Core Settings for Delta 3200 "Look"

### 1. Basic Panel (Tone)

The Delta 3200 "look" starts with a deliberately flat, low-contrast base:

```
Contrast:      -15 to -30
Highlights:    -40 to -60  (protect highlights aggressively)
Shadows:       +20 to +40  (lift shadows, but don't overdo)
Whites:        -10 to -25  (muted whites, never pure 255)
Blacks:        +15 to +30  (critical: LIFTED blacks, never crush to 0)
```

**Why:** Delta 3200 has low native contrast. The characteristic curve has a soft toe (lifted blacks) and an early shoulder (compressed highlights). The midtones carry the image.

### 2. Tone Curve

The community consensus for the tone curve is:

```
Parametric Curve:
  Highlights:  -15
  Lights:      -5
  Darks:       +10
  Shadows:     +20

Point Curve:
  Blacks lifted:   (0, 18–22)  — black point NOT at zero
  Linear midtones
  Whites: flat section at top or slightly rolled
```

**Key:** The lifted black point is THE defining characteristic. Almost every community recipe starts with raising the black point to ~15–25 on the 0–255 scale. True black does not exist in Delta 3200 negatives — the film base has a deep charcoal grey with texture.

### 3. B&W Mixer / HSL Panel

Delta 3200's spectral response is panchromatic with extended red sensitivity:

```
B&W Mix (starting point):
  Red:         +10 to +25   (boost for skin tones)
  Orange:      +15 to +30   (warm skin, lift)
  Yellow:      +5 to +15
  Green:       -5 to -10    (slightly suppressed green)
  Aqua:        0 to -5
  Blue:        -10 to -20   (darken skies; moody feel)
  Purple:      -5 to -10
  Magenta:     0 to +5
```

**Why:** Delta 3200 has orthopanchromatic sensitivity — reds are slightly more sensitive, greens slightly less. Blues darken significantly, giving moody skies even in daylight. This creates the characteristic "noir" look with luminous skin tones.

### 4. Grain Settings (Critical)

Grain is the defining Delta 3200 aesthetic. Settings from community posts:

```
Lightroom Grain Panel:
  Amount:      55–75       (heavy — this is the point)
  Size:        45–65       (large, "golf-ball" grain)
  Roughness:   55–70       (pronounced texture, not smooth grain)
```

**Community tip:** Several users recommend exporting and re-importing with a second grain pass if Lightroom's built-in grain feels insufficient at maximum settings.

**Alternative:** Photoshop grain filters (Grain > Enlarge, or Add Noise > Gaussian + film grain overlay texture) for more authentic results than Lightroom.

#### Grain Distribution Pattern (from community observation)

- **Highlights (Zones VII–IX):** Grain is minimised — the dense emulsion creates smooth whites
- **Midtones (Zones IV–VI):** Grain is maximum and most visible
- **Shadows (Zones I–III):** Grain is present but merged into dark texture
- **Pattern:** Grain appears clumped, irregular — not the uniform noise of digital sensors

### 5. Sharpening

```
Sharpening:
  Amount:      +40 to +60   (moderate — grain is confused with sharpness)
  Radius:      1.0–1.4      (slightly larger to avoid digital sharpening halos)
  Detail:      25–40        (lower to avoid sharpening the grain itself)
  Masking:     +30 to +50   (mask flat areas to avoid sharpening grain in skies/shadows)
```

### 6. Effects Panel

```
Post-Crop Vignette:
  Amount:      -10 to -20    (subtle, never heavy)
  Midpoint:    35–50
  Roundness:   0
  Feather:     50–80

Dehaze:        -5 to -15     (negative dehaze = atmospheric haze, soft glow)
```

### 7. Calibration Panel (Color to B&W Conversion)

```
Process Version:  5 (current)
Profile:          Adobe Monochrome or Adobe Standard → B&W

Red Primary:    +10 Hue / +20 Sat   (warm tone penalty)
Green Primary:  -5 Hue / -5 Sat
Blue Primary:   -10 Hue / +10 Sat
```

---

## Specific Look Recipes

### Concert / Gig Photography Emulation

```
Exposure:      +0.30 to +0.70   (push look — brighten the midtones)
Contrast:      -25
Highlights:    -70              (stage lights are HOT — protect these)
Shadows:       +40              (lift the crowd, the back of the stage)
Whites:        -20
Blacks:        +25              (critical lifted blacks)
Clarity:       0 to -10         (negative clarity = softer gig haze)
Grain:         Amount 75 / Size 60 / Roughness 70
Vignette:      -15 to -25       (natural stage falloff)
```

### Night Street / Noir Emulation

```
Exposure:      -0.30 to 0       (slightly underexposed feel)
Contrast:      -20
Highlights:    -50
Shadows:       +35
Whites:        -15
Blacks:        +20
Clarity:       +5 to +15        (more bite for street textures)
Grain:         Amount 70 / Size 55 / Roughness 65
Vignette:      -25 (centered on subject)
B&W Mix:       Blue -25 (dark skies), Red +20 (warm skin under streetlights)
```

### Moody Portrait Emulation

```
Exposure:      +0.15 to +0.50
Contrast:      -35
Highlights:    -45
Shadows:       +25
Whites:        -20
Blacks:        +30              (maximum lifted black)
Clarity:       -15 to -25       (soft, forgiving skin)
Texture:       -10              (reduce skin texture)
Grain:         Amount 60 / Size 50 / Roughness 55
B&W Mix:       Orange +35 (luminous skin), Red +25
```

---

## Development Choices That Shape the Look (Analog Reference)

Different developers produce different aesthetics — useful to know what you're emulating:

| Developer | Look Produced | Digital Equivalent |
|-----------|--------------|-------------------|
| **Microphen** (stock) | Maximum speed, prominent grain, medium contrast | Standard Delta 3200 emulation |
| **DD-X** (1+4) | Finer grain, better shadow detail, smoother tonality | Lower grain slider, higher shadow lift |
| **Rodinal** (stand dev, 1+100) | Massive grain, high acutance, gritty | Max grain size + roughness, high clarity |
| **HC-110** (Dil B or H) | Moderate grain, snappy contrast | Higher contrast, moderate grain |
| **DF96 Monobath** | Variable, flatter tonality | Lower contrast, lower clarity |

---

## Scanning Influence on the "Delta 3200 Look"

Community consensus is that the final aesthetic is heavily influenced by scanning:

- **Flatbed scans** (Epson V550/V600/V700/V850): Softer, lower contrast, grain larger and less defined — closer to darkroom prints
- **DSLR/Mirrorless scans**: Sharper grain definition, more contrast, grain appears smaller and more textured
- **Lab scans (Noritsu/Frontier)**: Frontier gives higher contrast (classic look); Noritsu is flatter with more shadow detail
- **Drum scans**: Maximum detail, grain highly resolved — can actually be **too clean** for the Delta 3200 aesthetic

**For digital emulation of the authentic look:** Target the flatbed aesthetic — softer grain, slightly reduced micro-contrast, slightly warm-black shadows.

---

## Community Endorsed Free Resources

1. **PresetsHeaven MikeyG Ilford presets** (2009) — basic but historically accurate starting points
2. **G'MIC film emulation filters** (open source, works with GIMP/Krita)
3. **RawTherapee HaldCLUT** film emulation packs (some include Delta 3200)
4. **Darktable filmic module** — community .dtstyle files for Ilford emulation

---

## r/analog Community Notes

From Reddit threads about Delta 3200:

> "Delta 3200 at ISO 400? I shot it at 400 and I love it" — *u/superish64, r/analog*
>
> "Delta 3200 has quickly become one of my favorite films. I love the texture and contrast it provides." — *u/plusxpan, r/analog*
>
> "First time shooting Delta 3200 at a lower (recommended) ISO. Really like the results." — *u/TheHeadDrop, r/analog (shot at ISO 1000)*
>
> "Got grain?" — *u/FunkMasterQ, r/analog (2,314 upvotes, 7 years ago)* — became an iconic meme describing the Delta 3200 aesthetic

---

## Summary: The Delta 3200 Digital Recipe

```
┌─────────────────────────────────────────────┐
│ DELTA 3200 EMULATION — QUICK REFERENCE        │
├─────────────────────────────────────────────┤
│ Contrast:        -20                         │
│ Highlights:      -50                         │
│ Shadows:         +30                         │
│ Whites:          -15                         │
│ Blacks:          +22 (lifted blacks)         │
│ Tone Curve:      Raised black point to ~20   │
│ Clarity:         -10 (softer look)           │
│ Dehaze:          -10                         │
│ B&W Mix:         Red +15, Orange +20,        │
│                  Blue -15                    │
│ Grain Amount:    65                          │
│ Grain Size:      55                          │
│ Grain Roughness: 65                          │
│ Sharpening:      +50 / R1.2 / D30 / M40     │
│ Vignette:        -15                         │
└─────────────────────────────────────────────┘

---

## Post-Merge Update (fuzzy)

Changes applied to `Presets/Black-White/Ilford Delta 3200.xmp` via fuzzy community merge (2026-06-01):

| Parameter | Before | After | Method |
|---|---|---|---|
| Contrast2012 | -12.5 | -20 | Replaced (community -15 to -30) |
| Highlights2012 | -32.5 | -50 | Replaced (community -40 to -60) |
| Shadows2012 | +27.5 | +28.8 | Averaged (community +20 to +40) |
| Whites2012 | -12.5 | -13.8 | Averaged (community -10 to -25) |
| Blacks2012 | +22.5 | +22.3 | Averaged (community +15 to +30) |
| Clarity2012 | -17.5 | -10 | Replaced (community -10) |
| Texture | -12.5 | -11.3 | Averaged (community -10) |
| Dehaze | (none) | -10 | Added (community -5 to -15) |
| GrayMixerRed | +5 | +15 | Replaced (community +10 to +25) |
| GrayMixerOrange | +2.5 | +20 | Replaced (community +15 to +30) |
| GrayMixerYellow | (none) | +10 | Added (community +5 to +15) |
| GrayMixerGreen | +5 | -7.5 | Replaced (community -5 to -10) |
| GrayMixerAqua | (none) | -2.5 | Added (community 0 to -5) |
| GrayMixerBlue | -7.5 | -15 | Replaced (community -10 to -20) |
| GrayMixerPurple | (none) | -7.5 | Added (community -5 to -10) |
| GrayMixerMagenta | (none) | +2.5 | Added (community 0 to +5) |
| GrainAmount | +77.5 | +71.3 | Averaged (community 55-75) |
| GrainSize | 60 | 57.5 | Averaged (community 45-65) |
| GrainFrequency | +77.5 | +71.3 | Averaged (community 55-70) |

## Community Validated Values (2026)

Final consensus values from cross-referencing community recipes. Applied to `Presets/Black-White/Ilford Delta 3200.xmp` on 2026-06-01.

| Parameter | Final Value | Community Range | Source |
|-----------|------------|-----------------|--------|
| **Basic Panel** | | | |
| Contrast2012 | -20 | -15 to -30 | Low native contrast |
| Highlights2012 | -50 | -40 to -60 | Aggressive highlight protection |
| Shadows2012 | +28.8 | +20 to +40 | Averaged |
| Whites2012 | -13.8 | -10 to -25 | Muted whites |
| Blacks2012 | +22.3 | +15 to +30 | Critical: LIFTED blacks |
| Clarity2012 | -10 | -10 | Softer look |
| Dehaze | -10 | -5 to -15 | Atmospheric haze |
| Texture | -11.3 | -10 | Averaged |
| **B&W Mix** | | | |
| Red | +15 | +10 to +25 | Skin tones |
| Orange | +20 | +15 to +30 | Warm skin lift |
| Yellow | +10 | +5 to +15 | Midpoint |
| Green | -7.5 | -5 to -10 | Suppressed green |
| Aqua | -2.5 | 0 to -5 | Midpoint |
| Blue | -15 | -10 to -20 | Moody sky darkening |
| Purple | -7.5 | -5 to -10 | Midpoint |
| Magenta | +2.5 | 0 to +5 | Midpoint |
| **Grain** | | | |
| Amount | 71.3 | 55-75 | Heavy — defining characteristic |
| Size | 57.5 | 45-65 | Large "golf-ball" grain |
| Frequency | 71.3 | 55-70 | Pronounced texture |

**Key sources:** r/analog, r/Lightroom, r/Darkroom, Photrio, 35mmc, VSCO Film 02 reference, Mastin Labs Ilford Pack reference.
```
