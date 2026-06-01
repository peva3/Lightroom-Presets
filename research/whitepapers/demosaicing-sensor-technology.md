# Digital Camera Sensors & Demosaicing

**Source URLs:**
- https://www.cambridgeincolour.com/tutorials/camera-sensors.htm (Cambridge in Colour)
- https://rawpedia.rawtherapee.com/Demosaicing (RawPedia)
**Authors:** Cambridge in Colour / RawTherapee Contributors
**Dates:** 2005-2020 (Cambridge in Colour) / December 2019 (RawPedia)

---

## Part 1: Digital Camera Sensors (Cambridge in Colour)

A digital camera uses an array of millions of tiny light cavities or "photosites" to record an image. When you press your camera's shutter button and the exposure begins, each of these is uncovered to collect photons and store those as an electrical signal. Once the exposure finishes, the camera closes each of these photosites, and then tries to assess how many photons fell into each cavity by measuring the strength of the electrical signal. The signals are then quantified as digital values, with a precision that is determined by the bit depth. The resulting precision may then be reduced again depending on which file format is being recorded (0 - 255 for an 8-bit JPEG file).

### Bayer Color Filter Array

To capture color images, a filter has to be placed over each cavity that permits only particular colors of light. Virtually all current digital cameras can only capture one of three primary colors in each cavity, and so they discard roughly 2/3 of the incoming light. As a result, the camera has to approximate the other two primary colors in order to have full color at every pixel. The most common type of color filter array is called a "Bayer array."

A Bayer array consists of alternating rows of red-green and green-blue filters. Notice how the Bayer array contains twice as many green as red or blue sensors. Each primary color does not receive an equal fraction of the total area because the human eye is more sensitive to green light than both red and blue light. Redundancy with green pixels produces an image which appears less noisy and has finer detail than could be accomplished if each color were treated equally. This also explains why noise in the green channel is much less than for the other two primary colors.

Note: Not all digital cameras use a Bayer array. The Foveon sensor captures all three colors at each pixel location. Other sensors might capture four colors: red, green, blue and emerald green.

### Bayer Demosaicing

Bayer "demosaicing" is the process of translating this Bayer array of primary colors into a final image which contains full color information at each pixel. If the camera treated all of the colors in each 2x2 array as having landed in the same place, then it would only be able to achieve half the resolution in both the horizontal and vertical directions. If a camera computed the color using several overlapping 2x2 arrays, then it could achieve a higher resolution.

### Demosaicing Artifacts

Images with small-scale detail near the resolution limit of the digital sensor can sometimes trick the demosaicing algorithm - producing an unrealistic looking result. The most common artifact is moiré, which may appear as repeating patterns, color artifacts or pixels arranged in an unrealistic maze-like pattern.

However, even with a theoretically perfect sensor that could capture and distinguish all colors at each photosite, moiré and other artifacts could still appear. This is an unavoidable consequence of any system that samples an otherwise continuous signal at discrete intervals or locations. For this reason, virtually every photographic digital sensor incorporates something called an optical low-pass filter (OLPF) or an anti-aliasing (AA) filter.

### Microlens Arrays

Real-world camera sensors do not actually have photosites which cover the entire surface of the sensor. In fact, they may cover just half the total area in order to accommodate other electronics. Digital cameras contain "microlenses" above each photosite to enhance their light-gathering ability. These lenses are analogous to funnels which direct photons into the photosite where the photons would have otherwise been unused.

Well-designed microlenses can improve the photon signal at each photosite, and subsequently create images which have less noise for the same exposure time.

## Part 2: Demosaicing Algorithms (RawPedia)

Most digital cameras use a sensor which contains millions of homogeneous light-sensitive elements, called sensels or photosites. In order to capture color, a color filter array (CFA) is placed over the sensor, so that specific photosites register specific wavelengths of light. The "Bayer filter" is the most common - it uses a repetitive 2x2 matrix of green, blue, red and green patches.

There is also a filter arrangement called "X-Trans", used by some Fujifilm cameras, with a repetitive 6x6 matrix of patches.

As each photosite is responsible for capturing only a specific band of light, there are three main problems:
1. There is no concept of color yet, as each photosite registers only a single electric charge
2. There are twice as many green photosites as either red or blue
3. Half (green) or three-fourths (red, blue) of each color channel consist of a lack of data

The process of converting the mosaic of discrete data points into a cogent color image is called **demosaicing**.

### Demosaicing Methods for Bayer Sensors

**AMaZE** (Aliasing Minimization and Zipper Elimination)
The default method in many raw processors. Generally the best method for lower-ISO images.

**RCD** (Ratio Corrected Demosaicing)
Does an excellent job for round edges (e.g., stars in astrophotography) while preserving almost the same level of detail as AMaZE.

**DCB**
Produces similar results to AMaZE. AMaZE can often be slightly superior in recovering details, while DCB can be better at avoiding false colors, especially in images from cameras without anti-aliasing filters.

**LMMSE and IGV**
Recommended when working with very noisy, high ISO images, in conjunction with Noise Reduction. They will prevent false maze patterns from appearing and prevent the image from looking washed-out due to heavy noise reduction. IGV is also quite effective at mitigating moiré patterns.

**VNG4** (Variable Number of Gradients)
Useful for medium format technical cameras with near-symmetrical wide angle lenses where crosstalk between photosites can cause mazing artifacts with AMaZE and DCB.

**AHD, EAHD, HPHD**
Older methods which are generally slower and inferior to the other methods.

**Pixel Shift**
Some Pentax and Sony cameras support Pixel Shift mode, which shoots four frames with the sensor offset one pixel at a time. All frames can be combined into one image while automatically masking-out moving objects, reducing noise and increasing sharpness.

### Demosaicing Methods for X-Trans Sensors

**3-Pass (Markesteijn)**
Runs three passes over the image which leads to sharper results on low ISO photos. Generally the best method for X-Trans sensors.

**1-Pass (Markesteijn)**
Faster than 3-pass but slightly inferior in quality, though this difference is only visible in low ISO shots.

### Dual Demosaic

Dual-demosaic methods (e.g., AMaZE+VNG4) allow demosaicing areas of high contrast using one method and areas of low contrast using another algorithm. Some algorithms are better at rendering fine detail while others are better at rendering smooth, plain areas.

### False Color Suppression

Sets the number of median filter passes applied to suppress demosaicing artifacts. False colors (speckles) could be introduced during the demosaicing phase where very fine detail is resolved. False color suppression is similar to color smoothing. The luminance channel is not affected.

False colors are generally more apparent in images from cameras without anti-aliasing filters. Note that it is foremost the selected demosaicing algorithm which is the deciding factor in how prominent the false color problem will be.

### Monochrome Cameras

A monochrome camera has a homogeneous filter in front of the sensor - you get a black-and-white image, and no demosaicing is required. Some have no infrared filter and are thus sensitive to infrared light, which can be used for creative black and white photography.

## Relevance to Lightroom/ACR

Adobe Camera Raw and Lightroom use proprietary demosaicing algorithms that are continuously improved with each Process Version update. The choice of demosaicing algorithm affects:
1. Fine detail rendering and sharpness
2. Color accuracy, especially near edges
3. Artifacts like maze patterns and false colors
4. Noise characteristics

This is why ProcessVersion is critical in XMP presets - older process versions use older demosaicing which may produce different color and detail rendering from what was intended.
