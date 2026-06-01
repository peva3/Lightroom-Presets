# Camera Color Characterization: DCP Profiles, Color Matrices, White Balance, and Color Pipelines

**Source URLs:**
- https://docs.darktable.org/usermanual/3.8/en/module-reference/processing-modules/input-color-profile/ (darktable 3.8 Manual)
- https://docs.darktable.org/usermanual/3.8/en/module-reference/processing-modules/white-balance/ (darktable 3.8 Manual)
- https://docs.darktable.org/usermanual/3.8/en/special-topics/color-pipeline/ (darktable 3.8 Manual)
- https://docs.darktable.org/usermanual/3.8/en/module-reference/processing-modules/color-calibration/ (darktable 3.8 Manual)

**Author(s):** darktable project contributors
**Date:** 2021 (darktable 3.8)

---

## Input Color Profile

The input color profile module takes the color space used by the image source (camera, scanner) and converts pixel encodings to a standardized working color space. This means subsequent pipeline modules don't need to be concerned with input device specifics.

### Color Matrices

For raw files, the module applies either a **standard** or **enhanced** color matrix specific to the camera model. The enhanced matrices are designed to provide a look closer to the camera manufacturer's rendering.

### Custom ICC Profiles

Users can supply custom input ICC profiles placed in:
- `$DARKTABLE/share/darktable/color/in`
- `$HOME/.config/darktable/color/in`

A common source is the software shipped with cameras, which often contains camera-specific ICC profiles. The "unbreak input profile" module may need to be activated when using custom profiles.

### Embedded ICC Profiles

DNG files and JPEG images may contain embedded ICC profiles, which darktable uses by default. This can be restored by selecting "embedded icc profile".

### Working Profile

Darktable's processing modules use "linear Rec2020 RGB" by default — a wide-gamut, linear working space. Each module can specify alternative working spaces, triggering conversions.

### Gamut Clipping

Input colors with saturation exceeding the permissible range of the selected profile are automatically clipped. Options include "linear Rec2020 RGB" and "Adobe RGB (compatible)" for broader unclipped ranges, or "sRGB" and "linear Rec709 RGB" for tighter clipping. Useful for highly saturated blue light sources that could create black pixel artifacts.

---

## White Balance

The white balance module adjusts **temperature** and **tint**, or directly sets **RGB channel coefficients**. Default settings are derived from the camera white balance stored in the image's Exif data.

### Core Concept

White balance is **not** a creative module — its primary goal is to technically correct the image so that neutral colored objects in the scene render as neutral colors. For creative color operations, use modules like **color calibration** or **color balance rgb**.

### Temperature and Tint

- **Temperature**: Color temperature in Kelvin
- **Tint**: Magenta (tint < 1) to green (tint > 1) adjustment

### White Balance Presets

- **As shot** (default): The WB as reported by the camera
- **From image area**: Draw a rectangle over a neutral color to calculate WB
- **User modified**: Most recently modified state
- **Camera reference**: Set temperature to camera reference white point, assumed to be D65 (~6502K). Channel multipliers calculated so pure white in camera colorspace converts to pure white in sRGB D65.

### RGB Channel Coefficients

The temperature and tint sliders are user-friendly abstractions over **RGB channel coefficients** (range 0-8). The relationship between them depends on camera-specific characteristics.

**Critical warning**: Applying WB settings from one camera model to another will generally NOT give consistent results. The mathematical relationship is not straightforward, and it's possible to set coefficients that have no valid equivalent temperature/tint (especially at very high temperatures).

### Modern Alternative: Color Calibration

The **color calibration** module now provides a more modern and flexible method of controlling white balance. It can be enabled by default using "modern" in preferences > processing > auto-apply chromatic adaptation defaults. Some basic settings are still required in the white balance module so that demosaic works correctly.

---

## Darktable's Color Pipeline

### Historical Context

Most image processing applications from the 1990s use a **"display-referred"** workflow:
- 8-bit unsigned integers with gamma encoding
- Bounded RGB (0-255)
- Non-linear transforms for encoding
- Hard-coded assumptions about black, middle-gray, and white values
- Breaks optical filters, alpha compositing, colors, and gradients
- Poor HDR support

### Scene-Referred Workflow

Modern darktable uses a **"scene-referred"** workflow:
- Floating point encoding
- Unbounded values (0 to +infinity)
- Pixels retain original radiometric relationships throughout the pipeline
- Display preparation deferred to the very end (filmic view transform)
- Accurate alpha compositing and optical filter emulations
- Scales naturally to any dynamic range (SDR or HDR)

### Key Concepts

| Term | Definition |
|------|-----------|
| **Linear** | Pixel values proportional to scene radiometric emission — enables accurate physical filter emulation |
| **Non-linear** | Pixel values re-scaled so low-lights get larger encoding range |
| **Display-referred** | Values expected to lie between 0-100% of display range (white = 20% reflective surface) |
| **Scene-referred** | Values expected to be >0 to +infinity. Meaning of values defined at runtime by user |

### Cognitive Shift

In display-referred: anchor white, maximize brightness, avoid clipping.  
In scene-referred: white and black values are fluid. **Anchor middle-gray** instead — it's preserved as-is for any output medium. The view transform (filmic) dilates or contracts dynamic range around that point.

### Module Compatibility

Some modules are inherently incompatible with scene-referred:
- **levels, rgb levels, tone curve, rgb curve**: GUI implies bounded 0-100% values
- **Blending modes** (overlay, linear light, soft light, etc.): Have hard-coded thresholds expecting display-referred encoding

In darktable 3.4+, hovering over a module header shows a tooltip detailing the color spaces, ranges, and encodings that the module expects, uses, and produces.

### Color Pipeline Order

The approximate pipeline order:
1. Raw black/white point subtraction
2. White balance (raw data)
3. Demosaic
4. Input color profile (camera → working space)
5. Processing modules (exposure, filmic, color balance, etc.)
6. Output color profile (working space → destination space)

---

## Camera Profile Types

### DCP Profiles (DNG Camera Profiles)

DCP files are XML-based camera profiles used by Adobe products (Lightroom, Camera Raw). They contain:
- **Color matrices**: 3x3 matrices mapping camera sensor responses to CIE XYZ
- **Forward matrices**: Additional transforms for specific illuminants
- **Hue/Saturation tables (HSV LUTs)**: Per-hue adjustments on top of the matrix transform
- **Tone curve**: Base contrast rendering

DCP profiles can be embedded in DNG files or stored externally.

### ColorChecker-Based Profiling

Using a physical color chart (e.g. X-Rite ColorChecker) photographed under controlled lighting:
- The darktable-chart tool maps camera responses to known reference values
- Creates either an ICC profile or an enhanced color matrix
- The ICC profile path handles non-linear transforms better; the matrix path preserves scene-referred linearity

---

## Demosaicing + Color Interaction (LibRaw)

LibRaw's Bayer moire research reveals an important color artifact insight:

> When testing demosaicing algorithms on synthetic targets, all methods produced abundant color aliasing. If your camera/lens can create a pixel-sized contrast object on the matrix, you can never predict what color it will be — or know if it will bear any resemblance to the initial color.

This is fundamentally a color characterization problem: demosaicing artifacts produce colors that are mathematically plausible (from the interpolation math) but physically meaningless.

---

## References

- darktable input color profile: https://docs.darktable.org/usermanual/3.8/en/module-reference/processing-modules/input-color-profile/
- darktable white balance: https://docs.darktable.org/usermanual/3.8/en/module-reference/processing-modules/white-balance/
- darktable color calibration: https://docs.darktable.org/usermanual/3.8/en/module-reference/processing-modules/color-calibration/
- darktable color pipeline: https://docs.darktable.org/usermanual/3.8/en/special-topics/color-pipeline/
- darktable color management: https://docs.darktable.org/usermanual/3.8/en/special-topics/color-management/
- LibRaw articles: https://www.libraw.org/articles
