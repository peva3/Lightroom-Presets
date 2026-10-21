# Dust Bowl Documentary Lightroom Preset — Characteristics

**Category**: Decade

The Dust Bowl Documentary Lightroom preset reproduces the Farm Security Administration's record of the southern Plains in the 1930s: a dry, low-saturation image with paper-warm highlights, a veiled sky, and grain belonging to the negative and the file print. It is deliberately flat rather than dramatic — the era's power comes from subject and light, not from a grade.

## Historical Context

From 1935 to 1943 the Resettlement Administration, renamed the Farm Security Administration and later folded into the Office of War Information, sent photographers across rural America to document poverty and the case for federal aid. Roy Stryker ran the project; Dorothea Lange, Walker Evans, Arthur Rothstein, Russell Lee, Marion Post Wolcott, Jack Delano and Ben Shahn did the fieldwork. The unit produced roughly 175,000 black-and-white negatives, now at the Library of Congress, plus a smaller body of colour transparencies. Behind the imagery is the Dust Bowl itself: drought in 1934, 1936 and 1939–40, topsoil stripped by deep ploughing, and "black blizzards" that turned midday dark.

## Photographic Technology

- **Cameras**: large-format and press equipment. Lange worked with a 4×5 Graflex reflex; others used 4×5 press cameras, medium-format rollfilm and, for slower work, view cameras. Big negatives mean fine grain at published sizes.
- **Negative**: panchromatic sheet and roll film of the mid-1930s — far closer to modern eyes than the orthochromatic stock of twenty years earlier, which is why FSA faces and cloth read normally rather than chalky.
- **Prints**: the FSA/OWI lab printed the negatives Stryker and the photographers selected. File prints are warm-toned silver gelatin on fibre paper, often with the sky burned in or left blank, and are why the archive looks browner than the negatives.
- **Colour**: a small number of colour transparencies were made under the same programme; they are the reference for this preset's low-saturation colour rather than full monochrome.
- **Dust colour**: the dust itself was grey to black, not beige — contemporary accounts describe clouds "black or gray (not beige or red)". The warmth in the archive is the paper and the toning.

## Visual Signature

- **Palette**: desaturated but not monochrome. `Saturation -20`; green −35 and blue −25 so grass and denim go quiet; `LuminanceAdjustmentOrange +8` lifts faces and dry earth; `Yellow -10` holds straw back. Highlights grade `40° / 8`, shadows `35° / 12` — paper warmth, applied lightly.
- **Contrast**: low to moderate. `Contrast +10` with `Highlights -45` and `Shadows +20` gives the evenly lit look of the file print; `Whites -10` keeps skies from going brilliant white.
- **Texture**: `45 / 32 / 65` — negative grain plus fibre print, at the top of the styleguide's organic band but inside it.
- **Tonal distribution**: midtone-heavy, with a pale near-detail-free sky and a dark foreground band of soil, clothing and shadow.

## Tonal Register

**Register**: warm-golden (muted, paper-warm)

Warm but not gilded: the warmth is a low-saturation paper cast (`40°/8`, `35°/12`, `Temp 5700`) under a 20-point mute, so it reads as faded rather than golden. It is stable across warm and neutral originals and fails only on very cool, high-key sources, where the cast fights a blue sky and the veil turns grey. Validate on hard midday sun with dry ground and a pale sky — the register the FSA worked in.

## Lighting & Subject Matter

Hard, high, unrelenting sun; flat overcast during dust; light filtered through soil until the sky goes brown-grey and shadows lose their edge. Subject matter is people at the edge of subsistence — migrant camps, dugouts, jalopies, cotton fields, windmills, abandoned farmhouses — photographed frontally, at eye level, horizon very high or removed.

## Lightroom Translation

- **Basic**: `Exposure2012 -0.25`, `Contrast2012 +10`; `Highlights2012 -45` and `Whites2012 -10` keep the sky pale rather than blown; `Shadows2012 +20` opens hats and doorways; `Blacks2012 -10` anchors the print.
- **Haze**: `Dehaze -5` models dust-veiled air. This is a documented override of the "grain presets keep Dehaze at 0" rule (see Verification).
- **Colour**: `Saturation -20` with `Green -35`, `Blue -25`, `Yellow -10` and `LuminanceAdjustmentOrange +8`; `Temperature 5700` for the warm paper base.
- **Color Grading**: highlights `40° / 8`, shadows `35° / 12`, `Blending 75`.
- **Effects**: `GrainAmount 45 / GrainSize 32 / GrainRoughness 65`; `PostCropVignetteAmount -22`. **Detail**: `Sharpness 10`, `LuminanceSmoothing 0`, Clarity/Texture unset.

## Verification

Pass after one correction.

- **Dehaze**: the page claimed "atmospheric haze" while `Dehaze` was unset, so the preset did nothing to model dust-veiled air. Changed **`Dehaze` 0 → −5**: enough to veil distant contrast without turning midtones to milk, which a stronger value plus `Grain 45` would do.
- **Rule override, documented**: STYLEGUIDE §VIII.2 asks grain-bearing presets to keep Clarity/Texture/Dehaze at 0. Here scattering is a defining trait, so the rule is overridden at the minimum effective value, with Clarity and Texture left at 0 so only one frequency band is touched.
- **Grain kept at 45**: large-format negatives suggest less, but the working objects are *prints*, often from copy negatives made for distribution. Size 32 / Roughness 65 keeps it structured rather than noisy.
- **Contrast stays modest**: the era's harshness is in the scene, not the grade; `+10` with lifted shadows is what the file prints look like.
- **Colour, not sepia**: `Saturation -20` keeps residual colour, matching the faded transparencies; warmth is graded in, not achieved by a mono conversion.
- **Vibrance** is absent from the XMP ("remove Vibrance entirely"), and **Temperature 5700** is absolute WB — the only portability risk, since the grade assumes a warm start.

### Validation Sweep 2026-10-21
- **Verdict:** accurate → one gap closed
- **Checked:** `Saturation -20` with HSL cuts on blue/green/yellow; `Temp 5700`; `Grain 45`; `Vignette -22`; `Shadows +20`.
- **Gap then:** "atmospheric haze" claimed, `Dehaze` 0. **This pass:** `Dehaze` −5, override documented.

## Sources

- [FSA/OWI Black-and-White Negatives — Library of Congress](https://www.loc.gov/collections/fsa-owi-black-and-white-negatives/about-this-collection/) — programme scope, negatives, colour transparencies.
- [FSA-OWI Photographic Prints — Library of Congress](https://www.loc.gov/pictures/collection/fsa/prints.html) — file prints made by the FSA/OWI laboratory, the objects this preset emulates.
- [Dust Bowl — Wikipedia](https://en.wikipedia.org/wiki/Dust_Bowl) — drought waves, "black blizzards", black-or-grey dust, near-zero visibility.
- [FSA cameras — Secondat](http://secondat.blogspot.com/2009/10/fsa-cameras.html) — Lange's 4×5 press and Graflex reflex equipment.

## See Also

- [Decade presets](../../docs/decade.md)
- [WWII Newsreel](../WWII%20Newsreel/) — the same impulse, mobilised for war.
- [Hollywood Glamour](../Hollywood%20Glamour/) — the same decade's silver print, lit from the other end of the scale.
- [Post-War Optimism](../Post-War%20Optimism/) — the American documentary look once the drought broke.
