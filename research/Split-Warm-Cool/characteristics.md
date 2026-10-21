# Split Warm-Cool — Aesthetic Characteristics

## Overview
A split-tone is a print or scan where the shadows and the highlights are pushed toward opposite
sides of the colour wheel. It is not a film characteristic and not a single chemical process — it
is a darkroom/digital printing convention, descended from split sepia-selenium toning and from
duotone/tritone reproduction printing.

## Core Aesthetic Signature

### Colour Shift (the defining trait)
- **Highlights warm, shadows cool** is the canonical arrangement (the inverse — cool highlights,
  warm shadows — reads as "cross-processed" and is a different look entirely).
- Warm highlight hue lands at 35–50° (amber to orange). Cool shadow hue lands at 200–230°
  (cyan-blue to blue).
- Saturation stays low — 10–18 per zone. Above ~20 the split becomes a two-colour poster and the
  neutrality of the midtones collapses.
- **Balance at 0** keeps the crossover at mid-grey so the midtones remain neutral; the whole point
  of the look is that only the extremes are tinted.

### Contrast & Tonality
- Neutral-to-slightly-elevated contrast. The tint itself does most of the perceptual work, so the
  tonal curve can stay close to base.
- Clean whites and near-black shadows; the tint should not lift the black point.

### Grain
- Inherited from the underlying emulsion. A split tone is applied *on top of* a completed B&W
  render, so grain amount here is a stylistic substrate, not a property of the toning.

## Emulation Notes for the Preset
- `Treatment` may legitimately be `Monochrome` with `ConvertToGrayscale="True"`; the ColorGrade
  wheels then tint the grayscale render.
- Do not mix `SplitToning*` legacy attributes with `ColorGrade*` in the same preset — double tinting.
- Balance near 0, saturation ≤ 18 per zone, otherwise the midtones stop being neutral.

## Sources
- Darkroom split-toning practice (sepia + selenium two-stage) in Photrio and r/Darkroom threads.
- Duotone/tritone reproduction printing convention (warm highlights, cool shadows).
- Adobe Camera Raw ColorGrade documentation (three-way wheel zone behaviour).

## Validation Sweep 2026-10-21

- **Verdict:** accurate
- **Defining traits checked:** warm highlights + cool shadows with neutral midtones; low per-zone saturation; crossover at mid-grey
- **Checked against XMP:** HighlightHue 45 / Sat 15, ShadowHue 220 / Sat 12, Balance 0 (crossover at mid-grey), MidtoneSat 0 (midtones stay neutral); Contrast +20 with Blacks -20 (blacks stay black, no lift); no legacy SplitToning* stacked on ColorGrade*
- **Sources:** darkroom split sepia/selenium practice (Photrio, r/Darkroom); duotone warm-highlight/cool-shadow convention; research/Split-Warm-Cool
- **Preset adjustments:** none
