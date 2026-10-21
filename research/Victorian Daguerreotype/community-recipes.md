# Victorian Daguerreotype Lightroom Preset — Community Recipes & Settings

Ranges for emulating an 1839–1860 silver plate, guided by museum scans and by the small modern revival of working daguerreotypists.

## Reference Looks

The best reference is a high-resolution museum capture of a cased plate (Getty, Library of Congress, Metropolitan Museum): neutral-to-warm silver, extremely fine detail, and a bright, slightly blown face against a dark ground. Contemporary daguerreotypists — Jerry Spagnoli, Mike Robinson, Takashi Arai — publish plates that show the real tonal signature: no grain at all, a hard specular shoulder, and a surface that changes with viewing angle. Because a plate is a mirror, flat scans usually look *lower* in contrast than the object; photographers who grade "daguerreotype" looks typically add contrast back rather than softening. Restoration workflows for cased images concentrate on removing tarnish rings and dust, not on warming the image.

## Slider Starting Points

| Panel | Range | Contribution |
|---|---|---|
| Exposure | −0.4 to −0.1 | Plate density; portraits sit dark |
| Contrast | +20 to +40 | The metallic shoulder — the defining move |
| Highlights | −40 to −20 | Keeps the sheen from clipping to white |
| Shadows | +5 to +20 | Holds dark clothing and studio ground |
| Whites | +5 to +20 | The mirror highlight |
| Blacks | −20 to −10 | Sooty but anchored; never below −30 |
| Clarity | 0 to +10 | Plates are sharp, unlike albumen or platinum |
| Texture | 0 | Detail comes from the lens, not from micro-contrast |
| Dehaze | 0 | No atmospheric veil in a studio |
| Saturation | −55 to −40 | Global mute |
| Vibrance | −5 to 0 | Never positive — it re-colours skin |
| HSL saturation | −55 to −35 per hue | One silver-warm axis only |
| HSL luminance | 0 to +12 (orange, yellow) | Face and collar as the bright passage |
| Color Grade — highlights | Hue 35–45°, Sat 6–12 | Gold-toned warmth, lightly applied |
| Color Grade — shadows | Hue 25–35°, Sat 10–18 | Tarnish brown, not blue |
| Grain | Amount 10–20, Size 30–40, Rough 60–75 | Plate mottle only; high size, low amount |
| Vignette | −45 to −25 | Mat aperture plus lens falloff |

## Common Mistakes

- **Heavy grain.** The process is grainless. Grain above Amount ~25 makes it look like pushed 35mm, which is a different century.
- **Cream-paper albumen warmth.** Daguerreotype silver is neutral at heart; a strong cream cast belongs to albumen prints from the 1860s–90s.
- **Soft focus.** Pictorialist blur is a 1890s idea. Period plates are bitingly sharp in the centre.
- **Ignoring the shoulder.** Without `Highlights` control and `Whites` lift, the mirror highlight either clips or the plate looks like flat grey card.
- **Weak vignette.** The mat and the fast portrait lens both fall off hard; a −10 vignette reads as a modern lens profile.
- **Cool shadows.** Tarnish is brown-black. Blue or teal shadows immediately read as a digital grade.

## See Also

- [Victorian Daguerreotype characteristics](characteristics.md)
- [Daguerreotype (alternative process)](../alt-daguerreotype/)
- [Civil War Era](../Civil%20War%20Era/) — the collodion successor.
