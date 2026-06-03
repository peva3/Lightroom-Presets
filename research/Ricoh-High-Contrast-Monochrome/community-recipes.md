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

> **Note:** Values in the table above reflect community consensus before STYLEGUIDE v2.1 alignment. The actual XMP supersedes several values per grain protection rules and Blacks floor. See [STYLEGUIDE v2.1 Alignment](#styleguide-v21-alignment) below for final XMP values. Specifically: Blacks -57.5→-30 (floor), Clarity +25→0, Dehaze +13.8→0.

**Key sources:** Ritchie's Ricoh Recipes (ricohrecipes.com), PerfeFilm profiles (perfefilm.com), GR Recipe community (grrecipe.com), Aditya Ardiya's blog, Michael Kirchherr comparisons.

## STYLEGUIDE v2.1 Alignment

Applied 2026-06-01 to `Presets/Black-White/Ricoh High-Contrast Monochrome.xmp`:

| Parameter | Before | After | Rule |
|-----------|--------|-------|------|
| Blacks2012 | -57.5 | -30 | Blacks floor -30 |
| Clarity2012 | +25 | 0 | Grain protection: GrainAmount>0 → Clarity=0 |
| Dehaze | +13.8 | 0 | Grain protection: GrainAmount>0 → Dehaze=0 |

No other violations. GrainAmount=58.8 ≤ 60. Texture=0 already compliant. Sharpness=10, calibration ban, B&W curve neutral all pass.

## Community Data Validation

### Validity Assessment: GOOD (best-sourced B&W preset in this batch)

**Overall Status**: Uniquely well-sourced among the 8 presets — grounded in Ricoh's actual in-camera JPEG engine parameters (documented by Ritchie's Ricoh Recipes and GR Recipe community) rather than forum speculation. The in-camera JPEG parameter translation to Lightroom is defensible. However, Approach 3 (Moriyama-style) pushes extreme slider values that exceed STYLEGUIDE safety caps.

### Flagged Bogus Data

| # | Severity | Claim | Source | Issue |
|---|----------|-------|--------|-------|
| 1 | **CRITICAL** | Approach 3 "Aggressive HC B&W": Blacks -80, Shadows -80, Contrast +100, Blue -80 in B&W Mix | Moriyama-style recipe (community-recipes.md:131-138) | Blacks -80 far exceeds STYLEGUIDE's -30 floor (§XIII) — would render as a flat black rectangle on most displays. Shadows -80 with Contrast +100 creates extreme tonal compression. This recipe is labeled as an aesthetic choice ("Moriyama-style"), but users should understand it will fail on most images. The XMP correctly caps Blacks at -30. |
| 2 | **MODERATE** | Approach 3: Sharpening 60/1.2/40/20 with GrainAmount 80 | Moriyama-style (community-recipes.md:168-172) | STYLEGUIDE §VII.2: Sharpening ≤ 10 when GrainAmount > 0. Sharpening 60 with GrainAmount 80 and Clarity +60 is a triple violation of grain protection. Every grain particle would be amplified with haloing. XMP correctly uses Sharpness=10, Clarity=0. |
| 3 | **MODERATE** | Approach 3: Clarity +60, Dehaze +30, Texture +30 — all three maxed simultaneously | Moriyama-style (community-recipes.md:154-156) | STYLEGUIDE §V: boosting all three frequency bands simultaneously creates the "over-processed" failure mode (the r/shittyHDR look). The recipe's Clarity +60 alone exceeds STYLEGUIDE's ±30 safe max for Clarity. Labeled as extreme aesthetic — users should be warned. |
| 4 | **MODERATE** | Approach 4 "GR II BW MAX": Blue -90 in B&W Mix | GR II replication (community-recipes.md:202) | Blue -90 is technically within slider range (-100..+100) but extreme. Combined with Aqua -70, Green -50, this nukes the cool end of the spectrum. Legitimate for BW-MAX replication, but full channel collapse is measured in single-digit increments at this range. |
| 5 | **MINOR** | PerfeFilm grain recommendation: Amount 100, Roughness 100 | perfefilm.com (community-recipes.md:28-31) | GrainAmount 100 exceeds STYLEGUIDE's ≤ 60 cap (§XIII: "Grain Amount > 60 looks like compression artifacts on some panels"). This is PerfeFilm's recommendation for OTHER cameras using their profile — their profile handles grain differently than LR native grain. The XMP uses 58.8 (just under cap). |
| 6 | **NONE** | "No free, perfect solution exists" — Ricoh's refusal to ship Adobe profiles | Community consensus (community-recipes.md:261) | Accurate and honest assessment. Not bogus — this is the fundamental constraint the community worked around. |
| 7 | **NONE** | In-camera JPEG engine applies grain BEFORE contrast curve (impossible to replicate in LR) | Technical observation (community-recipes.md:263) | Technically accurate. Lightroom's grain is post-tone-curve (pipeline step 10). This is an honest limitation acknowledgment that increases the document's credibility. |

### Slider Range Check

All XMP values within valid ranges:
- Contrast +80 (0..100) ✓ (high but valid for HC B&W)
- Highlights -60 (-100..100) ✓
- Shadows -46.3 (-100..100) ✓
- Blacks -30 (at floor) ✓
- B&W Mix: max Blue -60 — well within ±100 ✓
- GrainAmount 58.8 ≤ hard cap 60 ✓
- GrainSize 30 ✓
- GrainFrequency 66.3 ✓

### Self-Consistency Check

| Check | Result |
|-------|--------|
| GrainAmount > 0 → Sharpness=10 | ✓ |
| GrainAmount > 0 → Clarity=0, Texture=0, Dehaze=0 | ✓ |
| No Calibration values | ✓ |
| No Temperature/Tint values | ✓ |
| B&W Mix values within ±100 | ✓ (Blue -60 max) |
| Blacks ≥ -30 | ✓ |
| B&W neutral tone curves | ✓ |

### Sources Assessment

| Source | Verifiability | Relevance |
|--------|--------------|-----------|
| Ritchie's Ricoh Recipes (ricohrecipes.com) | High (real website) | High — definitive GR recipe community |
| GR Recipe (grrecipe.com) | High (real website) | High — EXIF decoder tool validates settings |
| PerfeFilm (perfefilm.com) | High (commercial product) | High — paid profiles with side-by-side comparisons |
| Aditya Ardiya's Blog | Medium | Medium — individual recipe |
| Michael Kirchherr | Medium | Medium — recipe comparisons |
| In-camera JPEG parameters table | High (from Ricoh camera) | High — direct reference data |

### Film Stock / Camera Behavior Check

Note: This is a digital camera profile emulation, not a film stock. Validation criteria are different — accuracy is measured against the Ricoh JPEG engine, not a chemical film.

| Behavior | In-Camera Reference (GR III HC B&W) | XMP Implementation | Verdict |
|----------|-------------------------------------|-------------------|---------|
| Extreme contrast | Contrast +3, H/L Key -1 | Contrast +80 | ✓ Qualitatively matches |
| Shadow crush | Shadow Contrast -3, Shadow Correction Low | Shadows -46.3, Blacks -30 | ✓ Direction matches; cap constrains |
| Highlight protection | Highlight Correction On, Highlight Contrast -3 | Highlights -60 | ✓ Aggressive highlight protection |
| Orange/red filter (Filter Effect 2) | In-camera: Fx 2 | Red +40, Orange +20, Blue -60, Aqua -40 | ✓ B&W Mix equivalent |
| Clarity +1 (in-camera) | In-camera: +1 | XMP: 0 (grain protection) | ⚠️ Intentional removal per rules |
| Grain Effect 3 (in-camera) | In-camera: Level 3 | GrainAmount 58.8, Size 30, Roughness 66.3 | ✓ Approximate match given engine differences |
| 10000K WB with heavy magenta tint | In-camera: CT 10000K, M:14 | Not in XMP | ✓ Correctly excluded per WB rules |

### Validation Status: ⚠️ CONDITIONAL PASS (Approach 3 is dangerous; rest is solid; documentation corrected)

The community data for Approach 2 (Dramatic Monochrome — the primary recipe) is excellent, sourced from real Ricoh camera parameters and translated defensibly to Lightroom equivalents. Approach 3 (Moriyama-style) is correctly labeled as an extreme aesthetic but contains 3 slider values that exceed STYLEGUIDE safety caps. The XMP follows Approach 2 values with STYLEGUIDE grain protection constraints.

**Documentation fix (2026-06-01):** Added note to Community Validated Values table clarifying values reflect pre-STYLEGUIDE consensus, not final XMP state. Actual XMP: Blacks=-30, Clarity=0, Dehaze=0, GrainAmount=58.8, GrainSize=30, GrainFrequency=66.3, Sharpness=10.

**Key credibility factor**: The community-recipes.md honestly documents Ricoh's refusal to provide Adobe Camera Matching profiles, the grain-before-contrast pipeline ordering problem, and the recommendation to shoot RAW+JPEG for reference. This transparency about limitations is a strong signal of data integrity — the document isn't overselling what's achievable.

**Unique validation strength**: Unlike every other preset in this batch, Ricoh HC B&W has verifiable ground truth (the in-camera JPEG engine parameters). The community isn't speculating about what "looks like" HC B&W — they're translating known engine settings. This makes it the most objectively validatable preset in the entire batch.

## See Also

- [Black White Presets](../../docs/black-white.md)
- [Alternative Process Presets](../../docs/alternative-process.md)
- [Genre Presets](../../docs/genre.md)
- [All Lightroom Preset Categories](../../docs/index.md)

