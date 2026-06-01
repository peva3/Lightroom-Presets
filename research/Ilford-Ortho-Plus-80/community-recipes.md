# Ilford Ortho Plus 80 — Community B&W Recipes

## Source: Ilford Technical Data + Community Practice

Ortho Plus 80 is a modern orthochromatic film — the unique spectral sensitivity demands a fundamentally different B&W mix approach than panchromatic films.

### Orthochromatic B&W Mix Translation

The key to ortho emulation: **zero red sensitivity**. Red channel must go near-black (negative values on Red Mixer). Blue channel goes very bright (positive values). Green channel goes bright for the luminous foliage effect.

#### Basic Panel
- **Exposure**: 0 (neutral — ISO 80 baseline)
- **Contrast**: +18 (medium — ortho films have distinctive midtone contrast)
- **Highlights**: -15 (controlled — ortho highlights can wash out blue sky)
- **Shadows**: +10 (moderate shadow lift — ortho shadows are clean)
- **Whites**: +5 (clean white point)
- **Blacks**: -10 (gentle black point)

#### B&W Mix (ConvertToGrayscale=True)
Orthochromatic sensitivity pattern: High blue+green sensitivity, ZERO red sensitivity.

| Color | Value | Rationale |
|-------|-------|-----------|
| Red | -40 | Strongly negative — red = black in ortho! |
| Orange | -25 | Low red sensitivity — warm objects darken |
| Yellow | +10 | Moderate sensitivity — warm highlights |
| Green | +25 | High sensitivity — luminous, bright foliage |
| Aqua | +20 | Blue-green — bright skies, cyan objects |
| Blue | +30 | Highest sensitivity — bright/white skies! |
| Purple | +5 | Mixed red+blue — net effect balanced |
| Magenta | -15 | Red+blue mix — red component darkens more |

#### Color Grading (Warm paper base split — vintage darkroom aesthetic)
- **Highlights**: Hue 40°, Sat 5 (warm paper base)
- **Shadows**: Hue 220°, Sat 5 (cool shadow ink)
- **Blending**: 50
- **Balance**: -10 (slight shadow bias)

#### Grain (Fine-grain ISO 80: Amount 15-25, Size 15-25, Roughness 40-55)
- **Amount**: 20 (fine grain — modern ISO 80)
- **Size**: 20 (small particles)
- **Roughness**: 45 (regular structure)

#### STYLEGUIDE Compliance
- No Calibration
- No Temperature/Tint
- Sharpness=10, Clarity=0, Texture=0, Dehaze=0 (grain protection)
- LuminanceSmoothing=0
- ProcessVersion 15.4, Treatment=Monochrome, ConvertToGrayscale=True
- Adobe Monochrome Look UUID 0C09521111114111B1115456789ABCDE
- Blacks -10 ≥ -30

## Community Notes

### Practical Ortho Emulation Limits in Lightroom
Lightroom's B&W Mix cannot fully replicate orthochromatic vision because:
1. **No per-wavelength sensitivity curve**: The Mix reduces to 8 fixed color channels, not a continuous spectral response
2. **Red objects already captured**: Lightroom converts from a full-color RAW — red data exists and must be darkened, rather than never being recorded
3. **Metamerism**: Some red objects may not darken as expected because of how LR maps color channels

### Creating the "Ortho Look"
For the most convincing ortho effect:
1. Red Mixer strongly negative (-40 to -50)
2. Blue and Green Mixers strongly positive
3. Contrast slightly elevated — ortho films were historically higher contrast
4. Accept that the result is an approximation of ortho character

### Historical Context
- Orthochromatic films were standard until panchromatic films became widespread in the 1930s
- The ortho "look" is the visual language of early 20th century photography
- Dark red lips (black), bright skies, and luminous foliage are the ortho hallmarks

## Sources
- Ilford Ortho Plus 80 technical data sheet
- Orthochromatic film photography community (Flickr, Photrio)
- Historical photographic process references
