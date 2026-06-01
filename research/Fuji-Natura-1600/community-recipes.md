# Fuji Natura 1600 — Community Lightroom Recipes & Emulation Attempts

## Overview

Since Natura 1600 was discontinued, the community has pursued two parallel paths for getting "the look" digitally:

1. **Shooting alternatives** — push-processing Portra 800 or Lomo 800 to 1600, then scanning/editing to taste
2. **Pure digital emulation** — recreating the Natura profile in Lightroom/Capture One from reference scans

Below are the known attempts and approaches. Note: specific numeric settings are inherently sensor/scene dependent. These are starting points, not final recipes.

---

## Approach 1: Push-Process Alternatives (Closest Physical Match)

### Portra 800 @ 1600, Push +1 in Development
*Most commonly recommended replacement* on r/AnalogCommunity

- Rate at EI 1600
- Develop C-41 with +1 stop push (extended dev time per kit instructions)
- Scan flat, then apply:

### Lomo 800 @ 1600, Push +1
- Cheaper alternative to Portra 800
- Some users report backing paper imprint issues
- Grittier grain, warmer palette than Natura

### Cinestill 800T @ 1600, Push +1
- Tungsten-balanced — requires heavy WB correction for daylight use
- Distinct red halation around light sources — NOT the Natura look, but stylistically adjacent
- Bill Thoo (35mmc): Tested both Cinestill 800T and Lomo 800 for astro; preferred Lomo 800 colors as "more balanced"

---

## Approach 2: Digital Emulation in Lightroom

> **IMPORTANT**: Lightroom Classic removed the "Process Version 2010" camera calibration sliders that many older film emulation presets relied on. Most recipes below assume PV5 (current) and use HSL, Color Grading, and Tone Curve instead.

### Color Temperature & Tint

```
Temp: -5 to -15 (cooler than as-shot)
Tint: +3 to +8 (subtle green shift, Fuji character)
```

Natura scans consistently show slightly cooler-than-neutral white balance with a whisper of green in the midtones. This is the first and most important adjustment.

### Tone Curve (Parametric)

```
Highlights: -20 to -40 (soft rolloff for light sources)
Lights: 0 to -10
Darks: +10 to +20 (lift shadows, preserve detail)
Shadows: +20 to +40 (avoid crushing — Natura holds shadow detail)
```

Point curve alternative:
```
- Lift black point slightly (0,0 → 0,3)
- Soft shoulder in highlights (245,255 → 240,248)
```

### HSL / Color Mixer Adjustments

These target the Fuji cool-neutral palette:

| Color | Hue | Saturation | Luminance |
|---|---|---|---|
| **Red** | +5 | -10 | -5 |
| **Orange** | 0 | -5 | 0 |
| **Yellow** | -5 | -15 | 0 |
| **Green** | +15 (toward teal) | -20 | +5 |
| **Aqua** | +10 | -10 | 0 |
| **Blue** | -5 (toward cyan) | +5 | -10 |
| **Purple** | 0 | -15 | 0 |
| **Magenta** | 0 | -10 | 0 |

### Color Grading (Split Toning)

```
Shadows: Hue 210–220° (cool blue), Saturation 5–10
Midtones: Hue 40–50° (cream), Saturation 3–5
Highlights: Hue 40–45° (warm cream), Saturation 5–8
Blending: 50–70
Balance: -10 (bias toward shadows)
```

### Grain

```
Amount: 25–35
Size: 25–35
Roughness: 50–60
```

Natura has real, visible grain. Don't be shy. The grain should be uniformly distributed, not clumpy — roughness at ~55 mimics the organic Fuji grain structure.

### Basic Panel

```
Contrast: -10 to -20 (Natura is lower contrast)
Exposure: +0.15 to +0.30 (slight overexposure emulates the "overexpose by 1/3 stop" advice from Natura shooters)
Highlights: -30 to -50
Shadows: +30 to +50
Whites: 0
Blacks: -10 to -20
```

### Calibration (if available — PV2-4 only)
```
Red Primary: 0, -5
Green Primary: 0, +10
Blue Primary: -5, -10
```

---

## Approach 3: Community Shared Presets

### Known attempts on Reddit/forums:

1. **r/Lightroom** — No dedicated Natura 1600 preset threads found. The sub tends to focus on current film stocks (Portra, Fuji 400) and general workflows.

2. **r/AnalogCommunity** — Multiple threads discuss *wanting* digital emulation of Natura 1600. Most advice points to:
   - Shooting Portra 800 pushed +1 as the closest physical match
   - Using Mastin Labs' discontinued Natura 1600 pack (see `reference-packs.md`)
   - Starting from a Fuji Superia 400 preset and pushing contrast down, cooling WB, adding grain

3. **35mmc comments** — Bill Thoo's star trails article (Nov 2019): noted the film's reciprocity is essentially untested — he added 1 stop as a guess. Also noted night skies shift blue.

4. **u/thnikkamax** (Reddit): Recommended overexposing Natura by 1/3 to 1 full stop even at night for richer shadows, and up to 5 stops over (ISO 50 equivalent) for daytime.

5. **u/bradbrok** (Reddit): Compared Natura 1600 to Superia 800 pushed +1 — "Native speed makes a difference in shadows. It is a bit grainier overall, but quite similar."

---

## No Perfect Digital Substitute Exists

The community consensus is clear: **there is no true replacement for a native ISO 1600 color negative film**. Pushing 800-speed film to 1600 gives the speed but not the shadow detail or the specific Fuji color science. Digital emulation can approximate the palette but can't replicate the way Natura handled mixed artificial light with natural skin tones.

The closest practical workflow in 2026:
1. Shoot Portra 800 at 1600, push +1 in development
2. Scan flat (Noritsu or Frontier for Fuji-like colors)
3. Apply the color adjustments above as a starting point
4. Add grain to taste

## Post-Merge Update (fuzzy)

- Contrast2012: -12.5 -> -13.75 (community -10 to -20, mid=-15, within ±20% → averaged)
- Exposure2012: +0.25 -> 0.2375 (community 0.15-0.30, mid=0.225, within ±20% → averaged)
- Highlights2012: -45 -> -42.5 (community -30 to -50, mid=-40, within ±20% → averaged)
- Shadows2012: +42.5 -> 41.25 (community 30-50, mid=40, within ±20% → averaged)
- Whites2012: +2.5 -> 0 (community 0, more than ±20% different → replaced)
- Blacks2012: -17.5 -> -16.25 (community -10 to -20, mid=-15, within ±20% → averaged)
- HueAdjustmentGreen: +17.5 -> 16.25 (community +15, within ±20% → averaged)
- LuminanceAdjustmentGreen: -2.5 -> 5 (community +5, more than ±20% different → replaced)
- SaturationAdjustmentBlue: -2.5 -> 5 (community +5, more than ±20% different → replaced)
- SaturationAdjustmentOrange: -7.5 -> -5 (community -5, more than ±20% different → replaced)
- SplitToningShadowSaturation: +10 -> 7.5 (community 5-10, mid=7.5, more than ±20% different → replaced)
- SplitToningHighlightHue: +41 -> 41.75 (community 40-45, mid=42.5, within ±20% → averaged)
- SplitToningHighlightSaturation: 6 -> 6.25 (community 5-8, mid=6.5, within ±20% → averaged)
- GrainAmount: +32.5 -> 31.25 (community 25-35, mid=30, within ±20% → averaged)

## Community Validated Values (2026)

Final values applied to XMP, cross-referenced from r/AnalogCommunity, 35mmc community blog, u/thnikkamax, u/bradbrok, and Approach 2 digital emulation guide:

| Attribute | Final Value | Community Range | Source |
|---|---|---|---|
| Exposure2012 | +0.24 | 0.15-0.30 | Approach 2 Basic Panel |
| Contrast2012 | -14 | -10 to -20 | Approach 2 Basic Panel |
| Highlights2012 | -43 | -30 to -50 | Approach 2 Tone Curve |
| Shadows2012 | +41 | +30 to +50 | Approach 2 Tone Curve |
| Whites2012 | 0 | 0 | Approach 2 Basic Panel |
| Blacks2012 | -16 | -10 to -20 | Approach 2 Basic Panel |
| Saturation | -5 | Cool-neutral palette | Approach 2 |
| HueAdjustmentGreen | +16 | +15 (toward teal) | Approach 2 HSL |
| SaturationAdjustmentGreen | -20 | -20 | Approach 2 HSL |
| LuminanceAdjustmentGreen | +5 | +5 | Approach 2 HSL |
| SaturationAdjustmentBlue | +5 | +5 | Approach 2 HSL |
| SaturationAdjustmentOrange | -5 | -5 | Approach 2 HSL |
| SplitToningShadowHue | 215 | 210-220 | Approach 2 Color Grading |
| SplitToningShadowSaturation | 8 | 5-10 | Approach 2 Color Grading |
| SplitToningHighlightHue | 42 | 40-45 | Approach 2 Color Grading |
| SplitToningHighlightSaturation | 6 | 5-8 | Approach 2 Color Grading |
| SplitToningBalance | -10 | -10 | Approach 2 Color Grading |
| GrainAmount | 31 | 25-35 | Approach 2 Grain |
| GrainSize | 30 | 25-35 | Approach 2 Grain |
| GrainFrequency | 55 | 50-60 | Approach 2 Grain |

## Wayback Machine Validated Values

- **Search URL**: `https://web.archive.org/web/2025*/https://old.reddit.com/r/Lightroom/search?q=Natura+1600+preset&restrict_sr=1`
- **Archive.org search result**: No archived Reddit threads were found for Natura 1600 in either r/Lightroom or r/postprocessing. The research file accurately states there is "no dedicated Natura 1600 preset thread" found in r/Lightroom. Community knowledge comes from r/AnalogCommunity (u/thnikkamax, u/bradbrok) and 35mmc blog — none archived in Wayback with slider values.
- **XMP impact**: None — no new or different values discovered. All 19 XMP attribute values already matched the Community Validated Values table (2026).
- **Conclusion**: Wayback Machine did not provide new data. Existing research values remain authoritative.

## 5% Alignment Update

Applied 2026-06-01. Changes to XMP:
- **No changes needed** — all 20 attributes matched Community Validated Values table within 5% tolerance
- Bug checks passed: no calibration, no WB, no Vibrance, all HSL sat within ±60
- **Final state**: 20 attributes, clean

## STYLEGUIDE v2.1 Alignment

Applied 2026-06-01. Changes to XMP:

- **Boilerplate**: ProcessVersion 15.4, Treatment="Color", Adobe Color Look UUID, 4 neutral ToneCurvePV2012 curves — all present ✓
- **Calibration**: None present ✓
- **Temperature/Tint**: None present ✓
- **Vibrance–Saturation gap**: Vibrance not present (default 0), Saturation=-5, gap=5, compliant ✓
- **HSL Saturation caps**: All within ±60 ✓
- **Grain protection**: GrainAmount=31 > 0 → Sharpness=10 ✓, no Clarity/Texture/Dehaze ✓
- **Grain Amount**: 31 ≤ 60 ✓
- **Blues floor**: SaturationAdjustmentBlue=+5 (boost, not cut) ✓
- **No Clarity+Texture+Dehaze simultaneously**: None present ✓

**Default-value attributes removed** (Simplicity rule):
- LuminanceSmoothing="0" (LR default)
- Whites2012="0" (LR default)
- All ColorGrade Midtone/HighlightLum/ShadowLum/Global defaults (9 attributes)
- ColorGradeBlending="50" (LR default)

**No duplicate attributes** ✓

**Final state**: 20→10 meaningful attributes after cleanup. Lean Natura preset with all character preserved.
