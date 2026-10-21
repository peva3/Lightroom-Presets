# Kodak Ektachrome 320T — Characteristics for Lightroom Presets

## Film Stock Profile
- **Type:** Tungsten-balanced color reversal (slide) film This document serves as a reference for creating a Lightroom preset that emulates Ektachrome 320T.
- **Manufacturer:** Kodak
- **ISO:** 320 (tungsten), 100 (daylight with 85B filter)
- **Status:** Discontinued
- **Format:** 35mm (EPJ 320T)
- **Related:** Ektachrome 64T (EPY), Ektachrome 160T (EPT)

## Cross-Processed in C-41
When processed in C-41 chemistry instead of E-6:
- **Contrast:** Dramatically increased — slide film gamma goes from ~1.5 to ~2.2+
- **Color shifts:** Strong green-magenta crossover is characteristic
  - Shadows shift toward blue-cyan (tungsten balance + C-41 = strong blue cast)
  - Midtones shift toward yellow-green (C-41 xpro signature)
  - Highlights shift toward magenta (complementary crossover)
- **Grain:** More prominent — C-41 processing increases apparent grain in slide film
- **Blacks:** Deep, crushed — slide film's DMax is pushed further
- **Unpredictability:** Every batch produces slightly different color shifts — part of the appeal

## Aesthetic Character
- **Primary:** High-contrast, blue/magenta/green color-shifted, gritty cross-processed look
- **Contrast:** Very high — slide + xpro = maximum contrast
- **Saturation:** Variable — C-41 xpro can increase or decrease depending on exposure
- **Blues:** Strong blue cast in shadows from tungsten balance — defining characteristic
- **Greens:** Shifted toward cyan/yellow-green in midtones
- **Reds/Magentas:** Boosted in highlights from xpro crossover
- **Skin tones:** Cool, pale, slightly cyan — tungsten balance makes skin go cold in C-41
- **Grain:** Pronounced, gritty — slide film grain amplified by xpro
- **Overall vibe:** 1990s fashion editorial, music video, experimental, punk/grunge aesthetic

## Historical Context
- Ektachrome 320T was the fast tungsten slide film for indoor/low-light work
- Popular with concert photographers and photojournalists before digital
- Cross-processing became an artistic technique in the 1990s fashion/editorial world
- The combination of tungsten balance + xpro creates uniquely "wrong" but compelling colors

## Lightroom Translation Source
- **Base:** STYLEGUIDE Cross-Processed E6→C41 formula + tungsten balance characteristics
- **Key moves:** High contrast, cool/green/magenta color grading, blue saturation boost, prominent grain
- **Translation date:** 2026-06-01

---

## See Also

For related Lightroom presets and film stock references:

- [Kodak Ektachrome E100](../Kodak-Ektachrome-E100/characteristics.md)
- [Kodak Ektachrome 64](../Kodak-Ektachrome-64/characteristics.md)
- [Kodak Ektachrome 400X](../Kodak-Ektachrome-400X/characteristics.md)
- [Kodak Ektachrome 200](../Kodak-Ektachrome-200/characteristics.md)
- [Kodak Ektachrome 100VS](../Kodak-Ektachrome-100VS/characteristics.md)

## Validation Sweep 2026-10-21

- **Verdict:** accurate (as a cross-processed E-6 -> C-41 interpretation)
- **Defining traits checked:** high slide contrast; tungsten-balance blue/cyan shadows; C-41 crossover (yellow-green midtones, magenta highlights); pronounced grain; muted overall saturation.
- **Verified in XMP:** Contrast +30, Highlights -45, grain 35 / 30 / 55; shadow grade 220 deg / 18 (blue-cyan), midtone 75 deg / 12 (yellow-green), highlight 330 deg / 15 (magenta); Saturation -5 with Blue +15 / Green -15 / Red -10. This maps one-for-one onto the crossover description recorded in this folder.
- **Scope note:** the file lives in Color-Negative but the stock is a reversal film; the preset intentionally emulates the xpro look, so it was judged against that reference rather than against an E-6 rendering.
- **Sources:** Kodak Ektachrome 320T (EPJ) data; Lomography/xpro crossover guides; repo characteristics.md.
- **Preset adjustments:** none in colour; display name aligned with the filename stem ("Kodak Ektachrome 320T" -> "Kodak-Ektachrome-320T").
