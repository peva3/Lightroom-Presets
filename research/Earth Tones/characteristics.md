# Earth Tones Lightroom Preset — Characteristics

**Category**: Decade

The Earth Tones Lightroom preset reproduces the muted brown-green palette of 1970s colour photography and interior design: olive foliage, ochre highlights, warm brown shadows and a global desaturation that keeps everything a step below vivid. It is a warm-golden, low-saturation colour preset with visible grain and a soft vignette, built for flat daylight and tungsten interiors rather than golden hour.

## Historical Context

The 1970s palette has a shopping history. Harvest gold was popular for kitchen and other appliances through the decade, alongside brown, burnt orange and avocado green ([Harvest gold — Wikipedia](https://en.wikipedia.org/wiki/Harvest_gold)); those colours migrated to carpet, laminate, wood veneer panelling and clothing. Earth Day (1970) gave the palette a politics as well as a fashion.

Photography moved the same way for its own reasons. The 1975 *New Topographics* exhibition at George Eastman House, curated by William Jenkins, grouped photographers — Robert Adams, Lewis Baltz, Stephen Shore, Frank Gohlke — who shot the man-altered landscape in flat light and muted colour ([New Topographics](https://en.wikipedia.org/wiki/New_Topographics)). William Eggleston's 1976 MoMA show made ordinary colour subjects legitimate ([Eggleston](https://en.wikipedia.org/wiki/William_Eggleston)). The preset inherits that register: warm, quiet, unglamorous.

## Photographic Technology

- **C-41 arrived in 1972**, superseding C-22 and becoming the standard chromogenic process ([C-41](https://en.wikipedia.org/wiki/C-41_process)). Kodacolor II carried the decade's family photographs; Kodacolor had been Kodak's print film since 1942 ([Kodacolor](https://en.wikipedia.org/wiki/Kodacolor_(still_photography))).
- **Small formats dominated** — 126 Instamatic and 110 cartridges, simple lenses, on-camera flash: low acutance, low micro-contrast, generous depth of field.
- **The prints have aged.** Chromogenic prints are dye images on RC paper, and cyan and yellow fade faster than magenta, so survivors drift warm-magenta and lose blue ([Chromogenic print](https://en.wikipedia.org/wiki/Chromogenic_print)). The preset's blue cut is correct twice: the film was restrained and the print has since lost blue.

## Visual Signature

Brown-orange midtones, olive greens, weak blues, no true white. Green is shifted toward yellow (Hue −20) and desaturated (−25) so foliage reads dusty rather than lush; blue drops 20 points, yellow 10. Only orange is lifted (+5), keeping skin and wood grain alive. Contrast is barely above neutral (+10) and highlights are pulled back (−35), so nothing sparkles. Grain at 25/28/55 is visible at 100%; a −12 vignette closes the frame like an album page.

## Tonal Register

**Register**: warm-golden, low-saturation

Exposure −0.10 with Whites −5 and Blacks −10 puts the image slightly under middle grey, where consumer prints sit. There is no Temperature value: warmth comes entirely from the 45°/8 highlight and 35°/10 shadow grades, so the preset cannot tip into an orange cast on an already-warm file. That makes it stable across registers — but on a cool image the olive shift reads as illness rather than nostalgia, since the greens are pulled toward yellow with nothing warm to anchor them.

## Lighting & Subject Matter

Flat overcast light, fluorescent kitchen tubes, tungsten against wood panelling, open shade. Subject matter is avocado appliances, brown glass, shag carpet, brick, parked cars, suburban sprawl. Hard midday sun fights the look: the palette depends on low contrast.

## Lightroom Translation

| Panel | Value | Function |
|---|---|---|
| Basic | Exposure −0.10, Contrast +10 | Slightly under-exposed consumer print |
| Basic | Highlights −35, Shadows +20 | Holds back window light; keeps panelling detail |
| Basic | Whites −5, Blacks −10 | No specular sparkle; firm but uncrushed floor |
| Presence | Saturation −5 | Global mute — the only global colour control |
| HSL | Green Hue −20, Green Sat −25 | Foliage toward yellow-olive, dusty not lush |
| HSL | Blue −20, Yellow −10, Orange +5 | Weak blues, muted yellows, skin and wood alive |
| Color Grading | Highlight 45/8, Shadow 35/10, blend 75 | Ochre above, warm brown below |
| Effects | Grain 25 / Size 28 / Roughness 55 | Consumer-negative texture, organic band |
| Effects | Post-Crop Vignette −12 | Album-page framing |

## Verification

**Structural**: Color, PV 15.4, `Adobe Color` Look, neutral curves, no Calibration, no Temperature or Tint. HSL saturation peaks at −25 / +5. Blacks −10, inside the −30 floor. Vibrance is absent while Saturation is −5, so the effective gap is 5 — at the limit, not over it.

**Grain rule engaged**: GrainAmount 25 with Sharpness 10, LuminanceSmoothing 0, and Clarity/Texture/Dehaze all absent. Grain 25/28/55 sits in the standard-colour-negative band; Roughness 55 is inside the 45–65 organic range. The preset spends its texture budget on grain alone.

### Validation Sweep 2026-10-21
- **Verdict:** accurate
- **Defining traits checked:** 1970s organic palette: green hue -20 with green/blue saturation -25/-20; warm shadow (35deg/10) and ochre highlight (45deg/8); muted Saturation -5; grain 25.
- **Sources:** In-Depth Cine, 'Why Movies From The 70s & 80s Look Like This: Kodak 100T 5247' (saturated warm stock, magenta-leaning blues); NARA 'Film Preservation 101' (magenta dye fade)
- **Preset adjustments:** none

**Review 2026-10-21 (research pass).** Palette corroborated by 1970s appliance/interior documentation and the New Topographics/Eggleston colour register. No XMP changes: green hue is negative (toward yellow-olive, correct on the Lightroom hue axis), the global mute is `Saturation` rather than HSL-only, and grain obeys the protection rule.

## Sources

- [Harvest gold — Wikipedia](https://en.wikipedia.org/wiki/Harvest_gold) — brown, burnt orange, avocado green appliances.
- [Kodacolor (still photography) — Wikipedia](https://en.wikipedia.org/wiki/Kodacolor_(still_photography)) — Kodak print film from 1942.
- [C-41 process — Wikipedia](https://en.wikipedia.org/wiki/C-41_process) — 1972, superseding C-22.
- [Chromogenic print — Wikipedia](https://en.wikipedia.org/wiki/Chromogenic_print) — dye prints, differential fading.
- [New Topographics — Wikipedia](https://en.wikipedia.org/wiki/New_Topographics) — 1975 Eastman House, muted landscape.
- [William Eggleston — Wikipedia](https://en.wikipedia.org/wiki/William_Eggleston) — 1976 MoMA show.
- [Earth tone — Wikipedia](https://en.wikipedia.org/wiki/Earth_tone) — the palette's definition.

## See Also

- [Decade presets](../../docs/decade.md)
- [Dust Bowl Documentary](../Dust%20Bowl%20Documentary/characteristics.md) — drought browns half a century earlier
- [Grunge](../Grunge/characteristics.md) — desaturated olive as 1990s corrosion
- [Kodak-Gold-200](../Kodak-Gold-200/characteristics.md) — warm consumer negative without the mute
