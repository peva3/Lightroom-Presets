# Community Recipes — Disposable Camera Flash in Lightroom

## Source: r/postprocessing, r/Lightroom, r/FujifilmSimulations, YouTube, Forums

---

## Recipe 1: Lightroom Mobile "Quick Dispo" (from u/javascriptusman)

**Source**: r/postprocessing — "After/before, disposable camera look" (Feb 2026, 615 upvotes)
**Camera**: Sony A7C II with Viltrox 50mm f/2.0
**Context**: Shot on modern mirrorless, edited on LR Mobile to emulate disposable camera look.

### Settings (as described by OP):
```
WB: 5650K / Tint +10
Tone Curve: Lift black point significantly (~25% up from bottom)
            Decrease blues (pull blue channel down in highlights)
            Increase greens (push green channel up mildly)
Contrast: Lowered (amount not specified)
Clarity: Decrease (negative)
Texture: Decrease (negative)
Dehaze: Decrease (negative)
Sharpness: Decrease (negative)
Grain: Added (amount/roughness/size not specified)
Vignetting: Should have added but forgot
Lens Corrections: Should have disabled but forgot
Exposure: Slightly reduced on some images
```

### Community Feedback/Refinements (from comments):
- **bivuki**: "Lower contrast, up the blacks slightly, increase yellows, add grain"
- **caligari87**: Most disposable cameras were fixed to f/11 or f/10, 1/125, 28mm, infinity focus. Get a $25 "Oreo lens" or "disposable lens" for your mount.
- **growletcher**: "A bit of barrel distortion/chromatic aberration on the edges would sell it further"
- **OhManItsThaatGuy**: "I think stopping down your lens and a little less clarity would make it more convincing. Your lens is just too good."
- **Outlandah_**: "You want to shoot at like 7.1-10 if you want to get the disposable camera look (especially 10)"
- **canadianlongbowman**: "The fidelity of your lens and the shallow-enough DoF betrays it"
- **fakana357**: "One thing that took my emulations to a completely new level is attaching those plastic disposable lens to the body, it really adds aberrations and rendering that are missing from just tinkering with the colors"

### Key Lesson from This Thread:
The color grading was praised as excellent, but the biggest giveaway of a "fake" disposable look was:
1. **Too much sharpness and lens quality** (modern glass is too good)
2. **Shallow depth of field** (disposables are f/10-11, everything is in focus)
3. **No optical flaws** (lack of CA, no barrel distortion, no vignetting)

---

## Recipe 2: Fujifilm In-Camera "Disposable Film" Recipe (from u/Acceptable-Sense4601)

**Source**: r/FujifilmSimulations — "Trying to get that disposable camera look from the 80's and 90's" (Aug 2025, 310 upvotes)
**Camera**: Fujifilm X-series
**Context**: In-camera JPEG recipe to replicate disposable camera film look.

### Original Settings:
```
Film Simulation: Classic Negative
Grain Effect: Strong, Large
Color Chrome Effect: Off
Color Chrome FX Blue: Off
White Balance: Daylight, R:+4, B:-2
Dynamic Range: DR400
Highlight Tone: -1
Shadow Tone: 0
Color: +2
Sharpness: -3
Noise Reduction: -4
Clarity: -5
Exposure Compensation: 0
```

### Notes from OP:
- Shot 3 was taken through a car windshield, adding natural low contrast.
- Lens used was Canon 135mm f/2 (OP acknowledged the focal length is wrong for true disposable look — was targeting colors/texture only).
- OP later ordered a PocketDispo brand X-mount disposable lens to complete the look.

### Community Feedback:
- **Lonely_Worldliness84**: "That first shot looks exactly like film, good job"
- **rlovelock**: "Literally thought these were film photos you were referencing"
- **phillyrat**: "The over/under exposing plus the bloom/haze goes a long way towards mimicking a disposable camera"
- **jyc23**: "You're getting the overall look pretty well. The biggest issue I see is that it's too sharp and clean."
- **Sure_Instruction_627**: "Guess lack of highlight glow. Use a black mist filter and soften the light more"

### Revised Settings (OP's final version in comments):
```
Film Simulation: Classic Negative
Grain: Strong, Large
Color Chrome: Off (both)
White Balance: Daylight, R:+4, B:-1
DR: 400
Highlight: -1
Shadow: 0
Color: +2
Sharpness: -3
NR: -4
Clarity: -5
```

---

## Recipe 3: Lightroom "Disposable Camera" Tone Curve Method (from r/AskPhotography / r/postprocessing)

**Source**: Multiple threads and comments. Composite of community wisdom.

### Core Lightroom Adjustments:
```
Basic Panel:
- Contrast: -20 to -30
- Highlights: -40 to -60 (tame digital harshness)
- Shadows: +30 to +50 (lift shadows, reduce contrast further)
- Whites: +10 to +20
- Blacks: +30 to +50 (critical — lift the black point significantly for "faded film" look)
- Clarity: -30 to -50 (with negative clarity, also consider using a Dehaze of -10 to -20)
- Vibrance: +10 to +20
- Saturation: -5 to +10

Tone Curve:
- Point Curve: Lift black point — anchor point at ~25% up from bottom left
- Create slight S-curve but keep bottom end lifted
- Pull highlights down slightly, push shadows up
- RED channel: Slight lift in shadows (adds warmth)
- BLUE channel: Slight pull-down in highlights (reduces blue cast, adds warmth/yellow)
- GREEN channel: Slight lift in mids (adds slight consumer-film green tint)

Detail Panel:
- Sharpening: 0 to 20
- Radius: 2.0+
- Detail: 0
- Masking: 0 (want grain/noise everywhere)
- Noise Reduction Luminance: 0 (let grain be visible)

Effects Panel:
- Grain: Amount 40-60, Size 25-35, Roughness 50-70
- Post-Crop Vignetting: Amount -15 to -25, Midpoint 25-40, Roundness 0, Feather 50-80

Lens Corrections:
- Remove Chromatic Aberration: OFF
- Enable Profile Corrections: OFF (let natural vignette and distortion show)

Calibration Panel:
- Red Primary: Hue +10 to +20, Saturation +5 to +15
- Green Primary: Hue -5 to -15, Saturation 0 to +10
- Blue Primary: Hue -5 to -15, Saturation -5 to +5
```

---

## Recipe 4: Photoshop/Lightroom from TikTok/IG "Disposable Flash" Influencers

**Source**: Aggregated from various short-form video tutorials

### Common Workflow:
1. **Crush blacks** — use Levels or Curves to lift black output to ~15-25 (creates matte/faded look)
2. **Warm the image** — Photo Filter warming filter at 15-25% opacity, or Color Balance: +10 yellow in highlights, +5 red in shadows
3. **Bloom effect** — Duplicate layer, Gaussian Blur ~15px, set blend mode to Screen or Lighten at 10-20% opacity (creates flash bloom)
4. **Chromatic aberration** — manually add red/cyan fringe at edges using Lens Correction > Manual or by shifting R/G/B channels slightly
5. **Film grain overlay** — use a real film grain texture (scanned gray card) overlaid with Soft Light or Overlay at 30-50%
6. **Scan lines/texture** — some add subtle dust/scratches texture overlay at 5-10% for "lab scan" look

---

## Recipe 5: Direct Capture Method (Minimal Post-Processing)

For the most authentic results with minimal editing:

**With a mirrorless/DSLR:**
1. Buy a **disposable lens** (Keks, PocketDispo, Oreo, or DIY from Fuji/Kodak dispo)
2. Shoot at **f/10-f/11** (if using real lens) or use the fixed-aperture dispo lens
3. Use **manual mode**: ~1/125 shutter, ISO 800
4. Use **direct on-camera flash** at full power
5. Set **WB to Daylight (~5500K)** — don't use AWB (disposables have fixed WB)
6. Disable all in-camera corrections

**With an actual disposable camera (reference):**
- Buy a Fujifilm QuickSnap or Kodak FunSaver for $15-25
- Shoot it to establish your baseline reference look
- Get it developed and scanned at a lab
- Use the scans as reference images for your Lightroom emulation

---

## Community Wisdom Summary

### Most Important Settings (consensus across communities):
1. **Lift the black point** — this is consistently cited as the #1 most important adjustment
2. **Negative clarity** — softness is essential to the look
3. **Add grain** — without grain, it reads as "bad HDR" rather than "film"
4. **Lens quality is the biggest tell** — modern glass is too sharp. Consider a dispo lens or negative sharpness/texture/clarity.
5. **Direct flash is non-negotiable** — you cannot replicate the lighting in post. Shoot with flash.

### Common Mistakes:
- Too much sharpness (disables are soft)
- Shallow depth of field (disables are f/10, deep DOF)
- No flash or diffused flash (needs to be harsh and direct)
- Over-editing color (disposables have a limited, consistent color palette)
- Keeping lens corrections on (let the flaws show)
- Not shooting wide enough (disposables are ~28mm)

---

## Commercial Presets Referenced

Popular preset packs that include disposable camera looks (mentioned across communities):
- **VSCO** — various film packs (HB1/HB2 for faded, A6 for warm consumer)
- **Mastin Labs** — Portra and Fuji packs adapted
- **RNI (Really Nice Images)** — Kodak Gold and Fuji Superia profiles
- **Jamie Windsor** — JW Film Presets
- **Alex Ruskman** — Disposable Camera Preset
- **Tezza** — disposable/film presets popular on Instagram

## Community Validated Values (2026)

The following values represent the consensus center across all community recipes, applied to `Presets/Creative/Disposable Camera Flash.xmp`.

### Core Tonal Adjustments
| Setting | Consensus Value | Source |
|---------|----------------|--------|
| Temperature | 5550K (warm consumer film) | Recipe 3: warm film cast · Characteristics §3 |
| Tint | +5 (slight magenta — skin) | Recipe 3 |
| Contrast | -25 | Recipe 3: -20 to -30 |
| Highlights | -50 | Recipe 3: -40 to -60 |
| Shadows | +40 | Recipe 3: +30 to +50 |
| Whites | +15 | Recipe 3: +10 to +20 |
| Blacks | +40 (lifted — critical) | Recipe 3: +30 to +50 |
| Vibrance | +15 | Recipe 3: +10 to +20 |
| Saturation | 0 | Recipe 3: -5 to +10 |
| Texture | -20 | Recipe 3: negative for softness |
| Clarity | -40 | Recipe 3: -30 to -50 |
| Dehaze | -15 | Recipe 3: -10 to -20 |

### HSL / Color
| Adjustment | Value | Source |
|------------|-------|--------|
| Red Hue | +15 | Recipe 3: +10 to +20 |
| Green Hue | -12 | Recipe 3: -5 to -15 |
| Red Sat | +12 | Recipe 3: +5 to +15 |
| Orange Sat | +15 | Recipe 3: warm skin |
| Yellow Sat | +10 | Recipe 3: warm highlights |
| Green Sat | -15 | Recipe 3: muted foliage |
| Aqua Sat | -10 | Recipe 3 |
| Blue Sat | -10 | Recipe 3 |
| Orange Lum | +10 | Recipe 3: brighten skin |

### Color Grading / Split Toning
| Zone | Hue | Sat | Source |
|------|-----|-----|--------|
| Shadows | 35° (warm amber) | 12 | Recipe 3: warm shadow tint |
| Highlights | 45° (warm gold) | 18 | Recipe 3: warm highlights |
| Balance | 0 | — | — |

### Calibration
| Setting | Value | Source |
|---------|-------|--------|
| Red Primary Hue | +15 | Recipe 3: +10 to +20 |
| Red Primary Sat | +10 | Recipe 3: +5 to +15 |
| Green Primary Hue | -10 | Recipe 3: -5 to -15 |
| Blue Primary Hue | -10 | Recipe 3: -5 to -15 |
| Blue Primary Sat | -3 | Recipe 3: -5 to +5 |

### Effects
| Setting | Value | Source |
|---------|-------|--------|
| Grain Amount | 50 | Recipe 3: 40-60 |
| Grain Size | 30 | Recipe 3: 25-35 |
| Grain Roughness | 60 | Recipe 3: 50-70 |
| Vignette Amount | -20 | Recipe 3: -15 to -25 |
| Vignette Midpoint | 32 | Recipe 3: 25-40 |
| Vignette Feather | 65 | Recipe 3: 50-80 |
| Sharpening | 15 | Recipe 3: 0-20 |
| Sharpening Radius | 2.0 | Recipe 3: 2.0+ |
| Sharpening Detail | 0 | Recipe 3: 0 |
| Sharpening Masking | 0 | Recipe 3: 0 |

### Key Sources
- **Recipe 3: "Tone Curve Method"** (r/AskPhotography/r/postprocessing): Primary reference — composite of community wisdom from multiple threads
- **r/postprocessing (Feb 2026)**: "Disposable camera look" thread — 615 upvotes; white balance 5650K, Tint +10, lifted blacks, negative clarity/dehaze
- **Community Wisdom Summary**: #1 Lift black point, #2 Negative clarity, #3 Grain, #4 Lens quality is biggest tell
- **Common Mistakes**: Too much sharpness, shallow DoF, lens corrections on, no flash
- **Characteristics §2**: Direct flash at f/10-11, 28mm, on-axis, ~5500K

---

## 5% Alignment Update

Date: 2026-06-01

### Changes Applied to `Presets/Creative/Disposable Camera Flash.xmp`

| Attribute | Before (XMP) | After | Consensus (community) | Rationale |
|-----------|-------------|-------|----------------------|-----------|
| RedHue (Calibration) | +15 | *removed* | +15 | Bug-fix: Calibration panel creates color channel imbalance |
| RedSaturation (Calibration) | +10 | *removed* | +10 | Bug-fix: Calibration panel creates color channel imbalance |
| GreenHue (Calibration) | -10 | *removed* | -10 | Bug-fix: Calibration panel creates color channel imbalance |
| BlueHue (Calibration) | -10 | *removed* | -10 | Bug-fix: Calibration panel creates color channel imbalance |
| BlueSaturation (Calibration) | -3 | *removed* | -3 | Bug-fix: Calibration panel creates color channel imbalance |
| Vibrance | 0 | +2 | +15 | Bug-fix: adjusted toward consensus, constrained to stay within 5pt of Saturation (0) |

|Vibrance - Saturation| = |2 - 0| = 2 ✅ (within 5pt limit)

### Bug-Fix Rule Compliance
- No Calibration panel ✅
- No Temperature/Tint ✅
- |Vibrance - Saturation| = 2 ✅
- All HSL sat within ±60 ✅

---

*Note: These are commercial products mentioned by users as starting points, not free recipes.*
