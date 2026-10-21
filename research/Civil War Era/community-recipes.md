# Civil War Era Lightroom Preset — Community Recipes & Settings

Ranges for recreating 1860s collodion-and-albumen photography, drawn from contemporary wet-plate practice and from photo-restoration workflows.

## Reference Looks

Working collodion photographers (Shane Balkowitsch, Sally Mann, Joni Sternbach) show what the process actually does: very fine detail, a warm-to-neutral image on glass or metal, uneven pouring marks at the edges, no grain. High-resolution scans of original albumen prints at the Library of Congress and Getty are the colour reference — check the paper margin, which is cream, and the shadows, which are warm brown rather than black. Restoration studios work the opposite direction, subtracting yellowing and foxing; their before/after pairs show how far a period print drifts warm.

## Slider Starting Points

| Panel | Range | Contribution |
|---|---|---|
| Exposure | −0.5 to 0 | Dense negative printed down |
| Contrast | +10 to +25 | Albumen's long straight line |
| Highlights | −40 to −20 | Blank sky instead of clipped white |
| Shadows | 0 to +15 | Collodion holds shadow detail |
| Whites | −10 to 0 | Cream paper, not 255 |
| Blacks | −20 to −5 | Anchor only; −30 is the floor |
| Clarity | −10 to 0 | Period lenses were soft-edged |
| Texture | −10 to 0 | One frequency band only |
| Dehaze | 0 to +5 | Clears scanner haze |
| Saturation | −60 to −40 | The primary move; must be global |
| Vibrance | −5 to 0 | Positive values re-invent selective colour |
| HSL saturation | −50 to −25 per hue | Keep every channel on one warm axis |
| HSL luminance | 0 to +12 (orange) | Faces as the bright passage |
| Grade — highlights | Hue 30–45°, Sat 8–15 | Albumen cream |
| Grade — shadows | Hue 20–35°, Sat 8–18 | Warm brown, never blue |
| Grain | Amount 15–30, Size 20–30, Rough 40–55 | Plate and paper surface |
| Vignette | −40 to −20 | Mat and fast-lens falloff |

Grain above Amount 30 or Size 35 stops reading as paper and starts reading as pushed Tri-X.

## Common Mistakes

- **Heavy grain.** Collodion on glass is grainless; grain is a 20th-century film signature.
- **Greyscale first.** A mono conversion loses the albumen and gold-toning cast. Mute in colour, then grade warm.
- **Orange "vintage" sepia.** Period prints are red-brown to purple-brown on cream. Keep highlight saturation under ~15.
- **Crushing blacks.** Prints have dense but visible shadow detail; below −30 looks digital.
- **Positive Clarity or Dehaze.** Micro-contrast no 1860s lens or contact print produced.
- **Recovering a blue sky.** Collodion was blind to red and over-sensitive to blue; period skies are blank paper.
- **One global tint.** Let highlight and shadow wheels differ by 5–10° or it reads as a filter.

## See Also

- [Civil War Era characteristics](characteristics.md)
- [Albumen Print](../alt-albumen-print/) — deeper paper yellow.
- [Wet Plate Ambrotype](../alt-wet-plate-ambrotype/) — plate texture, not print texture.
