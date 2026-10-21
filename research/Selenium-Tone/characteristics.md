# Selenium Tone — Aesthetic Characteristics

## Overview
Selenium toning is a post-development archival treatment: a silver-gelatin print is bathed in
dilute selenium toner (typically Kodak Rapid Selenium Toner at 1+20 to 1+40) which converts
metallic silver to silver selenide. The conversion is permanent and archival — selenium toning
is not primarily a colour effect, it is a *tonal* effect that happens to carry a colour shift.

## Core Aesthetic Signature

### Colour Shift (the defining trait)
- **Weak dilution (1+40, short time):** barely perceptible warming — a faint red-brown or
  aubergine cast in the midtones and shadows.
- **Strong dilution / long time (1+10 to 1+20):** the classic "eggplant" purple-brown, most
  visible in the shadows and lower midtones rather than the highlights.
- **Highlights stay near-neutral** — unlike sepia, selenium does not bleach the print, so the
  whites remain clean. The tint lives in the lower half of the tonal scale.
- Hue sits around 280–300° (violet → magenta-violet) for the strong tone, drifting toward
  20–30° (red-brown) at weak dilution.

### Contrast & Tonality (the part people forget)
- Selenium **increases D-max**: blacks get visibly deeper and denser ("blacker blacks").
- Perceived contrast rises a full half-grade; shadow separation *improves* because the
  toe densifies rather than flattens.
- It does **not** lift blacks and does **not** wash out highlights. This is the single
  biggest difference from sepia toning, which bleaches and lowers D-max.

### Grain
- No grain change. The silver structure is chemically altered, not enlarged. A selenium print
  shows exactly the grain of the original negative.
- Any grain in a digital emulation is therefore a *substrate* choice, not a toning artifact.

## Emulation Notes for the Preset
- `Treatment` may legitimately be `Monochrome` with `ConvertToGrayscale="True"`; the ColorGrade
  three-way wheels then tint the grayscale render.
- Shadow zone carries the tint (negative Balance biases to shadows), highlight saturation stays
  low. Selenium's defining signature is **cool violet shadows + neutral, deep blacks**.
- Contrast should be at or slightly above the untinted base print; Blacks should be negative
  (crushed), never lifted.

## Sources
- Wikipedia, "Photographic print toning" — weak selenium = red-brown, strong = purple-brown.
- DePaul University (S. Grais), "Duotones" — red-brown at weak strength, purple-brown at strong.
- J. Riley Stewart, "selenium toner" — "purple and white" / "eggplant and white" terminology.
- Darkroom practice threads (Photrio, r/Darkroom) on split sepia/selenium toning.

## Validation Sweep 2026-10-21

- **Verdict:** accurate
- **Defining traits checked:** silver -> silver selenide; purple-brown/eggplant at strength, red-brown when weak; D-max *increases* (deeper blacks); tint lives in the shadows while highlights stay near-neutral
- **Checked against XMP:** ColorGradeShadowHue 250 / Sat 8, HighlightHue 275 / Sat 12, Balance -10 (shadow-weighted, correct); Blacks -20 with Contrast +20 (D-max increase, no lift); Whites +10
- **Sources:** Wikipedia "Photographic print toning"; DePaul (S. Grais) "Duotones" (red-brown weak -> purple-brown strong); J. Riley Stewart ("purple and white" / "eggplant and white"); research/Selenium-Tone
- **Preset adjustments:** none
- **Note:** Hue 250-275 sits on the blue-violet side of eggplant; a strong real selenium bath reads ~280-300 (violet->magenta-violet). Within tolerance at 8-12% saturation, and it correctly avoids sepia's bleaching.
