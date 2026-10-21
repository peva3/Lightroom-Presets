# Grunge — Community Recipes

Working ranges for a 1991-94 Seattle colour grade: under-exposed, olive, coarse-grained, closed black point. The shipped `Grunge.xmp` is close to the middle of every range; the extremes below are where the look tips into "broken file".

## Reference Looks

- **Charles Peterson colour frames** — flash foreground, cross-processed cast, green-shifted shadows ([Seattle Times](https://archive.seattletimes.com/archive/19951023/2148380/the-vision-of-charles-peterson----seattle-photographers-style-finds-clear-success-in-the-blur-of-the-international-rock-scene)).
- **December 1992 "Grunge & Glory" (Meisel/Coddington)** — plaid, thermal grey, flat overcast light, almost no specular ([AnOther](https://www.anothermag.com/fashion-beauty/7476/marc-jacobs-s-s93-nirvana-tribute-at-perry-ellis)).
- **Cheap one-hour-lab colour prints** — the everyday version: cool/green cast, hard contrast, dust ([The Darkroom](https://thedarkroom.com/cross-processing-film/) on xpro casts).
- **Tri-X pushed to 1600** — the monochrome reference for grain size and shadow blocking, even though this preset stays in colour.

## Slider Starting Points

| Panel | Range | Notes |
|---|---|---|
| Exposure | -0.60 to -0.10 | Under-exposure is the look; never lift to "fix" it |
| Contrast | +20 to +40 | Past +40 shadows plug |
| Highlights | -70 to -35 | Kill any clean white |
| Shadows | -25 to 0 | Negative values are correct here — this is the muddy move |
| Whites | -10 to +5 | Whites should not read as white |
| Blacks | -30 to -15 | Never below -30 |
| Saturation | -35 to -15 | Global mute; do not add Vibrance on top |
| HSL Sat | Green -45…-15, Blue -35…-10, Orange -20…0, Yellow -30…-5 | One hue at a time; all downward |
| HSL Hue | Green -30…-10 | Toward yellow/olive. Positive is *wrong* here (it goes cyan) |
| Color Grading | Shadow 80-105 / 8-18, Highlight 35-50 / 3-10, Blend 60-75 | Olive bottoms, almost-neutral tops |
| Grain | 30-55 / size 25-40 / rough 55-80 | Coarse and irregular; keep Sharpness at 10 |
| Vignette | -30 to -12 | Small-room falloff |

## Common Mistakes

- **Encoding "olive" as a positive green hue shift.** The hue axis runs Red → Orange → Yellow → Green → Aqua, so olive needs `HueAdjustmentGreen` **negative**. Positive pushes foliage cyan, which is the opposite of this look.
- **Adding Vibrance.** Vibrance would selectively rescue the midtone greens the grade is trying to kill, producing a near-monochrome image with one surviving colour — the repo's classic "B&W with one colour" failure.
- **Lifting Shadows and calling it "faded".** Grunge is dark and dirty, not matte. Lifted blacks plus a -22 saturation reads as a modern Instagram fade.
- **Clarity or Texture over 0.** Both sharpen grain edges into digital noise; at Grain 40 the result looks like sensor failure, not film.
- **Sharpness left at the default 40.** With heavy grain, default sharpening produces jagged, crystalline noise. Sharpness 10 and Luminance Smoothing 0 is the only safe pairing.
- **Grading skin warm to compensate.** The era's flash frames do have warm faces; adding orange saturation here turns the whole image muddy-brown and loses the green cast that identifies the look.

## See Also

- [Grunge characteristics](characteristics.md)
- [Cross-Processed](../Cross-Processed/characteristics.md) — the cast mechanism, without the under-exposure
- [Bleach Bypass](../Bleach%20Bypass/community-recipes.md) — desaturation via a different physical route
- [Decade presets](../../docs/decade.md)
