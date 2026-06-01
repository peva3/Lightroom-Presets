# Fujicolor Pro 160NS — Community Recipes

> 7 Fuji X Weekly variants by Anders Lindborg, plus Ritchie Roesch's "Fujifilm Negative" recipe and community sources.

---

## 1. Fuji X Weekly — Anders Lindborg's 7-Variant System (May 2021)

Source: `fujixweekly.com/2021/05/24/a-different-approach-7-new-fujicolor-pro-160ns-film-simulation-recipes-yes-7/`

Anders Lindborg created a push/pull system using PRO Neg. Hi as the base. All variants share:
- FilmSim: PRO Neg. Hi
- DR400, Color Chrome Off, Grain Weak, NR -4
- WB: Daylight, 0 Red & 0 Blue
- ISO: Auto up to 6400
- Exposure Comp: varies per variant

### Box Speed
HL: 0, SH: 0, Color: 0, Sharpness: -3

### Pulled -1
HL: -1, SH: -1, Color: 0

### Pulled -2
HL: -2, SH: -1, Color: -1

### Pushed +1
HL: +1, SH: 0, Color: 0

### Pushed +2
HL: +2, SH: 0, Color: +1

### Pushed +3
HL: +2, SH: +1, Color: +2

### Pushed +4
HL: +3, SH: +2, Color: +3, Sharpness: -4

---

## 2. Fuji X Weekly — "Fujifilm Negative" (Oct 2024)

Source: `fujixweekly.com/2024/10/31/fujifilm-negative-fujifilm-x-t5-x-trans-v-film-simulation-recipe/`

By Ritchie Roesch, inspired by Fujicolor PRO 160NS. Uses newer Reala Ace film simulation:
- FilmSim: Reala Ace, DR400, Grain Weak Small, Color Chrome Strong, CCB Off
- WB: 5000K, 0 Red, -2 Blue
- HL: -1, SH: -0.5, Color: +2, Sharpness: -1, Clarity: -2
- NR: -4, ISO: Auto up to 6400
- Exposure Comp: +1/3 to +1

---

## 3. Fuji X Weekly — "Fujicolor PRO 160S" (Film Dial, May 2024)

Source: `fujixweekly.com/2024/05/16/fujifilm-x-t50-film-dial-settings-14-new-film-simulation-recipes-yes-14/`

Uses PRO Neg. Std — described as the closest to 160NS:
- FilmSim: PRO Neg. Std, DR400, Grain Weak Small, Color Chrome Strong, CCB Weak
- WB: Auto White Priority, +2 Red, -4 Blue
- HL: -1.5, SH: -1, Color: +3, Sharpness: -1, Clarity: -2

---

## Fuji→LR Translation for Box Speed

Using the project's Fuji→LR translation mapping:

| Fuji Parameter | Fuji Value | LR Attribute | LR Value |
|---|---|---|---|
| Highlight | 0 | Highlights2012 | -10 (with DR400 offset) |
| Shadow | 0 | Shadows2012 | 0 (inverted from 0=0) |
| Color | 0 | Saturation | 0 |
| Grain Weak | — | GrainAmount | 15 |
| Grain — | Small | GrainSize | 15 |
| Sharpness | -3 | Sharpness | 10 (capped per grain rule) |
| DR400 | — | Highlights2012 | extra -10 |
| Clarity | 0 | Clarity2012 | 0 |

---

## STYLEGUIDE Compliance Notes

- No Calibration (Commandment #3)
- No WB (Commandment #4 — 160NS's cool bias achieved via HSL/ColorGrade, not WB)
- Grain → Sharpness=10, Clarity=0, Texture=0, Dehaze=0 (Commandment #7)
- |Vibrance−Saturation| ≤ 5 (Commandment #5)
- HSL Sat ≤ ±60 (Commandment #6)
- Neutral tone curve 0,0→255,255 (Color-Negative category)

---

## Sources

- Fuji X Weekly — 7 Pro 160NS variants (Anders Lindborg, May 2021)
- Fuji X Weekly — Fujifilm Negative recipe (Ritchie Roesch, Oct 2024)
- Fuji X Weekly — Film Dial Fujicolor PRO 160S (May 2024)
- r/AnalogCommunity and r/Lightroom — Pro 160NS discussions
