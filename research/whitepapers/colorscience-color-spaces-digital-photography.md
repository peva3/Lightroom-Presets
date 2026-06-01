# Color Spaces for Digital Photography: sRGB, Adobe RGB, ProPhoto RGB, and P3

**Source:** https://www.cambridgeincolour.com/tutorials/color-spaces.htm
**Authors:** Cambridge in Colour (Sean McHugh) with additional content from Wikipedia
**Date:** Cambridge in Colour tutorials circa 2005-2020; consolidated 2025

---

## What is a Color Space?

A color space relates numbers to actual colors and is a three-dimensional object containing all realizable color combinations. Similar to how an artist organizes a paint palette, each direction in a color space represents aspects of color such as lightness, saturation, and hue.

A color space is effectively a digital palette — except these colors are much more precisely organized and quantified.

## Visualizing Color Spaces

A color space is typically a three-dimensional object. The outer surface represents the most extreme colors reproducible (the "color gamut"). Everything inside represents more subtle combinations.

For practical comparison, color spaces are often represented using **two-dimensional slices** at a specific luminance level (commonly 50% luminance, representing midtones). The diagram typically shows how different color spaces' gamuts compare as subsets of a reference space.

## Reference Color Spaces (CIE)

Nearly all color management software uses a device-independent space defined by the Commission International de l'Éclairage (CIE) in 1931. This space aims to describe all colors visible to the human eye based on the average response from people with no vision problems (the "standard colorimetric observer").

### CIE xyz (1931)
Based on a direct graph of the signals from each of the three types of color sensors in the human eye (X, Y, Z tristimulus functions). However, this representation allocates too much area to greens, confining most apparent color variation to a small area.

### CIE L*a*b* (CIELAB, 1976)
Remaps visible colors to extend equally on two axes, conveniently filling a square. Each axis represents an easily recognizable property of color:
- **L\*** — Lightness (0 = black, 100 = white)
- **a\*** — Red-green shift (-a = green, +a = red)
- **b\*** — Blue-yellow shift (-b = blue, +b = yellow)

These traits make L*a*b* useful for editing digital images in applications like Adobe Photoshop and GIMP.

### CIE L*u'v'* (CIELUV, 1976)
Created to correct CIE xyz distortion by distributing colors roughly proportional to their perceived color difference. A region twice as large in u'v' appears to have twice the color diversity — making it more useful for visualizing and comparing color spaces.

## Working Spaces for Digital Photography

### sRGB (IEC 61966-2-1:1999)

The most widely used color space. Created by HP and Microsoft in 1996 for use on monitors, printers, and the Web.

**Characteristics**:
- Smallest gamut of the major working spaces
- Standard for web content, consumer displays, and most digital workflows
- Gamma: approximately 2.2 (with linear portion near black)
- White point: D65
- Primaries derived from Rec. 709 (HDTV standard)

**Pros**: Universal compatibility, safe for web, no surprises across devices
**Cons**: Smallest gamut, clips saturated colors (especially cyans and greens), not suitable for print-preferred workflows

**Use case**: Web output, consumer photography, images destined for on-screen viewing

### Adobe RGB (1998)

Developed by Adobe Systems in 1998 to encompass most colors achievable on CMYK printers while using RGB primaries.

**Characteristics**:
- Significantly wider gamut than sRGB, especially in cyan-green regions
- Gamma: 2.2
- White point: D65
- Covers approximately 50% of visible colors (vs. 35% for sRGB)

**Pros**: Good balance of gamut vs. posterization risk, wider than sRGB, well-supported in software
**Cons**: Still clips some printable colors, many monitors cannot fully display

**Use case**: Print workflows, images with saturated greens/cyans, general-purpose high-quality editing

### ProPhoto RGB (also known as ROMM RGB)

Developed by Kodak. Designed to encompass all colors that photographic film can capture and all colors reproducible by current output devices.

**Characteristics**:
- Extremely wide gamut — includes imaginary/non-physical primaries
- Gamma: 1.8
- White point: D50
- Covers approximately 90% of visible colors

**Pros**: No gamut clipping of any real-world scene colors, future-proof for improved output devices
**Cons**: High risk of posterization in 8-bit images, requires 16-bit workflow, wide gamut means small editing moves produce large color shifts, contains colors that cannot be displayed on any monitor

**Use case**: Professional 16-bit photography workflows, archival masters, color-critical print work

### Display P3 (DCI-P3)

Originally developed by Digital Cinema Initiatives for digital cinema projection. Apple adopted a variant for consumer displays starting with the iPhone 7 and MacBook Pro (2016).

**Characteristics**:
- Gamut approximately 25% larger than sRGB
- Wider reds and greens compared to sRGB
- White point: D65 (Apple variant)
- Gamma: sRGB transfer function (Apple variant)

**Pros**: Wide gamut supported by modern consumer devices, good balance between sRGB and Adobe RGB, becoming the new consumer standard
**Cons**: Not as wide as Adobe RGB in some regions, inconsistent implementations

**Use case**: Modern consumer photography on Apple devices, HDR content, images destined for wide-gamut mobile/desktop displays

### Rec. 2020 / Rec. 2100

Ultra-wide gamut standard for UHDTV (4K/8K). Covers approximately 75% of the CIE 1931 color space.

**Characteristics**:
- Extremely wide gamut — significantly larger than DCI-P3 and Adobe RGB
- Monochromatic primaries (single wavelengths)
- Supports HDR (Rec. 2100 adds HDR to Rec. 2020)
- White point: D65

**Pros**: Future-proof, covers almost all real-world surface colors
**Cons**: No current consumer display can fully reproduce, requires advanced color management

## Gamut Comparison at 50% Luminance

At midtones (50% luminance):
- **sRGB**: Smallest, limited mainly in cyan-greens and saturated reds
- **Adobe RGB**: Significantly wider in cyan-greens, moderately wider in reds
- **ProPhoto RGB**: Encompasses both, extends far beyond into imaginary colors
- **DCI-P3**: Between sRGB and Adobe RGB, wider in reds than Adobe RGB
- **Rec. 2020**: Largest, covering nearly all surface colors

## Color Space Terminology

- **Device-dependent spaces** — Express color relative to some other reference space. Tell you about the subset of colors displayable/capturable by a particular device.
- **Device-independent spaces** — Express color in absolute terms (CIE L*a*b*, CIE XYZ). Serve as universal reference colors.
- **Working spaces** — Used by image editing programs and file formats to constrain the range of colors to a standard palette (sRGB, Adobe RGB, ProPhoto RGB).

## Choosing a Working Space

### Considerations

1. **Bit depth**: ProPhoto RGB requires 16-bit to avoid posterization
2. **Output intent**: Web (sRGB) vs. print (Adobe RGB or ProPhoto) vs. both (Adobe RGB as compromise)
3. **Scene content**: Wide-gamut scenes (vivid flowers, sunsets) benefit from wider spaces
4. **Software support**: Not all applications handle wide-gamut spaces correctly
5. **Monitor capability**: Most consumer monitors cannot display beyond sRGB

### General Recommendations

- **Web/screen only**: sRGB
- **Print only**: Adobe RGB (8-bit) or ProPhoto RGB (16-bit)
- **Both print and screen**: Edit in Adobe RGB or ProPhoto, export sRGB for web
- **Archival master**: ProPhoto RGB in 16-bit TIFF
- **Maximum compatibility**: sRGB with embedded ICC profile

## Color Space Conversion

Converting between color spaces involves:
1. Convert source space → Profile Connection Space (PCS, typically CIELAB or CIEXYZ)
2. Convert PCS → destination space

This is handled by the Color Management Module (CMM) using rendering intents:
- **Perceptual**: Smoothly compresses gamut, preserves visual relationships
- **Relative colorimetric**: Clips out-of-gamut colors, preserves in-gamut colors exactly
- **Absolute colorimetric**: Matches exact colorimetry values (includes paper white simulation)
- **Saturation**: Preserves saturation at expense of accuracy

## The Gamut Mapping Problem

The fundamental challenge: no output device can reproduce all colors the human eye can see. Every translation between devices requires compromises near the borders of the gamut.

**Example**: Dark highly saturated purplish-blue of a computer monitor's "blue" primary is impossible to print on paper with CMYK. The nearest approximation in the printer's gamut will be much less saturated. Conversely, an inkjet printer's "cyan" primary is outside the gamut of a typical monitor.

## ICC Profile Embedding

To ensure correct color interpretation, ICC profiles can be embedded in image files. Supported formats:
- TIFF
- JPEG
- PNG
- EPS
- SVG

Without an embedded profile, applications must assume a color space (typically sRGB), which may lead to incorrect color rendering.

## References

- Cambridge in Colour: "Color Management: Understanding Color Spaces". https://www.cambridgeincolour.com/tutorials/color-spaces.htm
- Cambridge in Colour: "sRGB vs. Adobe RGB 1998". https://www.cambridgeincolour.com/tutorials/sRGB-AdobeRGB1998.htm
- Rodney, Andrew (2005). *Color Management for Photographers*. Focal Press.
- Adobe Systems. "The role of working spaces in Adobe applications". Technical Paper.
- ICC White Paper 20: "Digital photography color management basics". https://www.color.org
- CIE 1931, 1976 specifications for standard colorimetric observer and color spaces
