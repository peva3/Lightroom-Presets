# Kodachrome 64 — Community Recipes for Lightroom Emulation

## Overview

Kodachrome 64 is the most-requested film emulation in the digital photography community. Unlike E-6 films (Velvia, Provia, Ektachrome) which have dye couplers *in* the emulsion, Kodachrome's dyes were formed *during processing* in the K-14 developer solutions. This fundamental difference means no existing film simulation can perfectly replicate it — digital emulations can only approximate the final visual result, not the chemical pathway.

The community consensus: **profile-based approaches** (ICC/LUT-based) get closer than slider-based approaches, but neither fully captures the Kodachrome "look."

---

## Common Lightroom Adjustment Patterns

These are recurring adjustments reported across forums (r/analog, r/Lightroom, fredmiranda.com, dpreview) by users attempting manual Kodachrome emulation:

### Base Tone Curve Adjustments

```
Highlights:  -10 to -20  (compensate for slide film's high contrast)
Shadows:     +15 to +30  (lift blacks slightly — Kodachrome shadows are deep but not crushed)
Whites:      -5 to -15   (slide film doesn't have pure digital white)
Blacks:      -20 to -30  (deepen blacks for slide-film density)
Clarity:     0 to -10    (slight negative clarity for mid-century softness)
Dehaze:      +5 to +15   (adds midtone contrast, Kodachrome-like structure)
```

### Color Adjustments — The "Kodachrome Blue" Sky

The most iconic characteristic is the rendering of blue skies. Users describe it as a **deep cyan-leaning blue** — not teal, not navy, but a "3D depth blue" that Velvia cannot reproduce.

```
HSL / Color Mixer:
  Blue Hue:        -5 to -15   (shift toward cyan — Kodachrome blues are cool, not purple)
  Blue Saturation: +10 to +25  (rich but not Velvia-electric)
  Blue Luminance:  -10 to -20  (darken skies — Kodachrome renders skies deep)
  Aqua Saturation: +10 to +20  (reinforce the blue-cyan transition)
```

### Deep Rich Reds

Kodachrome reds are famously deep, warm, and slightly orange-biased — never magenta.

```
HSL / Color Mixer:
  Red Hue:         +5 to +15   (slight shift toward orange)
  Red Saturation:  +15 to +30  (rich but maintain detail)
  Red Luminance:   -5 to -15   (deepen without going maroon)
  Orange Saturation: +10 to +20
```

### Warm-but-Not-Yellow Rendition

Kodachrome renders warm tones (skin, sunsets, gold) with warmth but *without* a yellow cast. This is the hardest aspect to emulate digitally.

```
HSL / Color Mixer:
  Yellow Hue:      0 to -10    (slightly toward orange — suppress greenish yellow)
  Yellow Saturation: -5 to +5  (restrained yellows)
  Green Hue:        +10 to +20 (shift toward yellow-green — 1950s-60s greens)
  Green Saturation: -10 to +10 (Kodachrome greens are natural, not neon)
```

### Cool Shadows / Shadow Color Toning

Kodachrome shadows have a subtle cool-blue cast that contrasts with warm mids/highlights.

```
Split Toning / Color Grading:
  Shadows:  Hue ~210-230°, Saturation ~5-15
  Midtones: Hue ~40-50°, Saturation ~3-8 (very subtle warmth)
  Highlights: Hue ~45-55°, Saturation ~5-10
```

### Calibration Panel (crucial for profile-based starting point)

Many community users argue that the **Camera Calibration panel** is essential:

```
Red Primary:   Hue +10 to +20, Saturation +5 to +15
Green Primary: Hue -5 to +5, Saturation -5 to +5
Blue Primary:  Hue -10 to -20, Saturation +10 to +25
```

---

## YouTube Tutorials & Video Walkthroughs

Common approaches from YouTube creators (searched across 2018-2025):

1. **Tone curve first** — establish slide-film contrast (S-curve, but gentler than Velvia)
2. **WB shift toward warmth** — many start at 5500-5800K with a slight magenta tint (+5 to +10)
3. **HSL is the core** — Kodachrome's palette is defined by its hue relationships, not raw saturation
4. **Grain overlay** — many add scanned grain from actual Kodachrome frames for authenticity

---

## The "McCurry Approach"

Steve McCurry's Afghan Girl (1984) was shot on Kodachrome 64. Community observers note the Kodachrome in McCurry's National Geographic work produces:

- Olive-green vegetation (not emerald)
- Skin tones with a slight coral warmth
- Sky rendered as a medium-deep cyan blue
- Reds that are deep and blood-like, not orange nor magenta
- Overall impression of "realism with presence" — not hyper-digital clarity

---

## Known Preset Packs & Emulation Strategies

### Alex Ruskman's Kodachrome Pack

Often cited on Reddit and YouTube as one of the more accurate community-developed Kodachrome preset sets. Reported characteristics:

- Uses Adobe Camera Profiles (.dcp) as a foundation
- Multiple variants for different lighting conditions (Direct Sun, Overcast, Flash, Tungsten)
- Includes a "Kodachrome 64 Faded" variant simulating slightly aged slides
- Sold through his website (alexruskman.com) — pricing typically $25-45 USD
- Approach: camera-profiled starting point + adjustment layers that preserve color relationships

### DIY Profile Method (Advanced Users)

A method described on forums for creating custom Kodachrome profiles:

1. Scan actual Kodachrome 64 slides using a calibrated scanner with Kodachrome ICC profiles (SilverFast Kodachrome mode)
2. Photograph an IT8 target on your digital camera under same lighting
3. Use Adobe DNG Profile Editor or Lumariver Profile Designer to match the digital camera's color response to the scanned Kodachrome
4. Save as a custom .dcp camera profile
5. Apply as a Lightroom profile — then fine-tune with sliders

This yields the most accurate results but requires access to well-preserved Kodachrome slides and specialized software.

---

## Reddit / Forum Wisdom (Compiled)

From r/analog, r/Lightroom, fredmiranda.com, rangefinderforum.com:

> "Kodachrome 64 is the one film that's legitimately impossible to replicate. You can get 90% there with profiles, but that last 10% is the dye chemistry." — u/analog_dreamer, r/analog

> "The blues are the giveaway. If your preset makes skies look teal or purple, you've missed. Kodachrome blue is neither — it's a deep, cool cyan that feels almost 3D." — Fred Miranda forums

> "I've tried every Kodachrome preset on the market. RNI gets closest on blues. Alex Ruskman gets closest on reds. Neither nails the skin tones." — dpreview forums

> "The secret to Kodachrome emulation isn't saturation — it's the hue relationships between blue/cyan, red/orange, and green/yellow. You have to shift hues, not just boost sat." — r/Lightroom

> "Ektachrome E100 is the closest living film stock to Kodachrome 64 if you slightly cool the WB. But it's still an E-6 film with couplers in the emulsion. It will never have that Kodachrome 'depth.'" — rangefinderforum.com

---

## Summary of Key Recipe Elements

| Element | Direction | Notes |
|---|---|---|
| **White Balance** | 5400-5800K, +5 Magenta | Slightly warm but not yellow |
| **Tone Curve** | S-curve, softer than Velvia | Slide contrast without clipping |
| **Blues** | Hue -10, Sat +15, Lum -15 | "Kodachrome blue" — cyan-leaning deep blue |
| **Reds** | Hue +10, Sat +20, Lum -10 | Deep rich red with orange bias |
| **Yellows** | Hue -5, Sat ±0 | Not yellow — warm but restrained |
| **Greens** | Hue +15, Sat -5 | Olive-green bias, not emerald |
| **Shadow tint** | Cool blue (~220°), Sat ~10 | Cool shadows signature |
| **Grain** | 25-35 strength, 50 roughness | Optional: scanned Kodachrome grain overlay |
