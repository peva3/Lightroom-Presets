# Kodak T-Max 400 — Lightroom Preset Settings & Recipes

## Primary Source: Fuji X Weekly (August 2020)

Created collaboratively by Thomas Schwab, Anders Lindborg, and Ritchie Roesch. Derived from the Kodak Tri-X 400 recipe but modified to capture T-Max 400's cleaner, sharper character.

### Recipe
- **Film Simulation**: Monochrome (+Y, +R, +G)
- **Dynamic Range**: DR200
- **Highlight**: 0
- **Shadow**: +3
- **Noise Reduction**: -4
- **Sharpening**: +2
- **Clarity**: +3
- **Toning**: WC +2, MG 0
- **Grain Effect**: Strong, Small
- **Color Chrome Effect**: Strong
- **Color Chrome Effect Blue**: Off
- **White Balance**: Daylight, +9 Red & -9 Blue
- **ISO**: Auto, up to ISO 6400
- **Exposure Compensation**: +1/3 to +1 (typically)

Source: https://fujixweekly.com/2020/08/31/

### Compatibility Notes
- X-Trans III cameras without Clarity: use +1 Highlight and +4 Shadow instead
- X-Trans III cameras without Grain size: set Grain to Strong
- X-T3/X-T30 Toning: use +1 (warm) instead of the WC+2, MG 0

### LR Preset Design Notes
- Derived from Tri-X recipe base, modified for T-Max character
- Shadow +3 creates deep, rich blacks characteristic of T-Max
- Clarity +3 in Fuji recipe adds midtone structure — in our XMP this is zeroed per STYLEGUIDE grain rule
- Sharpness +2 in Fuji → our XMP uses Sharpness=10 per grain+sharpening rule
- Toning WC+2 adds slight warmth reminiscent of darkroom sepia toning
- Our XMP uses neutral ColorGrade wheels (no toning) — Adobe Monochrome profile provides clean baseline
- Grain is Strong/Small in Fuji terms → moderate GrainAmount=45, GrainSize=30

---

## See Also

- [Kodak T Max 400 — Film Characteristics](../Kodak-T-Max-400/characteristics.md)
- [Kodak T Max 100 Lightroom Preset](../Kodak-T-Max-100/community-recipes.md)
- [Kodak T Max 3200 Lightroom Preset](../Kodak-T-Max-3200/community-recipes.md)
- [Kodak Tri X 400 Lightroom Preset](../Kodak-Tri-X-400/community-recipes.md)
