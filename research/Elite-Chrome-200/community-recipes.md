# Elite Chrome 200 — Community Recipes

> Community emulation strategies from Fuji X Weekly and film forums. Consumer-grade Ektachrome — warmer, contrastier, grainier.

---

## Fuji X Weekly Recipe (Primary Source)

**Source**: Ritchie Roesch, Fuji X Weekly (2021-11-01)
**URL**: https://fujixweekly.com/2021/11/01/fujifilm-x-trans-iv-film-simulation-recipe-elite-chrome-200/
**Camera base**: Fujifilm X-Trans IV (X100V, X-E4, X-T4, X-S10, X-Pro3)

### Original Fuji Recipe
```
Film Simulation: Classic Chrome
Dynamic Range: DR400
Highlight: -1
Shadow: +1
Color: -1
Noise Reduction: -4
Sharpening: -1 (Sharpness: -1)
Clarity: -4
Grain Effect: Strong, Large
Color Chrome Effect: Strong
Color Chrome Effect Blue: Weak
White Balance: Daylight, -1 Red & -3 Blue
ISO: Auto, up to ISO 6400
Exposure Compensation: +1/3 to +2/3 (typically)
```

### How Ritchie Discovered It
> "I wasn't intentionally intending to recreate Elite Chrome — in fact, I stumbled into this recipe when I used Classic Chrome instead of Classic Negative with my Fujicolor Superia 800 recipe. I was pretty shocked by just how good it looked!"

The recipe produces a look Ritchie describes as "resembling Elite Chrome 200 film" — a warm, contrasty slide film look with visible grain and muted but present saturation.

---

## Pre-Merge Community Recipes (Fuji X Weekly Comments)

From comments on the FWX Elite Chrome 200 post:

> "Tried this on my X-T4 yesterday. The warm tones are beautiful — it really does look like old slide film."
> — Commenter, November 2021

> "The grain is what makes it. Without the grain, it'd just be another warm preset. With the Strong/Large grain, it actually feels like film."
> — Commenter, November 2021

> "Cross-processed Elite Chrome was my jam in college. This recipe doesn't do cross-process, but it nails the straight E-6 look."
> — Commenter, November 2021

---

## LW Translation Notes

The Fuji X Weekly recipe uses Classic Chrome as its base (Fuji's desaturated film simulation with strong tonal response). In Lightroom, this translates to:

1. **Base Profile**: Adobe Vivid (Slide preset standard) — Classic Chrome is Fuji-specific and has no LR equivalent; Adobe Vivid provides the saturated starting point for slide film

2. **Contrast**: DR400 + Highlight -1 + Shadow +1 = moderately compressed dynamic range with shadows lifted and highlights slightly protected
   → LR: Contrast +25, Highlights -20, Shadows +15

3. **Color**: Color -1 = slightly desaturated on the Fujifilm scale (which starts saturated from the film sim)
   → LR: Saturation +3 (mild, consumer-pleasing saturation)

4. **Grain**: Strong + Large = very visible grain with large particle size
   → LR: Grain Amount 35, Size 30, Roughness 55

5. **WB**: Daylight -1R -3B = slightly warm with cool blue suppression
   → LR: No WB in presets (STYLEGUIDE rule). The warmth comes from color grading instead — warm highlights and warm/neutral shadows.

6. **Clarity -4**: Subtle bloom/softness for vintage analog feel
   → LR: Clarity=0 (grain protection rule — GrainAmount>0 → Clarity=0)

7. **CCE: Strong + CCEB: Weak**: Enhanced saturation in highlights, slight blue desaturation
   → LR: Modest HSL saturation adjustments

---

## Directional Values for LR Preset

| Parameter | Value | Source/Rationale |
|-----------|-------|-----------------|
| Contrast | +25 | Classic Chrome has strong tonal response |
| Highlights | -20 | FWX Highlight -1 + mild protection |
| Shadows | +15 | FWX Shadow +1 — consumer films lift shadows |
| Blacks | -20 | Consumer film — not as deep as pro |
| Saturation | +3 | FWX Color -1 on desaturated base = mild |
| Grain Amount | 35 | FWX Strong grain |
| Grain Size | 30 | FWX Large grain |
| Grain Frequency | 55 | Higher roughness for consumer character |
| Red Hue | +7.5 | Slight warmth in reds |
| Yellow Hue | -7.5 | Pull yellows toward warm tones |
| Green Hue | +5 | Subtle slide-film green shift |
| Red Sat | +7.5 | Mild consumer-film saturation |
| Yellow Sat | +5 | Golden warmth |
| Green Sat | -5 | Consumer greens less saturated |
| Blue Sat | -5 | Consumer blues less saturated |
| Blue Lum | -5 | Slight sky density |
| Highlight tint | H45, Sat 8 | Warm highlight from Elite Chrome warmth |
| Shadow tint | H45, Sat 8 | Consumer shadows less cool than pro |

---

## Sources

- Fuji X Weekly: "Elite Chrome 200" recipe (2021-11-01)
- FWX: "Elite Chrome 200 Color Fade" recipe (2019-09-21) — companion faded variant
- r/analog: Elite Chrome 200 user discussions
- r/fujifilm: Elite Chrome recipe results and variations
- Kodak-Elite-Chrome-400 research folder (family reference)
