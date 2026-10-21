# Victorian Daguerreotype Lightroom Preset — Characteristics

**Category**: Decade

The Victorian Daguerreotype Lightroom preset recreates the first commercially successful photographic process: a unique positive on polished silvered copper, seen by tilting the plate until the image appears. It is a hard, metallic, low-key near-monochrome with a mirror-bright highlight and a deep case vignette — the opposite of a soft antique wash.

## Historical Context

Announced in Paris in 1839 and in production until roughly the late 1850s, the daguerreotype put a camera portrait in ordinary middle-class hands for the first time. Studios ran on daylight, rooftop glasshouses and appointment books; sitters held still for seconds at a time, often with a head brace. Every plate was unique and laterally reversed, so it could not be editioned — which is precisely why collodion displaced it in the 1850s. The surviving objects are small, cased, and sit behind glass with a brass mat and a velvet-lined box.

## Photographic Technology

- **Plate**: copper plated with silver, polished to a mirror finish, sensitised by fuming with iodine (later bromine) vapour.
- **Process**: exposed in camera, developed in heated mercury vapour, fixed, then usually gilded with gold chloride to harden the surface and warm the tone slightly.
- **Optics**: the fast portrait lens introduced by Petzval in 1840 cut exposure dramatically and became the standard portrait optic; wide open it is soft toward the corners and falls off in illumination.
- **Image structure**: a microscopically fine light-scattering structure on bare silver, not pigment. The darkest areas are polished silver reflecting the dark inside of the case; highlights are roughened silver scattering light. Hence it reads positive from one angle and negative from another.
- **Resolution**: effectively grainless — a quarter plate holds detail no 1930s film could match.

## Visual Signature

- **Palette**: neutral silver at heart. Age pushes it warm — silver tarnish is brown-black, gold toning adds faint warmth, and the brass mat and case velvet bounce warm light onto the plate. The sepia here is a conventional shorthand for a tarnished plate, not the colour of a pristine one.
- **Contrast**: hard. `Contrast +30` with `Whites +10` gives the abrupt, mirror-bright shoulder; `Highlights -35` stops it clipping into a white hole, `Blacks -18` holds the sooty ground.
- **Texture**: almost none in the image; what exists is on the plate — polish marks, dust, tarnish rings, the odd scratch. `GrainAmount 18 / Size 38 / Roughness 70` reads as surface mottle, not film grain.
- **Tonal distribution**: low-key. A bright face and collar floating over dark clothing and a dark ground, corners falling away hard.

## Tonal Register

**Register**: sepia-toned (low-key, hard highlight)

Warm-neutral and low-key, which is what the preset is built for: it lifts the upper midtones (`Whites +10`, `Shadows +15`) while pinning the bottom (`Blacks -18`), so it behaves on dark, high-contrast originals. On a modern high-key frame the bright shoulder and −35 vignette fight the image and it reads as a heavy filter.

## Lighting & Subject Matter

North-facing studio skylights, sometimes supplemented with mirrors or blue glass to shorten exposure; later, direct sun. Subject matter is portraiture above all — individuals, couples, families, soldiers, post-mortem portraits — with a smaller trade in city views and copied engravings. Faces are lit flatly and frontally; backgrounds are plain painted canvas or dark cloth.

## Lightroom Translation

- **Basic**: `Exposure2012 -0.30` for plate density; `Contrast2012 +30` for the metallic shoulder; `Highlights2012 -35` and `Whites2012 +10` give the mirror sheen without clipping; `Shadows2012 +15` keeps dark clothing readable; `Blacks2012 -18` for the cased ground.
- **Colour**: `Saturation -48`, with all eight HSL saturation channels between −40 and −50 — one neutral-warm axis, no surviving hue. `LuminanceAdjustmentOrange +10` and `Yellow +5` lift skin and collar.
- **Color Grading**: highlights `38° / 10` (gilt), shadows `32° / 15` (tarnish), `Blending 80`.
- **Effects**: `PostCropVignetteAmount -35` for the mat aperture and lens falloff; `GrainAmount 18 / Size 38 / Roughness 70` for plate mottle.
- **Detail**: `Sharpness 10`, `LuminanceSmoothing 0`; Clarity/Texture/Dehaze unset — the plate is sharp in the centre and soft at the edges for free.
- **Tone Curve**: neutral.

## Verification

Accurate; no changes this pass.

- **Grain**: a daguerreotype is grainless and an earlier pass already cut this from 55 to 18. At `Size 38 / Roughness 70` and Amount 18 it reads as plate surface, so it is kept as a deliberate texture shorthand — below the styleguide's fine-grain band and far below any film emulation.
- **Contrast and shoulder**: `+30` with `Whites +10` and `Highlights -35` is the right structure for a mirror surface — bright, abrupt, unclipped.
- **Vignette**: `-35` is strong but justified by the mat aperture plus fast-lens falloff, not by a modern instinct.
- **Sepia**: `38°/10` and `32°/15` are conventional warm shorthand; a pristine plate is neutral silver, and only tarnish, gold toning and case materials justify warmth. Documented rather than removed, because the brown reading is how the era is recognised.
- **Not changed — Temperature 5900**: absolute WB; retained because at −48 saturation its contribution is small and removing it leaves nothing to tint the neutral.
- **Vibrance**: absent from the XMP, satisfying the "remove Vibrance entirely" alternative; the gap against `Saturation -48` is on the desaturating side.

### Validation Sweep 2026-10-21
- **Verdict:** minor drift → resolved
- **Checked:** `Saturation -48` plus per-hue desaturation; metallic sheen at `38°`; vignette −35.
- **Prior fix kept:** grain 55 → 18, `Contrast` +5 → +30, `Highlights` −55 → −35, `Whites` 0 → +10.
- **This pass:** no preset change; low grain documented as plate surface.

## Sources

- [Daguerreotype — Wikipedia](https://en.wikipedia.org/wiki/Daguerreotype) — silvered copper, mercury development, the positive/negative viewing angle, laterally reversed image.
- [Daguerreotypes and Book Sleuthing — NEDCC](https://www.nedcc.org/about/nedcc-stories/daguerreotypes-and-book-sleuthing) — how the plate must be angled to capture the image.
- [The Silver Canvas: Daguerreotype Masterpieces from the J. Paul Getty Museum (PDF)](https://d2aohiyo3d3idm.cloudfront.net/publications/virtuallibrary/0892365366.pdf) — formats, casing and the reversed mirror image.

## See Also

- [Decade presets](../../docs/decade.md)
- [Daguerreotype (alternative process)](../alt-daguerreotype/) — the process as a dedicated effect preset.
- [Civil War Era](../Civil%20War%20Era/) — the collodion decade that replaced it.
- [Salt Print](../alt-salt-print/) — the paper-positive alternative of the same years.
