# Kodak Portra 400NC — Full Aesthetic Characteristics for Lightroom Presets

> "Natural Color" at 400 speed — the most accurate, neutral 400-speed color negative film ever made. Discontinued in 2010.

---

## Executive Summary

Kodak Portra 400NC was the "Natural Color" variant of Portra 400, paired with 400VC ("Vivid Color"). Where standard Portra 400 is known for warmth, 400NC prioritized **colorimetric accuracy and neutral rendering**. It was the choice for commercial catalog work, art reproduction, and photographers who wanted Portra's latitude and grain structure without Portra's characteristic warm-amber bias. Both NC and VC were retired when Kodak unified Portra in 2010. This document serves as a reference for creating a Lightroom preset that emulates Portra 400NC.

---

## 1. The Color Palette

| Color Region | Portra 400NC Behavior |
|---|---|
| **Skin Tones** | Very neutral, accurate. Not the warm golden Portra 400 signature. |
| **Whites / Highlights** | Pure, neutral white. No warm cream cast. |
| **Greens** | Natural, accurate. Less yellow-olive shift than standard Portra 400. |
| **Blues** | Accurate rendering. Sky tones stay natural, not warm-shifted. |
| **Reds** | Muted, accurate. Lower saturation than standard Portra 400. |
| **Shadows** | Open, neutral-cool. Less amber warmth than standard. |
| **Overall** | Cooler, cleaner, more clinical than standard Portra 400. |

---

## 2. Contrast & Tonality

- **Low contrast** (lower than standard Portra 400's moderate contrast)
- Very long tonal scale — maximum shadow and highlight detail
- Designed for flat, accurate reproduction (scanning-friendly)
- Overexposure latitude comparable to standard Portra 400 (+3 stops)

---

## 3. Grain Structure

- **RMS ~6** — very fine for 400-speed film (slightly finer than standard Portra 400 at RMS 8)
- Excellent grain structure maintained through overexposure

---

## 4. Comparison: Portra 400NC vs Portra Family

| Aspect | 400NC | 400 (current) | 400VC | 800 |
|---|---|---|---|---|
| **Contrast** | Low | Moderate | Moderate-High | Moderate-High |
| **Saturation** | Lowest | Moderate | Higher | Higher |
| **Color bias** | Neutral | Warm | Vivid-warm | Warm |
| **Skin** | Most accurate | Warm-flattering | Warm-vibrant | Warm-flattering |
| **Best for** | Commercial, reproduction | Universal | Punchy color | Low-light |

---

## 5. Digital Emulation Targets

1. Lower contrast than standard Portra 400 (Contrast -12 vs -7.5)
2. More desaturated overall (Sat -15 vs -10 in standard)
3. Neutral color balance — cooler than standard Portra 400
4. Similar highlight latitude to standard Portra 400 (-55)
5. Open, neutral shadows without warm cast
6. Fine grain (Amount 22, Size 25)

---

## Sources

- t3mujinpack GitHub — Kodak Portra 400 NC Darktable preset
- Kodak Professional product literature (archived)
- r/AnalogCommunity — Portra NC discussion threads

---

## See Also

For related Lightroom presets and film stock references:

- [Kodak Portra 160NC](../Kodak-Portra-160NC/characteristics.md)
- [Kodak Portra 400VC](../Kodak-Portra-400VC/characteristics.md)
- [Kodak Portra 400](../Kodak-Portra-400/characteristics.md)
- [Kodak Portra 400UC](../Kodak-Portra-400UC/characteristics.md)
- [Kodak Portra 160VC](../Kodak-Portra-160VC/characteristics.md)
- [Kodak Portra 160](../Kodak-Portra-160/characteristics.md)
- [Kodak Portra 800](../Kodak-Portra-800/characteristics.md)
- [Kodak Gold 200](../Kodak-Gold-200/characteristics.md)
- [Kodak Ektar 100](../Kodak-Ektar-100/characteristics.md)
- [Kodak Ultramax 400](../Kodak-Ultramax-400/characteristics.md)
- [Fujifilm Pro 400H](../Fujifilm-Pro-400H/characteristics.md)
