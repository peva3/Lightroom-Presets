# Hollywood Glamour Lightroom Preset — Characteristics

**Category**: Decade

The Hollywood Glamour Lightroom preset recreates the toned studio portrait print of the 1930s and early 1940s: creamy high-key skin, soft diffusion bloom, gently lifted blacks and a warm sepia-leaning grade. It deliberately *removes* contrast, because the contrast in a Hurrell portrait was built by the lighting before the shutter opened.

## Historical Context

George Hurrell (1904–1992) was hired by MGM publicity at twenty-five and became the studio's principal portraitist; between 1930 and his 1942 draft he defined what a film star looked like ([National Portrait Gallery](https://npg.si.edu/exhibition/star-power)). He worked on an 8×10 view camera, often at shutter speeds slow enough that sitters held a pose ([Digital Field Guide](https://www.digitalfieldguide.com/blog/5473)). He invented the boom light and built portraits from designed shadows rather than floodlight — "the most essential thing about my style was working with shadows to design the face instead of flooding it with light" ([New Zealand Geographic](https://www.nzgeo.com/photography/starlet-express/)).

The style was commercial fantasy with a purpose: during the Depression the studios sold escape ([Walt Disney Family Museum](https://www.waltdisney.org/exhibitions/lights-camera-glamour-photography-george-hurrell)). Retouching was industrial — Hurrell worked graphite into the negative, removing blemishes and drawing highlights; Harlow's eyelashes in the 1935 portrait are pencil work ([California Heritage Museum](https://californiaheritagemuseum.org/lights-camera-glamour)). Prints were often sepia-toned ([LA Times](https://www.latimes.com/entertainment/tn-cpt-0301-george-hurrell-laguna-20130228-story.html)). The era ended with the equipment: postwar candid small-format work displaced the studio portrait — "When we stopped using those 8 x 10 cameras," Hurrell said, "the glamour was gone" ([NPG](https://npg.si.edu/exhibition/star-power)).

## Photographic Technology

The most misunderstood variable is the film. **Orthochromatic** emulsions — dominant until about 1927 — were blind to red, so lipstick rendered almost black, ruddy cheeks went dark and blue eyes went pale; panchromatic film rendered tones closer to human vision ([Cabinet](https://www.cabinetmagazine.org/issues/51/archibald.php); [Film Photography Project](https://filmphotographyproject.com/panchromatic-orthochromatic-film/)).

Hurrell used ortho early and then ran out of it. Mark Vieira's account has him switching around 1931 to panchromatic portrait stocks that gave skin "a creamy rather than burnished look" ([quoted at Photrio](https://www.photrio.com/forum/threads/the-hurrell-style-book-bad-information.84669/page-2)). So "Hollywood glamour skin" is a *panchromatic* characteristic — a distinction most digital imitations get backwards.

Everything else added glow: uncoated lenses produced halation, film was underexposed and over-developed, and the negative was retouched by hand ([Digital Field Guide](https://www.digitalfieldguide.com/blog/5473)). The key was "butterfly" or Paramount lighting — a hard source above and in front of the face, the nose shadow a design element.

## Visual Signature

Creamy, slightly luminous skin; highlights that roll off instead of clipping; a soft bloom around edges and speculars; shadows open and warm rather than black; whites that stay white in the gown but never paper-white in the face. Colour is suppressed, so the image reads as toned monochrome.

## Tonal Register

**Register**: high-key, sepia-toned

At +0.35 EV with Whites +10, Blacks +5 and Shadows +25 the preset has no true black and no crushed shadow: the range is compressed upward, as a retouched, diffused, toned print is. The grade is warm at both ends (highlight 38/8, shadow 30/5), so sepia comes from a consistent gold cast rather than a split.

## Lighting & Subject Matter

Hard fresnel key from above, a kicker on the shadow side, hair and background lights, often a fill card. Subject matter is head-and-shoulders or three-quarter studio portraits: white chiffon, fur, feathers, faces held still for a one-second exposure.

## Lightroom Translation

| Panel | Value | Function |
|---|---|---|
| Basic | Exposure +0.35, Contrast -5 | High-key density; no double-grading of a hard-lit face |
| Basic | Highlights -40, Whites +10 | Holds the white gown and the cheek specular |
| Basic | Shadows +25, Blacks +5 | Open shadow side; lifted black point = toned print |
| Clarity | Clarity -10 | Diffusion bloom of an uncoated lens and retouching |
| HSL | Orange Lum +12, Orange Sat -5 | Creamy, less ruddy skin — the panchromatic reading |
| HSL | Blue -8, Green -10, Yellow +5 | Suppresses ambient colour; mid-tone warmth |
| Color Grading | Highlight 38/8, Shadow 30/5, blend 75 | Consistent sepia cast across the range |
| Effects / Detail | Vignette -12, Sharpness 10, Grain 0 | Studio falloff; retouched 8×10 has no grain |

## Verification

**Structural**: Color treatment, PV 15.4, Adobe Color Look, neutral curves, no Calibration, no WB cast. Grain is 0, so the grain rule is not engaged; Clarity -10 is the defining diffusion. Blacks +5 sits above the -30 floor by design; HSL peaks at ±10.

Contrast -5 looks like a contradiction for a photographer famous for "dramatic high contrasts between lights and darks" ([Digital Field Guide](https://www.digitalfieldguide.com/blog/5473)). It is not: Hurrell's contrast lived in the lighting and in over-development of the negative, both already present in a photograph of a hard-lit face. A preset that adds contrast afterwards produces a look no 1930s print has.

### Validation Sweep 2026-10-21
- **Verdict:** accurate
- **Defining traits checked:** Hurrell-era studio print: high key (+0.35 EV), lifted blacks (+5), Clarity -10 for diffusion bloom, GrainAmount 0 (retouched 8x10), warm 30-38deg with orange luminance +12.
- **Sources:** George Hurrell / MGM glamour portraiture references; 1930s nitrate print characteristics
- **Preset adjustments:** none

**Review 2026-10-21 (research pass).** The ortho/panchromatic sourcing supports the creamy-skin reading, not a high-contrast one. No XMP changes made.

## Sources

- [Star Power: George Hurrell — National Portrait Gallery](https://npg.si.edu/exhibition/star-power) — MGM tenure, 8×10 prints.
- [Lights! Camera! Glamour! — Walt Disney Family Museum](https://www.waltdisney.org/exhibitions/lights-camera-glamour-photography-george-hurrell) — boom light, the "Hurrell style".
- [Lights! Camera! Glamour! — California Heritage Museum](https://californiaheritagemuseum.org/lights-camera-glamour) — graphite retouching.
- [Hurrell Lighting — Digital Field Guide](https://www.digitalfieldguide.com/blog/5473) — ortho vs pan, halation, butterfly lighting.
- [Making Up Hollywood — Cabinet](https://www.cabinetmagazine.org/issues/51/archibald.php) — orthochromatic dominance to 1927.
- [Starlight and Shadow — The Atlantic](https://www.theatlantic.com/magazine/archive/2007/07/starlight-and-shadow/305978/) — Hurrell's 1930–42 vocabulary.

## See Also

- [Decade presets](../../docs/decade.md)
- [Gatsby Art Deco](../Gatsby%20Art%20Deco/characteristics.md) — interwar glamour in colour
- [Edwardian Pictorialist](../Edwardian%20Pictorialist/characteristics.md) — the earlier soft-focus tradition
- [WWII Newsreel](../WWII%20Newsreel/characteristics.md) — the register that replaced studio portraiture
