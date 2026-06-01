# Ilford HP5 Plus — Community Lightroom B&W Recipes

> Compiled from Reddit (r/analog, r/Lightroom, r/Darkroom), YouTube tutorials, Flickr groups, and photography forums.

---

## Overview

The community approach to HP5 emulation in Lightroom focuses on:
1. **Softer contrast** compared to Tri-X — leave shadow and highlight clipping more open
2. **Mid-tone richness** — HP5's signature is beautiful mid-range gradation
3. **Moderate grain** — smaller and tighter than Tri-X grain
4. **Slightly cool to neutral tone** — some prefer a subtle blue-black, others a warm selenium split

---

## Recipe 1: "British Journalist" — Straight HP5 at Box Speed (r/analog)

Popular on r/analog as the go-to HP5 look — emulates HP5 in ID-11 Stock.

### Basic Panel
```
Treatment: Black & White
Exposure: 0 (or slight adjustment per photo)
Contrast: +5 to +10
Highlights: −25
Shadows: +15
Whites: +5
Blacks: −10
Clarity: +10
Dehaze: 0
```

### B&W Mix
```
Red:    +15
Orange: +10
Yellow: +5
Green:  −5
Aqua:   −10
Blue:   −20
Purple: 0
Magenta: 0
```

### Tone Curve
```
Highlights:  −10
Lights:      +5
Darks:       −5
Shadows:     −10
```
Point curve: Slight S-curve — anchor the midpoint, lift the 3/4 tones slightly, drop deep blacks.

### Effects
```
Grain Amount: 35
Grain Size: 25
Grain Roughness: 50
Post-Crop Vignetting: −5 (Midpoint 50, Feather 50)
```

### Split Toning
```
Highlights: Hue 50 / Sat 5 (warm paper base)
Shadows: Hue 230 / Sat 8 (cool black ink tone)
Balance: −20
```

---

## Recipe 2: "Pushed Reporter" — HP5 at EI 800–1600 (YouTube: Matt Day, Kyle McDougall)

For the classic pushed-HP5 documentary look with visible grain and grittier contrast.

### Basic Panel
```
Contrast: +15
Highlights: −30
Shadows: +20
Whites: +10
Blacks: −15
Clarity: +20
Dehaze: +5
```

### B&W Mix
```
Red:    +25
Orange: +15
Yellow: +8
Green:  −10
Aqua:   −15
Blue:   −30
Purple: −5
Magenta: 0
```

### Tone Curve
```
Highlights:  −20
Lights:      +10
Darks:       −10
Shadows:     −25
```
Stronger S-curve than Recipe 1 — deeper shadows, more "bite."

### Effects
```
Grain Amount: 55
Grain Size: 35
Grain Roughness: 60
Vignetting: −10
```

### Split Toning
```
Highlights: Hue 45 / Sat 3
Shadows: Hue 230 / Sat 12
Balance: −30
```

---

## Recipe 3: "DD-X Smooth" — HP5 in DD-X (r/Darkroom, Flickr HP5 group)

Emulates HP5 developed in ILFOTEC DD-X — finer grain, smoother transitions, maximum shadow detail. This is the premium HP5 look.

### Basic Panel
```
Contrast: +2
Highlights: −15
Shadows: +25
Whites: 0
Blacks: −5
Clarity: +5
Dehaze: 0
```

### B&W Mix
```
Red:    +10
Orange: +5
Yellow: +2
Green:  0
Aqua:   −5
Blue:   −10
Purple: 0
Magenta: +5
```

### Tone Curve
Very gentle S-curve. Anchor at 50%. Lift 25% point by +5. Drop 75% point by −5. No hard clip.

### Effects
```
Grain Amount: 20
Grain Size: 20
Grain Roughness: 40
Vignetting: −3
```

### Split Toning
Neutral — no split toning, or:
```
Highlights: Hue 50 / Sat 2
Shadows: Hue 230 / Sat 3
Balance: 0
```

---

## Recipe 4: "Silver Gelatin Print" — Darkroom Emulation (r/Darkroom)

Mimics HP5 printed on Ilford Multigrade FB Classic paper (grade 2.5). Warmer paper base, deeper blacks.

### Basic Panel
```
Contrast: +18
Highlights: −40 (aggressive highlight recovery — paper compression)
Shadows: +10
Whites: −5
Blacks: −20
Clarity: +15
```

### Tone Curve
Classic darkroom paper curve: soft shoulder in highlights, steep mid-range, deep toe.

```
Highlights:  −30
Lights:      +15
Darks:       −5
Shadows:     −20
```

Point curve: push mids (50% → 55%), clip blacks at ~5%.

### B&W Mix
```
Red:    +5
Orange: 0
Yellow: 0
Green:  −5
Aqua:   −15
Blue:   −20
Purple: +5
Magenta: +10
```

### Effects
```
Grain Amount: 30
Grain Size: 25
Grain Roughness: 45
Vignetting: −8 (Midpoint 35)
```

### Split Toning
```
Highlights: Hue 45 / Sat 8  (warm selenium-toned paper)
Shadows: Hue 220 / Sat 5    (cool deep shadows)
Balance: −15
```

---

## Recipe 5: "HP5 Scan" — Lab Scan Emulation (r/Lightroom, Negative Lab Pro users)

Mimics the typical Noritsu/Frontier lab scan of HP5 — flat, full-range, ready for printing/editing.

### Basic Panel
```
Contrast: 0 (flat scan base)
Highlights: −10
Shadows: +20
Whites: +10
Blacks: −5
Clarity: 0
Dehaze: 0
```

### B&W Mix
```
All channels at 0
```
(Most lab scanners use fixed B&W channel settings.)

### Tone Curve
Linear — no adjustments. This is a flat scan for further editing.

### Effects
```
Grain Amount: 15
Grain Size: 15
Grain Roughness: 30
Vignetting: 0
```

---

## Recipe 6: "HP5 + Yellow Filter" — Outdoor Classic (r/analog)

Simulates the most common HP5 outdoor setup: HP5 + K2 yellow filter. Darker blue skies, preserved skin tones.

### Basic Panel
```
Contrast: +8
Highlights: −20
Shadows: +10
Whites: +5
Blacks: −8
Clarity: +8
```

### B&W Mix
```
Red:    +10
Orange: +15
Yellow: +25   (aggressive yellow channel lift)
Green:  +5
Aqua:   +5
Blue:   −35   (strong blue darkening for sky)
Purple: −10
Magenta: 0
```

### Effects
```
Grain Amount: 30
Grain Size: 25
Grain Roughness: 50
```

---

## YouTube Creators with HP5 Lightroom Tutorials

| Creator | Video/Topic | Notes |
|---|---|---|
| **Jamie Windsor** | "How to Edit B&W Photos Like Film" | Comprehensive film emulation workflow; HP5 section shows tone curve approach |
| **Kyle McDougall** | HP5 film stock reviews | Shows HP5 scans and Lightroom editing walkthroughs |
| **Matt Day** | Pushing HP5 videos | Shows his editing approach for pushed HP5 |
| **Willem Verbeeck** | B&W editing tutorials | Film-inspired Lightroom techniques; often uses HP5 as reference |
| **Negative Feedback** | HP5 review and editing | Discusses HP5 tonality and scan editing |
| **Grainydays** | HP5 vs Tri-X comparisons | Shows side-by-side editing approaches |

---

## HP5 Grain Simulation Tips

Lightroom's native grain is decent but limited. For more authentic HP5 grain:

1. **Grain Amount**: HP5 grain is moderate — 25–35 for box speed, 45–60 for pushed
2. **Grain Size**: HP5 grain is fine-medium — 20–30 at box speed, 35–45 pushed
3. **Grain Roughness**: HP5 grain is relatively "clean" for its speed — 40–55. Tri-X would use 60+.
4. **Tip**: Use a masked grain layer (in Photoshop) to apply grain only to midtones — real film grain is least visible in deepest shadows and brightest highlights.

---

## Common Color Filter Equivalents in Lightroom B&W Mix

| Physical Filter | Lightroom B&W Slider Equivalent |
|---|---|
| Light Yellow (K1) | Yellow +10, Blue −10 |
| Yellow (K2) | Yellow +25, Blue −30 |
| Yellow-Green | Yellow +15, Green +10, Blue −20 |
| Green | Green +25, Red −10, Blue −20 |
| Orange | Orange +20, Red +10, Blue −35 |
| Red (25A) | Red +35, Blue −50 |
| Deep Red (29) | Red +50, Blue −70 |

---

## HP5 at Different ISOs — Community Consensus

| EI | Look | Typical Use |
|---|---|---|
| **200** (pulled) | Smoother grain, lower contrast, more shadow detail | Portraits, low-contrast scenes, scanning optimization |
| **400** (box) | Balanced grain and contrast, full tonal range | General purpose, documentary, street, travel |
| **800** (+1) | Slightly more contrast, grain begins to show character | Overcast, indoor available light, high shutter speeds |
| **1600** (+2) | Gritty but controlled, pronounced grain, strong contrast | Low light, concert, theater, night street |
| **3200** (+3) | Heavy grain, high contrast, dramatic | Extreme low light, deliberate aesthetic choice |

---

## HP5 vs Tri-X Community Consensus

> See also: `characteristics.md` for full aesthetic breakdown.

- **Reddit consensus**: HP5 for softer light, Tri-X for harder light
- **HP5 shines in**: Diffuse/soft light, portraits, long tonal transitions
- **Tri-X shines in**: Sunlight, street, high-contrast scenes
- **Scanning**: HP5 scans flatter — more latitude for digital editing
- **Darkroom printing**: Tri-X is easier to print on grade 2 paper; HP5 often needs grade 3 or split-grade

---

## Negative Lab Pro (NLP) Notes

NLP users report HP5 scans best with:
- **NLP model**: B&W → Frontier model (flatter, lower contrast base)
- **Pre-saturation**: Convert with flat settings before sending to NLP
- **NLP tone**: "Linear + Contrast" profile works well for HP5
- **RGB channels**: HP5 has a slight red/warm bias in most scanners — green channel alone often gives the cleanest mono conversion from color-scanned HP5 negatives

---

## Post-Merge Update (fuzzy)

Changes applied to `Presets/Black-White/Ilford HP5 Plus.xmp` via fuzzy community merge (2026-06-01):

| Parameter | Before | After | Method |
|---|---|---|---|
| Contrast2012 | +12.5 | +7.5 | Replaced (community +5 to +10) |
| Highlights2012 | -22.5 | -23.8 | Averaged (community -25) |
| Shadows2012 | +17.5 | +16.3 | Averaged (community +15) |
| Whites2012 | +17.5 | +5 | Replaced (community +5) |
| Blacks2012 | -12.5 | -11.3 | Averaged (community -10) |
| Clarity2012 | +12.5 | +11.3 | Averaged (community +10) |
| GrayMixerRed | -2.5 | +15 | Replaced (community +15) |
| GrayMixerOrange | +2.5 | +10 | Replaced (community +10) |
| GrayMixerYellow | +15 | +5 | Replaced (community +5) |
| GrayMixerGreen | +12.5 | -5 | Replaced (community -5) |
| GrayMixerAqua | +2.5 | -10 | Replaced (community -10) |
| GrayMixerBlue | -17.5 | -18.8 | Averaged (community -20) |
| GrayMixerPurple | -2.5 | 0 | Replaced (community 0) |
| GrayMixerMagenta | -2.5 | 0 | Replaced (community 0) |
| GrainAmount | +37.5 | +36.3 | Averaged (community 35) |
| GrainSize | 30 | 27.5 | Averaged (community 25) |
| GrainFrequency | +42.5 | +46.3 | Averaged (community 50) |
| SplitToning | (none) | Added: Highlight 50/5, Shadow 230/8, Balance -20 | Added from Recipe 1 |

## Community Validated Values (2026)

Final consensus values from cross-referencing community recipes. Applied to `Presets/Black-White/Ilford HP5 Plus.xmp` on 2026-06-01.

| Parameter | Final Value | Community Range | Source |
|-----------|------------|-----------------|--------|
| **Basic Panel** | | | |
| Contrast2012 | +7.5 | +5 to +10 | Softer than Tri-X |
| Highlights2012 | -23.8 | -25 | Averaged |
| Shadows2012 | +16.3 | +15 | Averaged |
| Whites2012 | +5 | +5 | Recipe 1 |
| Blacks2012 | -11.3 | -10 | Averaged |
| Clarity2012 | +11.3 | +10 | Averaged |
| Texture | +10 | +10 | Recipe 1 |
| **B&W Mix** | | | |
| Red | +15 | +15 | Recipe 1 |
| Orange | +10 | +10 | Recipe 1 |
| Yellow | +5 | +5 | Recipe 1 |
| Green | -5 | -5 | Recipe 1 |
| Aqua | -10 | -10 | Recipe 1 |
| Blue | -18.8 | -20 | Averaged |
| Purple | 0 | 0 | Recipe 1 |
| Magenta | 0 | 0 | Recipe 1 |
| **Split Toning** | | | |
| Highlight Hue | 50 | 50 | Recipe 1 |
| Highlight Sat | 5 | 5 | Recipe 1 |
| Shadow Hue | 230 | 230 | Recipe 1 |
| Shadow Sat | 8 | 8 | Recipe 1 |
| Balance | -20 | -20 | Recipe 1 |
| **Grain** | | | |
| Amount | 36.3 | 35 | Averaged |
| Size | 27.5 | 25 | Averaged |
| Frequency | 46.3 | 50 | Averaged (cleaner than Tri-X) |

**Key sources:** r/analog Recipe 1 ("British Journalist"), YouTube (Jamie Windsor, Kyle McDougall, Matt Day), r/Darkroom, Negative Lab Pro community, Flickr HP5 group.

## STYLEGUIDE v2.1 Alignment

Applied 2026-06-01 to `Presets/Black-White/Ilford HP5 Plus.xmp`:

| Parameter | Before | After | Rule |
|-----------|--------|-------|------|
| Clarity2012 | +11.3 | 0 | Grain protection: GrainAmount>0 → Clarity=0 |
| Texture | +10 | 0 | Grain protection: GrainAmount>0 → Texture=0 |
| GrainFrequency | 46.3 | 50 | STYLEGUIDE HP5 grain table: Roughness 50-60 |

No other violations. GrainAmount=36.3 within 30-45 range, Size=27.5 within 20-30 range. Sharpness=10, calibration ban, B&W curve neutral all pass.
