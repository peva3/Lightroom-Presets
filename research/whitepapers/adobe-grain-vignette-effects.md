# Adobe Camera Raw Effects Engine: Grain, Vignette, and Dehaze

**Source URL:** https://helpx.adobe.com/camera-raw/using/vignette-grain-effects-camera-raw.html
**Author:** Adobe Inc.
**Date:** November 3, 2023 (last updated)

---

## Simulate Film Grain

The Grain section of the Effects tab has controls for simulating film grain for a stylistic effect reminiscent of particular film stocks. You can also use the Grain effect to mask enlargement artifacts when making large prints.

Together, the Size and Roughness controls determine the character of the grain. Check grain at varying zoom levels to ensure that the character appears as desired.

### Grain Parameters

**Amount**
Controls the amount of grain applied to the image. Drag to the right to increase the amount. Set to zero to disable grain.

**Size**
Controls grain particle size. Specifying a value of 25% or higher can cause some image blurring.

**Roughness**
Controls the regularity of the grain. Drag to the left to make the grain more uniform; drag to the right to make the grain more uneven.

## Post Crop Vignette

To apply a vignette to a cropped image for artistic effect, use the Post Crop Vignetting feature.

### Vignette Styles

**Highlight Priority**
Applies the postcrop vignette while protecting highlight contrast but can lead to color shifts in darkened areas of an image. Appropriate for images with important highlight areas.

**Color Priority**
Applies the postcrop vignette while preserving color hues but can lead to loss of detail in bright highlights.

**Paint Overlay**
Applies the postcrop vignette by blending original image colors with black or white. Appropriate when a soft effect is desired but can reduce highlight contrast.

### Vignette Parameters

**Amount**
Positive values lighten the corners, negative values darken them.

**Midpoint**
Higher values restrict the adjustment to the area closer to the corners, lower values apply the adjustment to a larger area away from the corners.

**Roundness**
Positive values make the effect more circular, negative values make the effect more oval.

**Feather**
Higher values increase the softening between the effect and its surrounding pixels, lower values reduce the softening.

**Highlights**
(Available for Highlight Priority or Color Priority when Amount is negative) Controls the degree of highlight "punch" in bright areas of an image, such as in the glow of a streetlight or other bright light source.

## Dehaze

The Dehaze slider is available in the Effects tab starting from Process Version 5. Positive values reduce atmospheric haze, increasing contrast and saturation in hazy areas. Negative values add haze for creative atmospheric effects.

### Significance for XMP Presets

Critical findings for preset creation:
1. **Grain + Sharpening interaction**: Any preset with `GrainAmount > 0` MUST have `Sharpness="10"` (or lower) and `LuminanceSmoothing="0"` to prevent Lightroom's digital sharpening from turning organic grain into jagged digital noise
2. **Grain + Clarity/Texture/Dehaze**: Keep Clarity, Texture, and Dehaze at 0 for grain-heavy presets - let the tonal curve and grain structure carry the character
3. Vignette styles affect highlights and color differently - choose based on whether color accuracy or highlight preservation matters more
4. Post-crop vignette is applied after cropping, so it always affects the final composition
5. Grain is applied late in the pipeline, after sharpening and noise reduction
