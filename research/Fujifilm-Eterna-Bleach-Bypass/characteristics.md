# Fujifilm Eterna Bleach Bypass — Characteristics for Lightroom Presets

## Process Profile
- **Type:** Silver retention cinema process (bleach bypass on Eterna stock) This document serves as a reference for creating a Lightroom preset that emulates Eterna Bleach Bypass.
- **Base stock:** Fujifilm Eterna color negative cinema film
- **Process:** C-41 development with bleach step skipped → silver retained in emulsion
- **Status:** Specialty lab process (not standard)

## Aesthetic Character
- **Primary:** High-contrast, heavily desaturated, gritty cinema look with metallic silver highlights
- **Contrast:** Very high — silver retention dramatically increases density range
- **Saturation:** Heavily desaturated — silver masks dye clouds, reducing color purity by 40-60%
- **Blacks:** Deep, rich — silver in shadows creates true "blacker than black" density
- **Highlights:** Metallic sheen — retained silver reflects light, creating specular character
- **Skin tones:** Desaturated, porcelain-like, slightly cool
- **Greens:** Muted to near-gray
- **Blues:** Retained more than other channels — silver interacts least with blue dye layer
- **Grain:** Pronounced, gritty — silver particles add visible grain structure
- **Overall vibe:** War cinema, dystopian sci-fi, high-fashion editorial, music video noir

## Comparison: Eterna BB vs Standard Bleach Bypass
| Aspect | Eterna Bleach Bypass | Standard Bleach Bypass |
|---|---|---|
| Base stock contrast | Lower native contrast | Can be any stock |
| Color palette | Warmer Eterna base bleeds through | Colder, more neutral |
| Grain character | Finer, more even | Depends on stock |
| Silver retention effect | More subtle metallic | Stronger metallic |
| Best for | Fashion, urban, cinematic | War films, gritty documentary |

## Notable Films Using Bleach Bypass
- Saving Private Ryan (ENR process on Kodak stock)
- Seven (bleach bypass on selected scenes)
- Minority Report (bleach bypass + desaturation)
- Fight Club (selected scenes)

## Lightroom Translation Source
- **Base:** Fujifilm Eterna stock characteristics + bleach bypass processing effects
- **Key moves:** Extreme contrast, heavy HSL desaturation, metallic color grading, coarse grain
- **Translation date:** 2026-06-01

---

## See Also

For related Lightroom presets and film stock references:

- [Fujifilm Eterna](../Fujifilm-Eterna/characteristics.md)
- [Fujifilm Classic Negative](../Fujifilm-Classic-Negative/characteristics.md)

## Validation Sweep 2026-10-21
- **Verdict:** accurate
- **Defining traits checked:** (1) silver-retention contrast — Contrast +55, Highlights -60, Shadows -20, Whites +10, Exposure -0.50; (2) heavy desaturation with blue least affected — Saturation -20 / Vibrance -15 plus per-channel Red -25, Orange -20, Yellow -30, Green -35, Aqua -40, Blue -15, Purple -30, Magenta -35; (3) Eterna's warmer base — Highlight H50/S5, Shadow H220/S12, Grain 40/35/60.
- **Minor drift:** the research promises "inky, blacker-than-black" density, but Blacks is 0 and the house curve lifts the floor to output 20, so the shadows read filmic rather than blocked. Left alone — the Eterna variant is explicitly the softer, lower-contrast member of the bleach-bypass family.
- **Sources:** Kodak processing-tech note (silver retention: higher contrast, lower saturation, denser shadows); finalcolor.com bleach-bypass primer; Fujifilm Eterna stock notes (low native contrast, warm base); research/community-recipes.
- **Preset adjustments:** none.
