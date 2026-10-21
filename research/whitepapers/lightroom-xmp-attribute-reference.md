# Complete Lightroom / Camera Raw `crs:` Attribute Reference

Source basis: Adobe XMP "Camera Raw namespace" specification (namespace URI
`http://ns.adobe.com/camera-raw-settings/1.0/`, preferred prefix `crs`), the Exiv2/ExifTool `crs`
schema tables, and empirical ground truth from XMP files exported directly by Lightroom Classic
15.4 (Process Version 6). Ranges are the values Camera Raw accepts; values outside them are clamped
silently or cause the attribute to be ignored.

## 1. Required structural elements (not optional)

| Element | Why it matters | Failure mode if missing |
|---|---|---|
| `crs:ProcessVersion="15.4"` | Selects PV6 demosaic + tone mapping + banding-free Color/B&W Mixer | Falls back to a legacy pipeline; tonal response and HSL behaviour shift |
| `crs:Treatment` = `Color` / `Monochrome` | Declares which processing branch to use | B&W presets render in colour |
| `crs:ConvertToGrayscale="True"` | Actual desaturation flag | Treatment alone does not desaturate |
| `crs:SupportsAmount="True"` | Allows the preset Amount slider | Preset applies at fixed strength only |
| `<crs:Look>` block | Selects the camera profile; without it the non-linear input colour matrix is skipped | Flat, washed-out, near-linear render |
| `<crs:ToneCurvePV2012>` + Red/Green/Blue variants | Explicit neutral baseline, or the creative curve | Lightroom applies its own default curve |
| `<crs:Name>` + `<crs:Group>` child elements | Display name and import folder | Preset lands in an "Unknown" folder or shows a blank name |

Camera profiles and their UUIDs:

| Profile | UUID | Use |
|---|---|---|
| Adobe Color | `B952C21111114111B1115456789ABCDE` | General colour presets |
| Adobe Monochrome | `0C09521111114111B1115456789ABCDE` | B&W presets |
| Adobe Vivid | `EA1DE074F188405965EF399C72C221D9` | Slide film presets |
| Adobe Neutral | `01F9A11111114111B1115456789ABCDE` | Maximum-latitude starting point |
| Adobe Landscape | `AABBCC1111114111B1115456789ABCDE` | (unused in this repo) |

## 2. Basic panel

| Attribute | Range | Default | Notes |
|---|---|---|---|
| `crs:WhiteBalance` | As Shot, Auto, Daylight, Cloudy, Shade, Tungsten, Fluorescent, Flash, Custom | As Shot | Enum, not a number |
| `crs:Temperature` | 2000–50000 | As Shot | **Absolute Kelvin.** Writing a relative offset (`+300`) is a silent error |
| `crs:Tint` | −150 to +150 | 0 | Positive = magenta, negative = green |
| `crs:Exposure2012` | −5.0 to +5.0 | 0 | Linear gain; 1.0 = one stop |
| `crs:Contrast2012` | −100 to +100 | 0 | S-curve around mid-grey |
| `crs:Highlights2012` | −100 to +100 | 0 | Shoulder compression |
| `crs:Shadows2012` | −100 to +100 | 0 | Toe lift |
| `crs:Whites2012` | −100 to +100 | 0 | White point |
| `crs:Blacks2012` | −100 to +100 | 0 | Black point |
| `crs:Texture` | −100 to +100 | 0 | 5–15 px detail band |
| `crs:Clarity2012` | −100 to +100 | 0 | 30–100 px local contrast |
| `crs:Dehaze` | −100 to +100 | 0 | Negative values add atmospheric haze |
| `crs:Vibrance` | −100 to +100 | 0 | Midtone-weighted, skin-protected saturation |
| `crs:Saturation` | −100 to +100 | 0 | Global saturation |

## 3. Tone curve

Curves are **elements**, not attributes: `<crs:ToneCurvePV2012>` plus
`ToneCurvePV2012Red`, `ToneCurvePV2012Green`, `ToneCurvePV2012Blue`, each an `rdf:Seq` of
`"input, output"` pairs on a 0–255 scale.

Legacy parametric attributes (PV2012 still honours them):

| Attribute | Range | Default |
|---|---|---|
| `crs:ParametricShadows` / `Darks` / `Lights` / `Highlights` | −100 to +100 | 0 |
| `crs:ParametricShadowSplit` / `MidtoneSplit` / `HighlightSplit` | 0–100 | 25 / 50 / 75 |

## 4. HSL / Color Mixer (8 hue bands × 3 axes)

Bands: `Red, Orange, Yellow, Green, Aqua, Blue, Purple, Magenta`.

| Attribute pattern | Range | Default |
|---|---|---|
| `crs:HueAdjustment{Colour}` | −100 to +100 | 0 |
| `crs:SaturationAdjustment{Colour}` | −100 to +100 | 0 |
| `crs:LuminanceAdjustment{Colour}` | −100 to +100 | 0 |

### 4.1 Hue-axis directions (frequently encoded backwards)

| Slider | −100 | +100 |
|---|---|---|
| `HueAdjustmentYellow` | toward orange | toward green |
| `HueAdjustmentGreen` | **toward yellow (olive)** | **toward aqua (cyan)** |
| `HueAdjustmentAqua` | toward green | toward blue |
| `HueAdjustmentBlue` | toward aqua (cyan) | toward purple |

Any preset whose research calls for "olive" or "yellow-green" foliage must use a **negative**
`HueAdjustmentGreen`. A positive value pushes foliage cyan.

## 5. Color Grading (three-way wheels)

| Attribute | Range | Default | Notes |
|---|---|---|---|
| `crs:ColorGradeShadowHue` / `MidtoneHue` / `HighlightHue` | 0–360 | 0 | Degrees around the wheel |
| `crs:ColorGradeShadowSat` / `MidtoneSat` / `HighlightSat` | 0–100 | 0 | 0–30 reads natural in stills |
| `crs:ColorGradeShadowLum` / `MidtoneLum` / `HighlightLum` | −100 to +100 | 0 | Luminance offset per zone |
| `crs:ColorGradeGlobalHue` / `GlobalSat` / `GlobalLum` | as above | 0 | Applies over the whole image |
| `crs:ColorGradeBlending` | 0–100 | 50 | 50 = overlapping zones; 75–80 = clean separation |
| `crs:ColorGradeBalance` | −100 to +100 | 0 | Negative biases to shadows |

Legacy `crs:SplitToningShadowHue/…Saturation`, `SplitToningHighlightHue/…`, `SplitToningBalance`
still import, but they are the pre-CC panel. Do not mix them with ColorGrade in one preset.

## 6. Detail (sharpening & noise reduction)

| Attribute | Range | Default | Notes |
|---|---|---|---|
| `crs:Sharpness` | 0–150 | 40 | Amount slider |
| `crs:SharpenRadius` | 0.5–3.0 | +1.0 | Written with a leading `+` |
| `crs:SharpenDetail` | 0–100 | 25 | |
| `crs:SharpenEdgeMasking` | 0–100 | 0 | |
| `crs:LuminanceSmoothing` | 0–100 | 0 | Luminance NR |
| `crs:LuminanceNoiseReductionDetail` | 0–100 | 50 | |
| `crs:LuminanceNoiseReductionContrast` | 0–100 | 0 | |
| `crs:ColorNoiseReduction` | 0–100 | 25 | |
| `crs:ColorNoiseReductionDetail` | 0–100 | 50 | |
| `crs:ColorNoiseReductionSmoothness` | 0–100 | 50 | |

Silent-failure aliases that DO NOT EXIST: `SharpnessRadius`, `SharpnessDetail`,
`SharpnessEdgeMasking`, `SharpnessMasking`.

## 7. Effects (grain + vignette)

| Attribute | Range | Default | Notes |
|---|---|---|---|
| `crs:GrainAmount` | 0–100 | 0 | |
| `crs:GrainSize` | 0–100 | 25 | ≥25 begins to soften detail |
| `crs:GrainRoughness` | 0–100 | 50 | 0 = uniform digital noise, 100 = irregular |
| `crs:PostCropVignetteAmount` | −100 to +100 | 0 | Negative darkens |
| `crs:PostCropVignetteMidpoint` | 0–100 | 50 | |
| `crs:PostCropVignetteFeather` | 0–100 | 50 | |
| `crs:PostCropVignetteRoundness` | −100 to +100 | 0 | |
| `crs:PostCropVignetteStyle` | 0–3 | 1 | 0 Highlight Priority, 1 Color Priority, 2 Paint Overlay, 3 (legacy) |
| `crs:PostCropVignetteHighlightContrast` | 0–100 | 0 | |

Silent-failure alias that DOES NOT EXIST: `GrainFrequency`. The real attribute is
`GrainRoughness`.

## 8. Calibration (primary reinterpretation)

| Attribute | Range | Default |
|---|---|---|
| `crs:ShadowTint` | −100 to +100 | 0 |
| `crs:RedHue` / `crs:RedSaturation` | −100 to +100 | 0 |
| `crs:GreenHue` / `crs:GreenSaturation` | −100 to +100 | 0 |
| `crs:BlueHue` / `crs:BlueSaturation` | −100 to +100 | 0 |

## 9. B&W Mixer

`crs:ConvertToGrayscale="True"` plus `crs:GrayMixer{Colour}` for the same eight bands,
each −100 to +100 (default 0).

## 10. Lens correction, defringe, transform

| Attribute | Range | Notes |
|---|---|---|
| `crs:LensProfileEnable` | 0/1 | 1 = enable profile corrections |
| `crs:LensProfileSetup` | `LensDefaults` / `Custom` | |
| `crs:LensManualDistortionAmount` | −100 to +100 | |
| `crs:VignetteAmount` | −100 to +100 | Lens vignetting, distinct from post-crop |
| `crs:AutoLateralCA` | 0/1 | |
| `crs:DefringePurpleAmount` / `DefringeGreenAmount` | 0–20 | |
| `crs:DefringePurpleHue` / `DefringeGreenHue` | 0–100 | |
| `crs:PerspectiveUpright` | 0–5 | 0 off, 1–4 auto modes, 5 guided |
| `crs:PerspectiveVertical` / `Horizontal` / `Rotate` / `Aspect` / `Scale` / `X` / `Y` | −100 to +100 | Manual transform |

## 11. Metadata / bookkeeping

| Attribute | Meaning |
|---|---|
| `crs:PresetType` | `Normal` for user presets |
| `crs:Cluster` | Grouping string, usually empty |
| `crs:UUID` | 32-hex identifier, unique per preset |
| `crs:HasSettings="True"` | Marks the XMP as carrying develop settings |
| `crs:SupportsColor` / `SupportsMonochrome` | Which image types the preset may apply to |
| `crs:SupportsHighDynamicRange` / `SupportsNormalDynamicRange` / `SupportsSceneReferred` / `SupportsOutputReferred` / `RequiresRenditionBehavior` | Capability flags written by 15.x |

## 12. What this repo deliberately does not use

| Capability | Why excluded |
|---|---|
| `crs:HasCrop` / `crs:Crop*` | Presets must never carry a crop |
| Local adjustments (masks, gradients, brushes) | Cannot be represented in a preset |
| `crs:CameraProfile` (text) | Superseded by the `<crs:Look>` block |
| `crs:SplitToning*` | Replaced by ColorGrade; mixing both causes double-tinting |
| Absolute `WhiteBalance` enums | Presets should leave WB as shot unless the film's cast is the point |
