# Fuji 100 Industrial — Lightroom Preset Settings & Recipes

> Compiled from Fuji X Weekly (Ritchie Roesch, Jun 2019), Japanese photography forums, and Reddit (r/analog, r/fujifilm). Japan domestic-market-only film with a unique tungsten-balanced emulsion.

---

## Fuji X Weekly Recipe (Jun 2019)

**Source**: `https://fujixweekly.com/2019/06/13/my-fujifilm-x-t30-fujicolor-100-industrial-film-simulation-recipe/`

One of Fuji X Weekly's earliest film simulation recipes. Created on Fujifilm X-T30.

```
Film Simulation: PRO Neg. Std
Dynamic Range: DR400
Highlight: +1
Shadow: +2
Color: +1
Color Chrome Effect: Weak
Sharpening: +2
Noise Reduction: -4
Grain Effect: Weak
White Balance: 3200K, +8 Red & -8 Blue
ISO: Auto up to ISO 6400
Exposure Compensation: +1/3 to +2/3 (typically)
```

### Translation to Lightroom Concepts

| Fuji Setting | Lightroom Approximate |
|-------------|----------------------|
| PRO Neg. Std base | Neutral, flat contrast rendering |
| Highlight +1 | Slightly lifted highlights (+15) |
| Shadow +2 | Lifted shadows (+25) |
| Color +1 | Mild saturation (+3) |
| WB 3200K +8R -8B | Cool tungsten with strong red tint (defining characteristic) |
| Sharpening +2 | Moderate sharpening |
| Grain: Weak | Ultra-fine grain (Amount 12-15) |
| DR400 | Extended dynamic range |
| EC +1/3 to +2/3 | Slight overexposure (+0.50) |

### The WB 3200K +8R -8B Anomaly

The defining characteristic of Fuji 100 Industrial is its tungsten-balanced emulsion (3200K) with daylight-shifted dyes. The +8 Red shift on a 3200K base creates a unique color signature:
- **Strong cool-blue cast** from the 3200K base temperature
- **Red channel boost** from +8 Red to offset the cool cast
- **Blue suppression** from -8 Blue to control excess cool tones
- **Net result**: Cool-neutral balance with subtle red warmth in specific channels

This is fundamentally different from a simple WB adjustment — it's emulating a specific emulsion chemistry design.

## Community Consensus

### Defining Characteristics
1. **Unique color balance** — neither warm nor cold; cool-neutral with subtle red warmth
2. **Ultra-clean** — ISO 100 with essentially zero visible grain
3. **Mild in every dimension** — low saturation, low contrast, gentle tones
4. **Higher contrast scenes preferred** — the recipe "needs the right subject and light to stand out"
5. **Japanese convenience store aesthetic** — the look of budget-friendly Japanese domestic film

### Ritchie Roesch's Notes
"I find that this recipe is especially good in higher-contrast scenes, although it can still deliver interesting results in lower-contrast scenes. It's a milder recipe that doesn't have a lot of saturation... It creates lovely pictures that are soft and not bold."

### Lightroom Community Values

From Reddit and community discussions:

```
Exposure: +0.35 to +0.65
Contrast: -8 to -15 (mildly flat)
Highlights: +10 to +20 (lifted, not protected)
Shadows: +20 to +30 (lifted)
Blacks: +5 to +12
Saturation: 0 to +5 (very mild)
Vibrance: 0 to +3
Color Grading: Subtle cool shadows (Hue 195-210°, Sat 3-5)
Grain: Amount 10-15, Size 12-18 (barely visible)
```

### Key Warning
Community users note: this preset can look too flat on low-contrast scenes. The recipe works best with strong directional light, urban environments, and scenes with natural contrast. "It needs the right subject and light to stand out."

## Source Attribution

- **Fuji X Weekly**: Primary recipe source (Ritchie Roesch, Jun 13, 2019)
- **Japanese photography blogs**: Fujicolor 100 Industrial usage guides
- **Reddit r/fujifilm**: User experiences and sample images
- **Flickr**: Fujicolor 100 Industrial sample galleries

---

*Compiled June 2026 from Fuji X Weekly, Japanese photography communities, and Reddit data.*

---

## See Also

- [Fuji 100 Industrial — Film Characteristics](../Fuji-100-Industrial/characteristics.md)
- [Kodak ColorPlus 200 Lightroom Preset](../Kodak-ColorPlus-200/community-recipes.md)
- [Fuji Superia 200 Lightroom Preset](../Fuji-Superia-200/community-recipes.md)
- [XMP Preset: Fuji 100 Industrial](../../Presets/Color-Negative/Fuji 100 Industrial.xmp)
