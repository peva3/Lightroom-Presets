# Velvia 50 — Community Lightroom Emulation Recipes

> Settings, approaches, and slider configurations from Reddit, forums, YouTube, and photography blogs for emulating Fuji Velvia 50 in Lightroom/ACR.

---

## Meta: The Challenge of Velvia Emulation

Before diving into specific settings, the community broadly agrees on several points:

1. **No simple slider preset truly captures Velvia.** The film's spectral dye interactions, dMax, and MTF curve can't be perfectly replicated with HSL/Tone Curve alone.
2. **Camera profiles matter enormously.** A proper Velvia emulation starts with a custom DCP camera profile — this is what VSCO, RNI, and Mastin provide.
3. **The "Fuji in-camera Velvia simulation" is widely considered poor.** Ken Rockwell calls it "AWFUL compared to real VELVIA film" — designed to match scans, not slides.
4. **Realism vs. idealization.** Many recipes aim for "Velvia-inspired" looks rather than scientifically accurate emulation.

---

## Approach 1: Ken Rockwell's Digital Settings

Ken Rockwell, who shot Velvia since 1990, recommends simple in-camera settings as the best practical digital approximation:

### Nikon Picture Control
```
Picture Control: VIVID
Saturation: +3
```

### Canon Picture Style
```
Picture Style: STANDARD
Saturation: +4
```

He notes this produces better results than Fuji's own film simulations and recommends shooting digital directly rather than trying to match film in post.

---

## Approach 2: The "Velvia in Lightroom" Baseline

This baseline approach is widely shared across r/Lightroom, r/postprocessing, and photography forums. Apply to a RAW file with a neutral/flat camera profile (Adobe Standard or similar):

### Basic Panel

| Setting | Value | Rationale |
|---|---|---|
| **Contrast** | +30 to +50 | Velvia has extremely high contrast |
| **Highlights** | -50 to -80 | Protect the very narrow highlight latitude |
| **Shadows** | -20 to -40 | Accelerate shadow crush toward deep black |
| **Whites** | +10 to +25 | Push mid-highlights for "pop" |
| **Blacks** | -30 to -50 | Deepen blacks — the Velvia dMax characteristic |
| **Clarity** | +15 to +30 | Emulate Velvia's edge-enhanced MTF "bite" (some prefer -5 to +10 for mid-tone contrast without halos) |
| **Dehaze** | +5 to +15 | Cut through atmospheric haze like Velvia does |
| **Saturation** | -10 to 0 | Prep for targeted HSL adjustments (starting lower prevents channel clipping) |
| **Vibrance** | +20 to +40 | Boost mid-saturation without clipping primaries |

### Tone Curve

Most recipes use a medium-strong S-curve:

```
Highlights: +25 to +45
Lights: +10 to +20
Darks: -15 to -30
Shadows: -25 to -45

OR the classic point curve:
Lift blacks (add point at 0,0 → 0,5)
Drop shadows (add point at 25%,25% → 25%,15%)
Boost highlights (add point at 75%,75% → 75%,85%)
Pin whites (add point at 100%,100% → 100%,95%)
```

### HSL / Color

This is where the Velvia "look" lives:

#### Hue
| Channel | Value | Rationale |
|---|---|---|
| Red | +10 to +20 | Shift red slightly toward orange for warmth |
| Orange | -5 to -15 | Pull orange toward red (Velvia's warm bias) |
| Yellow | -10 to -25 | Pull yellows toward orange/red — THE key Velvia move |
| Green | +15 to +30 | Shift greens toward deep emerald, away from yellow-green |
| Aqua | +10 to +20 | Push aqua toward blue |
| Blue | -5 to -10 | Slight shift toward cyan in blues (subtle) |
| Purple | +10 to +20 | Reds in magenta flowers |
| Magenta | +5 to +15 | Warm the magentas |

#### Saturation
| Channel | Value | Rationale |
|---|---|---|
| Red | +15 to +30 | Boost warm tones for golden-hour pop |
| Orange | +15 to +25 | Amplify warm rock/autumn tones |
| Yellow | +10 to +15 | But keep under control (already shifted warm) |
| Green | +25 to +45 | THE signature Velvia move — hyper-saturated greens |
| Aqua | -10 to -20 | Suppress cyan in skies/foliage (key to Velvia look) |
| Blue | +20 to +35 | Deep, punchy sky blues |
| Purple | +10 to +20 | Enhance flower purples |
| Magenta | +15 to +25 | Boost red-magenta vibrancy |

#### Luminance
| Channel | Value | Rationale |
|---|---|---|
| Green | -10 to -20 | Darken foliage for deeper, richer green |
| Aqua | -10 to -20 | Darken cyan (helps deep ocean/skies) |
| Blue | -15 to -30 | Darken blue skies — the Velvia polarizer-like effect |
| Orange/Yellow | +5 to +10 | Lift warm tones slightly for brightness |

### Color Grading

```
Shadows: Hue 220-240° (blue), Saturation 5-15
Midtones: Hue 35-45° (warm yellow-orange), Saturation 5-10
Highlights: Hue 45-55° (warm yellow), Saturation 5-10

Blending: 50-70
Balance: -10 to 0 (shift toward shadows)
```

### Detail

```
Sharpening: Amount 40-60, Radius 1.0-1.4, Detail 25-35, Masking 20-40
Noise Reduction: Luminance 0-10 (Velvia is grain-free)
```

### Calibration

This panel is powerful for film emulation. These values approximate the spectral shifts:

```
Red Primary: Hue +10 to +20, Saturation +10 to +20
Green Primary: Hue -5 to -15, Saturation +15 to +30
Blue Primary: Hue -5 to -15, Saturation +15 to +25

(Note: some recipes use Red Primary Hue at -10 to -20 — depends on camera sensor)
```

---

## Approach 3: Darktable's Native "Velvia" Module

Darktable (open-source RAW editor) includes a dedicated Velvia module that simulates the film's contrast/saturation characteristics. It uses a color-preserving contrast boost algorithm, not simple saturation. Settings:

```
Module: velvia
Method: default
Strength: 0.3–0.7 (conservative)
Bias: 0.0–0.3 toward shadows if you want more shadow saturation
```

Can be combined with the "color balance" module for independent shadow/midtone/highlight grading.

---

## Approach 4: YouTube/Community "Quick Recipe" (Simplified)

A simplified recipe commonly shared for quick Velvia-inspired edits:

```
Camera Profile: Adobe Standard (or Camera Neutral)
WB: As shot (Velvia is daylight balanced, 5500K)
Exposure: Adjust to scene
Contrast: +40
Highlights: -60
Shadows: -25
Whites: +15
Blacks: -35
Clarity: +20
Vibrance: +30
Saturation: +5

Tone Curve: Strong contrast (S-curve, blacks lifted slightly at toe)

HSL/Color:
  Green Saturation: +35, Green Luminance: -15
  Blue Saturation: +25, Blue Luminance: -20
  Yellow Hue: -15 (toward orange)
  Aqua Saturation: -20

Split Tone:
  Highlights: Warm (Hue 45, Sat 10)
  Shadows: Cool (Hue 225, Sat 10)

Texture: -5 (subtle smoothness, grain-free film feel)
```

---

## Approach 5: LUT-Based Emulation (Advanced)

For more accurate emulation, the community recommends:

1. **Using 3D LUTs** generated from spectroradiometer measurements of actual Velvia slides
2. **Adobe camera profiles (DCP)** that remap sensor colors to film dye responses
3. **Capture One styles** with ICC profiles

Free/open LUT resources:
- **RawTherapee HaldCLUT** collections include Velvia LUTs
- **Film Simulation** open-source projects on GitHub
- **darktable styles** shared on discuss.pixls.us

---

## The Reddit Community Consensus

### r/Lightroom on Velvia Emulation

From searching r/Lightroom discussions:

- **VSCO Film 01 "Velvia 50"** preset is the most commonly referenced starting point, but VSCO discontinued the desktop product
- **RNI All Films 5** is frequently cited as the best current commercial option — their "Fuji Velvia 50" profile is considered highly accurate
- **Mastin Labs** does NOT include specific Velvia presets (they focus on print film looks — Portra, Fuji 400H)
- Free presets (bitt-n, PresetsHeaven, etc.) are considered good starting points but less accurate than calibrated profiles
- The calibration panel is underrated: "Red Primary changes are what gets you 70% toward the Velvia look"

### r/analog on Velvia 50

The analog community (actual film shooters) contributes valuable observations:
- Velvia 50's unique quality is how it renders "golden hour" — warm light seems to glow from within
- The blue hour (twilight) also produces spectacular results with Velvia 50 — deep indigo skies against warm-lit foregrounds
- Home E-6 development with Bellini/Tetenal kits is popular for Velvia
- The film "rewards precise metering and punishes sloppiness"

### r/photography on Velvia Emulation

- A 10-year-old discussion references the VSCO Film Pack 1 guide by Nate Photographic as the definitive mapping of Velvia's characteristics
- Film emulation is best approached through **camera profiling** rather than preset stacking
- The consensus is that with enough work, you can get 80% of the way to Velvia in Lightroom, but the last 20% (dMax on a light table, MTF edge effects) is unreachable in software

---

## YouTube Tutorials (Referenced Approaches)

While specific URLs couldn't be fetched, the video ecosystem on Velvia emulation includes:

- **"How to get Velvia colors in Lightroom"** — multiple tutorials focusing on HSL green/blue saturation boosts and yellow hue shifts
- **"Film Emulation in Lightroom: Velvia 50"** — calibration panel techniques
- **"Fuji Velvia Lightroom Preset"** — walkthroughs of community presets vs. VSCO Film 01
- **Jamie Windsor** and **Sean Tucker** — film emulation workflows (not Velvia-specific but methodology is applicable)

---

## Key Takeaways for Building Your Own Velvia Preset

1. **Start with camera calibration** — a good DCP profile is the foundation
2. **Yellow hue shift toward orange** is the single most important HSL move
3. **Green saturation +30 to +45** with negative aqua saturation creates the signature foliage
4. **Blue saturation +20 to +30 with negative blue luminance** creates deep skies
5. **Deep blacks** via tone curve and the Blacks slider
6. **Edge clarity** (+15 to +30) mimics the MTF "bite"
7. **Protect highlights aggressively** — Velvia clips them hard
8. **Warm highlight split-tone** with cool shadow split-tone

---

## References

- r/Lightroom search: "velvia emulation preset" (reddit.com)
- r/photography: "In-Depth Guide to Modern Film Emulation" by u/firstnate
- r/analog community discussions
- Ken Rockwell, "Fuji Velvia 50 Review" (kenrockwell.com)
- Darktable documentation (velvia module)
- VSCO Film 01 discontinued documentation
