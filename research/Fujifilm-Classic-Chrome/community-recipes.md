# Classic Chrome — Community Recipes for Lightroom

> Compiled from Reddit (r/Lightroom, r/fujifilm, r/postprocessing), YouTube tutorials, and photography forums.

---

## How Fuji Shooters Use Classic Chrome In-Camera

### Popular In-Camera Recipe Pattern

The most commonly shared Classic Chrome "recipe" structure on r/fujifilm:

```
Film Simulation:  Classic Chrome
Grain Effect:     Strong, Small (or Weak, Small)
Color Chrome:     Strong
Color Chrome FX Blue: Weak (or Off)
White Balance:    Daylight, R+3 B-5 (warm shift)
Dynamic Range:    DR400
Tone Curve:       Highlights 0, Shadows 0 (or H-1, S+1)
Color:            +2
Sharpness:        0 (or -2)
Noise Reduction:  -4
```

This produces a warm, slightly desaturated look with crushed but not clipped shadows — the "vintage documentary" aesthetic with a hint of warmth from the WB shift.

### Variations

| Variation | In-Camera Changes | Result |
|---|---|---|
| **"Leica X" look** (by u/carlcruzsnaps) | Classic Chrome base, tweaked color/shadow/highlight balance | Warmer, more saturated midtones, slight green shift in shadows |
| **"Portra 400 on Classic Chrome"** | Classic Chrome + warm WB shift, Color +2, Shadows +1 | Hybrid of Classic Chrome tonality with Portra-like warmth |
| **Classic Chrome "pushed"** | Highlights -2, Shadows +2, DR400, Color -1 | Extreme contrast, very deep shadows, even more muted color |

### Community Workflow Observations

**RAW + JPEG Workflow:**
- Many users shoot RAW+JPEG, using the SOOC JPEG as reference and editing the RAW in Lightroom
- The Adobe Camera Matching "Classic Chrome" profile is used as a starting point
- **Common complaint:** Adobe's Classic Chrome profile doesn't precisely match SOOC JPEGs — the RAW looks flatter/darker

**Fuji X Raw Studio:**
- Some users export from Lightroom → Fuji X Raw Studio for the "real" Classic Chrome conversion
- This uses the camera's own processor (connected via USB), producing identical-to-in-camera JPEGs
- Drawback: disrupts Lightroom-centric workflow

---

## Replicating Classic Chrome in Lightroom (Non-Fuji Cameras)

Since non-Fuji users cannot access Camera Matching profiles, they must manually approximate the look.

### Method 1: Preset Packs (Commercial)

The community frequently references these commercial preset packs for Classic Chrome emulation:

| Product | Approach | Notes |
|---|---|---|
| **RNI All Films 5** | Camera-profiled presets | Widely praised for accuracy; includes Classic Chrome profile for multiple camera brands |
| **VSCO Film Pack** | Emulated film stocks via camera profiles | Discontinued but still widely used via legacy installs; MP1/FP8 packs include "Classic Chrome" variants |
| **Mastin Labs** | Film stock presets | Not Classic Chrome specifically, but "Portra Pushed" gets close to CC's contrast/saturation profile |
| **Cobalt Image** | Camera-profiled base profiles | Produces profiles that mimic Fuji film sims on Sony/Canon/Nikon sensors |
| **Alex Ruskman's Fuji Presets** | Lightroom presets | Recommended by r/fujifilm users for bridging CC JPEG-to-RAW gap |

### Method 2: Manual Lightroom Settings

Based on community posts, here is a composite manual recipe for emulating Classic Chrome on non-Fuji RAWs:

#### Basic Panel
```
Exposure:      0 (adjust to taste)
Contrast:      +15 to +25
Highlights:    -40 to -60  (recover sky)
Shadows:       -15 to -30  (deepen shadows, don't crush)
Whites:        -10 to +10
Blacks:        -15 to -25  (punchy deep blacks)
```

#### Tone Curve
```
Parametric:
  Highlights:  -10 to -20
  Lights:      -5 to +5
  Darks:       -10 to -20
  Shadows:     -5 to +5

Point Curve:
  Raise black point slightly (matte shadow look)
  Leave white point at 255
  Create gentle S-curve for midtone contrast
```

#### HSL / Color

This is the most critical section. Classic Chrome's distinguishing character lives in the HSL panel:

```
Hue:
  Red:         +5 to +15    (shift toward orange)
  Orange:      0 to +5
  Yellow:      0
  Green:       +15 to +25   (push toward yellow — key CC characteristic)
  Aqua:        +5 to +15
  Blue:        -5 to -10    (push toward cyan — removes magenta)
  Purple:      -10 to -20
  Magenta:     -5 to +5

Saturation:
  Red:         -15 to -30   (desaturate reds)
  Orange:      -10 to -20
  Yellow:      0 to -10
  Green:       -20 to -40   (strong desaturation of greens)
  Aqua:        -15 to -25
  Blue:        -20 to -35   (subdued blues — KEY characteristic)
  Purple:      -20 to -30
  Magenta:     -15 to -30

Luminance:
  Red:         -10 to -20   (darken reds)
  Orange:      -5 to -15
  Yellow:      -5 to -10
  Green:       -15 to -25   (darken greens — adds weight)
  Aqua:        -5 to -15
  Blue:        -10 to -25   (darken sky — deep punchy blues)
  Purple:      -5 to -15
  Magenta:     -10 to -20
```

#### Color Grading
```
Shadows:       Hue 210-220, Saturation 5-10  (cool blue shadows)
Midtones:      Hue 40-50,  Saturation 3-8    (warm midtones)
Highlights:    Hue 50-60,  Saturation 3-5    (slight warmth in highlights)
Blending:      70-80
Balance:       -10 to 0 (slightly shadow-weighted)
```

#### Effects
```
Texture:       +10 to +20  (documentary sharpness)
Clarity:       +5 to +15   (midtone definition)
Dehaze:        +5 to +10   (sky/contrast enhancement)
Vignette:      -5 to -15   (subtle edge darkening)
Grain:         15-25 (Size 25, Roughness 50) — emulate X-Trans grain character
```

#### Calibration
```
Red Primary:   Hue +10, Sat -10
Green Primary: Hue +15, Sat -20  (green→yellow shift)
Blue Primary:  Hue -5,  Sat -15  (blue→cyan shift)
```

### Method 3: Color Checker / Profiling (Advanced)

For the most accurate match (used by u/holywhateverbatman to build fujify.me):

1. Photograph a color checker chart (X-Rite ColorChecker Passport) under controlled lighting
2. Shoot the chart with your non-Fuji camera AND with a Fuji camera in Classic Chrome
3. Use Adobe DNG Profile Editor or Lumariver Profile Designer to build a .dcp camera profile that maps your camera's colors to match the Fuji output
4. This produces a Camera Matching-style profile rather than a preset — more accurate, applied at the demosaic level

---

## YouTube / Video Tutorial References

Popular YouTube tutorials for Classic Chrome replication (found via search):

| Channel / Title | Key Takeaway |
|---|---|
| "Fuji Classic Chrome Lightroom Preset" by various creators | Most use HSL panel for sky desaturation + tone curve for contrast |
| "How to Edit Like Fujifilm Classic Chrome" (multiple channels) | Emphasize desaturating blues/greens, adding warm midtones, crushing shadows |
| Jamie Windsor's Fuji film simulation videos | Detailed breakdown of color theory behind each simulation |
| Sean Tucker's "Fuji Film Simulations for Non-Fuji Shooters" | Practical walkthrough of manual replication |

---

## Common Pitfalls

1. **Too much contrast:** Classic Chrome has strong contrast but retains shadow detail. Don't clip blacks to 0.
2. **Over-desaturating blues:** The look is "subdued blue," not "gray sky." Preserve some chroma.
3. **Ignoring WB:** Classic Chrome often looks best with a slightly warm white balance (5500-6000K with +5-10 magenta tint).
4. **Applying to all scenes:** Classic Chrome looks best in harsh/high-contrast daylight. It falls apart in flat overcast light without shadow tone adjustments.

---

## Key Reddit Threads Referenced

- r/Lightroom: "fujifilm's film simulations on other brands?" — 21 points, 26 comments
- r/fujifilm: "Recreating Film Simulations with CCR/CCB" — detailed profile-building approach
- r/fujifilm: "Has anyone figured out how to exactly replicate a Fujifilm Recipe in lightroom?" — discussion of Color Chrome Effect emulation
- r/fujifilm: "My Leica Recipe" — popular Classic Chrome variant recipe
- r/Lightroom: "How to achieve color chrome/density/nonlinear saturation effect?" — deep dive into Color Chrome emulation
