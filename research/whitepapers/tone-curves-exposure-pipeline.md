# Tone Curves & Exposure Pipeline in Raw Processing

**Source URL:** https://rawpedia.rawtherapee.com/Exposure
**Author:** RawTherapee Contributors
**Date:** January 20, 2023 (last updated)

**Note:** This document describes raw processing concepts that are directly applicable to Adobe Camera Raw and Lightroom. Adobe's processing pipeline was the inspiration for many of these algorithms, particularly the "Film-Like" curve mode which is Adobe's DNG-standard tone curve.

---

## Exposure & Tone Pipeline Overview

The exposure pipeline in a raw processor converts linear raw sensor data into a perceptually pleasing image. The typical order of operations is:

1. Demosaicing
2. White balance
3. Exposure compensation
4. Highlight reconstruction/recovery
5. Shadow/highlight compression
6. Tone curves
7. Saturation adjustments
8. Output color space conversion

## Key Exposure Controls

### Exposure Compensation
Values are in ISO/EV (exposure value) units. A value of +1 equals one stop of overexposure (+1 EV). Moving the slider right shifts the entire histogram right - this changes both the black point and white point.

**Technical note on EV=0:** While EV=0 equals 1.0 in gain (no change), there is a white balance dependent base gain applied before exposure. This base gain is calculated such that the color channel with the smallest range can just reach the maximum value. As white balance changes raw channel gains, the base gain changes as a side effect when white balance is changed.

### Highlight Reconstruction
Attempts to restore clipped (blown-out) regions by relying on the fact that the three channels in a raw file do not clip at the same time. A missing (clipped) region in one channel can be guessed from the present data of the other color channels.

Four methods:
1. **Luminance Recovery**: Recovered details are neutral gray
2. **Color Propagation**: Most powerful - restores both luminosity and color by "bleeding" surrounding known color into missing clipped areas. Best on small overexposed areas; can work wonders on skin
3. **Inpaint opposed**: Uses average of neighboring unclipped pixels
4. **CIELab**: Reduces luminance channel and tries to restore colors afterwards
5. **Blend**: Fills in clipped channels from closest match in unclipped highlight regions

### Highlight Compression
Works only on data that is already there - not irreversibly lost at time of shooting. If the original image has no clipping, but due to exposure compensation you caused clipping, Highlight Compression can compress these clipped regions back into view. Works on both raw and normal images.

**Key rule:** A correctly developed image's histogram should touch both ends. If you increase HC too much, whites turn gray as the histogram no longer touches the maximum end. Recover what you can, but what's clipped beyond repair should stay white.

### Black & Shadow Compression
The Black slider sets the black point. The Shadow Compression slider dampens the effect of the Black slider - maximum value of 100 gives a less dark image.

### Lightness
Applies a hard-coded tone curve to lift or lower tonalities. Applied separately to each R, G and B channel. The black point and white point keep their positions.

### Contrast
Applies a contrast curve centered at the average luminance level. Tonalities above average are lifted, below average are lowered. Applied separately to each R, G and B channel.

### Saturation
Adjusts saturation by applying a multiplier to the saturation level of pixels in the HSV color space.

## Tone Curves

Tone curves work on all three R, G and B channels simultaneously (not per-channel). The histogram displayed as the curve's background shows data as it flows into the curve at that point in the processing pipeline (different from the final image histogram).

Using two tone curves provides finer tonal control than one. The typical approach is to lower values using the first curve and raise values using the second - similar to an S-curve but with finer adjustments.

### Curve Types

**Linear**
Represents unaltered (linear) image without any tone curve applied. Disables the curve.

**Standard**
A classic cubic spline curve. Editing one node can have significant impact on the curve in relation to other nodes. A typical usage is the S-curve: mark three points and drag the shadows down and highlights up to add "punch."

**Flexible**
Centripetal Catmull-Rom spline curve. Allows adjustments to any part of the curve with little impact on other parts - more localized control than Standard.

**Parametric**
Uses four sliders (Highlights, Lights, Darks, Shadows) and three control points. The sliders control which tonal ranges are affected. Less "extreme" control but more predictable shaping. Moving the middle control point right darkens, left brightens.

**Control Cage**
Similar to Standard but the curve passes nearby control points rather than through them. Allows for straight sections of the curve. Holding Shift snaps points to create straight lines.

### Curve Modes (Blending Algorithms)

The curve mode determines how the curve affects colors, which has a strong effect on color appearance, especially with contrast-enhancing S-curves.

#### Standard
The most basic mode: the same curve is applied to each RGB channel independently. An S-curve will increase separation of channels and thus increase saturation - similar behavior to how color film reacts to contrast. This is the only mode available in many older/less flexible software.

Drawback: An orange color (high R, high G, low B) with an S-curve will shift toward yellow because R and G are raised while B is lowered.

#### Weighted Standard
Limits the color shift of the standard curve. Raises one component and linearly adjusts the other two. The process runs for each component, producing 9 values (R,g,b / r,G,b / r,g,B) which are mixed together, resulting in smaller color shift.

#### Film-Like (Adobe DNG Standard)
**This is the curve mode used by Adobe Camera Raw and Lightroom.** It was designed by Adobe as part of the DNG specification. The film-like curve provides results highly similar to Standard (strong saturation increase with increased contrast), but the RGB-HSV hue is kept constant - there are fewer color-shift problems.

#### Saturation and Value Blending
The average value of the three components is computed, and the curve is applied to this value, giving a positive or negative gain. If gain is positive, the pixel linearly targets Value=1 and Saturation=0 (preserving Hue). If negative, targets Value=0 (preserving Saturation and Hue). Results are similar to a luminance curve in Lab space.

For contrast-increasing curves, the look will typically be slightly desaturated - not because the curve desaturates, but because in human vision, contrast and saturation are tightly coupled. The same image with higher contrast requires higher saturation to appear to have the same saturation level.

#### Luminance
Each component is boosted by the same factor so color and saturation are kept stable. Despite showing an RGB histogram, the curve operates on luminance values where Relative Luminance Y = R*0.2126729 + G*0.7151521 + B*0.0721750. The multiplication factor between before/after luminance is calculated and applied to each R, G, B component.

#### Perceptual
Keeps original color appearance concerning hue and saturation. An S-curve increases contrast but hues stay the same and the image appears neither more nor less saturated than the original. Useful for establishing a baseline contrast without distorting colors from a camera profile that doesn't apply its own curve.

The algorithm analyzes the curve to get a contrast value, which is used as a base to scale chroma such that more contrast leads to more saturation (to keep saturation appearance constant). Further fine-tunings include increasing saturation more in shadows, and less for already highly saturated colors. Near the white point, the algorithm blends to white.

This mode is slower than others due to its many computational components.

## Relevance to Lightroom/ACR XMP Presets

Key takeaways for XMP preset creation:
1. Adobe Camera Raw and Lightroom use the **Film-Like** curve mode (part of DNG specification) - this preserves hue while increasing contrast/saturation
2. The `crs:ToneCurvePV2012` block in XMP files represents the parametric tone curve
3. All 4 curves (RGB + Red + Green + Blue) must be set to neutral (`0, 0` to `255, 255`) for clean preset behavior
4. S-curves increase saturation as a side effect (just like film) - factor this in when setting Saturation/Vibrance values
5. The order of operations matters: tone curves are applied before HSL adjustments
6. Heavy tone curve adjustments can conflict with HSL and split toning adjustments
7. Perceptual curve mode explains why Vibrance and Saturation interact non-linearly: human vision couples contrast and saturation perception
