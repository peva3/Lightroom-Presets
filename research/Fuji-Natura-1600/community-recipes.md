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
