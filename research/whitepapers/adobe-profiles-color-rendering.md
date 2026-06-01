# Adobe Profile System & Color Rendering

**Source URL:** https://helpx.adobe.com/camera-raw/using/adjust-color-rendering-camera-camera.html
**Author:** Adobe Inc.
**Date:** December 12, 2024 (last updated)

---

## Overview

Profiles allow you to control the colors and tonality in your photos, providing a foundation for your edits. Applying a profile doesn't change the values of other editing sliders, so you can edit your pictures freely and then use a profile to enhance the already edited image.

## Default Profiles

When you import photos, Adobe Color and Adobe Monochrome profiles are applied by default to color and black-and-white photos, respectively.

## Types of Profiles

### Adobe Adaptive (Beta) Profile
The Adobe Adaptive (beta) profiles help with image-adaptive adjustments for SDR and HDR images. Perfect for raw photos, Adobe Adaptive (beta) can help adjust the tone and color, enhancing contrast.

The Adobe Adaptive (beta) profiles work best on raw HDR images. The default version does not support Monochrome raw files, while the Monochrome version does.

**Tips:**
- When you select B&W, the Adobe Adaptive Monochrome (beta) profile is selected automatically
- It's recommended to NOT apply the Auto and Adobe Adaptive (beta) profiles together
- Apply the Adobe Adaptive (beta) profiles before making other edits and adjustments

### Adobe Raw Profiles
Adobe provides several built-in profiles designed to be good starting points:
- **Adobe Color**: Designed for photos with a wide range of colors, from vibrant sunsets to lush landscapes
- **Adobe Monochrome**: Optimized for black and white photos
- **Adobe Landscape**: Enhances blues and greens in landscape photos
- **Adobe Neutral**: Provides a low-contrast, low-saturation starting point for images you intend to extensively edit
- **Adobe Portrait**: Optimized for skin tones in portrait photos
- **Adobe Standard**: Legacy profile, available for backward compatibility
- **Adobe Vivid**: Provides a saturated and contrasty starting point

### Camera Matching Profiles
Camera Matching profiles attempt to match the color rendering of the manufacturer's own image processing software. These profiles include:
- Camera Faithful
- Camera Landscape
- Camera Neutral
- Camera Portrait
- Camera Standard
- And camera-specific variants

### Creative Profiles
Creative profiles include the following groups:
- **Artistic**: Profiles that create unique artistic effects
- **B&W**: Black and white creative profiles
- **Modern**: Contemporary styling profiles
- **Vintage**: Retro and film-like profiles

When you apply any of the Adobe Adaptive (beta), Artistic, B&W, Modern, and Vintage profiles, an Amount slider lets you manually adjust the intensity of the profile. For other profiles, the Amount slider is dimmed or inactive.

## Profile Browser

The Profile Browser panel allows you to:
- View profiles as Grid thumbnails or as a List
- Filter profiles by Color, B&W, or All
- Mark profiles as Favorites
- Preview any profile by hovering over it

## Camera Raw Settings Management

Adobe Camera Raw settings are stored in either:
1. **Sidecar XMP files**: Settings stored in `.xmp` files alongside raw files
2. **Camera Raw database**: Settings stored in a central database

The choice affects workflow portability - XMP sidecar files are more portable between systems.

## Significance for XMP Presets

Critical for XMP preset creation:
1. The `crs:Look` block is MANDATORY for proper rendering
2. For Color presets: `crs:Name="Adobe Color"` with UUID `B952C21111114111B1115456789ABCDE`
3. For B&W presets: `crs:Name="Adobe Monochrome"` with UUID `0C09521111114111B1115456789ABCDE`
4. Without a Look block, Lightroom skips the non-linear input color matrix, resulting in flat/washed-out rendering
5. Profiles are the foundation layer - they set the baseline before HSL, tone curves, and other adjustments
6. Camera profiles contain DCP (DNG Camera Profile) data including color lookup tables and tone curves
7. Never use Calibration panel adjustments (CalibrationRedHue/Sat, etc.) as they conflict with the profile's color rendering pipeline
