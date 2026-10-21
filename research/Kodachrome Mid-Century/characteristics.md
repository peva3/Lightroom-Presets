# Kodachrome Mid-Century Lightroom Preset — Characteristics

**Category**: Decade

The Kodachrome Mid-Century Lightroom preset recreates the 1950s family slide as it was actually seen — on a projector screen or in a fifty-year-old scan — with dense saturated reds, deep blue skies, high transparency contrast and a warm cast at both ends of the tonal range. It models the 10 ASA and Kodachrome II films, not the later K-14 emulsions.

## Historical Context

Kodachrome (1935) was the only mass-market film whose dyes were not in the emulsion: couplers were added during processing, in three separate colour developers, so the film itself was three monochrome layers ([K-14 process](https://en.wikipedia.org/wiki/K-14_process)).

| Period | Film | Speed | Process |
|---|---|---|---|
| 1936–1962 | Kodachrome (35mm daylight) | 10 ASA | pre-K-11, then K-11 |
| 1961–1974 | Kodachrome II | 25 ASA | K-12 |
| 1962–1974 | Kodachrome-X | 64 ASA | K-12 |
| 1974–2009 | Kodachrome 25 / 64 / 200 | 25 / 64 / 200 | K-14 |

**The distinction from the Slide presets is chronological.** `Presets/Slide/Kodachrome 25.xmp`, `Kodachrome 64.xmp` and `Kodachrome 200.xmp` model K-14 emulsions — post-1974 films with published RMS granularity (9, 10, 16) and E-55 datasheet behaviour ([Kodak E-55](https://125px.com/docs/film/kodak/e55-2009_06.pdf)). They are stock emulations: hue rotations on red, yellow, green and blue, blacks at -25, grain of 5–8 at size 15, and a cool 220–225° shadow grade. This preset is upstream of all that — the pre-K-14 era as projected, printed and scanned.

## Photographic Technology

- **Dyes.** Kodak called it "reproduces subtle color naturally" and "the most archival transparency films" ([E-55](https://125px.com/docs/film/kodak/e55-2009_06.pdf)). Dark-storage stability was exceptional — the yellow dye would lose 20% in 185 years — but projection fade was about one hour, against two and a half for Fujichrome ([Kodachrome](https://en.wikipedia.org/wiki/Kodachrome)).
- **The cyan problem.** Cyan was the least thermally stable layer until the 1980s, so aged transparencies drift **red** ([Topics in Photographic Preservation](https://resources.culturalheritage.org/pmgtopics/2009-volume-thirteen/13_13_Weaver.html)). Kodachrome's cyan also extends into the near infrared, which is why scans need an IT8 target and the film has a reputation for scanning blue ([Kodachrome](https://en.wikipedia.org/wiki/Kodachrome)).
- **Blue and green.** The red channel's mean sensitivity sits long, so skies record slightly darker with more cyan dye — a genuine cyan lean — while cyan makes greens and blues print dark on E-6-tuned materials ([VISNS](https://visns.neocities.org/4x5LFphotography/HGWK)).

## Visual Signature

Red first: dense, slightly orange-biased, textured rather than neon. Blue second: deep skies with weight and gradation. Greens are vivid but the print register calms them. Contrast is high and the highlight shoulder steep, yet black stays *dense* rather than crushed. The warmth is projection, ageing and print reproduction, not emulsion.

## Tonal Register

**Register**: warm-golden, high-contrast

Contrast +20 with Highlights -40 describes a steep shoulder pulled back just enough to stop slide highlights blocking; Shadows +20 and Blacks -10 keep the bottom end dense but open. Crucially, **both** grading ends are warm — highlight 40/10 and shadow 35/8 — unlike the Slide Kodachromes, which pair a yellow highlight with a 220–225° cool shadow. That encodes the artefact — projector bulb, print stock, cyan loss — rather than the dye set.

## Lighting & Subject Matter

Daylight, electronic flash and 1950s blue flashbulbs; tungsten only with an 80A filter ([E-55](https://125px.com/docs/film/kodak/e55-2009_06.pdf)). Subject matter is the family-slide canon — vacations, cars, birthdays, national parks — plus the advertising work sheet Kodachrome enabled before Ektachrome displaced it in 1951.

## Lightroom Translation

| Panel | Value | Function |
|---|---|---|
| Basic | Exposure +0.15, Contrast +20 | Slide density and the steep transparency curve |
| Basic | Highlights -40, Whites +10 | Recovers the abrupt reversal shoulder |
| Basic | Shadows +20, Blacks -10 | Dense but readable shadows, no crush |
| Presence | Saturation +10, Vibrance +10 | Saturated but controlled; gap of 0 |
| HSL | Red +20, Red Lum +5 | The defining red, kept from blocking up |
| HSL | Orange +10, Yellow +10 | Warm earth axis; skin and foliage warmth |
| HSL | Blue +18, Green -10 | Deep sky weight; print-era restraint on greens |
| Color Grading | Highlight 40/10, Shadow 35/8, blend 75 | Warm at both ends — projection/print cast |
| Effects / Detail | Vignette -10, Sharpness 10, Grain 15/24/45 | Slide-mount falloff; reproduction texture |

## Verification

**Structural**: Color treatment, PV 15.4, Adobe Color Look, neutral four-curve ToneCurvePV2012, no Calibration, no WB cast. Grain present with Sharpness 10, Luminance Smoothing 0, no Clarity/Texture/Dehaze. HSL peaks at +20; Blacks -10; |Vibrance − Saturation| = 0.

**Two honest gaps, deliberately not "fixed".**

1. *No hue rotations.* The Slide Kodachromes carry `HueAdjustmentBlue` of -10 to -15 (blue toward cyan); this preset has none, so its blue is saturated but not cyan-shifted. Left alone because a cyan rotation under a 40° warm highlight grade and +10 global saturation fights the projection register.
2. *Grain is heavier than the datasheets.* 15 at size 24 is coarser than every Slide Kodachrome (5–8 at 15), while the era's film was 10–25 ASA and finer-grained than K-14 stock. It is defended as *reproduction* grain — 1950s prints, halftone and consumer scans are far coarser than the transparency — but it is the preset's weakest link against an RMS reading.

### Validation Sweep 2026-10-21
- **Verdict:** accurate
- **Defining traits checked:** Kodachrome register: red +20 and blue +18 saturation with vibrance/saturation +10/+10; Contrast +20; grain 15 (fine); warm 35-40deg; deep but not crushed blacks (-10).
- **Sources:** Kodachrome 25/64 colour response references; Slide-category cross-check
- **Preset adjustments:** none

**Review 2026-10-21 (research pass).** Cross-checked against `Presets/Slide/Kodachrome 25/64/200.xmp`: same red/blue emphasis, correct divergence on hue rotation, black point (-25 vs -10), shadow temperature and grain. No XMP changes made.

## Sources

- [Kodachrome — Wikipedia](https://en.wikipedia.org/wiki/Kodachrome) — emulsion, archival stability, timeline.
- [K-14 process — Wikipedia](https://en.wikipedia.org/wiki/K-14_process) — dyes formed during processing.
- [Kodak E-55](https://125px.com/docs/film/kodak/e55-2009_06.pdf) — RMS values, 80A for tungsten.
- [Topics in Photographic Preservation](https://resources.culturalheritage.org/pmgtopics/2009-volume-thirteen/13_13_Weaver.html) — cyan instability → red drift.
- [VISNS Kodachrome colour analysis](https://visns.neocities.org/4x5LFphotography/HGWK) — cyan dye and cyan-leaning skies.

## See Also

- [Decade presets](../../docs/decade.md)
- [Kodachrome 64](../Kodachrome-64/characteristics.md) — the K-14 emulation this preset is *not*
- [Kodachrome 25](../Kodachrome-25/characteristics.md) and [Kodachrome 200](../Kodachrome-200/characteristics.md) — the rest of the Slide family
- [Post-War Optimism](../Post-War%20Optimism/characteristics.md) — the same decade graded for prints
