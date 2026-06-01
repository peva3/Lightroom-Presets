# Color Management Workflows: ICC Profiles, Rendering Intents, and Chromatic Adaptation

**Source:** https://en.wikipedia.org/wiki/Color_management, https://www.color.org/whitepapers.xalter, https://en.wikipedia.org/wiki/Chromatic_adaptation
**Authors:** Wikipedia contributors, International Color Consortium (ICC), CIE
**Date:** ICC v4 published 2001 (ISO 15076-1); consolidated 2025-2026

---

## Color Management Overview

Color management is the process of ensuring consistent and accurate colors across various devices, such as monitors, printers, and cameras. It involves the use of color profiles—standardized descriptions of how colors should be displayed or reproduced.

### The Three-Step Process

1. **Characterize** — Every color-managed device requires a personalized table ("color profile") which characterizes the color response of that particular device.
2. **Standardize** — Each color profile describes these colors relative to a standardized set of reference colors (the "Profile Connection Space").
3. **Translate** — Color-managed software uses these standardized profiles to translate color from one device to another, usually via a color management module (CMM).

## ICC Profiles

The International Color Consortium (ICC) is an industry consortium that has defined:
- An open standard for a Color Matching Module (CMM) at the OS level
- Color profiles for devices, including DeviceLink profiles
- Working spaces (the color spaces in which color data is meant to be manipulated)

### Profile Types

Device profiles describe the color capabilities of specific hardware:
- **Input profiles** — scanners, digital cameras
- **Display profiles** — monitors, projectors
- **Output profiles** — printers, presses

**DeviceLink profiles** transform one device profile (color space) to another without passing through an intermediate color space (like L*a*b*), more accurately preserving color.

### Profile Embedding

Image formats (TIFF, JPEG, PNG, EPS, PDF, SVG) may contain embedded color profiles but are not required to. The ICC standard permits embedding color profiles as metadata, storing them in databases or profile directories.

### Working Spaces

Common working spaces include sRGB, Adobe RGB, and ProPhoto RGB. These are color spaces that facilitate good results while editing. Key considerations:
- **Large gamut** working space → risk of posterization
- **Small gamut** working space → risk of clipping

This trade-off is a critical consideration for image editors.

## Profile Connection Space (PCS)

Translations between two color spaces go through a profile connection space:
```
Color Space 1 → PCS (CIELAB or CIEXYZ) → Color Space 2
```
Conversions into and out of the PCS are each specified by a profile.

## Gamut Mapping and Rendering Intents

When the gamut of source color space exceeds that of the destination, saturated colors are liable to become clipped. The ICC specification includes four rendering intents:

### Absolute Colorimetric
- Exact output of specified CIELAB values (instrument measurements match)
- Colors outside the output system's gamut are mapped to the boundary
- Useful for getting exact specified colors (e.g., "IBM blue") or quantifying mapping accuracy
- **Not recommended for photography** — causes color casts when media white differs

### Relative Colorimetric
- Truthful to specified color, with only media white correction
- Default rendering intent on many systems
- In-gamut colors unchanged; out-of-gamut colors are clamped
- Useful in proofing applications
- **Recommended for photography** when most colors are in-gamut

### Perceptual
- Smoothly moves out-of-gamut colors into gamut, preserving gradations
- Distorts in-gamut colors in the process
- Results depend heavily on profile maker (key differentiator among competitors)
- **Recommended for color separation** and when many colors are out-of-gamut

### Saturation
- Preserves saturation (colorfulness) at the expense of hue accuracy
- Useful for charts, diagrams, business graphics with discrete color palettes
- **Not recommended for photography**

### Black Point Compensation (BPC)
A technique commonly used in ICC-based workflows. For ICCv4, always applied to the perceptual intent. For ICCv2 sRGB profiles, BPC application varies between profiles. Published as ISO 18619.

## Chromatic Adaptation Transforms

Chromatic adaptation is the human visual system's ability to adjust to changes in illumination to preserve the appearance of object colors. A chromatic adaptation transform (CAT) function emulates this in color appearance models.

### Von Kries Transform

The fundamental approach: apply independent gain adjustments to each of the three cone response types:
```
D = diag(L_2/L_1, M_2/M_1, S_2/S_1)
```
This diagonal matrix maps cone responses from one adaptation state to another. When adaptation state is determined by the illuminant, this is an illuminant adaptation transform.

The full von Kries transform includes matrix transformations into and out of LMS space with the diagonal transform in the middle:
```
XYZ_source → LMS_source → [diagonal scaling] → LMS_dest → XYZ_dest
```

### CIE CAT Implementations

- **CIELAB** — Performs a "simple" von Kries-type transform directly in XYZ space (often called "wrong von Kries")
- **CIELUV** — Uses a Judd-type (translational) white point adaptation
- **CMCCAT97** — Used in CIECAM97s
- **CMCCAT2000** — Simplified version of CMCCAT97
- **CAT02 / CIECAT02** — Used in CIECAM02; performs adaptation in spectrally sharpened LMS space with the degree of adaptation controlled by the D parameter
- **Bradford Transform** — Used in LLAB color appearance model and adopted by ICC profiles in conjunction with CIELAB to compensate for CIELAB's limitations

The degree of adaptation D can range from:
- **D = 0**: No adaptation (stimulus considered self-luminous)
- **D = 1**: Complete adaptation (full color constancy)
- **Typical values**: 0.65 to 1.0

### Partial Adaptation

ICC has published a technical note on partial adaptation, recognizing that in practice, complete chromatic adaptation rarely occurs, particularly when viewing images on displays.

## Color Management Modules (CMMs)

A CMM is the software algorithm that adjusts numerical values sent to/received from different devices to maintain consistent perceived color. Well-known CMMs:
- **ColorSync** (Apple) — Default on macOS/iOS since 1993
- **Adobe CMM / Adobe Color Engine** — Used in Adobe applications, also available as standalone
- **Little CMS (lcms)** — Open source, widely used on Linux and in many applications
- **ArgyllCMS** — Open source, focus on measurement and profiling

## OS-Level Color Management

### macOS/iOS (Apple)
System-wide color management via ColorSync since 1993. Automatic color management assuming sRGB and DCI-P3 for most content on modern systems.

### Windows
ICM (Image Color Management) since 1997. WCS (Windows Color System) since Vista, which uses CIECAM02 for color matching. Auto Color Management (ACM) was introduced in Windows 11 22H2. Applications must explicitly opt in to color management; many do not.

### Linux
ICC profile support via X Window System. Coordinated through OpenICC at freedesktop.org, using LittleCMS. Less mature than macOS or Windows implementations.

## ICC White Papers

The ICC publishes extensive documentation on color management:

- **WP3**: Recommendations for colour measurement
- **WP4**: Conceptual overview of color management (updated Oct 2020)
- **WP7**: ICC profiles in a colour reproduction system
- **WP9**: Common color management workflows & rendering intent usage
- **WP17**: Using ICC profiles with digital camera images
- **WP20**: Digital photography color management basics
- **WP24**: ICC Profiles, Color Appearance Modeling, and WCS
- **WP26**: Using the v4 sRGB ICC profile
- **WP27**: Evaluating color transforms in ICC profiles
- **WP40**: Black-point compensation: theory and application (superseded by ISO 18619)

## Digital Photography Considerations

The ICC White Paper 20 notes that photographers face unique challenges: the actual scene may go beyond the recording capability of cameras and beyond the ability of output devices to reproduce. The paper describes:
- Steps from raw camera capture to rendered output and data encoding
- Scene-referred vs. output-referred colorimetry
- The role of color rendering in scene-to-picture processing

## References

- Rodney, Andrew (2005). *Color Management for Photographers*. Focal Press.
- Fraser, Bruce; Bunting, Fred; Murphy, Chris (2004). *Real World Color Management* (2nd ed.). Pearson Education.
- ICC White Papers collection: https://www.color.org/whitepapers.xalter
- CIE TC 1-52 (2004). *A Review of Chromatic Adaptation Transforms*. CIE 160:2004.
- Luo, Ming Ronnier (2015). "CIE Chromatic Adaptation; Comparison of von Kries, CIELAB, CMCCAT97 and CAT02". *Encyclopedia of Color Science and Technology*. Springer.
