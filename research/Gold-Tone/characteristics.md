# Gold Tone — Look Characteristics

## Overview
Gold Tone is a darkroom-toning look, not a film emulation. It models a silver gelatin print treated
with a **gold toner** (gold chloride / thiourea or gold-borax baths). Classic gold toning has two
faces depending on process and paper:

1. **Protective / blue-black gold toning** — a light gold bath on a warmtone or chloro-bromide paper
   shifts the silver toward a cool blue-black with a slight plum cast, and is prized for archival
   permanence.
2. **Warm gold toning** (often applied after sepia or on POP/albumen-style papers) — pushes the image
   toward a rich yellow-gold to orange-brown.

This preset models the **warm gold** reading: a golden cast over a complete monochrome scale, in the
same family as sepia but more yellow and more metallic, less red.

## Key Characteristics
- **Tonal range**: intact; toning tints, it does not fade the print
- **Colour**: golden yellow, roughly 45–50° on the HSL wheel, strongest in highlights and upper
  mid-tones
- **Contrast**: unchanged from the untoned print; keep Clarity/Texture at 0
- **Split**: a small positive balance bias weights the cast toward the highlights, matching how a
  gold bath acts on the denser, warmer-toned silver
- **Grain**: source-print grain only; the preset is not grain-defined

## Visual Signature
- Warm, gilded monochrome: full blacks, golden highlights, no colour in the deep shadows
- Sits just above Sepia Tone (hue 35) and well above Copper Tone (hue 20), i.e. the yellow-most of the three
- Reads as a fine print on warmtone paper rather than as a digital colour grade

## Modeling Notes
- Keep `ColorGradeHighlightHue` near 48° and `ColorGradeShadowHue` a few degrees lower (~40°) so the
  shadows stay nearly neutral and the gold reads as a highlight tone
- Saturation 10–20 total; anything above ~25 stops reading as a colour photograph
- No calibration, no WB, no `Saturation` cut — the neutral base must come from the B&W Mixer

## Sources
- Darkroom references on gold chloride toners (protective blue-black vs. warm gold variants)
- Print-toning hue charts: sepia ~40°, copper ~15–25°, gold ~48°

## Validation Sweep 2026-10-21
- **Verdict:** accurate (no prior research file existed — folder created during the sweep)
- **Defining traits checked:** gold toning = golden ~45–50° cast concentrated in highlights. Preset: ColorGrade Highlight hue 48 / sat 16, Shadow hue 40 / sat 10, Balance +5 (mild highlight weighting), identical tonal base to Copper Tone (Contrast +20, Highlights −15, Shadows +15, Whites +10, Blacks −20). Hue separation across the toning trio is clean and monotonic — Copper 20/15, Sepia 35/25, Gold 48/40 — which is the point of having all three. GrainAmount 35 / GrainSize 25 is print texture; Sharpness 10, LuminanceSmoothing 0, Clarity/Texture 0 satisfy the repo grain rule. The cool blue-black gold-toning variant is not modelled — acceptable, since the folder now records that choice explicitly.
- **Sources:** gold-toner process descriptions (gold chloride + thiourea, protective vs. warm variants) and print-toning hue charts; cross-check against Copper Tone / Sepia Tone presets in this repo.
- **Preset adjustments:** none

## Gap
Folder created during the sweep; no community-recipes.md. Validation relied on toning chemistry and
cross-comparison instead of a collected recipe set.
