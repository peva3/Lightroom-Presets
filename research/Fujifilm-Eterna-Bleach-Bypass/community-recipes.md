# Fujifilm Eterna Bleach Bypass — Community Recipes

## Source: Extrapolation from Fuji X Weekly Eterna + Bleach Bypass recipes

### Rationale
This preset combines:
1. **Eterna base characteristics**: Low native contrast, warm color cast, soft highlight rolloff
2. **Bleach bypass processing effects**: Silver retention → high contrast, heavy desaturation, metallic highlights, gritty grain

No single Fuji X Weekly recipe exists for Eterna + Bleach Bypass combined. This preset synthesizes the Eterna Summer recipe with bleach bypass processing effects documented in the STYLEGUIDE (Section XI.D).

### Fuji → Lightroom Translation
| Element | LR Attribute | Value | Source |
|---|---|---|---|
| BB Contrast | Contrast2012 | +55 | Bleach bypass formula (reduced from +70 for Eterna base) |
| BB Highlights | Highlights2012 | -60 | Standard bleach bypass shoulder compression |
| BB Shadows | Shadows2012 | -20 | Silver retention crushes shadows |
| Eterna Warmth | ColorGrade Shadow H40/S6 | via grading | Eterna warm cast in shadows |
| BB Metallic | ColorGrade Shadow H220/S12 | via grading | Cool metallic silver character |
| Desaturation | Saturation | -20 | Global desaturation from silver masking |
| Channel Desat | HSL Sat (all 8) | -15 to -40 | Per-channel desaturation hierarchy |
| Grain | GrainAmount/Size/Freq | 40/35/60 | Coarser than standard Eterna (silver grain) |

### Key Design Decisions
1. **Contrast +55 (not +70)**: Eterna's softer base stock produces less aggressive contrast even with bypass
2. **Warm-cool split in color grading**: Shadows carry the cool metallic silver character (H220), highlights retain Eterna's warmth (H50)
3. **Blacks at 0**: Per Creative category double-fade prevention — the cinematic curve already lifts blacks
4. **Grain coarser than Eterna**: Silver particles add visible grain structure beyond the base film grain
5. **All 8 HSL channels desaturated**: True bleach bypass reduces all colors, with hierarchy of retention (blues > reds > greens)

### Comparison to Existing Bleach Bypass Preset
The existing `Bleach Bypass.xmp` uses Contrast +70 and Clarity +45. The Eterna variant reduces both (Contrast +55, Clarity 0) to respect the Eterna base's softer character while keeping the silver retention look.
