# Moody Cinematic Film — Creator Tuned — Characteristics

## Origin
This preset was provided as an exact XMP file by the user. The name "Creator Tuned" suggests it was produced by a YouTube content creator or photographer who sells or distributes preset packs. The XMP metadata carries Adobe XMP Core 5.5-c021 79.156103, 2017/08/07-23:16:39 — consistent with a preset exported from Lightroom Classic around 2017-2018.

## Aesthetic Intent
A moody, cinematic film look that balances warmth with cool shadow depth. The signature is a 75-Blending warm amber color grade on both midtones and highlights (Hue 45°), contrasted against cool teal/blue shadows (Hue 215°). The negative contrast (-15) and negative clarity (-12) soften the image for a filmic bloom, while positive Dehaze (+10) adds atmospheric density to prevent the look from going too soft.

## Key Visual Characteristics

### 1. The "Soft But Dense" Paradox
Negative Contrast (-15) lowers global tonal separation, but Dehaze (+10) and Texture (+20) bring back mid-frequency detail. The result is an image that feels soft and filmic overall but retains texture in foliage, fabric, and skin pores. Clarity (-12) contributes to highlight bloom while Dehaze compresses atmospheric scatter.

### 2. Vibrance/Saturation Split (gap = 20)
Vibrance (+30) far exceeds Saturation (+10). This is an intentional "selective-color-like" effect where midtone colors pop while shadows and highlights remain near their global saturation baseline. In Lightroom, this creates a filmic midtone color pop — skin tones and foliage in the midtones register as vibrant, while the extremes stay controlled. Community and STYLGUIDE both warn that gaps >10 can create the selective-color bug on some images, but this gap appears purposeful for the preset's intended "creator tuned" use on creator-provided hero images.

### 3. Warm Amber / Cool Teal Dual-Color Grade
- Shadow wheel: Hue 215°, Sat 10 (cool teal/blue depth)
- Midtone wheel: Hue 45°, Sat 15 (warm amber body)
- Highlight wheel: Hue 45°, Sat 20, Lum -10 (warm golden pop with luminance anchor)
- Blending: 75 (clean color separation)

The midtone and highlight wheels share the identical 45° warm hue but at increasing saturation (15→20) and with a -10 lum drag on highlights. The shadow wheel at 215° is 170° apart from the highlights — near-opponent relationship creates strong warm/cool perceptual contrast.

### 4. Green Channel Desaturation (the Moody Move)
Green hue is shifted +25 toward yellow/olive, and green saturation is crushed to -45. This kills "digital neon green" and replaces it with a muted, cinematic olive. The complementary moves: Orange saturation is boosted +15 (warm skin/earth tone pop). This is the classic cinematic color palette — kill greens, boost warm tones.

### 5. Blue → Teal Shift
Blue hue is pulled -35 toward cyan, with a -10 saturation reduction. Combined with the BluePrimary calibration shift (-15 hue toward cyan, +5 saturation), blues in the image read as muted cyan/teal rather than electric blue. This integrates the sky and blue objects into the cool shadow color grade.

### 6. Grain + Detail Formula
- Grain: Amount 35, Size 40, Roughness 50 (medium-visible, slightly chunky, moderately irregular — reads as ISO 400-800 consumer film)
- Sharpness: 15 (slightly above STYLGUIDE's ≤10 rule, but the +20 Texture partially offsets grain degradation — the higher Texture keeps fine detail visible through the grain)
- LuminanceSmoothing: 25 (unusual — smooths luma noise to create a "wax" base that grain sits on top of, the "Melted Base" technique from STYLGUIDE §VII.4)
- ColorNoiseReduction: 25 (reduces chroma noise from high Vibrance, keeps grain monochrome)

### 7. Calibration Panel
- Red Primary Hue: +5 (very subtle warmth shift — cautious)
- Blue Primary Hue: -15 (push blues toward cyan at the profile level)
- Blue Primary Saturation: +5 (preserve blue channel intensity after the hue shift)

The BluePrimary shift reinforces the cool shadow grade. This is a pre-HSL-hue-shift that moves the overall color science toward the cyan side before any slider adjustments land. It's the equivalent of selecting a slightly cooler camera profile.

### 8. Exposure + Tone Settings
- Exposure: +0.45 (brightness boost for the "cinematic lift")
- Contrast: -15 (film-like softness)
- Highlights: -30 (smooth highlight roll-off)
- Shadows: +25 (lift dark areas for detail)
- Whites: -10 (prevents blown-out speculars)
- Blacks: +5 (very subtle lift — maintains anchor while preventing deep crush)

The overall tonal signature: slightly bright, soft contrast, recovered highlights, lifted shadows, anchored whites, near-neutral blacks.

## Ideal Source Materials
- Golden hour portraits with warm skin tones
- Overcast outdoor lifestyle (warm split-tone lifts the mood)
- Urban night scenes with mixed lighting (teal shadows pop against warm ambient)
- Foliage-heavy compositions (olive green transformation is the #1 visual cue)
- NOT ideal for: bright midday beach scenes (Exposure +0.45 would blow highlights), studio product shots (negative contrast kills commercial pop)

## STYLGUIDE Compliance Notes
This preset has intentional STYLGUIDE deviations that appear to be creator decisions, not errors:
- |Vibrance − Saturation| = 20 (exceeds ≤5 rule, but intentional film midtone pop)
- Calibration panel present (BluePrimary shifts — common in cinematic grading at a profile level)
- Sharpness = 15 (above ≤10 rule, but offset by Texture +20 and LuminanceSmoothing 25)
- LuminanceSmoothing = 25 (creates wax base for grain — the "Melted Base" technique)
- Clarity = -12 + Dehaze = +10 with grain (intentional paradox for bloom + density)
- Temperature/Tint present (warm daylight base)
