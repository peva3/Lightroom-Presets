# Summer of Love Lightroom Preset — Characteristics

**Category**: Decade

The Summer of Love Lightroom preset reconstructs the colour of Haight-Ashbury documentary photography in 1967: warm, slightly over-exposed, softly bloomed, with yellow-magenta highlights and foliage pulled toward olive. It is a warm-golden colour preset with lifted blacks, no grain and a mild 5800 K bias — a Kodachrome or Ektachrome slide printed a little hot, not the acid palette of the era's concert posters.

## Historical Context

As many as 100,000 young people converged on Haight-Ashbury and Golden Gate Park in the summer of 1967 ([Wikipedia](https://en.wikipedia.org/wiki/Summer_of_Love)). The event was photographed cheaply and constantly, and the surviving images are street portraits, park encampments, painted vans and storefronts in daylight colour ([History.com](https://www.history.com/photos-of-the-summer-of-love); [PBS](https://www.pbs.org/wgbh/americanexperience/films/summer-of-love/)).

Two palettes are routinely conflated. The Fillmore poster tradition (Wes Wilson, Victor Moscoso, Mouse and Kelley) used acid greens and vibrating complements, but the photographs are far more restrained — this preset follows the photographs.

## Photographic Technology

- **Kodachrome II (25 ASA)** and **Kodachrome-X (64 ASA)** were the serious slide options, processed through K-12 chemistry until K-14 arrived in 1974 ([Kodachrome](https://en.wikipedia.org/wiki/Kodachrome)). K-12 was fixed — labs could not simply push it, so low light meant flash, tripod or faster film.
- **High Speed Ektachrome** reached 160 ASA in 1959 and *was* pushable ([Ektachrome](https://en.wikipedia.org/wiki/Ektachrome)); pushing shifted colour toward magenta-red, as Kodak's datasheets state ([E-55](https://125px.com/docs/film/kodak/e55-2009_06.pdf)). Consumer negative was still Kodacolor-X on C-22 — C-41 did not arrive until 1972 ([C-41](https://en.wikipedia.org/wiki/C-41_process)).
- **Optics leaked.** Single-coated elements flared easily and perished foam light seals leaked. Flare and edge leaks are equipment artefacts of the era, not a graded effect.

## Visual Signature

Sun-facing frames have a yellow-white core and a magenta fringe. Foliage is the tell: green sits toward yellow-olive, not emerald. Skin is warm and slightly ruddy, never neutral. Blacks are **lifted**, not crushed — a slide printed to paper cannot hold a true black, encoded as Blacks +5 with Contrast −5. Bloom sits in the highlights (Clarity −10, Dehaze −5). There is no grain, because 25–160 ASA colour slide is among the finest-grained colour material ever made.

## Tonal Register

**Register**: warm-golden, high-key end

Exposure +0.25 EV, Whites +10 and lifted Blacks +5 place the image above middle grey, which is what a slightly over-exposed slide looks like when printed. Warmth is carried at *both* ends — highlight 50 (yellow) at 10, shadow 40 (orange) at 8 — so no cool counterweight exists. On an overcast or blue-hour frame the grade has nothing warm to amplify and turns sepia-ish; it is built for daylight and golden hour.

## Lighting & Subject Matter

Low sun raking across the frame, flare washing the bottom third, backlit hair, dappled eucalyptus shade, bare bulbs at a free clinic. Subject matter is street portraiture, park blankets and guitars, painted buses, flowers held to the lens.

## Lightroom Translation

| Panel | Value | Function |
|---|---|---|
| Basic | Exposure +0.25, Contrast −5 | Slide printed hot; contrast back so highlights bloom |
| Basic | Highlights −40, Shadows +30 | Recovers sun cores; opens shaded faces |
| Basic | Whites +10, Blacks +5 | Bright edge; **lifted** black point |
| White Balance | Temperature 5800 | Deliberate +300 K warm bias — the only WB value |
| Presence | Saturation +10, Vibrance +8 | 2-point gap, inside the ±5 rule — no selective colour |
| HSL | Green Hue −10, Green Sat −20 | Foliage toward yellow-olive, not emerald |
| HSL | Magenta +15, Red +10, Yellow +10, Blue +8, Orange +5 | Psychedelic accents, kept modest |
| Color Grading | Highlight 50/10, Shadow 40/8, blend 75 | Warm both ends: sun above, amber in shade |
| Effects | Clarity −10, Dehaze −5 | Halation and consumer-lens veiling |

## Verification

**Structural**: Color, PV 15.4, `Adobe Color` Look, neutral four-curve tone curves, no Calibration, no Tint. |Vibrance − Saturation| = 2. HSL saturation peaks at +15 / −20. Blacks +5, not crushed. GrainAmount 0, so the grain rule is not engaged and Clarity −10 / Dehaze −5 are free to do bloom work; Sharpness sits at 10 regardless.

`Temperature="5800"` is the only white-balance value, retained deliberately: the warm cast defines 1960s slide printed to paper, and 5800 K is only +300 K from daylight.

### Validation Sweep 2026-10-21
- **Verdict:** accurate
- **Defining traits checked:** 1967: Temp 5800, +0.25 EV with Blacks +5 (faded print), Vibrance +8 / Saturation +10, magenta +15 and yellow/green pushes, Clarity -10; GrainAmount 0.
- **Sources:** 1960s psychedelic-era colour print references
- **Preset adjustments:** none

**Review 2026-10-21 (research pass).** Confirmed against Kodachrome/Ektachrome-era slide behaviour and Haight-Ashbury documentary photographs. No XMP changes: the lifted black point, the 2-point Vibrance/Saturation gap and the two-ended warm grade all match the period. Caveat: "light leaks" attributed to the era are camera faults, not a grade.

## Sources

- [Summer of Love — Wikipedia](https://en.wikipedia.org/wiki/Summer_of_Love) — dates, scale, the district.
- [A Photographic Trip Through the Summer of Love — History.com](https://www.history.com/photos-of-the-summer-of-love) — the photographic register.
- [Summer of Love — PBS American Experience](https://www.pbs.org/wgbh/americanexperience/films/summer-of-love/) — the district's arc.
- [Charles W. Cushman Photograph Collection — Indiana University](https://webapp1.dlib.indiana.edu/cushman/) — Kodachrome documentary archive of the period.
- [Kodachrome — Wikipedia](https://en.wikipedia.org/wiki/Kodachrome) — 25/64 ASA stocks, K-12 until 1974.
- [Ektachrome — Wikipedia](https://en.wikipedia.org/wiki/Ektachrome) — High Speed Ektachrome 160 ASA.
- [Kodak E-55 datasheet](https://125px.com/docs/film/kodak/e55-2009_06.pdf) — push shifts colour toward magenta-red.

## See Also

- [Decade presets](../../docs/decade.md)
- [Mod London](../Mod%20London/characteristics.md) — the same decade in Swinging London monochrome
- [Kodachrome Mid-Century](../Kodachrome%20Mid-Century/characteristics.md) — Kodachrome clean and saturated rather than faded
- [Cross-Processed](../Cross-Processed/characteristics.md) — slide film deliberately mis-developed
