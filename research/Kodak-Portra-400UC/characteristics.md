# Kodak Portra 400UC / 400VC — Full Aesthetic Characteristics for Lightroom Presets

> "Ultra Color" / "Vivid Color" — Portra 400 with the saturation turned up. The choice for fashion, editorial, and vibrant commercial work.

---

## Executive Summary

Kodak Portra 400UC ("Ultra Color," later renamed 400VC "Vivid Color") was the higher-saturation variant of Portra 400. Where 400NC aimed for neutral accuracy, 400UC delivered **bold, saturated colors while retaining Portra's legendary skin tone handling**. It was the go-to for fashion editorial, vibrant travel photography, and any work where color needed to "pop" without looking like consumer film. Discontinued when Kodak unified Portra in 2010; the closest current equivalent is Portra 800 (which has higher saturation) or Ektar 100 (significantly more saturated). This document serves as a reference for creating a Lightroom preset that emulates Portra 400UC.

---

## 1. The Color Palette

| Color Region | Portra 400UC Behavior |
|---|---|
| **Skin Tones** | Warm, vibrant — still flattering but more saturated than standard Portra. |
| **Whites / Highlights** | Clean, warm-tending. Highlight roll-off preserves color saturation. |
| **Greens** | Rich, full greens. More saturation than standard Portra — foliage pops. |
| **Blues** | Deep, rich blues. Skies are dramatic, not pastel. |
| **Reds** | Rich, saturated reds — bold without oversaturation. |
| **Yellows** | Warm, golden, saturated. |
| **Shadows** | Warm-tending, rich. Not neutral/cool. |
| **Overall** | Portra skin handling + elevated global saturation = "editorial pop." |

---

## 2. Contrast & Tonality

- **Moderate contrast** — similar to standard Portra 400
- Clean highlight roll-off with retained color
- Shadow detail preserved despite increased color density
- The contrast curve is similar to standard Portra 400 — the saturation is the differentiator

---

## 3. Grain Structure

- **RMS ~7–8** — similar to standard Portra 400
- Fine, even grain structure
- Slightly more visible than NC variants (color density makes grain slightly more apparent)

---

## 4. Comparison: Portra 400UC vs Portra Family

| Aspect | 400UC/VC | 400 (current) | 400NC | Ektar 100 |
|---|---|---|---|---|
| **Saturation** | High | Moderate | Low | Very High |
| **Contrast** | Moderate | Moderate | Low | High |
| **Skin tones** | Warm-vibrant | Warm-flattering | Neutral | Red-heavy |
| **Color bias** | Saturated-warm | Warm | Neutral | Punchy-warm |
| **Best for** | Fashion, editorial | Universal | Commercial/accurate | Landscape |

---

## 5. Digital Emulation Targets

1. Higher saturation than standard Portra 400 (Sat +10 vs 0)
2. Retain Portra highlight latitude (-55 Highlights)
3. Warm color bias, more saturated than standard
4. Richer blues and reds — less desaturation in HSL
5. Standard Portra grain (Amount 25)
6. Warm, saturated shadows with retained detail

---

## Sources

- t3mujinpack GitHub — Kodak Portra 400 UC + 400 VC Darktable presets
- Kodak Professional product literature (archived)
- r/AnalogCommunity — Portra UC/VC discussion

---

## See Also

For related Lightroom presets and film stock references:

- [Kodak Portra 160NC](../Kodak-Portra-160NC/characteristics.md)
- [Kodak Portra 400VC](../Kodak-Portra-400VC/characteristics.md)
- [Kodak Portra 400](../Kodak-Portra-400/characteristics.md)
- [Kodak Portra 400NC](../Kodak-Portra-400NC/characteristics.md)
- [Kodak Portra 160VC](../Kodak-Portra-160VC/characteristics.md)
- [Kodak Portra 160](../Kodak-Portra-160/characteristics.md)
- [Kodak Portra 800](../Kodak-Portra-800/characteristics.md)
- [Kodak Gold 200](../Kodak-Gold-200/characteristics.md)
- [Kodak Ektar 100](../Kodak-Ektar-100/characteristics.md)
- [Kodak Ultramax 400](../Kodak-Ultramax-400/characteristics.md)
- [Fujifilm Pro 400H](../Fujifilm-Pro-400H/characteristics.md)
