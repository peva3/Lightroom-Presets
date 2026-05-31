# Bleach Bypass — Community Recipes & Digital Emulation

## How to Digitally Simulate Bleach Bypass

The core principle: **overlay a luminance-derived contrast boost while pulling saturation.** The silver retention of real bleach bypass acts as a neutral-density overlay proportional to exposure — darker in highlights, adding density everywhere, and "graying out" color information.

In digital tools, this translates to:
1. Crush blacks
2. Boost contrast (aggressive S-curve)
3. Reduce saturation (often 40–70%)
4. Add grain (luminance grain, not color grain)
5. Optionally cool the color temperature slightly (the silver adds a cool cast)

---

## Adobe Lightroom Classic Recipes

### Recipe 1: The "Saving Private Ryan" Base

```
Exposure: -0.33 to -0.66
Contrast: +60 to +80
Highlights: -50 to -80
Shadows: -30 to -50
Whites: +10 to +20
Blacks: -40 to -60

Clarity: +35 to +55 (perceptual midtone contrast)
Dehaze: +15 to +25

Tone Curve:
  Parametric:
    Highlights: -10
    Lights: +20
    Darks: -10
    Shadows: -25
  Point Curve: Strong Contrast

HSL / Color Mixer:
  Saturation:
    Red: -30
    Orange: -25
    Yellow: -35
    Green: -40
    Aqua: -45
    Blue: -20
    Purple: -35
    Magenta: -40

Color Grading:
  Shadows: H:220-230, S:8-12 (cool blue shadows)
  Midtones: H:30-40, S:3-5 (subtle warmth)
  Highlights: H:40-50, S:5-8

Sharpening: Amount 60-80, Radius 1.0-1.4, Detail 25, Masking 20
Noise Reduction: 0 (grain is desirable)
Grain:
  Amount: 35-55
  Size: 35-45
  Roughness: 50-70
```

### Recipe 2: The "Seven" Deep Black Variant

Heavier on blacks, more amber/copper undertones (ENR print characteristics):

```
Exposure: -0.5 to -1.0
Contrast: +90 to +100
Highlights: -70 to -100
Shadows: -60 to -80
Whites: 0
Blacks: -70 to -90

Clarity: +40 to +60
Dehaze: +20 to +30

Tone Curve:
  Point Curve: Strong Contrast with lifted toe
  (crushed blacks, steep midtones)

HSL Saturation: -50 to -70 across all channels
  Exception: Keep Orange at -20 to -30 for skin tone hint

Color Grading:
  Shadows: H:25-35, S:10-15 (warm amber blacks — ENR signature)
  Midtones: H:30-40, S:5-8
  Highlights: H:40-50, S:3-5

Grain: Amount 40-60, Size 40-50, Roughness 55-75

Calibration:
  Red Primary: H:-10, S:-15
  Green Primary: H:+5, S:-20
  Blue Primary: H:-5, S:-25
```

### Recipe 3: The "Minority Report" Steely Blue Variant

High-speed Fuji negative bleach bypass on OCN — blown highlights, intense grain, cold steely cast:

```
Exposure: -0.33
Contrast: +70
Highlights: -100 (let them blow — characteristic of OCN bleach bypass)
Shadows: -40
Whites: +30
Blacks: -50

Temperature: -5 to -10 (cooler)
Tint: -3 to -5 (slightly green — Fuji film characteristic)

Clarity: +30
Dehaze: +10

Tone Curve:
  Aggressive S-curve with shoulder roll-off in highlights

HSL:
  Saturation: -45 to -65 globally
  Luminance:
    Blue: -15 to -25 (darken skies)
    Aqua: -20

Color Grading:
  Shadows: H:210-220, S:15-20 (steely blue)
  Midtones: H:200-210, S:5-8
  Highlights: H:40-50, S:3-5

Grain: Amount 50-70, Size 45-55, Roughness 60-80 (heavy — OCN grain)
```

### Recipe 4: The "Fight Club" Variant

Khondji's work — gritty, sickly green-yellow cast in shadows, crushed blacks, extreme contrast:

```
Exposure: -0.66 to -1.0
Contrast: +80 to +100
Highlights: -60
Shadows: -70
Whites: 0
Blacks: -80

Clarity: +50
Dehaze: +25

Tone Curve:
  Heavy S-curve, crushed toe

HSL:
  Global Saturation: -50 to -60
  Green Luminance: -30 (dirty green shadows)
  Yellow Luminance: -20

Split Toning (or Color Grading):
  Shadows: H:60-80, S:12-18 (sickly green-yellow)
  Highlights: H:35-45, S:5-8 (warm tungsten cast)

Grain: Amount 45-60, Size 40-50, Roughness 55-70

Calibration:
  Green Primary: H:+10, S:-25 (push greens toward yellow-brown)
```

---

## DaVinci Resolve — Node Tree Approach

### Basic Bleach Bypass Node Tree

```
[Node 1: Exposure/Contrast]
  - Contrast: 1.3-1.5
  - Pivot: 0.435 (standard)
  - Lift: -0.05 to -0.10
  - Gain: 1.05-1.10

[Node 2: Luma vs Saturation Curve]
  - Custom Curve: Pull saturation DOWN as luminance increases
  - Dark areas retain more color, highlights go near-monochrome

[Node 3: Parallel — Desaturation]
  - Saturation: 0.30-0.50
  - Composite mode: Normal at 70-90% opacity

[Node 4: Grain / Texture]
  - Film Grain OFX or Resolve FX Texture
  - Luminance grain only, no color grain
  - Strength: 0.4-0.6

[Node 5: Look Adjustment]
  - Warm/cool balance per scene
  - Skin tone protection via qualifier + outside node
```

### Alexis Van Hurkman's Bleach Bypass Method (from *Color Correction Look Book*)

Van Hurkman describes a "simulated bleach bypass look" using the following approach in DaVinci Resolve:

1. **Use the Luma Mix slider** (in Curves) set to a high value (80-100) — this mixes luminance into the color channels, effectively reducing saturation proportionally to brightness
2. **Apply an aggressive S-curve** to crush shadows and boost highlights
3. **Reduce saturation** via the Saturation vs. Luminance curve — pull saturation down in the highlights
4. **Add grain** matching the film stock being emulated
5. **Protect skin tones** — qualifier isolating skintones, slight desaturation only, keeping them slightly more saturated than surroundings

Key insight: The Luma Mix parameter is critical because it simulates the silver overlay — the luminance information bleeds into the chroma channels, reducing color purity exactly where the silver would be densest.

### DaVinci Resolve Film Look Creator (FLC) Reference

DaVinci Resolve 19's **Film Look Creator** plugin can approximate bleach bypass:

- **Color Space:** Set to the appropriate film print emulation (e.g., Kodak 2383)
- **Bleach Bypass slider:** Some film emulation LUTs and OFX plugins include a direct bleach bypass parameter
- **Alternative in FLC:**
  - Contrast: Push to 1.5-1.8
  - Split Tone: Cool shadows, warm highlights
  - Halation: Subtle (film edge glow from silver)
  - Grain: Heavy, luminance-only
  - Print Stock: Choose a stock known for ENR/bleach bypass grading

### Resolve Color Space Transform (CST) Approach

For a more technically accurate emulation:
```
Timeline Color Space: DaVinci Wide Gamut / DaVinci Intermediate
CST Output: Rec.709 / Gamma 2.4

Node 1 (CST to film log):
  Input: Timeline
  Output: Arri LogC or Cineon Film Log

Node 2 (Film Print LUT):
  Kodak 2383 or Fuji 3513DI LUT
  These LUTs already compress the gamut and add film-like contrast

Node 3 (Bleach Bypass):
  Luma Mix: 0.85
  Custom S-curve
  Saturation: 0.35-0.50
  Luma vs Sat: Pull down in upper range

Node 4 (CST back to delivery):
  Output: Rec.709 / Gamma 2.4
```

---

## Photoshop Bleach Bypass Action

A documented community method:

1. **Duplicate background layer**
2. **Desaturate** the duplicate layer (Image → Adjustments → Desaturate)
3. **Set blend mode to Overlay** (or Soft Light for milder effect)
4. **Add Levels adjustment** to the desaturated layer — crush blacks and whites
5. **Add Hue/Saturation layer** below — reduce master saturation by 40-60%
6. **Add grain** via Filter → Noise → Add Noise (monochromatic, ~3-5%)
7. **Optional:** Add a Curves layer with a slight S-curve on top

The Overlay blend mode of the desaturated layer perfectly simulates the silver retention principle — luminance information overlaid on color.

---

## Capture One Recipe

```
Exposure: -0.3 to -0.5
Contrast: +25 to +35
Brightness: -5 to -10
Saturation: -50 to -65

High Dynamic Range:
  Highlight: -40 to -60
  Shadow: -30 to -50

Clarity: +30 to +45 (use "Neutral" method for less haloing)
Structure: +15 to +25

Curve:
  Luma curve: Strong S-shape
  Pull shadow point up slightly (crush blacks)
  Lift highlight point slightly (blown highlights characteristic)

Color Balance:
  3-Way:
    Shadows: Cool (blue-cyan, -5 to -10)
    Midtones: Neutral to slightly warm
    Highlights: Slightly warm

Grain:
  Film Grain tool:
    Type: Silver Rich or Tabular
    Impact: 40-60
    Granularity: 45-55
```

---

## Common Pitfalls in Digital Emulation

| Pitfall | Why It Happens | Fix |
|---------|---------------|-----|
| "Muddy" look | Too much desaturation without enough contrast | Increase contrast first, then pull saturation |
| Skin looks dead | Silver retention should leave *some* color | Protect skin tones with a mask or qualifier; keep them 10-20% more saturated |
| Digital-looking grain | Using color noise instead of luminance grain | Add luminance-only grain or monochromatic noise |
| Highlights too gray | Real bleach bypass has specular highlight roll-off | Lift the shoulder of the tone curve, or add a highlight compression node |
| Shadows too colorful | Real bleach bypass desaturates shadows heavily | Use Luma vs Sat curve to pull saturation from low luma values too |

---

## Community Discussion Summary

### r/colorists (Reddit) — Common Themes:

- Bleach bypass is frequently discussed as a reference look for "gritty" grades
- Most colorists recommend building it as a **parallel node** in Resolve rather than using a preset LUT
- The **Luma Mix** slider in Resolve's Custom Curves is the single most important tool for the look
- General consensus: ENR/silver retention feels "organic" in a way pure digital contrast boosts don't
- Many colorists note that true bleach bypass **reduces saturation more in highlights than shadows** — the opposite of what a simple global desaturation does

### r/Lightroom (Reddit) — Common Themes:

- Clarity slider abuse is a common newbie mistake — bleach bypass needs **contrast** first and clarity second
- Grain is essential; without it the look feels "plasticky"
- The desaturated layer + Overlay blend mode in Photoshop is the most recommended "quick and dirty" method
- Split toning with cool shadows + warm highlights consistently cited

### r/postprocessing (Reddit) — Common Themes:

- Many photographers use bleach bypass as a starting point for "cinematic" edits
- Common complaint: "My bleach bypass looks just look underexposed and gray"
- Resolution: the underlying image needs proper exposure and lighting contrast BEFORE the grade

### YouTube Tutorial Makers (Consensus Settings):

- **Contrast first** — the silver-retention look is primarily about luminance, not color
- **Desaturate by channel**, not globally — reds and greens particularly should be pulled harder than blues
- **Grain MUST be luminance-only** — grain with color chroma noise looks digital/video, not filmic
- **Slight blue cast in shadows** helps sell the "silver" feel
- **Underexpose slightly** — bleach bypass traditionally paired with -1 stop underexposure

---

## Sources

- Alexis Van Hurkman, *Color Correction Look Book: Creative Grading Techniques for Film and Video*, Chapter 2: "Bleach Bypass Looks" (Peachpit Press, 2013)
- DaVinci Resolve 19 Reference Manual, Film Look Creator section
- Cinematography.com — David Mullen ASC, Gautam Valluri, Seth Baldwin, Robert Houllahan, Ludwig Hagelstein
- Reddit: r/colorists, r/postprocessing, r/Lightroom (bleach bypass discussions)
- YouTube: various color grading tutorial creators
