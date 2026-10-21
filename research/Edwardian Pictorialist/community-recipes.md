# Edwardian Pictorialist Lightroom Preset — Community Recipes & Settings

Ranges for a 1900s platinum-toned pictorial print, based on what contemporary platinum printers produce and on how the movement's prints behave next to modern soft-focus grades.

## Reference Looks

Contemporary platinum/palladium printers (Bostick & Sullivan's published work, the platinum rooms of the Met and Art Institute) show the target clearly: matte, warm-neutral, no true black, and a very long gradation from paper white to a soft brown-black. Modern "dreamy" or "soft glow" grades — Orton effect, negative Clarity, bloom plug-ins — get the diffusion right and the tone wrong: they usually add a warm haze *and* keep a hard black floor, which is the opposite of a platinum print. The closest modern analogue is a well-printed 8×10 contact print scanned flat, not a blurred digital file. Emulation packs for the pictorialists tend to pair negative Clarity with a lifted black point; that pairing, not the blur, is what sells the period.

## Slider Starting Points

| Panel | Range | Contribution |
|---|---|---|
| Exposure | 0 to +0.3 | Prints are made light, not dense |
| Contrast | −25 to −5 | Long scale; contrast is the enemy of softness |
| Highlights | −50 to −25 | Slow shoulder, no clipping |
| Shadows | +15 to +30 | Open shadows; pictorialists dodged them in |
| Whites | −5 to +5 | Paper white, slightly warm |
| Blacks | 0 to +10 | **Must stay positive** — platinum has no true black |
| Clarity | −30 to −15 | The diffusion |
| Texture | −15 to 0 | Secondary softening; use one band primarily |
| Dehaze | −15 to −5 | Atmospheric veil, mist and bloom |
| Saturation | −20 to −5 | Near-neutral; a heavy mute kills the platinum warmth |
| Vibrance | −5 to 0 | Keep within a few points of Saturation |
| HSL saturation | Green −35 to −20, Blue −35 to −20 | Quiet foliage and sky |
| HSL luminance | 0 to +10 (orange) | Keep faces from going grey |
| Color Grade — highlights | Hue 35–45°, Sat 5–12 | Warm black, lightly |
| Color Grade — shadows | Hue 25–40°, Sat 5–12 | Neutral-warm; blue-black is also period-correct |
| Grain | 0 to 10 | Contact print — effectively none |
| Vignette | −30 to −15 | Gentle; a hard vignette is a modern tell |

## Common Mistakes

- **Keeping a black floor.** `Blacks` at −20 or a normal S-curve destroys the platinum signature. The deepest tone must sit above black.
- **Over-fogging.** Negative Clarity beyond about −30 plus negative Dehaze produces milk, not atmosphere; the print stops having a subject.
- **Sepia-by-default.** Platinum ranges from warm black to blue-black. A fixed brown is a claim the process does not support.
- **Adding grain.** These are contact prints from large negatives. Grain instantly reads as 35mm.
- **Positive Clarity/Texture.** The HDR look is the exact inverse of pictorialism; it also fights the diffusion already applied.
- **Blurring instead of veiling.** A Gaussian-blur style effect removes structure; a real soft-focus lens preserves it and blooms only the highlights.

## See Also

- [Edwardian Pictorialist characteristics](characteristics.md)
- [Platinum Print](../alt-platinum-print/) — the process at full strength.
- [Gum Bichromate](../alt-gum-bichromate/) — pigment texture rather than platinum smoothness.
