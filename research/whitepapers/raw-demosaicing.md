# Demosaicing Algorithms: Bayer, X-Trans, and RAW Interpolation

**Source URLs:**
- https://rawpedia.rawtherapee.com/Demosaicing (RawTherapee / RawPedia)
- https://docs.darktable.org/usermanual/3.8/en/module-reference/processing-modules/demosaic/ (darktable 3.8 Manual)
- https://www.libraw.org/articles/bayer-moire.html (LibRaw)

**Author(s):** RawTherapee contributors, darktable project, Alex Tutubalin (LibRaw LLC)
**Date:** 2019-12-09 (RawPedia last edit), 2021 (darktable 3.8), 2012+ (LibRaw)

---

## Introduction

Most digital cameras use a sensor which contains millions of homogeneous light-sensitive elements, called sensels or photosites. In order to capture color, a **color filter array** (CFA) is placed over the sensor, so that specific photosites register specific wavelengths of light.

The **Bayer filter** is the most common — it uses a repetitive 2x2 matrix of green, blue, red and green patches. It is used by most camera manufacturers. There is also a filter arrangement called **X-Trans**, used by some Fujifilm cameras, with a repetitive 6x6 matrix of patches.

As each photosite captures only a specific band of light, there are three main problems:

1. There is no concept of color yet, as each photosite registers only a single electric charge
2. There are twice as many green photosites as either red or blue
3. Half (green) or three-fourths (red, blue) of each color channel consist of missing data

The process of converting a mosaic of discrete data points into a coherent color image is called **demosaicing** (also: demosaicking, CFA interpolation).

The choice of demosaicing algorithm can have a visually significant effect on fine detail rendering and artifact visibility (maze-like patterns, moiré, false colors).

---

## Bayer Demosaicing Algorithms

### AMaZE (Aliasing Minimization and Zipper Elimination)
The **default** method in RawTherapee and generally the best for lower-ISO images. Handles fine detail well and minimizes zipper artifacts. Can be slightly more prone to color overshoots than RCD.

### RCD (Ratio Corrected Demosaicing)
Does an excellent job for round edges (e.g. stars in astrophotography), while preserving almost the same level of detail as AMaZE. Now the default algorithm in darktable due to better performance and fewer color overshoots.

### DCB (Diagonal Interpolation Correction)
Produces similar results to AMaZE. AMaZE can be slightly superior in recovering details, while DCB can be better at avoiding false colors especially in images from cameras without anti-aliasing filters.

### LMMSE (Linear Minimum Mean Square Error)
Best suited for **high ISO, noisy images** in conjunction with noise reduction. Prevents false maze patterns and keeps the image from looking washed-out due to heavy noise reduction. In LibRaw's Bayer moire testing with blurred targets (more photographically realistic), LMMSE produced the **smallest amount of moire** among all methods.

### IGV (Iterative Green-VNG)
Effective at mitigating moiré patterns and performs well on high ISO images, similar to LMMSE.

### VNG4 (Variable Number of Gradients)
If you use a medium format technical camera with near-symmetrical wide angle lenses (e.g. Schneider Digitar 28mm or 35mm), crosstalk between photosites can cause mazing artifacts with AMaZE and DCB. VNG4 handles this situation well at the cost of some fine detail. Also useful when combining mirrorless cameras with adapted wide-angle film lenses.

### AHD, EAHD, HPHD
AHD (Adaptive Homogeneity-Directed), EAHD (Horvath's AHD), and HPHD (Heterogeneity-Projection Hard-Decision) are older, generally slower, and inferior to modern methods.

### PPG (Patterned Pixel Grouping)
Fast algorithm, formerly darktable's default. Other algorithms generally yield better results.

### Fast / Bilinear
Very fast but simple and low quality. Not recommended for production use.

### Pixel Shift
Some Pentax and Sony cameras support Pixel Shift mode, which shoots four frames with the sensor offset one pixel at a time in a circular direction. RawTherapee can combine all frames into one image while automatically masking-out moving objects.

---

## X-Trans Demosaicing (Fujifilm)

For Fujifilm cameras with X-Trans sensors:

### 3-pass (Markesteijn)
Runs three passes over the image for sharper results — visible mainly on low ISO photos. Slower than 1-pass.

### 1-pass (Markesteijn)
Faster than 3-pass but slightly inferior in quality, though the difference is only visible in low ISO shots. If speed is an issue, use this on high ISO shots.

### VNG (X-Trans)
Faster than Markesteijn 1-pass on some computers, but more prone to artifacts.

---

## Dual Demosaic Algorithms

Both RawTherapee and darktable support **dual demosaicing** methods (e.g. AMaZE+VNG4, RCD+VNG4). These demosaic areas of high contrast (detail) using one algorithm and areas of low contrast (plain areas like sky) using another.

The high-frequency algorithm (AMaZE, RCD, etc.) handles fine detail, while VNG4 handles smooth, featureless areas. The result provides a better starting point for sharpening or noise reduction.

The threshold is controlled by a **contrast threshold** slider. A gaussian-blurred single channel selection mask is calculated from the threshold and the pixels' luminance — the brighter the mask pixel, the more the output comes from the high-frequency algorithm.

Downside: the image must be demosaiced twice, doubling processing time.

---

## False Color Suppression

False colors (speckles) can be introduced during demosaicing where very fine detail is resolved. False color suppression applies median filter passes to suppress these artifacts. The luminance channel is not affected.

False colors are more apparent in cameras without anti-aliasing filters. In some situations, changing the demosaicing algorithm is preferable to enabling false color suppression, as the latter reduces color resolution.

---

## Monochrome Cameras

A monochrome camera has a homogeneous filter in front of the sensor — no demosaicing is required. Some have no infrared filter and are sensitive to IR light. RawTherapee and darktable support monochrome cameras with the "Mono" or "passthrough (monochrome)" demosaicing methods.

---

## Bayer Moire: LibRaw Analysis

LibRaw conducted experiments feeding RAW converters with artificially generated test data to isolate demosaicing behavior:

### Anti-aliasing Stability Test
A "porcupine" target — one-pixel-wide lines emerging from a common center, with intervals of 1-2 degrees — was generated as DNG. Of 12 interpolation methods tested on this synthetic target:

- **None** produced satisfactory results — ALL generated abundant color aliasing
- Three methods performed significantly better: **AMaZE > LMMSE > AHD** (in quality order)
- Half-size binning (combining 4 pixels into 1) also produced strong moire

### Commercial Converter Identification
Using the porcupine target:
- **Adobe Camera Raw 6.3**: Uses an algorithm strikingly resembling modified AHD by Paul Lee
- **HDR PhotoStudio 2.15.42**: Results extremely similar to bilinear interpolation (quality=0 in dcraw)
- **Capture One 5.2.1**: Could not be identified — unique magenta artifact pattern

### Closer-to-Reality Testing
With a Gaussian-blurred target (radius 1.0, simulating real lens/sensor behavior), **LMMSE produced the smallest amount of moire** among all methods.

### Key Conclusion
> If your camera/lens can create a pixel-sized contrast object on the matrix, you can never predict what color it will be — or know if it will bear any resemblance to the initial color.

---

## Border Handling

Demosaicing relies on sampling surrounding pixels. When demosaicing a pixel at the image edge, there are no pixels beyond the border. Most raw converters crop off a few rows and columns from the periphery. RawTherapee allows overriding this: setting border to 0 disables cropping, but artifacts may appear.

---

## Sub-Image Handling (Fujifilm EXR)

Some Fujifilm EXR cameras support "SN mode" (Signal to Noise priority) at capture time. When editing such images, the sub-image combobox allows selecting "SN mode", which blends pixels from both sub-images using a mean average for reduced noise.

---

## Match Greens / Green Equilibration

In some cameras the green filters have slightly varying properties. Darktable provides an additional equalization step to suppress artifacts with options: "disabled", "local average", "full average", and "full and local average". This is not shown for X-Trans sensors.

---

## Practical Recommendations

| Scenario | Recommended Algorithm |
|----------|----------------------|
| Low ISO, fine detail | AMaZE or RCD |
| High ISO, noisy | LMMSE or IGV |
| X-Trans (Fujifilm) | 3-pass Markesteijn (quality) or 1-pass (speed) |
| Astrophotography | RCD |
| Wide-angle crosstalk | VNG4 |
| Mixed detail + flat areas | Dual demosaic (AMaZE+VNG4 or RCD+VNG4) |
| Monochrome cameras | Mono / passthrough |

---

## References

- RawPedia Demosaicing: http://rawpedia.rawtherapee.com/Demosaicing
- darktable Demosaic module: https://docs.darktable.org/usermanual/3.8/en/module-reference/processing-modules/demosaic/
- LibRaw Bayer Moire Analysis: https://www.libraw.org/articles/bayer-moire.html
- Wikipedia Demosaicing: https://en.wikipedia.org/wiki/Demosaicing
- Wikipedia Bayer filter: https://en.wikipedia.org/wiki/Bayer_filter
- Wikipedia X-Trans sensor: https://en.wikipedia.org/wiki/Fujifilm_X-Trans_sensor
