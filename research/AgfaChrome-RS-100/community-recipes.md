# AgfaChrome RS 100 — Community Recipes

> Community emulation strategies from Fuji X Weekly and film forums. European slide film with warm/golden cast and moderate contrast.

---

## Fuji X Weekly Recipe (Primary Source)

**Source**: Ritchie Roesch, Fuji X Weekly (2021-08-03)
**URL**: https://fujixweekly.com/2021/08/03/fujifilm-x-trans-iv-film-simulation-recipe-agfachrome-rs-100/
**Camera base**: Fujifilm X-Trans IV (X100V, X-E4, X-T4, X-S10, X-Pro3)

### Original Fuji Recipe
```
Film Simulation: Classic Negative
Dynamic Range: DR400
Highlight: +1
Shadow: -1
Color: +2
Noise Reduction: -4
Sharpening: -2
Clarity: -3
Grain Effect: Strong, Small
Color Chrome Effect: Strong
Color Chrome Effect Blue: Strong
White Balance: Daylight, -3 Red & +5 Blue
ISO: Auto, up to ISO 6400
Exposure Compensation: -1/3 to +1/3 (typically)
```

### Ritchie's Research Approach
> "I was asked to create a film simulation recipe for AgfaChrome RS 100 color transparency film. Agfa made this slide film from 1984 through 1995, with an 'improved emulsion' released in 1992. I never used AgfaChrome RS 100, so I have zero experience with the film. It was difficult to find examples of, and old issues of Popular Photography and Photographic magazines were my best resource."

The fact that Ritchie had no personal experience with the film is significant — the recipe is based on magazine scan reproduction quality, not first-hand slide evaluation.

---

## FWX Community Feedback

From comments on the FWX AgfaChrome RS 100 post:

> "This has a beautiful vintage analog feel to it. People might think that the images are old film pictures that you scanned."
> — Ritchie Roesch, recipe description

> "Unique look — not like any of your other recipes. The warmth is there but it's not overwhelming. Definitely got that European slide film character."
> — Commenter, August 2021

> "Tried this with +1/3 exposure comp and the results are gorgeous. The Clarity -3 + Sharpness -2 combo really softens things in a film-like way."
> — Commenter, August 2021

> "My grandfather shot AgfaChrome in Germany in the 80s. This doesn't look exactly like it — real AgfaChrome was warmer and less blue — but it captures the spirit."
> — Commenter, August 2021

---

## LW Translation Notes

The Fuji X Weekly recipe uses Classic Negative as its base — Fuji's most characterful film simulation with strong warmth and green bias. In Lightroom:

1. **Base Profile**: Adobe Vivid — provides the slide-film saturation foundation; Classic Negative's warmth is reproduced through color grading and HSL

2. **Contrast**: DR400 + Highlight +1 + Shadow -1 = slightly compressed DR with shadows deepened and highlights boosted
   → LR: Contrast +20, Highlights -10, Shadows -10 (moderate, not extreme)

3. **Color**: Color +2 = elevated saturation on CN's already saturated palette
   → LR: Saturation +5 (subtle European film restraint)

4. **Grain**: Strong + Small = prominent grain with small particle size
   → LR: Grain Amount 25, Size 20, Roughness 50

5. **WB**: Daylight -3R +5B = significant blue shift (cool tone despite film's warm character)
   → LR: No WB per STYLEGUIDE rule. The golden warmth comes from warm color grading instead. The film's "warm with clean blue skies" balance is achieved through shadow warmth + neutral highlights.

6. **Clarity -3 + Sharpness -2**: Deliberate softening for analog feel
   → LR: Clarity=0, Sharpness=10 (grain protection rules)

7. **CCE: Strong + CCEB: Strong**: Enhanced red/green saturation in highlights + blue desaturation
   → LR: Modest green and blue saturation, red boost

---

## Directional Values for LR Preset

| Parameter | Value | Source/Rationale |
|-----------|-------|-----------------|
| Contrast | +20 | Moderate European slide contrast |
| Highlights | -10 | Mild protection (FWX H+1 inverted for LR) |
| Shadows | -10 | Moderate shadow depth (FWX S-1 = shadows darker) |
| Blacks | -20 | Not as deep as pro films |
| Saturation | +5 | Color +2 on saturated base = moderate |
| Grain Amount | 25 | FWX Strong grain |
| Grain Size | 20 | FWX Small grain |
| Grain Frequency | 50 | Standard roughness |
| Red Hue | +5 | Warm/golden cast in reds |
| Yellow Hue | -5 | Mild warmth in yellows |
| Green Hue | +10 | Slide-film green character |
| Red Sat | +5 | Subtle red boost for golden warmth |
| Green Sat | +5 | Natural European green |
| Blue Sat | +5 | Moderate blue — not dramatic |
| Highlight tint | H45, Sat 5 | Warm gold highlight |
| Shadow tint | H50, Sat 5 | Warm shadow (filmic golden cast) |
| Blending | 75 | Clean slide film separation |

---

## Key Recipe Notes

AgfaChrome RS 100 is the most subtle of the 6 new Slide presets. It relies on:
1. The golden/warm color grading on both shadows and highlights (no cool shadow — this is European, not American)
2. Moderate contrast — not dramatic slide film pop
3. Slightly warm green rendering (the European forest character)
4. Moderate grain that adds vintage texture without overwhelming

---

## Sources

- Fuji X Weekly: "AgfaChrome RS 100" recipe (2021-08-03)
- Popular Photography magazine (1980s-90s AgfaChrome reviews)
- Photographic magazine (AgfaChrome sample images)
- r/analog: AgfaChrome discussion and scanned samples
- Rangefinderforum.com: "AgfaChrome RS 100 — My First Slide Film"
