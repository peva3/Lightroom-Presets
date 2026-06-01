# Ricoh High-Contrast Monochrome — Community Lightroom Recipes

## The Problem

Ricoh does **not** provide Adobe Camera Matching profiles (`.dcp` files) for Lightroom or Camera Raw. Unlike Fujifilm, whose film simulations have official Adobe counterparts, Ricoh GR users shooting RAW must either:

1. Convert RAW in-camera to JPEG with the HC B&W effect applied
2. Use third-party paid Lightroom profiles (PerfeFilm, RNI, etc.)
3. Build a manual Lightroom preset that approximates the look

This document collects community-sourced approaches for replicating Ricoh's HC B&W aesthetic in Lightroom.

---

## Approach 1: PerfeFilm Lightroom Profiles (Paid)

**Source**: [perfefilm.com](https://perfefilm.com/collections/ricoh-digital-camera-collection)

PerfeFilm sells Lightroom camera raw color profiles that simulate Ricoh GR in-camera color modes. Their GR II and GR III packs include:

- **GR II**: BW, BW Hard, BW Hi-Contrast MAX, BW Soft, Positive Film, Cross Process, Bleach Bypass, Monochrome
- **GR III**: Monotone, Soft Monotone, Hard Monotone, Hi-Contrast B&W, Positive Film, Negative Film, Bleach Bypass, Cross Processing

They also sell complementary "Film Tone" presets and a grain preset.

**PerfeFilm's own grain recommendation for GR3 BW-hi on other cameras**:
```
Amount: 100
Size: 26
Roughness: 100
```
Apply these Lightroom grain settings after applying the PerfeFilm profile to more closely simulate high-ISO negative grain texture.

**Cost**: ~$25 USD for a single camera pack; ~$40 for the "King Bundle" (all cameras + all films).

**Quality**: According to PerfeFilm's published side-by-side comparisons, their profiles achieve very close color/tone matching to the camera's output. However, grain rendering will always differ because Lightroom's grain engine is different from Ricoh's in-camera grain synthesis.

---

## Approach 2: Manual Lightroom Preset — "Dramatic Monochrome"

**Source**: Ritchie's Ricoh Recipes — adapted from the in-camera "Dramatic Monochrome" recipe to Lightroom equivalents.

The in-camera recipe (GR III) uses:
- Effect: **Hi-Contrast B&W**
- High/Low Key: **-1**
- Contrast: **+3**
- Contrast (Highlight): **-3**
- Contrast (Shadow): **-3**
- Sharpness: **0**
- Toning: **Off**
- Filter Effect: **2** (digital red/orange filter for darkening skies)
- Shading: **0**
- Clarity: **+1**
- Grain Effect: **3**
- Highlight Correction: **On**
- Shadow Correction: **Low**
- White Balance: **CT 10000K**
- WB Compensation: **A:0 M:14**
- ISO: up to ISO 6400
- Exposure Compensation: **-1/3 to +1/3**

### Lightroom Approximations

#### Basic Panel
```
Treatment: Black & White
Exposure: -0.33 to +0.33 (scene-dependent)
Contrast: +80
Highlights: -60 (important — preserve some highlight detail)
Shadows: -50 (crush toward black)
Whites: +30
Blacks: -60
```

#### B&W Mix Panel (to mimic Filter Effect 2 / orange-red filter)
```
Red: +40
Orange: +20
Yellow: 0
Green: -30
Aqua: -40
Blue: -60
Purple: -30
Magenta: 0
```
This mix simulates a red/orange filter: darkens sky, lightens skin tones slightly.

#### Tone Curve
```
Point Curve: Strong Contrast (built-in)
Parametric:
  Highlights: +15
  Lights: +10
  Darks: -10
  Shadows: -15
```

#### Presence
```
Clarity: +25
Dehaze: +15 (adds midtone punch and grit)
```

#### Grain
```
Amount: 55
Size: 30
Roughness: 70
```

#### Vignette (to simulate Shading 0 / slight natural vignette)
```
Post-Crop Vignetting: -10
Midpoint: 50
Feather: 50
```

---

## Approach 3: "Aggressive HC B&W" Preset (the Moriyama-style recipe)

This pushes closer to the Daido Moriyama aesthetic — heavier grain, more extreme contrast, less highlight protection.

### Lightroom Settings

```
Treatment: Black & White
Profile: Adobe Monochrome (or a linear B&W profile)

Basic:
  Exposure: -0.50 (slight underexposure raises contrast)
  Contrast: +100
  Highlights: -20
  Shadows: -80
  Whites: +50
  Blacks: -80

Tone Curve (Point):
  [0,0] → [25,0] (crush bottom 10%)
  [75,255] → [100,255] (push highlights toward clipping)
  A sharp S-curve with minimal shoulder/knee

B&W Mix (intensify Moriyama's preferred film sensitivity):
  Red: +20
  Orange: +15
  Yellow: -10
  Green: -50
  Aqua: -60
  Blue: -80
  Purple: -40
  Magenta: 0

Presence:
  Texture: +30
  Clarity: +60
  Dehaze: +30

Grain:
  Amount: 80
  Size: 35
  Roughness: 85

Effects:
  Post-Crop Vignetting: -15
  Midpoint: 35

Sharpening:
  Amount: 60
  Radius: 1.2
  Detail: 40
  Masking: 20
```

**Notes**: This preset should be used on images exposed for the highlights. Moriyama's darkroom style involved high-contrast printing paper (grades 4–5), often with pushed development. The aggressive grain + clarity + dehaze combination reproduces the "gritty" texture.

---

## Approach 4: "GR II BW Hi-Contrast MAX" Replication

The GR II's BW-MAX mode is considered by some to be superior to the GR III's HC B&W — punchier, less refined.

### Lightroom Settings

```
Treatment: Black & White

Basic:
  Exposure: -0.33
  Contrast: +95
  Highlights: -40
  Shadows: -70
  Whites: +40
  Blacks: -70

B&W Mix:
  Red: +30
  Orange: +25
  Yellow: 0
  Green: -50
  Aqua: -70
  Blue: -90
  Purple: -30
  Magenta: 0

Tone Curve:
  Lights: +20
  Darks: -20
  Shadows: -25

Presence:
  Clarity: +20
  Dehaze: +10

Grain:
  Amount: 60
  Size: 28
  Roughness: 75

Effects:
  Post-Crop Vignetting: -20
  Midpoint: 40
  Grain: applied as above
```

---

## Approach 5: Using Linear Profile + Manual Curve (Most Accurate)

For maximum control and accuracy, some community members recommend starting from a **linear RAW profile** (bypassing Adobe's default tone curve) and building the HC B&W look completely from scratch.

This requires generating a linear DCP profile (using Adobe DNG Profile Editor or similar tools) and building the contrast curve manually.

### Steps:
1. Create or download a "Linear" or "Neutral Flat" DCP profile for your camera
2. Apply B&W treatment
3. Build a custom Point Curve that maps:
   - Input 0–15% → Output 0–5% (shadow crush)
   - Input 15–40% → Output 5–20% (steep midtone ramp)
   - Input 40–60% → Output 20–50% (midtones)
   - Input 60–85% → Output 50–90% (highlight push)
   - Input 85–100% → Output 90–100% (highlight compression)
4. Add grain, clarity, vignette to taste

This is the most work-intensive approach but yields the closest match to the actual JPEG engine output.

---

## Community Recipe Sources

| Source | URL | Notes |
|--------|-----|-------|
| Ritchie's Ricoh Recipes | ricohrecipes.com | The definitive community GR recipe site; 6 B&W JPEG recipes plus a mobile app |
| GR Recipe | grrecipe.com | Recipe sharing community with recipe decoder tool (extracts settings from JPEG EXIF) |
| PerfeFilm | perfefilm.com | Paid LR profiles; includes free demo |
| Aditya Ardiya's Blog | ardiya.dev/blog/ricoh-bw-recipe/ | Clean monochrome recipe using Hard Monotone |
| Michael Kirchherr | michaelkirchherr.com | Recipe comparisons; emphasizes shooting RAW+JPEG for flexibility |

## Key Takeaways

1. **No free, perfect solution exists.** Ricoh's refusal to ship Adobe profiles means users must choose between paid profiles (PerfeFilm), in-camera JPEG conversion, or approximate manual presets.

2. **The in-camera JPEG engine applies grain BEFORE the contrast curve**, which is impossible to replicate exactly in Lightroom (Lightroom's grain is applied post-tone-curve). This means the grain character will always differ.

3. **GR II vs GR III HC B&W are different looks.** If you're targeting one specifically, calibrate accordingly.

4. **The red/orange filter simulation is critical.** Ricoh's HC B&W profile, even at default, has a built-in panchromatic sensitivity that differs from a straight desaturation. The B&W Mix panel in LR is the main tool for matching this.

5. **Underexpose slightly (-0.3 to -0.7 EV) when shooting RAW intended for HC B&W conversion.** This protects highlight detail and produces a contrast starting point that's closer to the in-camera JPEG engine's behavior.

6. **Shoot RAW+JPEG** if possible — use the SOOC JPEG as a reference for your Lightroom preset calibration.

---

## Post-Merge Update (fuzzy)

Changes applied to `Presets/Black-White/Ricoh High-Contrast Monochrome.xmp` via fuzzy community merge (2026-06-01):

| Parameter | Before | After | Method |
|---|---|---|---|
| Contrast2012 | +50 | +80 | Replaced (community +80) |
| Highlights2012 | +32.5 | -60 | Replaced (community -60) |
| Shadows2012 | -42.5 | -46.3 | Averaged (community -50) |
| Blacks2012 | -55 | -57.5 | Averaged (community -60) |
| Clarity2012 | +40 | +25 | Replaced (community +25) |
| Dehaze | +12.5 | +13.8 | Averaged (community +15) |
| GrayMixerRed | -12.5 | +40 | Replaced (community +40) |
| GrayMixerOrange | -2.5 | +20 | Replaced (community +20) |
| GrayMixerYellow | +2.5 | 0 | Replaced (community 0) |
| GrayMixerGreen | +10 | -30 | Replaced (community -30) |
| GrayMixerAqua | +2.5 | -40 | Replaced (community -40) |
| GrayMixerBlue | -22.5 | -60 | Replaced (community -60) |
| GrayMixerPurple | -5 | -30 | Replaced (community -30) |
| GrayMixerMagenta | -5 | 0 | Replaced (community 0) |
| GrainAmount | +62.5 | +58.8 | Averaged (community 55) |
| GrainSize | 50 | 30 | Replaced (community 30) |
| GrainFrequency | +62.5 | +66.3 | Averaged (community 70) |

## Community Validated Values (2026)

Final consensus values from cross-referencing community recipes. Applied to `Presets/Black-White/Ricoh High-Contrast Monochrome.xmp` on 2026-06-01.

| Parameter | Final Value | Community Range | Source |
|-----------|------------|-----------------|--------|
| **Basic Panel** | | | |
| Contrast2012 | +80 | +80 | Approach 2 (Ritchie's Recipes) |
| Highlights2012 | -60 | -60 | Approach 2 |
| Shadows2012 | -46.3 | -50 | Averaged |
| Whites2012 | +25 | +25 | Approach 2 |
| Blacks2012 | -57.5 | -60 | Averaged |
| Clarity2012 | +25 | +25 | Approach 2 |
| Dehaze | +13.8 | +15 | Averaged |
| **B&W Mix** | | | |
| Red | +40 | +40 | Simulates Filter Effect 2 (orange-red) |
| Orange | +20 | +20 | Approach 2 |
| Yellow | 0 | 0 | Approach 2 |
| Green | -30 | -30 | Approach 2 |
| Aqua | -40 | -40 | Approach 2 |
| Blue | -60 | -60 | Strong sky darkening |
| Purple | -30 | -30 | Approach 2 |
| Magenta | 0 | 0 | Approach 2 |
| **Grain** | | | |
| Amount | 58.8 | 55 | Averaged |
| Size | 30 | 30 | Approach 2 |
| Frequency | 66.3 | 70 | Averaged |

**Key sources:** Ritchie's Ricoh Recipes (ricohrecipes.com), PerfeFilm profiles (perfefilm.com), GR Recipe community (grrecipe.com), Aditya Ardiya's blog, Michael Kirchherr comparisons.
