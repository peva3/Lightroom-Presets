# Fujifilm Nostalgic Negative — Characteristics for Lightroom Presets

## Film Simulation Profile
- **Type:** Digital film simulation (Fujifilm X-T5 / X-Trans V) This document serves as a reference for creating a Lightroom preset that emulates Nostalgic Negative.
- **Based on:** Classic photo album aesthetic — 1960s-70s American color snapshot
- **Introduced:** 2022 (X-T5, X-H2, X-H2S)
- **Status:** Built-in Fujifilm film simulation

## Aesthetic Character
- **Primary:** Warm, amber-toned vintage color negative look with classic photo album feel
- **Contrast:** Low to moderate — soft tonal transitions like aged prints
- **Saturation:** Moderate — not desaturated, but warm-toned saturation
- **White balance:** Amber/golden cast (Auto +5R -1B in Nostalgic Air recipe)
- **Skin tones:** Warm, slightly amber — flattering vintage portrait look
- **Greens:** Amber-green — warm olive rather than cool green
- **Blues:** Muted, slightly warm-leaning
- **Shadows:** Gentle, open — no harsh black crush
- **Highlights:** Soft, compressed — slight warmth
- **Overall vibe:** 1970s family photo album, vintage wedding, golden hour nostalgia, Kodak Instamatic era

## Technical Notes
- Nostalgic Negative is Fujifilm's "amber era" film simulation — distinct from Classic Negative's "Superia era"
- The amber cast is baked into the color matrix, not just white balance
- Grain is prominent in Fuji's rendering — part of the "nostalgic" character
- Differs from Classic Chrome (desaturated) and Classic Negative (higher contrast, cooler)
- Performs best in warm light, golden hour, indoor tungsten-adjacent scenarios

## Comparison to Classic Negative
| Aspect | Nostalgic Negative | Classic Negative |
|---|---|---|
| Era referenced | 1960s-70s | 1990s-2000s |
| Color cast | Amber/golden | Cool/neutral |
| Contrast | Lower | Moderate |
| Saturation | Moderate warm | Moderate neutral |
| Best for | Vintage warmth | Street/documentary |

## Lightroom Translation Source
- **Base:** Fuji X Weekly "Nostalgic Air" recipe
- **Key moves:** Soft contrast, warm color grade, amber-green HSL shifts, moderate grain
- **Translation date:** 2026-06-01

---

## See Also

For related Lightroom presets and film stock references:

- [Fujifilm Classic Negative](../Fujifilm-Classic-Negative/characteristics.md)
- [Fujifilm Pro 400H](../Fujifilm-Pro-400H/characteristics.md)
- [Fuji Astia 100F](../Fuji-Astia-100F/characteristics.md)

---

## Validation Sweep 2026-10-21
- **Verdict:** major miss (corrected)
- **Defining traits checked:** warm amber cast; greens shifted toward yellow/olive (not cyan); gentle open shadows; moderate warm-toned saturation.
- **Sources:** research dossier; fujifilm-x.com Nostalgic Neg. page ("warm amber tones, rich skin in shadow"), jmpeltier Classic Neg vs Nostalgic Neg ("shifts greens toward yellow and adds overall warmth"), veresdenialex ("greens are olive-tinted").
- **Preset adjustments:** `HueAdjustmentGreen +10 -> -10`. In Lightroom's mixer, positive Green Hue moves greens toward Aqua/cyan; the preset was pushing foliage the opposite way from Fuji's documented amber-olive rendering. Warm grades (45/40 deg) and Saturation +15 were already correct for an amber-era simulation.
