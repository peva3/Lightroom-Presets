# Civil War Era Lightroom Preset — Characteristics

**Category**: Decade

The Civil War Era Lightroom preset reproduces American wet-plate photography of 1861–1865 as the public saw it: a collodion glass negative contact-printed on albumen paper, gold-toned and since browned by age. It is a warm, near-monochrome look with real shadow density and almost no silver grain.

## Historical Context

The war was the first American conflict photographed systematically. Brady's studios sent Gardner, O'Sullivan, Gibson and Barnard into camps and onto battlefields; the views were sold as stereo cards and cartes-de-visite and redrawn as wood engravings for the weeklies, since halftone reproduction did not yet exist. Exposures ran to seconds, so the record is of stillness — posed sitters, camps, ruins, and the dead photographed days later.

## Photographic Technology

- **Negative**: wet collodion on glass (Archer, 1851), which displaced the daguerreotype by the late 1860s. Coating, sensitising, exposure and development had to happen within about fifteen minutes, so field work needed a portable darkroom.
- **Print**: albumen silver print (1850; dominant 1855–1890) — silver salts in an egg-white binder on thin paper, contact-printed in sunlight, usually gold-toned, then mounted on card. Untoned prints are red-brown; gold toning pushes them purple-brown; the albumen yellows with age.
- **Spectral sensitivity**: collodion sees only blue and ultraviolet. Warm colours record dark, cool colours light, and a blue sky and its white clouds expose almost identically — hence blank white skies and the "mourning" look of bright dresses.
- **Resolution**: a large glass negative contact-printed gives exceptional detail and effectively no grain.

## Visual Signature

- **Palette**: one warm axis. Midtones brown-orange, highlights creamy rather than white, shadows a darker red-brown. Chroma is nearly gone but never zero.
- **Contrast**: high, not crushed. Collodion holds shadow detail; albumen paper gives an abrupt bright shoulder. Skies and stone go near-white, uniforms and foliage very dark.
- **Texture**: fine plate and paper irregularity — drying marks, pinholes, the odd comet — not silver grain.
- **Tonal distribution**: weighted low. Large dark masses, a narrow band of luminous faces, blown skies.

## Tonal Register

**Register**: sepia-toned (warm, mid-contrast, low-key weighted)

A warm brown print, not a neutral one, so it is stable on warm and skin-heavy sources: the preset drives every channel onto the same brown axis and removes half the saturation before grading. It is flattest on cool, high-key originals (snow, overcast sky), where the albumen cream has nothing to sit against — validate those separately.

## Lighting & Subject Matter

Hard noon sun, open shade, tent interiors lit by a single skylight, flat north studio light. Subject matter is documentary and formal at once: soldiers in rigid rows, families on porches, pontoon bridges, shattered brick. Faces are the only bright passage.

## Lightroom Translation

- **Basic**: `Exposure2012 -0.35` and `Contrast2012 +18` build collodion density; `Highlights2012 -30` holds the blank sky; `Shadows2012 +8` recovers blocked detail; `Whites2012 -5` and `Blacks2012 -15` anchor both ends.
- **Colour**: `Saturation -50` does the global mute, with per-hue HSL saturation between −35 and −45 so no hue survives as an accent. `LuminanceAdjustmentOrange +8` lifts faces. `Temperature 5800` supplies paper warmth.
- **Color Grading**: highlights `38° / 12`, shadows `30° / 12`, `Blending 80` — albumen brown in both zones, redder in the shadows.
- **Effects**: `PostCropVignetteAmount -35`; `GrainAmount 20 / GrainSize 25 / GrainRoughness 50` for plate-and-paper surface.
- **Detail**: `Sharpness 10`, `LuminanceSmoothing 0`; Clarity/Texture/Dehaze unset.
- **Tone Curve**: neutral on all four channels; contrast comes from the Basic panel.

## Verification

Pass after one correction.

- **Grain**: the preset carried `60 / 40 / 75`, the styleguide's *pushed Tri-X* band, on a process with no silver grain. Changed to **20 / 25 / 50**, so texture reads as plate and paper. Nothing else touched.
- **Contrast**: `+18` reproduces the albumen density range; the earlier flat `-10` rendering is gone.
- **Warm axis**: `38°/12` and `30°/12` sit inside the albumen red-brown to purple-brown range; `Highlights -30` and `Whites -5` keep the paper creamy rather than clipped.
- **Vibrance**: not written to the XMP at all, which meets the rule's "remove Vibrance entirely" alternative. The 50-point gap against `Saturation -50` is on the desaturating side, so it cannot lift a hue out of the mono; setting Vibrance to match would double-desaturate.
- **Not changed — Temperature 5800**: absolute WB is a portability risk; retained because the albumen cast needs a warm start and there is no aggressive HSL to cascade with it.

### Validation Sweep 2026-10-21
- **Verdict:** minor drift → resolved
- **Checked:** `Saturation -50` plus per-hue −35 to −45; warm 30–38°, `Temp 5800`; `Vignette -35`.
- **Prior fix kept:** `Contrast +18`, `Shadows +8`. **This pass:** grain moved from pushed-film to fine-grain values.

## Sources

- [Civil War Glass Negatives and Related Prints — Library of Congress](https://www.loc.gov/pictures/collection/cwp/civilwarphotos.html) — the wet-plate workflow and surviving negatives.
- [Civil War Photographs: New Technologies and New Uses — Library of Congress](https://www.loc.gov/classroom-materials/civil-war-photographs-new-technologies-and-new-uses/) — albumen printing and press distribution.
- [Collodion process — Wikipedia](https://en.wikipedia.org/wiki/Collodion_process) — blue/UV-only sensitivity, the fifteen-minute window, blank skies.
- [Albumen silver print — MoMA](https://www.moma.org/collection/terms/albumen-silver-print) — binder, gold toning, the warm-yellow to purple shift.
- [Photographic Prints — PSAP, University of Illinois](https://psap.library.illinois.edu/collection-id-guide/photoprint) — yellowing and fading of albumen prints.

## See Also

- [Decade presets](../../docs/decade.md)
- [Albumen Print](../alt-albumen-print/) — the print half, pushed further toward paper yellow.
- [Wet Plate Ambrotype](../alt-wet-plate-ambrotype/) — plate texture instead of paper.
- [Victorian Daguerreotype](../Victorian%20Daguerreotype/) — the preceding process and its tighter range.
