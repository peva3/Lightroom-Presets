# Sepia Tone — Aesthetic Characteristics

## Overview
Sepia toning is a two-bath (or single-bath thiourea) process that bleaches the silver image and
re-develops it as silver sulphide. Unlike selenium, which is a hardening/archival bath with a
side-order of colour, sepia is a *true colour* transformation — the image is chemically replaced.

## Core Aesthetic Signature

### Colour Shift (the defining trait)
- Warm yellow-brown to reddish-brown. Hue sits roughly 25–45° on the HSL wheel: 25° reads as
  deep chocolate, 40° reads as amber/honey.
- The tint is **strongest in the highlights and midtones** — that is where the silver sulphide
  conversion is most visible, and why sepia portraits look "suntanned" rather than muddy.
- Shadows stay comparatively neutral-to-dark; a fully toned print keeps near-black shadows.
- Saturation is low by design: 10–20 points reads authentic, above ~25 it looks like an
  Instagram filter rather than a toned print.

### Contrast & Tonality
- Sepia **bleaches and reduces D-max**. The classic failure mode of an over-toned sepia print is
  washed-out, weak blacks.
- A well-executed sepia print compensates by printing slightly darker/contrastier first, so the
  final sepia carries roughly the original contrast with softer blacks.
- Highlights compress; the print loses a little of the sparkle of an untoned gelatin silver print.

### Grain
- No grain change — the grain structure is inherited from the negative. Sulphide conversion does
  not enlarge or roughen it.

## Emulation Notes for the Preset
- `Treatment` may legitimately be `Monochrome` with `ConvertToGrayscale="True"`; ColorGrade then
  tints the grayscale render.
- Positive Balance biases the tint toward the highlights — correct for sepia, and the opposite of
  selenium's shadow-weighted bias.
- Contrast should be at least the base print level, Blacks negative, so the "bleached" look does
  not become a milky low-contrast mess.

## Sources
- Wikipedia, "Photographic print toning" — sulphide (sepia) vs selenide (selenium) chemistry.
- Ilford and Kodak sepia toning kit instructions (bleach-and-redevelop order).
- Darkroom forums (Photrio, r/Darkroom) on over-toning and D-max loss.

## Validation Sweep 2026-10-21

- **Verdict:** accurate
- **Defining traits checked:** sulphide bleach-redevelop; yellow->red-brown (25-45 deg); tint strongest in highlights and midtones; D-max drops so printers compensate with contrast and a darker print
- **Checked against XMP:** HighlightHue 35 / Sat 18, ShadowHue 25 / Sat 12, Balance +25 (highlight-weighted, correct); Contrast +20 and Whites +10 offset the bleach; Blacks -20 so it does not read milky
- **Sources:** Wikipedia "Photographic print toning"; Ilford / Kodak sepia kit instructions; r/Darkroom over-toning threads; research/Sepia-Tone
- **Preset adjustments:** none
