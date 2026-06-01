# Ilford SFX 200 — Community B&W Recipes

## Source: Ilford Technical Data + IR Photography Community

SFX 200 is a near-infrared extended-red B&W film. The preset simulates the "with R72 filter" look: white foliage, near-black skies, luminous landscapes. Without a filter, SFX behaves like slightly extended-red panchromatic film — but the defining look is the IR Wood Effect.

### Near-IR B&W Mix Translation

IR effect: Chlorophyll-rich vegetation reflects IR → bright white. Blue skies absorb IR → near-black. Red/orange objects brighten. This requires extreme B&W Mix values.

#### Basic Panel
- **Exposure**: +0.15 (slight brightness — IR scenes can be dark)
- **Contrast**: +25 (high contrast — dramatic IR look)
- **Highlights**: -20 (protect bright foliage highlight detail)
- **Shadows**: +10 (open IR shadow detail)
- **Whites**: +15 (bright foliage — the Wood Effect white)
- **Blacks**: -18 (deep IR black skies)

#### B&W Mix (ConvertToGrayscale=True)
Near-IR sensitivity pattern: Bright vegetation (green→red shift), dark blue skies, bright warm tones.

| Color | Value | Rationale |
|-------|-------|-----------|
| Red | +35 | Extended red sensitivity — warm objects brighten |
| Orange | +30 | Strong IR reflectance in warm tones |
| Yellow | +25 | Bright warm highlights — IR Wood Effect |
| Green | +40 | Chlorophyll IR reflection → brilliant white foliage! |
| Aqua | +15 | Mixed blue-green — moderate IR response |
| Blue | -35 | Strongly negative — blue sky = near-black in IR |
| Purple | -10 | Mixed red+blue — red component brightens |
| Magenta | -5 | Slightly negative — neutral tonal balance |

#### Color Grading (Warm selenium tone — classic IR darkroom print)
- **Highlights**: Hue 42°, Sat 5 (warm selenium-toned highlights)
- **Shadows**: Hue 220°, Sat 3 (subtle cool shadow)
- **Blending**: 50
- **Balance**: +10 (slight highlight emphasis for bright IR foliage)

#### Grain (ISO 200, near-IR: Amount 25-35)
- **Amount**: 30 (medium — extended-red emulsion character)
- **Size**: 28 (moderate)
- **Roughness**: 50 (regular — near-IR film structure)

#### STYLEGUIDE Compliance
- No Calibration
- No Temperature/Tint
- Sharpness=10, Clarity=0, Texture=0, Dehaze=0 (grain protection)
- LuminanceSmoothing=0
- ProcessVersion 15.4, Treatment=Monochrome, ConvertToGrayscale=True
- Adobe Monochrome Look UUID 0C09521111114111B1115456789ABCDE
- Blacks -18 ≥ -30

## Community Notes

### IR Emulation Limits in Lightroom
Like ortho emulation, full IR emulation is impossible in Lightroom because:
1. **No IR channel**: RAW sensors have IR-cut filters — IR data is physically absent
2. **Wood Effect approximation**: The Green Mixer at +40 creates bright foliage, but this is based on visible green, not actual IR reflectance
3. **Selective brightness**: Real IR makes some leaves white and others grey depending on chlorophyll content — a global green slider can't differentiate
4. **Atmospheric penetration**: Real IR cuts through haze — Lightroom's Dehaze can simulate this but isn't physically equivalent

### Getting the Most Convincing IR Look
1. Shoot in direct sunlight (IR reflectance is strongest in bright sun)
2. Choose images with distinct blue sky and deciduous foliage
3. The preset works best on images that already have strong sky/foliage separation
4. Consider combining with the Dehaze slider (not included per STYLEGUIDE grain rule) for haze penetration simulation
5. Accept the result as an "IR-inspired" look rather than true infrared

### Without IR Filter (Standard SFX 200 look)
For SFX 200 shot without a filter (behaves like extended-red panchromatic):
- Red Mixer: +10 to +15
- Green Mixer: +10 to +15
- Blue Mixer: -10 to -15
- More moderate contrast

## Sources
- Ilford SFX 200 technical data sheet
- Infrared photography community (Flickr IR groups, digital IR forums)
- YouTube: IR film reviews and comparisons
- Photrio: SFX 200 vs Rollei Infrared comparisons
