# Ilford HP5 Plus in Paid B&W Preset Packs

> How major commercial preset packs approach Ilford HP5 emulation.

---

## VSCO Film (Discontinued)

VSCO Film 03 and VSCO Film 07 were the gold standard for Lightroom film emulation. Their HP5 preset family included:

### HP5 400 (03 pack)
- Profile: Ilford HP5 400 (custom camera profile)
- **Contrast**: Moderate — softer than the Tri-X preset
- **Tone curve**: Gentle shoulder in highlights, open shadows
- **Grain**: Custom grain pattern overlay — moderate, tight
- **Split toning**: Warm highlights (Hue 50, Sat 5), cool shadows (Hue 230, Sat 3)
- **B&W Mix**: Slight red/orange emphasis for skin tones

### HP5 400 Push +1 (03 pack)
- Higher contrast, more grain
- Deeper blacks, brighter whites
- Grain amount increased ~50% over base preset

### HP5 400 Push +2 (03 pack)
- Heavy contrast, pronounced grain
- Shadow clipping introduced
- For "concert photography" aesthetic

### HP5 400 Pull −1 (03 pack)
- Flatter, more grey tones
- Reduced grain
- "Portrait HP5" look

### Key VSCO Insight
VSCO's HP5 preset was noticeably **less contrasty** than their Tri-X preset, with a **warmer paper-base tone** in the split toning. This reflected the real difference in the films.

---

## Mastin Labs

Mastin Labs includes HP5 in their **Ilford Original Pack**:

### Ilford HP5 (Mastin)
- **Approach**: Mastin uses custom camera profiles + tone curves
- **Base profile**: Lifts the 3/4 tones more than Ilford FP4 preset
- **Contrast**: "Medium-low" — softer than their Tri-X emulation
- **Push versions**: +1, +2, +3 (with increasing grain and contrast)
- **Grain**: Moderate grain overlay — finer than Tri-X, coarser than FP4
- **Tone**: Slightly cool-neutral rendering; less warm than VSCO
- **Special feature**: Mastin captures the HP5 "grey range" between Zone IV and Zone VI distinctively

### Mastin Labs Philosophy
Mastin's Ilford presets are described as "true to the film in a darkroom print" rather than "true to the negative scan." This means contrast and tone curves reference **printed** HP5 on Ilford Multigrade paper, not the negative itself.

---

## RNI All Films (Really Nice Images)

RNI includes HP5 in their film preset packs:

### Ilford HP5 Plus (RNI)
- **Profile-based**: Custom camera profiles with tone curves similar to VSCO
- **Rendering**: Neutral-to-warm paper base
- **Grain**: Custom grain texture — smaller and less obtrusive than Tri-X
- **Variants**: 
  - HP5 400 — standard box-speed emulation
  - HP5 800 — moderate push
  - HP5 1600 — heavy push
- **B&W Mix**: RNI tends to use slightly more red sensitivity than VSCO

### RNI vs VSCO
Users generally find RNI's HP5 slightly **cleaner** (less grain) and **more neutral** in color cast than VSCO's version.

---

## DxO FilmPack

DxO FilmPack includes Ilford HP5 Plus as a film rendering:

### HP5 Plus 400 (DxO)
- **Approach**: Physics-based film emulation using measured spectral data
- **Grain**: Algorithmically generated grain matching real HP5 RMS granularity
- **Tone curve**: Based on measured characteristic curves from Ilford datasheet
- **Contrast**: Accurate to real HP5 in ID-11 — medium-low contrast
- **Filters**: DxO includes virtual color filter simulation (Yellow, Orange, Red, etc.)
- **Frames**: Includes 35mm film frame overlays

### DxO Variants
| Variant | Equivalent |
|---|---|
| HP5 Plus 400 (standard) | Box speed, ID-11 stock |
| HP5 Plus 400 (fine grain) | HP5 in Perceptol / DD-X |
| HP5 Plus 400 (pushed +1) | EI 800 |
| HP5 Plus 400 (pushed +2) | EI 1600 |

### DxO Advantage
DxO FilmPack's rendering is widely considered the most **scientifically accurate** HP5 emulation available, as it uses measured sensitometric data rather than purely aesthetic matching.

---

## Nik Silver Efex Pro (DxO, formerly Google/Nik)

### Ilford HP5 Plus (Silver Efex)
- **Approach**: B&W conversion preset + grain simulation
- **Contrast**: Adjustable via "Soft Contrast" and structure sliders
- **Grain**: Customizable grain per luminosity zone
- **Strength**: HP5's tonality — the midtone "glow" — is well-captured by Silver Efex's U-Point local adjustments
- **Variants**: No explicit push/pull presets; contrast controlled manually

### Silver Efex Workflow for HP5
1. Select "Ilford HP5 Plus 400" film type
2. Adjust "Sensitivity" to taste (simulates EI changes)
3. Use "Soft Contrast" slider (20–30% for box speed HP5)
4. Add "Film Grain" — Silver Efex grain is generally preferred over Lightroom's native grain
5. Apply "Finish" — slight selenium or sepia split tone

---

## Dehancer Film

### Ilford HP5 (Dehancer)
- **Approach**: Film emulation via custom profiles + grain + halation
- **Strength**: Dehancer includes **halation simulation** (light bloom around highlights), which is more authentic for B&W film than most competitors
- **Grain**: Physically-based grain — HP5 grain is cubic and slightly larger than Delta 400
- **Bloom**: HP5 bloom is moderate — less than older films, more than T-grain films

---

## Cobalt Image

### HP5 Base Profiles
- Cobalt provides custom camera profiles calibrated to HP5 spectral response
- **B&W Panel**: Dedicated B&W mix panel with HP5's actual spectral sensitivity
- **Contrast**: Three variants — Standard, Soft, Hard (developer variations)
- **Grain**: No built-in grain — users add grain separately

---

## Capture One Styles

Several third-party vendors sell HP5 styles for Capture One:

### Key Differences from Lightroom
- Capture One styles affect Levels, Curve, and Clarity (no B&W Mix equivalent — color handled in Base Characteristics)
- Grain in Capture One is generally superior to Lightroom's — more film-like structure
- C1's "Film Grain" tool offers Impact and Granularity sliders that better mimic HP5's cubic grain

### Community-Favorite C1 HP5 Vendors
- **1Styles.pro**: Ilford B&W bundle (includes HP5, FP4, Delta 100/400, Pan F)
- **Phase One Styles**: "Analog Film B&W" pack
- **RNI All Films for Capture One**: Includes HP5 emulations

---

## Lightroom Mobile / Free Presets

Several community creators have released free HP5 presets:

| Creator | Platform | URL/Handle |
|---|---|---|
| The Lightroom Preset | Free | thelightroompreset.com |
| Presetlove | Free | presetlove.com |
| FilterGrade | Marketplace | filtergrade.com |
| Presetpro | Free/Paid | presetpro.com |
| Etsy Creators | Various | etsy.com — search "HP5 Lightroom preset" |

*Note: Free presets vary dramatically in quality. Most are simple contrast + B&W mix adjustments without proper grain or spectral modeling.*

---

## Comparative Summary

| Pack | Accuracy | Grain Quality | Tone Curve | Split Tone | Push Variants |
|---|---|---|---|---|---|
| **VSCO (discontinued)** | High | Good | Excellent | Yes | +1, +2, −1 |
| **Mastin Labs** | High | Good | Excellent | Yes | +1, +2, +3 |
| **RNI All Films** | High | Good | Very Good | Minimal | 400, 800, 1600 |
| **DxO FilmPack** | Highest (scientific) | Excellent | Excellent | No | +1, +2 |
| **Nik Silver Efex** | Medium | Excellent | Very Good | Manual | Manual |
| **Dehancer** | High | Excellent | Very Good | Yes | Manual (via exposure) |
| **Cobalt Image** | Very High (profiles) | None built-in | Excellent | No | Standard/Soft/Hard |
| **Free/Community** | Variable | Variable | Variable | Variable | Rarely |

---

## HP5-Specific Settings Comparison (Box Speed)

### Contrast (relative)
```
Lowest  →  Highest
DxO     < RNI  < Mastin < VSCO  < Dehancer
(14%)     (18%)  (22%)    (25%)    (28%)
```

### Grain Amount (relative)
```
Least   →  Most
DxO     < RNI  < Cobalt* < VSCO  < Dehancer < Nik SEFX
(15)      (20)   (n/a)     (25)    (30)       (35-40)
*Cobalt doesn't add grain
```

### Warmth of Split Tone
```
Coolest  →  Warmest
SilverEfex < Mastin < RNI < VSCO < Dehancer
(neutral)     (slight) (warm) (warm) (warmest)
```

---

## What Commercial Packs Get Right

1. **Mid-tone contrast**: HP5's signature is mid-tone contrast, not overall contrast. Packs with separate "mid-tone contrast" sliders (Mastin, Silver Efex) capture this best.
2. **Shadow openness**: HP5 shadows are more open than Tri-X. Commercial packs reflect this with higher shadow values.
3. **Grain character**: HP5 grain is present but not dominant at box speed — larger and more structured than T-grain films.

## What Commercial Packs Miss

1. **Developer variation**: Few packs model different developers (ID-11 vs DD-X vs HC-110). DxO comes closest.
2. **Format differences**: 35mm HP5 has more apparent grain than 120 HP5. Almost no pack distinguishes formats.
3. **Spectral accuracy**: Most packs use generic B&W Mix without modeling HP5's actual spectral sensitivity curve. Cobalt Image is the exception.
4. **Reciprocity effects**: No pack models the contrast/grain changes from long exposures.
