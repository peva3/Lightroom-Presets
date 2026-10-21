# WWII Newsreel Lightroom Preset — Characteristics

**Category**: Decade

The WWII Newsreel Lightroom preset emulates a 1940s theatrical newsreel frame: hard, near-monochrome black-and-white (global `Saturation -45`) with crushed shadows, a blown highlight shoulder, heavy structured grain, and a cool silver cast. It is the most contrasty preset in the Decade set, built for the look of a release print several generations away from the camera negative.

## Historical Context

Newsreels ran from the 1910s to the late 1960s and were a standard part of a cinema programme, usually preceding the feature. The American series that covered the war were *The March of Time* (1935–1951), *Pathé News*, *Paramount News*, *Fox Movietone News*, *Hearst Metrotone News* and *Universal Newsreel*. Wartime coverage came from two pools: newsreel staff cameramen and the military's own photographic units, whose footage was pooled and re-edited. The result was a house style — urgent, narrated, tightly cut, and technically uneven, because footage shot in the field was intercut with studio-shot and archival material.

## Photographic Technology

- **Format**: 35mm for theatrical newsreels. 16mm was the military field and combat-camera format, and later the television format; a 35mm release print is what audiences actually saw.
- **Stock and base**: 35mm nitrate negative and positive stock. Nitrate was standard until about 1951, is chemically unstable, and shrinks and decomposes — which is why so much surviving newsreel is a duplicate rather than an original.
- **Generations**: camera negative → duplicate negative → release print. Every analogue duplication step adds contrast and grain — "generation loss" in preservation vocabulary — so a 1944 newsreel frame is typically harder and grainier than the negative it came from.
- **Sound**: optical sound-on-film took a strip of the frame, adding to the coarse, dense look.
- **Projection**: carbon-arc projectors on silver screens lifted apparent contrast further and gave highlights a hot, slightly veiled quality. Release prints were neutral silver-gelatin; some were toned sepia for warmth or blue for night.

## Visual Signature

- **Palette**: near-monochrome with a cool bias. `Saturation -45` plus per-hue cuts of −40 to −50, then highlights graded `210° / 5` and shadows `220° / 8` at `Blending 70` — a blue-grey that sits mostly in the shadows. The residual chroma is small enough that the cast reads as silver rather than as colour.
- **Contrast**: hard. `Contrast +35` with `Highlights -50`, `Shadows -10` and `Blacks -25` produces the dense, slightly blocked-up look of a dupe-derived print; `Whites +5` keeps a spark in the highlights.
- **Texture**: heavy and coarse — `GrainAmount 50 / GrainSize 35 / GrainRoughness 70`, at the boundary where the styleguide stops calling roughness organic and starts calling it pushed.
- **Tonal distribution**: bimodal and dark. Big black masses (uniforms, vehicles, night), small hot highlights, and very little midtone separation.

## Tonal Register

**Register**: cool-overcast

The register is cool and hard, matching the blue-grey silver of the preset: `Temperature 5200` shifts the base cool and the grading wheels are both in the 210–220° blue region. Because the image is muted to −45 saturation, the cast is subtle but unmistakable — it is a *look*, not a neutral print emulation, since genuine 1940s release prints were neutral to warm. Validate against a cool, high-contrast, overcast or night original; on a warm golden-hour frame the preset will fight the source and produce a muddy grey-green.

## Lighting & Subject Matter

Available light and flashbulb: overcast beachheads, harsh noon in the desert, searchlights and flares at night, interiors lit by a single bulb. Subject matter is action and aftermath — landing craft, columns on a road, rubble, factory production lines, generals at maps, civilians queueing. Composition is fast and often off-level; the frame is cropped by the camera operator's nerve rather than by a tripod.

## Lightroom Translation

- **Basic**: `Exposure2012 -0.20` for print density; `Contrast2012 +35`; `Highlights2012 -50` to hold the shoulder; `Shadows2012 -10` to deepen the blacks toward dupe-print density; `Whites2012 +5`; `Blacks2012 -25` — the darkest value in the Decade set, still inside the −30 portability floor.
- **Colour**: `Saturation -45` globally, with all eight HSL saturation channels between −40 and −50 so no hue survives as an accent. There are no HSL luminance moves: the preset wants a flat silver response.
- **Color Grading**: highlights `210° / 5`, shadows `220° / 8`, `Blending 70` — cool but restrained; the blend is the lowest in the group so the tint stays out of the midtones.
- **Effects**: `GrainAmount 50 / GrainSize 35 / GrainRoughness 70`; `PostCropVignetteAmount -25`.
- **Detail**: `Sharpness 10`, `LuminanceSmoothing 0`; `Clarity`/`Texture`/`Dehaze` unset.
- **Tone Curve**: neutral on all four channels.

## Verification

Pass; no changes, with two documented caveats.

- **Contrast structure matches the technology**: `+35` contrast with `Shadows -10` and `Blacks -25` correctly models a release print that has been through at least one duplication generation.
- **Grain is at the edge, not over it**: `Roughness 70` is the styleguide's boundary between organic and pushed; `Amount 50` stays under the 60 distribution cap. Acceptable for a format whose grain was genuinely coarse, but this is the preset most likely to look like noise on a small screen.
- **Cool cast — documented as a look**: 1940s release prints were neutral to warm; the blue-grey here is a modern war-film convention, reinforced by `Temp 5200`. At `Saturation -45` the cast is weak enough to pass as silver, and it is retained knowingly.
- **Format note**: `docs/decade.md` calls this "16mm newsreel". Theatrical newsreels were 35mm; 16mm was the military field format. The preset's grain and contrast fit the 35mm release print, so it is unchanged and the doc line is left for a separate edit.
- **Blacks −25** sit near the −30 floor but inside it; on a dim, uncalibrated display the deepest areas will merge — period-correct, worth knowing.
- **Vibrance**: absent from the XMP ("remove Vibrance entirely"); the gap against `Saturation -45` is on the desaturating side and cannot create selective colour.

### Validation Sweep 2026-10-21
- **Verdict:** minor drift, documented
- **Defining traits checked:** near-monochrome via `Saturation -45` plus per-hue desaturation −40 to −50; `Contrast +35`, `Highlights -50`, `Blacks -25`; `Grain 50`; `Vignette -25`; `Temp 5200`.
- **Drift recorded:** cool 210–220° tint is a modern grade, not a period print characteristic; left as a documented stylistic choice because saturation is low enough for it to read as silver.
- **This pass:** no preset change; sourcing and the format note added.

## Sources

- [Newsreel — Wikipedia](https://en.wikipedia.org/wiki/Newsreel) — the format's exhibition context and the major American series, including *The March of Time* and *Universal Newsreel*.
- [Film-Based Negatives and Positives — National Archives](https://www.archives.gov/preservation/holdings-maintenance/film-based) — nitrate negative and positive stock, its instability, and preservation consequences.
- [All about... nitrate film — BFI](https://www.bfi.org.uk/features/all-about-nitrate-film) — nitrate's working life, projection practice and archival handling.
- [Glossary of Technical Terms — FIAF](https://www.fiafnet.org/pages/E-Resources/Technical-Terms-Full-List.html) — definition of "generation loss", the mechanism behind the era's contrast and grain build-up.

## See Also

- [Decade presets](../../docs/decade.md)
- [Dust Bowl Documentary](../Dust%20Bowl%20Documentary/) — the same documentary register, softer and warmer.
- [Hollywood Glamour](../Hollywood%20Glamour/) — wartime-era silver print under studio control.
- [Dramatic Monochrome](../Dramatic-Monochrome/) — the modern high-contrast mono this preset is often mistaken for.
