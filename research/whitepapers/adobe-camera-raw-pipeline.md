# Adobe Camera Raw Pipeline & Processing

**Source URL:** https://helpx.adobe.com/camera-raw/using/introduction-camera-raw.html
**Author:** Adobe Inc.
**Date:** April 16, 2024 (last updated)
**Also covers:** Process Versions (https://helpx.adobe.com/camera-raw/using/process-versions.html) and Settings Management (https://helpx.adobe.com/camera-raw/using/camera-raw-settings.html)

---

## About Camera Raw Files

A camera raw file contains unprocessed, uncompressed grayscale picture data from a digital camera's image sensor, along with information about how the image was captured (metadata). Photoshop Camera Raw software interprets the camera raw file, using information about the camera and the image's metadata to construct and process a color image.

Think of a camera raw file as your photo negative. You can reprocess the file at any time, achieving the results that you want by making adjustments for white balance, tonal range, contrast, color saturation, and sharpening. When you adjust a camera raw image, the original camera raw data is preserved. Adjustments are stored as metadata in an accompanying sidecar file, in a database, or in the file itself (in the case of DNG format).

When you shoot JPEG files with your camera, the camera automatically processes the JPEG file to enhance and compress the image. You generally have little control over how this processing occurs. Shooting camera raw images with your camera gives you greater control than shooting JPEG images, because camera raw does not lock you into processing done by your camera.

**Note:** The Photoshop Raw format (.raw) is different from camera raw file formats. File extensions for camera raw files vary depending on the camera manufacturer.

## Linear Tone Response

Digital cameras capture and store camera raw data with a linear tone response curve (gamma 1.0). Both film and the human eye have a nonlinear, logarithmic response to light (gamma greater than 2). An unprocessed camera raw image viewed as a grayscale image would seem very dark, because what appears twice as bright to the photosensor and computer seems less than twice as bright to the human eye.

## About Adobe Camera Raw

Camera Raw software is included as a plug-in with Adobe After Effects and Adobe Photoshop, and also adds functionality to Adobe Bridge. Camera Raw gives each of these applications the ability to import and work with camera raw files. You can also use Camera Raw to work with JPEG and TIFF files.

- Camera Raw supports images up to 65,000 pixels long or wide and up to 512 megapixels
- Camera Raw converts CMYK images to RGB upon opening

### Processing Workflow

1. **Transfer and organize:** Copy camera raw files to your hard disk, organize them, and (optionally) convert them to DNG using Adobe Bridge's Get Photos From Camera command

2. **Open in Camera Raw:** Open camera raw files from Adobe Bridge, After Effects, or Photoshop. JPEG and TIFF files can also be opened in Camera Raw from Adobe Bridge

3. **Adjust color:** Color adjustments include white balance, tone, and saturation. Most adjustments are made on the Basic tab, with fine-tuning on other tabs. Auto can be used for approximate tonal adjustments

4. **Make other adjustments:** Use tools for sharpening, noise reduction, lens defect correction, and retouching

5. **Save settings as preset:** Settings can be saved as a preset or as default image settings for a camera model, specific camera, or ISO setting

6. **Set workflow options:** Configure how images are saved from Camera Raw and how Photoshop opens them

7. **Save or open:** Apply adjustments to the camera raw file, open the adjusted image in Photoshop or After Effects, save to another format, or cancel

### Where Settings Are Stored

Adjustments are stored as metadata in either:
- The Camera Raw database
- As metadata embedded in the image file
- In a sidecar XMP file (a metadata file that accompanies a camera raw file)

Camera Raw cannot save an image in a camera raw format. After processing, you can save in DNG, JPEG, TIFF, or PSD formats.

## About the Digital Negative (DNG) Format

The Digital Negative (DNG) format is a non-proprietary, publicly documented, and widely supported format for storing raw camera data. Because DNG metadata is publicly documented, software readers such as Camera Raw do not need camera-specific knowledge to decode and process files created by a camera that supports DNG.

Metadata for adjustments made to images stored as DNG files can be embedded in the DNG file itself instead of in a sidecar XMP file or in the Camera Raw database.

## Process Versions

Process version is the technology that Camera Raw uses to adjust and render photos. Depending on which process version you use, different options and settings are available in the Basic tab and for local adjustments.

### Process Version 6
Introduced in Camera Raw 15.4 (June 2023 release). Process version 6 reduces banding when using the Color Mixer and B&W Mixer adjustments.

### Process Version 5
New images edited in Camera Raw 11 use Process Version 5. PV 5 features improved high ISO rendering that helps remove purple color casts sometimes visible in the shadows of lower light images. PV5 also features an improved Dehaze slider - you can add haze for creative reasons by moving the Dehaze slider to the left.

### Process Version 4
Images edited for the first time in Camera Raw 10 use process version 4. PV 4 adds support for the Range Mask feature and an improved Auto Mask that handles image noise better. PV 3 (2012) images are automatically upgraded to PV 4 when they have no Auto Mask adjustments applied.

### Process Version 3 (2012)
Images edited for the first time in Camera Raw 7 use process version 3. PV 3 offers new tone controls and new tone-mapping algorithms for high-contrast images. With PV 3, you can adjust Highlights, Shadows, Whites, Blacks, Exposure, and Contrast in the Basic panel. You can also apply local corrections for white balance (Temp and Tint), Highlights, Shadows, Noise, and Moiré.

### Process Version 2 (2010)
Images edited in Camera Raw 6 used PV 2 by default. PV 2 offers improved sharpening and noise-reduction from PV 1.

### Process Version 1 (2003)
The original processing engine used by Camera Raw versions 5.x and earlier.

## Snapshots

You can record the state of an image at any time by creating a snapshot. Snapshots are stored renditions of an image that contain the complete set of edits made up until the time the snapshot is created. Benefits include:
- Easily compare the effects of adjustments
- Return to an earlier state
- Work from multiple versions of an image without duplicating the original

## Significance for XMP Presets

Critical for XMP preset creation:
1. **crs:ProcessVersion="15.4"** is mandatory to force modern Camera Raw engine
2. Process version determines which sliders and behaviors are available
3. Older process versions use legacy color matrices that render differently
4. PV6 reduces banding in Color Mixer - important for film emulation presets
5. Settings from one process version may not map cleanly to another
