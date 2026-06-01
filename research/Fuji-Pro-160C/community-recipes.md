# Fuji Pro 160C — Community Recipes

> Two Fuji X Weekly PRO Negative 160C recipes, plus t3mujinpack Darktable reference.

---

## 1. Fuji X Weekly — PRO Negative 160C X-Trans IV/V (Mar 2024)

Source: `fujixweekly.com/2024/03/28/pro-negative-160c-film-simulation-recipe-for-fujifilm-x-trans-iv-x-trans-v/`

By Ritchie Roesch, using PRO Neg. Hi (paired with Reala Ace X100VI version):
- FilmSim: PRO Neg. Hi, DR400, Grain Weak Small, Color Chrome Strong, CCB Weak
- WB: Auto, +1 Red, -3 Blue
- HL: +0.5, SH: -1.5, Color: +4, Sharpness: -1, Clarity: -2
- NR: -4, ISO: Auto up to 6400
- Exposure Comp: 0 to +2/3

---

## 2. Fuji X Weekly — Film Dial "Fujicolor PRO 160C Warm" (May 2024)

Source: `fujixweekly.com/2024/05/16/fujifilm-x-t50-film-dial-settings-14-new-film-simulation-recipes-yes-14/`

Uses Reala Ace film simulation:
- FilmSim: Reala Ace, DR400, Grain Weak Small, Color Chrome Strong, CCB Weak
- WB: Auto White Priority, +2 Red, -4 Blue
- HL: -1.5, SH: -1, Color: +3, Sharpness: -1, Clarity: -2

---

## 3. t3mujinpack Darktable Preset

The t3mujinpack project includes Fuji Pro 160C as a Darktable style using Lab tone curves for color manipulation. Available at `github.com/t3mujinpack/t3mujinpack`.

---

## Fuji→LR Translation (X-Trans IV/V PRO Neg. Hi version)

| Fuji Parameter | Fuji Value | LR Attribute | LR Value |
|---|---|---|---|
| Highlight | +0.5 | Highlights2012 | -5 (DR400 offset applied) |
| Shadow | -1.5 | Shadows2012 | +15 (inverted) |
| Color | +4 | Saturation | +20 |
| Grain Weak Small | — | GrainAmount/Size | 15/15 |
| Sharpness | -1 | Sharpness | 10 (grain cap) |
| Clarity | -2 | Clarity2012 | 0 (must be 0 with grain) |
| Color Chrome Strong | — | Vibrance | +5 (approximated) |

---

## STYLEGUIDE Compliance Notes

- No Calibration (Commandment #3)
- No WB (Commandment #4)
- Grain → Sharpness=10, Clarity=0, Texture=0, Dehaze=0 (Commandment #7)
- |Vibrance−Saturation| ≤ 5 (Commandment #5) — Sat=+20, Vib=+17 (gap=3)
- HSL Sat ≤ ±60 (Commandment #6)

---

## Sources

- Fuji X Weekly — PRO Negative 160C X-Trans IV/V (Mar 2024)
- Fuji X Weekly — X-T50 Film Dial (May 2024)
- t3mujinpack GitHub — Fuji Pro 160C Darktable preset
