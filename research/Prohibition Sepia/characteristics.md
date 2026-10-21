# Prohibition Sepia Lightroom Preset — Characteristics

**Category**: Decade

The Prohibition Sepia Lightroom preset renders the 1920s as its readers saw it in print: warm brown-black photographs on cream paper, reproduced in a rotogravure section. It is a flash-lit, smoky look with hot highlights, sooty-but-open shadows, and a single warm axis from paper white to black.

## Historical Context

Prohibition ran from 1921 to 1933 under the Eighteenth Amendment, and it coincided with the great expansion of the illustrated daily press. Photographs reached mass audiences as glossy silver prints sold to papers and agencies, and as rotogravure reproductions printed at high speed on newsprint — the process that gave the 1920s its soft, brown-black pictorial page. The subject was urban and nocturnal: raids and seizures, speakeasy interiors, dance halls, prizefights, gangsters on courthouse steps, and the deadpan police portrait.

## Photographic Technology

- **Camera**: the 4×5 press camera, above all the Graflex Speed Graphic — focal-plane shutter for action, fast barrel lens for available light, handheld and flash-dependent.
- **Light**: flash powder, then the disposable flashbulb from about 1929–30. Flash gave press photographs their signature: a hard, close, single-source burst that blows out collars and drops the background to near-black.
- **Negative**: 4×5 nitrate sheet film, orthochromatic or early panchromatic. Nitrate is chemically unstable, which is why so many 1920s negatives are yellowed or degraded.
- **Print**: glossy gelatin silver, often sepia-toned or printed warm, then halftoned or gravure-printed. Toned silver converts to brown silver sulphide; the paper base is cream rather than white.
- **Optics**: wide-open press lenses are soft at the edges and vignette slightly; nothing in a 1920s frame is sharp corner to corner.

## Visual Signature

- **Palette**: one warm axis, 30–40° in both highlight and shadow. Blues and greens are removed — blue −60, green −55, at the repo's HSL cap — because a sepia print has no cool chroma left. Yellow is pushed 5° toward orange.
- **Contrast**: moderate and *lifted*. `Highlights -40` holds the burnt collar, `Shadows +20` opens the room, `Blacks -10` keeps a paper anchor: the legible tonal range of a newspaper reproduction, not a moody grade.
- **Texture**: visible but structured grain (`40 / 32 / 65`) — sheet film enlarged for print, plus halftone dot.
- **Tonal distribution**: bright faces, shirtfronts and glassware against dark suits and dark rooms.

## Tonal Register

**Register**: sepia-toned

Warm and mid-contrast, but nearly register-independent: muting saturation by 45 points and grading both wheels into the same 30–38° band removes most of the source's colour temperature. It is deliberately *not* low-key — `Shadows +20` means a dark speakeasy still reads as a print rather than a silhouette. Validate on a flash-lit or hard-light frame; flat overcast originals lose the hot-highlight/dark-ground structure the era depends on.

## Lighting & Subject Matter

Flash powder and bare bulbs: hard frontal light, hot speculars on bottles and brass, smoke in the beam, hat brims cutting the eyes. Poses are either stiffly formal (the blotter portrait) or caught mid-gesture (the raid, the dance floor). Backgrounds are unimportant and dark.

## Lightroom Translation

- **Basic**: `Exposure2012 -0.15`, `Contrast2012 +15`; `Highlights2012 -40` for flash burn; `Shadows2012 +20` for interiors; `Whites2012 -5`, `Blacks2012 -10` to hold the paper base.
- **Colour**: `Saturation -45` carries the global mute; HSL alone cannot. HSL saturation runs from −10 on orange (skin left alive) to −60 blue and −55 green, wiping the cool end. `HueAdjustmentYellow -5` walks yellow toward orange, warming paper and lamplight.
- **Color Grading**: highlights `38° / 15`, shadows `35° / 18`, `Blending 80` — warm in both zones, differing only in saturation.
- **Effects**: `GrainAmount 40 / GrainSize 32 / GrainRoughness 65`; `PostCropVignetteAmount -20`.
- **Detail**: `Sharpness 10`, `LuminanceSmoothing 0`; Clarity/Texture/Dehaze unset.
- **Tone Curve**: neutral on all four channels.

## Verification

Accurate; no changes.

- **Sepia construction**: global `Saturation -45` plus per-hue cuts, `38°/15` and `35°/18` grading, and `Temp 6000` produce brown-black on cream, not an orange filter.
- **Flash signature**: `Highlights -40` with `Shadows +20` is the correct pairing for hard flash with smoke in the room — lifted shadows, not crushed (`Blacks -10`).
- **Dehaze deliberately 0**: the stub called this "smoke haze", but haze here belongs to the room, not the print; press photographs were flash-lit at a few metres, which defeats atmospheric veiling. Negative Dehaze over Grain 40 would only muddy the midtones.
- **HSL at the cap**: blue −60 and green −55 sit exactly on ±60; intentional, since less leaves a cyan cast in the shadows.
- **Vibrance**: absent from the XMP, satisfying the "remove Vibrance entirely" alternative; the 45-point gap against `Saturation -45` is on the desaturating side and cannot create selective colour.
- **Not changed — Temperature 6000**: absolute WB, so results vary with the raw's as-shot balance; retained because the brown axis assumes a warm neutral.

### Validation Sweep 2026-10-21
- **Verdict:** accurate
- **Checked:** `Saturation -45` with per-hue −35 to −60; warm 30–38°, `Temp 6000`; `Grain 40`; `Vignette -20`; `Contrast +15`.
- **Preset adjustments:** none.

## Sources

- [The Rotogravure Process — Library of Congress](https://www.loc.gov/collections/world-war-i-rotogravures/articles-and-essays/the-rotogravure-process/) — high-speed gravure on newsprint, the brown-black pictorial page.
- [Press Cameras: A Stroll Through the Early Years of Press Photography — Macfilos](https://www.macfilos.com/2017/04/13/2017-4-12-press-cameras-a-stroll-through-the-early-years-of-press-photography/) — Speed Graphic and flash-era working method.
- [The Old Speed Graphic Is Alive and Clicking — The New York Times, 1986](https://www.nytimes.com/1986/06/15/arts/camera-the-old-speed-graphic-is-alive-and-clicking.html) — the camera's grip on photojournalism.
- [Photographic Prints — PSAP, University of Illinois](https://psap.library.illinois.edu/collection-id-guide/photoprint) — silver toning, yellowing and the warm period base.

## See Also

- [Decade presets](../../docs/decade.md)
- [WWII Newsreel](../WWII%20Newsreel/) — the next war's monochrome, far cooler.
- [Hollywood Glamour](../Hollywood%20Glamour/) — same technology, lit instead of flashed.
- [Bromoil](../alt-bromoil/) — a period print process with similar warm density.
