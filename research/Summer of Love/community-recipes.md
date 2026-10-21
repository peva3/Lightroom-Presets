# Summer of Love — Community Lightroom Recipes

Community settings for a 1967 Haight-Ashbury colour look, compiled from r/analog and r/postprocessing threads, Film Simulation recipes for Ektachrome and Kodachrome, and the published settings photographers post alongside 1960s slide scans. The consensus is narrow: warm, soft, slightly lifted, and much less saturated than the poster art the decade is remembered for.

## Reference Looks

- **Charles Cushman, San Francisco 1967** — Kodachrome street colour: warm skin, olive foliage, small magenta fringes at the frame edge. The closest thing to a colour reference for the summer.
- **Gene Anthony's Haight Street frames** — over-exposed highlights, flare, loose framing; the whites bloom rather than clip.
- **Fillmore poster art (Wilson, Moscoso)** — useful for accent hue *choice* (magenta, yellow) but not for saturation level. Treat as a palette, not an exposure target.
- **Family Kodacolor-X prints** — muddy shadows, warm cast, low acutance. Use when the source image is soft or low-resolution.

## Slider Starting Points

| Panel | Range | Notes |
|---|---|---|
| Exposure | +0.10 to +0.35 | Push toward the highlight; do not clip sun discs |
| Contrast | −10 to 0 | The era's prints are flat; contrast comes from flare |
| Highlights | −30 to −50 | Essential when the sun is in frame |
| Shadows | +20 to +35 | Shaded faces need opening |
| Blacks | 0 to +10 | **Lifted** — a negative black point is wrong here |
| Temperature | 5600 to 5900 | Mild; stop before skin goes orange |
| Saturation / Vibrance | +5 to +12, within 5 of each other | Global cut-and-boost, never HSL alone |
| HSL Green | Hue −15 to −5, Sat −25 to −15 | Olive foliage |
| HSL Magenta | Sat +10 to +20 | The signature accent |
| Color Grading | Highlight 45–55 / 8–12; Shadow 35–45 / 6–10 | Warm both ends |
| Clarity / Dehaze | −15 to −5 / −10 to 0 | Bloom and veiling; never positive Dehaze |
| Grain | 0 | Slide film is fine-grained |

## Common Mistakes

- **Chasing poster saturation.** Acid greens and hot magenta belong to screen-printed posters, not 1967 colour film. Oversaturating produces a modern "vintage filter", not an era.
- **Crushing blacks.** The faded-slide look depends on a lifted black point; Blacks −20 or lower is a contemporary contrast grade.
- **Letting Vibrance run ahead of Saturation.** A 15-point gap creates the selective-colour effect the styleguide warns about.
- **Adding heavy grain.** Kodachrome II and Ektachrome are fine-grained stocks; Grain 40+ reads as a 1990s zine.
- **Positive Dehaze.** It removes the veiling and halation that make the look feel like film through a consumer lens.
- **Grading in light leaks.** They were camera faults — thin foam seals, hinged backs. Add them as a physical overlay, not a global shift.

## See Also

- [Summer of Love — Characteristics](characteristics.md)
- [Kodachrome Mid-Century](../Kodachrome%20Mid-Century/characteristics.md)
- [Cross-Processed](../Cross-Processed/characteristics.md)
- [Decade presets](../../docs/decade.md)
