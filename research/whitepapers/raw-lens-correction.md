# Lens Correction Profiles and Distortion Models

**Source URLs:**
- https://docs.darktable.org/usermanual/3.8/en/module-reference/processing-modules/lens-correction/ (darktable 3.8 Manual)
- https://lensfun.github.io/ (lensfun library project)

**Author(s):** darktable project contributors, Torsten Bronger (lensfun calibration), lensfun contributors
**Date:** 2021 (darktable 3.8), ongoing (lensfun)

---

## Overview

Lens correction in RAW processing addresses three primary optical aberrations:

1. **Distortion**: Barrel or pincushion geometric warping
2. **Transversal Chromatic Aberrations (TCA)**: Color fringing at high-contrast edges due to different wavelengths focusing at slightly different positions on the sensor
3. **Vignetting**: Light falloff toward image corners (brightness and sometimes color shift)

These corrections rely on the external **lensfun library**, which maintains a database of correction parameters for thousands of camera/lens combinations.

---

## How Lens Correction Works

The module identifies the camera/lens combination from the image's Exif data. If the system lensfun library has a profile, it provides correction parameters automatically.

If no profile is found:
- Controls are replaced with a warning message
- Users can search the lens list manually
- Lens may need exiv2 adjustments for correct identification
- Use `lensfun-update-data` tool to get the latest profile database
- Submit new profiles to the lensfun project

### Supported Corrections

Not all profiles provide all correction types. A status message indicates which corrections were applied:

| Correction | Input Parameters | Notes |
|-----------|-----------------|-------|
| **Distortion** | Focal length | Geometric warping correction |
| **TCA** | Focal length, aperture | Red/cyan and blue/yellow fringe correction |
| **Vignetting** | Focal length, aperture, focal distance | Brightness falloff correction |

### Photometric Parameters

Corrections depend on three parameters read from Exif:
- **Focal length**: For distortion, TCA, and vignetting
- **Aperture**: For TCA and vignetting
- **Focal distance**: For vignetting (many cameras don't record this — must be set manually)

Users can override all parameters manually from drop-down menus or by typing custom values.

---

## Lens Correction Models

### Distortion Models

Lensfun supports multiple distortion models:

1. **Polynomial model** (most common):
   ```
   r_d = r * (1 + k1*r² + k2*r⁴ + k3*r⁶)
   ```
   Where `r` is the undistorted radius and `r_d` is the distorted radius. `k1` controls the main barrel/pincushion, `k2` and `k3` handle complex wide-angle distortion (mustache distortion).

2. **PTLens model**: Alternative parameterization used by some lens databases.

### TCA Models

Transversal chromatic aberration is modeled as a magnification difference between color channels:
```
r_red = r * (1 + TCA_red_parameter)
r_blue = r * (1 + TCA_blue_parameter)
```
Green is used as reference (no correction). Positive values enlarge the channel, negative shrink it.

### Vignetting Models

```
V(r) = 1 + k1*r² + k2*r⁴ + k3*r⁶
```
Where `V(r)` is the vignetting factor at radius `r`. Values < 1 darken the corners, > 1 brighten them. Some models also include per-channel vignetting to correct color shifts.

---

## Geometry / Projection Changes

Beyond fixing lens flaws, the module can **change the projection type** of the image:

| Projection | Use Case |
|-----------|----------|
| **Rectilinear** | Standard perspective — straight lines stay straight |
| **Fish-eye** | Circular or full-frame fisheye look |
| **Panoramic / Cylindrical** | Wide panoramas with horizontal line preservation |
| **Equirectangular** | Full 360° spherical projection |
| **Orthographic** | Constant angular magnification |
| **Stereographic** | Conformal mapping preserving angles locally |
| **Equisolid angle** | Common in scientific fisheye lenses |
| **Thoby fish-eye** | Specialized fisheye variant |

### Anamorphic Lenses

For anamorphic lens aspect ratio correction, use the **rotate and perspective** module in conjunction with lens correction.

---

## Mode: Correct vs. Distort

The module operates in two modes:
- **Correct** (default): Removes real lens flaws to produce a corrected image
- **Distort**: Simulates the flaws of a specific lens — useful for creating lens effects on CGI or non-distorted images

---

## Manual TCA Override

When a profile lacks TCA data, or the automatic correction isn't sufficient:
- **TCA red** and **TCA blue** sliders allow manual override
- Look for colored seams at high-contrast edges
- Adjust to minimize fringing
- Monochrome images skip TCA corrections automatically

---

## Border Filling

Lens correction can create missing data at image borders (especially for strong distortion corrections). darktable fills these by **repeating border pixels**. For strong corrections, this can be visible (especially on noisy images). Crop the image if necessary.

The **scale** slider adjusts image scaling to minimize black corners. An auto-scale button finds the best fit automatically.

---

## Lens Calibration

If your lens is not in the lensfun database:

1. Check the [currently supported lenses list](https://lensfun.github.io/lenslist/)
2. Run `lensfun-update-data` to get the latest database
3. Use the [lens calibration service](https://www.darktable.org/2013/07/have-your-lens-calibrated/) by Torsten Bronger
4. Generate your own calibration parameters:
   - Shoot a calibration target (brick wall or test chart) at multiple focal lengths
   - Use tools like Hugin's lens calibration or lensfun's calibration tools
   - Submit profiles to the lensfun project

### Calibration Best Practices

- Use a flat, well-lit target with straight lines and fine detail
- Shoot at multiple focal lengths (for zooms)
- Shoot at multiple apertures (wide open, f/5.6, f/8, f/11) for vignetting and TCA
- Record focal distance if your camera doesn't embed it in Exif
- Use RAW files — JPEG may have in-camera corrections applied

---

## Lens Correction in Lightroom (XMP)

Lightroom's lens correction in XMP presets uses different parameters:

```xml
<crs:AutoLateralCA>0</crs:AutoLateralCA>  <!-- 0=off, 1=on -->
<crs:LensProfileEnable>1</crs:LensProfileEnable>
<crs:LensProfileSetup>Default</crs:LensProfileSetup>
<crs:LensManualDistortionAmount>0</crs:LensManualDistortionAmount>
<crs:PerspectiveVertical>0</crs:PerspectiveVertical>
<crs:PerspectiveHorizontal>0</crs:PerspectiveHorizontal>
<crs:PerspectiveRotate>0</crs:PerspectiveRotate>
<crs:PerspectiveScale>100</crs:PerspectiveScale>
```

Lightroom uses its own internal lens profile database (separate from lensfun). Adobe's profiles are stored in `.lcp` (Lens Correction Profile) files.

Key differences from lensfun:
- Adobe profiles are binary/compiled, not text
- No projection change capability
- Integrated with Upright/Guided perspective corrections
- Per-manufacturer profile indexing

---

## X-Trans and Lens Correction

Fujifilm X-Trans sensors do not fundamentally change how lens correction works. However, X-Trans's more complex CFA pattern means that:
- TCA artifacts may appear slightly different due to the 6x6 demosaicing pattern
- Sharpening interactions with distortion correction need more careful handling
- Some older lensfun profiles may not have been tested with X-Trans cameras using the same lens

---

## References

- darktable lens correction: https://docs.darktable.org/usermanual/3.8/en/module-reference/processing-modules/lens-correction/
- Lensfun project: https://lensfun.github.io/
- Lensfun supported lenses: https://lensfun.github.io/lenslist/
- Lensfun update tool: https://lensfun.github.io/manual/v0.3.2/lensfun-update-data.html
- darktable lens calibration service: https://www.darktable.org/2013/07/have-your-lens-calibrated/
