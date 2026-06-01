# XMP Profile & Color Grading Styleguide
Version: 2.1
Purpose: An authoritative architectural and artistic framework for constructing and refining Lightroom XMP presets. Synthesizes film physics, color science, pipeline architecture, whitepaper research, and YouTube pro creator techniques. Treat this as the single source of truth before editing any XMP.

## I. Structural Integrity & System Safeguards

Adobe's Camera Raw (PV2012) engine is incredibly strict regarding XML structure.

- **Attribute Encapsulation**: All `crs:` color grading parameters, slider values, and toggles must be formatted as standard XML attributes within the root `<rdf:Description>` tag. Raw text appended outside attribute scope is silently dropped.
- **Zero Duplication**: Standard XML parsers will strictly reject any element that defines the same attribute more than once. Automated presets must ensure attributes like `crs:ColorGradeMidtoneHue` appear exactly once per file.
- **Default Fallbacks**: If an attribute is omitted from the XMP entirely, Lightroom applies its application-default value, not a neutral 0. For example, omitting `crs:Sharpness` results in Lightroom applying a default Sharpness of 40, which can severely damage film grain profiles.
- **Mandatory Boilerplate**: Every XMP MUST include ProcessVersion 15.4 (forces PV6 engine), Treatment (Color/Monochrome), the Look block (Adobe Color UUID `B952C21111114111B1115456789ABCDE` or Adobe Monochrome UUID `0C09521111114111B1115456789ABCDE`), and neutral ToneCurvePV2012 baselines (all 4 curves: `0,0` → `255,255`). Slide film presets use Adobe Vivid (`EA1DE074F188405965EF399C72C221D9`).

## II. Adobe Camera Raw Pipeline Architecture

Understanding the exact order of operations is essential — pushing sliders without knowing where they sit in the pipeline causes cascading conflicts.

### The Pipeline Order (RAW → Final Image)

```
1. RAW black/white point subtraction
2. White Balance (RGB multipliers on linear raw data)
3. Demosaicing (Bayer/X-Trans → full-color RGB)
4. Input Color Profile (DCP: sensor RGB → working color space)
5. Exposure compensation (linear gain in gamma 1.0 space)
6. Highlight reconstruction / Shadow-White-Black sliders
7. Tone Curves (parametric + point, Film-Like blending)
8. HSL / Color Grading
9. Detail (Sharpening, Noise Reduction)
10. Effects (Grain, Vignette, Dehaze)
11. Output color space conversion
```

**Critical consequences of this order:**
- **Tone curves operate BEFORE HSL.** An aggressive S-curve increases saturation (via Film-Like blending), and then HSL adjustments operate on already-saturated data. This is the primary mechanism behind the "double-boost: curve + saturation" bug.
- **Grain is the LAST effect.** It sits on top of sharpening artifacts. Any sharpening applied to an image with grain amplifies each grain particle as a false "edge," creating jagged digital noise. The rule: Sharpness ≤ 10 when GrainAmount > 0.
- **Temperature/Tint are applied at step 2**, before demosaicing. WB shifts cascade through every subsequent pipeline stage, changing what HSL targets hit. Avoid WB in presets unless it's a defining film characteristic.

### Process Version 6 (PV6 / v15.4)

PV6 (June 2023) **reduces banding when using Color Mixer and B&W Mixer adjustments.** This is mandatory for film emulation presets that do heavy HSL work. Always set `crs:ProcessVersion="15.4"`.

### The Linear Gamma 1.0 Workspace

Digital sensors capture light linearly. The human eye perceives logarithmically. This mismatch creates specific effects:
- **Exposure operates in linear space** — +1 EV literally multiplies pixel values by 2.0
- **Saturation shifts are nonlinearly affected by exposure.** Brightening in linear space compresses highlight headroom; channels clip at different rates, causing saturation loss in highlights
- **Underexpose + curve-boost = different saturation than correct exposure.** This is why pushing Exposure +0.50 AND Contrast +30 creates different color rendering than Contrast +30 alone

## III. Color Science & Human Perception

### The Three Perceptual Effects That Shape Every Slider

These effects are hardwired into human vision. You can't disable them — you must work with them.

**Hunt Effect**: Colorfulness increases with luminance. Raising Exposure boosts perceived saturation even without touching the Saturation slider. Practical rule: when brightening an image, reduce Saturation proportionally to prevent a "nuclear" look.

**Stevens Effect**: Contrast increases with luminance. Brighter viewing conditions make images appear contrastier. A preset that looks perfectly graded in a dark editing room will appear flat and washed out in a bright room. Mitigation: design at 120 cd/m² brightness, test at 80 and 160 cd/m².

**Helmholtz-Kohlrausch Effect**: Saturated colors appear brighter than desaturated ones at identical luminance. Boosting Saturation perceptually brightens the image. This is why hyper-saturated presets look "overexposed" even when the Exposure value is neutral.

### Simultaneous Contrast (Chevreul's Law)

When one hue is boosted, adjacent hues in the image appear to shift toward its complement. Boosting orange makes blues appear bluer. Boosting green makes skin appear redder. This is why:
- A warm split-tone looks more dramatic on images with natural blue content (sky, water)
- A preset that looks perfect on a portrait (warm subject, cool background) breaks on a forest scene (green everywhere — no warm anchor to balance the split)
- **Always test presets on at least 3 image types**: skin tones, landscapes, and mixed-color scenes

### Bezold-Brücke Hue Shift

Hue changes with luminance at constant chromaticity. Pushing a tone curve on a blue sky shifts its perceived hue. The Film-Like curve mode partially compensates for this — another reason to always use Film-Like mode explicitly.

### OkLab: The Perceptually Uniform Ideal

OkLab (Ottosson, 2020) is the best-to-date perceptual color space. Key properties:
- Orthogonal L, C, h axes — one can be altered without affecting the other two
- Lightness RMSE 0.20, Chroma RMSE 0.81 — dramatically better than CIELAB (1.70, 1.84)
- LR's sliders approximate OkLab's ideals but imperfectly: Hue sliders feel more predictable than Saturation sliders (exactly what OkLab predicts)

### Color Difference (Delta E) — Evaluating Preset Accuracy

| ΔE Value | Meaning |
|----------|---------|
| < 1.0 | Imperceptible |
| 1.0–2.0 | Perceptible through close observation |
| 2.0–5.0 | Perceptible at a glance ("feels similar") |
| 5.0–10.0 | Clearly different |
| 11.0+ | More similar than opposite |
| 50–100 | Exact opposites |

For preset accuracy testing: use CIEDE2000, not simple Euclidean distance. The blue hue region (~275°) has the poorest perceptual uniformity — small HSL shifts in blues produce larger perceived changes than in other hues.

## IV. Tone Mapping & The Curve Engine

### The "Film-Like" Curve Mode

This is Adobe's DNG-standard curve mode. Here's what it actually does:
- The same curve is applied to each RGB channel independently
- **But** the RGB-HSV hue is preserved (no color shifts unlike Standard mode)
- **An S-curve increases saturation as a side effect** — roughly 5–10 saturation points for a contrast +30 curve

**Critical rule**: When you apply an S-curve AND add Saturation=+20, you're double-boosting saturation. The curve already did it. This is why the original working presets had very mild saturation values — the curve was carrying the saturation load.

### Tone Mapping Operator Theory Applied to LR

**Reinhard photographic TMO**: `Vout = Vin / (Vin + 1)`. Compresses highlights while preserving midtone contrast. LR's Highlights/Shadows sliders use similar rolloff logic. The more you pull Highlights negative, the closer you approximate Reinhard's highlight compression.

**Durand bilateral filter TMO**: Separates image into base layer (large-scale luminance, compressed) and detail layer (texture, preserved). This is the conceptual foundation of Clarity — but the Durand insight is that **human vision is more sensitive to local contrast than global contrast.** You can crush global contrast while preserving local detail, and the brain still reads the image as "contrasty."

**ACES 2 S-curve**: Scene-linear → perceptually uniform → tonescale (S-curve with toe and shoulder) → chroma compression → gamut compression. The key principle: **both toe and shoulder should be smooth rolloffs, not hard clips.** In LR terms: use Highlights (negative) for shoulder, Shadows (positive) for toe, and Whites/Blacks to set the hard clipping boundaries.

### Parametric vs. Point Curves

- **Parametric curves**: Slider-driven, intelligent edge blending between tonal ranges. Safer, more predictable.
- **Point curves**: Direct (input, output) mapping. More precise but more dangerous — a misplaced point creates weird crossovers.
- **All 4 curves** (RGB, Red, Green, Blue) must be set to neutral `0,0 → 255,255` unless you specifically need per-channel curve work (which is rare in presets).

### Per-Category Curve Recipes

| Category | Curve Type | Points | Use Case |
|----------|-----------|--------|----------|
| Color-Negative | Neutral | 0,0 / 255,255 | Let Basic panel drive contrast |
| Slide | S-curve | 0,0 / 42,28 / 128,128 / 213,230 / 255,255 | Deep blacks, clean highlights |
| Creative | Cinematic | 0,20 / 64,55 / 128,128 / 192,196 / 255,235 | Lifted matte with anchor |
| B&W | Neutral | 0,0 / 255,255 | GrayMixer + Basic handle tonality |

## V. Local Contrast Trio: Clarity, Texture, Dehaze

All three derive from the same algorithm: `enhanced = original + (original − blurred) × amount`. The only difference is the blur radius.

| Control | Effective Radius | Frequency Band | What It Affects |
|---------|-----------------|----------------|-----------------|
| Sharpening | 0.5–3 px | High | Edge acuity |
| Texture | 5–15 px | Medium | Fine-to-medium detail (fabric, foliage, pores) |
| Clarity | 30–100+ px | Low | Mid-tone contrast, "pop" |
| Dehaze | Multi-scale | Multiple | Atmospheric transmission + saturation + black point |

### The Destructive Interaction Problem

When Clarity, Texture, and Dehaze are all pushed high simultaneously, every spatial frequency band gets amplified. The human Contrast Sensitivity Function peaks at 2–5 cycles/degree (medium frequencies — Texture's territory). When no frequency is left un-boosted, the image reads as "over-processed." This is the "r/shittyHDR" failure mode.

**The coordination rule**: Pick ONE frequency band as primary, suppress the others. A film look enhances low frequencies via the Tone Curve (NOT Clarity — the Tone Curve is gentler). A modern look enhances high frequencies via Sharpening + Texture. Never boost all three simultaneously.

### Safety Caps

| Tool | Natural Range | Max Safe | Notes |
|------|--------------|----------|-------|
| Clarity | -10 to +10 | ±30 | Negative = bloom, positive = crunch |
| Texture | -5 to +15 | ±40 | Most visible slider — small changes are immediately apparent |
| Dehaze | -10 to +15 | ±30 | Negative = atmospheric haze addition (PV5+) |
| Grain presets | Clarity=0, Texture=0, Dehaze=0 | — | Must not interact with grain texture |

## VI. Color Grading Architecture

### Primary vs. Secondary Hierarchy

```
Primary (whole image, all channels):
  Basic Panel → Tone Curve
  ↓
Primary-Secondary Bridge:
  Color Grading wheels (Lift/Gamma/Gain hue offsets)
  ↓
Secondary (specific hue/sat/lum ranges):
  HSL Panel → Calibration (avoid in presets)
```

**The cardinal rule**: Keep the hierarchy clean. Don't fight tone curve choices with HSL, and don't fight HSL with calibration. Primary sets the foundation; secondary refines; calibration should almost never be used in presets (it redefines what "red" means at the profile level, cascading through all downstream adjustments).

### ColorGrade Blending

Lightroom defaults `crs:ColorGradeBlending` to 50. At 50, highlight and shadow color injections overlap in the midtones, creating muddy brown transitions in the blend zone.

- **Blending 50–55**: Natural, subtle (Color-Negative, B&W)
- **Blending 75–80**: Clean color separation, stylized (Creative, Slide)
- **Blending < 40**: Harsh, stylized transitions (special effects only)

### ColorGrade Wheel Formulas ("The Split-Toning Upgrade")

The three-way ColorGrade wheel system replaces legacy SplitToning. All Lum defaults to 0.

**Cinematic Teal/Orange (Hollywood Look):**
```
Shadows:  Hue 210°, Sat 15–20
Midtones: Hue 35°,  Sat 5–10
Highlights: Hue 40°, Sat 10–15
Blending: 70
```

**Vintage Fade:**
```
Shadows:  Hue 30° (brown),  Sat 10–15
Midtones: Hue 50° (yellow), Sat 5–10
Highlights: Hue 45° (gold),  Sat 5–10
Blending: 80
```

**Moody Blue Hour:**
```
Shadows:  Hue 220°, Sat 20–25
Midtones: Hue 210°, Sat 8–12
Highlights: Hue 230°, Sat 10–15
Blending: 55
```

**Cross-Processed (E6→C41):**
```
Shadows:  Hue 160° (green-cyan),   Sat 20–30
Midtones: Hue 70° (yellow-green), Sat 15–20
Highlights: Hue 320° (magenta),    Sat 15–25
Blending: 40 (sharper transitions for the xpro contrast look)
```

### The Opponent Process Connection

Human vision processes color through opponent channels: Red-Green, Blue-Yellow. Color grading that aligns with opponent channels creates natural perceptual contrast. Orange/Teal works because it directly engages both opponent systems simultaneously. Near-complements work better than exact complements — a 210° teal shadow + 35° orange highlight (175° apart, not exactly 180°) looks richer than exact opposites.

### The Film Saturation-Luminance Curve

Real film's saturation varies with luminance in a specific pattern:
- 0–10% luminance: Very low saturation (near black)
- 10–25% luminance: Rising but subdued
- **25–65% luminance: Peak saturation zone** ← color "lives" here in film
- 65–90% luminance: Declining saturation
- 90–100% luminance: Very low saturation (near white)

This is fundamentally different from digital, where saturation is uniform across the tonal range. **HSL Luminance sliders are the tool for simulating this** — pulling luminance up in the 25–65% zone and down near black/white.

### Seven Color Grading Pitfalls

1. **Over-saturation**: Sat >30 on any wheel looks artificial in stills (video can go higher because motion masks the fake)
2. **HSL + Color Grading conflict**: Desaturating blues in HSL then adding blue shadows via wheels = fighting yourself
3. **Midtone wheel contamination**: The midtone wheel affects skin tones most directly — never push it beyond Sat 10 on portrait presets
4. **8-bit banding**: Heavy Color Grading on 8-bit images creates visible bands. Target 16-bit-capable workflows.
5. **Maximum complementary = garish**: 180° apart looks like a video game filter. 160–175° looks cinematic.
6. **Luminance mismatch**: Don't brighten shadows (positive Shadows) AND darken shadows (negative Lum on shadow wheel) simultaneously
7. **Blend zone mixing**: At Blending 50, transition areas mix hues unpredictably. Higher Blending creates cleaner separation.

## VII. Grain: The Physics of Chemical Texture

### How Adobe's Grain Engine Works

Grain is a **generative synthetic texture**, not a noise overlay:
1. Seed-based pseudo-random luminance-only pattern is generated
2. Size controls kernel diameter — values ≥25 cause measurable image blurring
3. Roughness controls uniformity: 0 = uniform (digital-looking), 100 = maximally irregular (pushed-film look)
4. Amount is the blend opacity

**Pipeline placement**: Grain is the **last effect** applied, after sharpening and noise reduction. This is the single most important grain fact: sharpening sees grain as "detail" and amplifies it into jagged digital noise.

### Real Film Grain vs. Digital Simulation

| Property | Real Film | Lightroom Grain |
|---|---|---|
| Grain structure | Image IS grain | 2D noise overlay |
| Rotation | 3D varied angles | None |
| Cluster formation | Natural clumping | No clustering |
| Highlight grain | Dmax — maximum silver | Uniform across tones |
| Shadow grain | Dmin — media grain visible | Can create muddy shadows |
| Color | Dye clouds (post-development) | Luminance-only by design |

### The "Melted Base" Technique

To make grain appear authentically chemical rather than digital:
1. Set `crs:Sharpness="10"` (suppress digital sharpening)
2. Set `crs:LuminanceSmoothing="0"` (don't confuse this with the STYLEGUIDE's optional variant of 25 for specific looks)
3. Set `crs:Clarity2012="0"`, `crs:Texture="0"`, `crs:Dehaze="0"`
4. Let the grain particle size (Size) carry the texture character — larger grain reads as pushed film, smaller as fine-grain stock

### Grain by Film Type

| Film Type | Amount | Size | Roughness | Character |
|-----------|--------|------|-----------|-----------|
| Fine-grain color neg (Portra 160) | 15–25 | 20–25 | 30–45 | Virtually invisible at normal sizes |
| Standard color neg (Portra 400) | 25–35 | 25–30 | 40–50 | Visible at 100%, organic |
| High-speed color neg (Portra 800) | 35–45 | 35–40 | 45–55 | Prominent but structured |
| Consumer color neg (Gold/Ultramax) | 35–50 | 30–35 | 55–65 | Noticeable, "analog character" |
| Slide film (Ektachrome, Velvia) | 0–15 | 15–25 | 30–40 | Almost invisible — slide film has extremely fine grain |
| Classic B&W (Tri-X) | 50–65 | 35–45 | 65–75 | Signature "salt and pepper" structure |
| Pushed B&W (Delta 3200) | 65–85 | 50–65 | 70–85 | Heavy "golf ball" grain |
| Specialty (Cinestill, xpro) | 35–50 | 30–40 | 50–65 | Pronounced, adds to the lo-fi aesthetic |

### Negative vs. Positive Grain Characteristics

- **Color negative**: Grain is more pronounced in highlights (silver halide clumps form most densely where the most light hit, then dye clouds are densest after development)
- **Slide/Positive**: Grain is softer, less prominent in highlights (reversal process inherently reduces grain visibility in bright areas)

Practical rule: for negative film emulations, don't globally boost grain — concentrate roughness in highlight regions. For slide film emulations, use minimal grain or omit it entirely.

## VIII. The Physics of Film Emulation (Traps & Pitfalls)

### 1. The Clarity and Texture Trap ("The HDR Nightmare")

Pushing `crs:Clarity2012` or `crs:Texture` into high positive numbers (> +10) creates a crunchy, aggressive, over-processed look. Vintage glass and CCD sensors possess a specific, organic micro-contrast. Digital clarity forces a look that kills this filmic illusion.

- **The Rule**: True film emulations rely on the Tone Curve for contrast. Keep Clarity near 0, or push it slightly negative (-5 to -15) for an authentic, soft bloom. Let the curve do the tonal work.
- **Frequency-band discipline**: The human Contrast Sensitivity Function peaks at 2–5 cycles/degree (Texture's territory). You can push Texture harder than Clarity without triggering the "over-processed" alarm, but only in moderation. Pick one frequency band as primary.

### 2. The Grain vs. Sharpening Clash

If `crs:GrainAmount` is active, digital sharpening must be aggressively suppressed. Sharpening (small-radius USM, 0.5–3px) creates artificial Mach bands — overshoot/undershoot at edges. When applied on top of simulated grain (random luminance perturbations), sharpening treats each grain particle as an "edge" and amplifies it into jagged digital noise with ringing artifacts.

- **The Rule**: If GrainAmount > 0, explicitly set `crs:Sharpness="10"` or lower. Keep `crs:Clarity2012="0"`, `crs:Texture="0"`, `crs:Dehaze="0"`.
- **The "Melted Base" Trick** (optional, for specific looks): Apply `crs:LuminanceSmoothing="25"` to subtly smooth the digital pixel structure. This creates a smooth, waxy base that allows grain to sit organically on top. Not always needed — test per preset.

### 3. The "Double-Fade" Shadow Wash

When building a cinematic matte look, raising the Tone Curve's black point (e.g., `0, 20`) creates a faded shadow.

- **The Trap**: If you apply a lifted curve but leave the `crs:Blacks2012` slider at a positive value, you "double-fade" the image, turning shadows into a muddy, flat gray wash.
- **The Rule**: If utilizing a lifted cinematic curve, anchor `crs:Blacks2012` to 0 or slightly negative. This preserves the fade while keeping a photographic anchor point.

### 4. The S-curve + Saturation Double-Boost

The Film-Like curve mode increases saturation as a side effect of contrast (by separating RGB channels while preserving hue). An S-curve with contrast +30 effectively adds ~5–10 saturation points. If you ALSO add Saturation=+15, you get double-boosted saturation of +20–25.

- **The Rule**: Let the curve carry the saturation. Use mild global Saturation (±5) and target specific color channels via HSL saturation for fine-tuning.

### 5. The Vibrance-Saturation Gap

Vibrance is a midtone-biased saturation boost with skin tone protection. When `Vibrance - Saturation > 10`, Lightroom desaturates globally (via Saturation) then selectively boosts midtones (via Vibrance), creating a "selective color" effect — near-monochrome with one popping hue.

- **The Rule**: Keep `|Vibrance − Saturation| ≤ 5`, or remove Vibrance entirely. This is a hard rule — violating it is the #1 cause of presets that create unnatural selective-color effects.

### 6. WB + HSL Cascade Failures

White Balance adjusts RGB multipliers on the raw data BEFORE demosaicing (step 2 in the pipeline). All downstream HSL shifts then operate on different color values than intended. A +5 Hue shift on orange means something completely different before and after a WB adjustment.

- **The Rule**: Avoid Temperature/Tint in presets unless warm/cool balance is a defining characteristic of the film stock or look. Document why the WB shift exists when you do include it.

### 7. Calibration Cascade (The Nuclear Option)

Calibration (RedHue/Sat, GreenHue/Sat, BlueHue/Sat, ShadowTint) redefines what "red," "green," and "blue" are at the profile level. Every subsequent slider — HSL, Color Grading, even the Tone Curve — operates on the reinterpreted primaries.

- **The Rule**: NEVER use Calibration in presets. Exception: the Canon Color Science preset, where calibration shifts ARE the defining characteristic (emulating Canon's in-camera color science).
- **Why the original presets had zero calibration values**: Each working preset was a clean single-pass look. Adding calibration creates an unpredictable feedback loop with every other slider.

### 8. HSL Saturation Caps

Beyond ±60, entire color channels are destroyed — not "desaturated," but mathematically collapsed. Combined with demosaicing artifacts (particularly on X-Trans sensors), extreme HSL values amplify invisible aliasing into catastrophic color noise.

- **The Rule**: Cap all HSL saturation adjustments at ±60. No exceptions.

### 9. The Display-Referenced Trap

XMP presets operate in display-referred space, not scene-referred. By the time your slider values execute, the RAW has been through linearization, demosaicing, WB, color space transform, and tone mapping. The preset can't recover data that was already discarded in the scene→display conversion.

- **The Rule**: Presets cannot recover blown highlights or crushed blacks that were already clipped in the pipeline. Design slider values conservatively to avoid pushing data toward clipping boundaries.
- **The 95th Percentile Display**: Design for D65, gamma 2.2, 120 cd/m², sRGB gamut. Extreme slider values that only work on HDR or wide-gamut displays will fail for the majority of users.

## IX. Film Emulation Theory

### ACES & Scene-Referred Color

The ACES pipeline normalizes all camera inputs into a common scene-referred color space (AP0/AP1), applies look transforms, then converts to display output. LR approximates this with:
```
Camera Profile (Input Transform) → Internal RGB → [Adjustments] → Output Space
```

**Key ACES principle**: The rendering transform (the final view) defines the "look." Changing the Tone Curve and Camera Profile changes rendering dramatically — much more than individual HSL adjustments.

### LMTs (Look Modification Transforms)

LMTs are small, single-purpose transforms chained together. The lesson for preset design: **8–15 well-chosen attributes produce better results than 55–68 attributes fighting each other.** Multiple small, targeted adjustments compose better than one monolithic change.

### Subtractive Saturation (The Film Print Look)

Film's saturation decreases as luminance increases — a subtractive color model behavior. In additive digital RGB, saturation is uniform across luminance. To simulate film-like subtractive saturation in Lightroom:
1. Use a gentle S-curve (which compresses highlight values, reducing saturation in bright areas via the Film-Like mode)
2. Pull Saturation slightly negative (-5 to -10)
3. Boost specific midtone colors via HSL Saturation (which operates on the perceptual midtone range)
4. Optionally reduce HSL Luminance on bright colors to add "density"

### The Profile IS The Foundation

A DCP profile contains three components that define the entire baseline rendering:
1. **Color matrices** (3x3: sensor RGB → CIE XYZ) — the fundamental color translation
2. **HSV LUTs** — per-hue saturation and hue corrections (this is where "film stocks" live in profile-based workflows)
3. **Tone curve** — base contrast rendering baked in before sliders activate

Slider presets operate on top of this foundation. Without the `crs:Look` block specifying which profile to use, Lightroom skips the non-linear input color matrix entirely — producing flat, desaturated, washed-out images regardless of slider values.

### Why Camera Profiles Beat Slider Presets

DCP profiles can do things slider presets fundamentally cannot:
- **Cross-channel transforms**: Film's color response involves inter-channel interactions (e.g., red exposure affecting blue density in the negative). 3D LUTs (embedded in DCP profiles) capture these non-separable relationships.
- **Hue trajectory**: As luminance changes, real film shifts hue along specific trajectories. Sliders are static; 3D LUTs can encode the full trajectory.
- **Gamut boundary behavior**: Film handles out-of-gamut colors by gentle compression. Sliders clip them.

**The art of slider-based film emulation is knowing which approximations work.** Some film behaviors (e.g., Portra's specific subtractive saturation curve) can be convincingly approximated with sliders. Others (e.g., the full Kodachrome K-14 dye response) fundamentally require 3D LUTs.

## X. Archetypal Look Recipes

### Archetype A: The "Teal and Orange" Cinematic Look

```
Basic Panel:
  Exposure: -0.10 (slight underexposure for richness)
  Contrast: +20 to +30
  Highlights: -40 to -50 (smooth shoulder rolloff)
  Shadows: +20 to +30 (lift for visibility)
  Whites: -10 to -15
  Blacks: -10 to -15 (anchor, not crushed)

Color Grading (Blending 75):
  Shadows:  Hue 210°, Sat 15–20
  Midtones: Hue 35°,  Sat 5–10
  Highlights: Hue 40°, Sat 10–15

HSL:
  Green Hue: -60 to -70 (push green → yellow/olive)
  Green Sat: -40 to -50 (desaturate foliage)
  Blue Sat: -15 to -25 (muted cool tones)
  Orange Lum: +10 to +15 (creamy skin)

Tone Curve: Cinematic (0,20 / 64,55 / 128,128 / 192,196 / 255,235)
```

### Archetype B: Moody Pastoral (PNW Forest)

```
Basic Panel:
  Exposure: -0.30 to -0.50 (dark and moody)
  Contrast: +30 to +40
  Highlights: -60 to -75
  Shadows: +50 to +75 (extreme shadow lift)
  Whites: +10 to +20
  Blacks: -10 to -20

Color Grading (Blending 75):
  Shadows:  Hue 250–260° (cool blue), Sat 8–12
  Midtones: neutral (no midtone injection)
  Highlights: Hue 150–160° (green-teal), Sat 8–12

HSL:
  Green Hue: +40 to +55 (green → yellow-brown, the defining move)
  Green Sat: -50 to -60 (crush green — natural grass is the enemy)
  Orange Lum: +60 to +80 (earth tones glow through the gloom)
  Yellow Sat: -25 to -35

Clarity: 0 (let the Tone Curve carry contrast structure)
Grain: Amount 25–35, Size 30–35, Roughness 50–60
```

### Archetype C: High-Key Coastal Pastel (Light & Airy)

```
Basic Panel:
  Exposure: +0.75 to +1.05 (flood the sensor)
  Contrast: -30 to -40 (compress tonal range)
  Highlights: -55 to -70 (protect highlight detail)
  Shadows: +35 to +50 (everything visible)
  Whites: +15 to +25
  Blacks: +15 to +25 (lifted matte black point)

Color Grading (Blending 75):
  Shadows:  Hue 200–210° (cool teal), Sat 4–8 (very subtle)
  Highlights: Hue 40–50° (warm), Sat 4–8 (very subtle)

HSL:
  Green Hue: +15 to +25 (green → aqua-mint)
  Green Sat: -30 to -40
  Aqua Lum: +30 to +40 (airy sky glow)
  Orange Lum: +10 to +15 (bright skin)

Clarity: -10 to -15 (soft, dreamy bloom)
Texture: -5 to -10
Dehaze: -10 to -15 (atmospheric softness)
```

### Archetype D: The "Portra 400" Film Emulation

```
Basic Panel:
  Exposure: +0.25 to +0.50 (slight overexposure sweet spot)
  Contrast: -7 to -12 (soft, organic contrast)
  Highlights: -45 to -55 (Portra's legendary highlight latitude)
  Shadows: +20 to +30 (lifted shadow detail)
  Whites: -5 to +5
  Blacks: +10 to +15 (never crushed — Portra's black is gentle)

HSL:
  Green Hue: +10 to +15 (green → olive)
  Green Sat: -15 to -25 (Portra's signature green desaturation)
  Orange Lum: +10 to +15 (creamy skin — the Portra hallmark)
  Blue Sat: -5 to -15 (muted sky)
  Red Sat: +5 to +10 (warmth without aggression)

Color Grading (Blending 50):
  Shadows:  Hue 45–55° (warm brown, not teal), Sat 5–10
  Highlights: Hue 40–45° (golden), Sat 5–8

Grain: Amount 25–30, Size 25–30, Roughness 40–50
Sharpness: 10 (grain protection)
Clarity: 0
Texture: 0
Dehaze: 0
```

## XI. YouTube & Pro Creator Techniques

### A. B&W Editing — Mixer, Contrast, Grain

**The B&W Mixer** (triggered by one click or `V` key) converts each color channel into a luminance contribution. The real art is in the B&W Mix tab. Generic B&W conversion is flat — every image needs shot-specific tonal separation.

| Color | Direction | Effect on Grayscale |
|-------|-----------|---------------------|
| Red | +10 to +20 | Lighten skin / lips |
| Orange | +5 to +15 | Lighten skin tones (key portrait control) |
| Yellow | +10 to +20 | Brighten grass, warm highlights |
| Green | 0 to -20 | Darken foliage for depth |
| Aqua | -5 to -15 | Darken coastal blues |
| Blue | -10 to -20 | Dramatic dark skies |
| Purple | 0 to -10 | Subtle background darkening |
| Magenta | -5 to -15 | Tame artificial light sources |

**Contrast layering for B&W** (from Jeff Ascough/Anthony Morganti philosophy):
- Clarity builds structural "shape" at the midtone level — use locally with brushes, not globally
- Texture affects fine edge detail (skin precision) — smaller radius than Clarity
- Dehaze darkens near-light areas — easily overpowers in B&W; cap at 5–15 max
- Stack small amounts of each for richer results than one slider maxed
- Sean Tucker: "Shadows that go to black should do so deliberately, not accidentally"

**B&W Grain by film stock:**
| Film Stock | Amount | Size | Roughness |
|------------|--------|------|-----------|
| Tri-X 400 | 40–55 | 25–35 | 50–65 |
| HP5+ | 30–45 | 20–30 | 50–60 |
| Delta 3200 | 50–70 | 40–55 | 60–80 |
| T-Max 3200 | 55–75 | 40–60 | 65–85 |
| Acros | 15–25 | 15–25 | 45–55 |

### B. Portrait Editing Techniques

**Skin softening without Photoshop:** Negative Clarity (-15 to -40) via Brush or Radial Gradient over skin areas. Must pair with small Sharpness boost (+10 to +15) to retain realistic texture — negative Clarity alone creates plastic skin. Never apply globally. Julia Trotti and Anita Sadowska both use this as their primary Lightroom skin retouching method.

**Skin tone protection (HSL priorities):**
- Orange Lum +5 to +15: Brightens skin naturally (the most important skin slider)
- Orange Sat -5 to -15: Calms ruddy/overly red skin
- Red Sat -5 to -10: Reduces blemish prominence
- Jessica Kobeissi's signature: Orange Lum +10, Orange Sat -10, Yellow Sat -5

**Eye pop** (Peter McKinnon technique): Radial Gradient over each eye, Exposure +0.3, Clarity +25, Dehaze +10. For catchlights: tiny Brush on the sparkle, Exposure +1.0, Whites +30.

### C. Landscape & Sky Editing

**Sky darkening (three methods):**
1. AI Select Sky mask → Exposure -0.5 to -1.0, Contrast +15 to +25, Dehaze +15 to +30
2. Linear Gradient from top → Exposure -0.5 to -1.0, Contrast +15, Dehaze +15
3. Multiple gradients: one for sky darkening, second flipped (press `'`) for foreground Clarity +20

**Golden hour formula** (Peter McKinnon + community consensus):
- Temp +10 (if WB not committed to preset), Tint +5 toward magenta
- Orange Sat +15 to +20, Yellow Sat +10 to +15
- Orange Lum +10 to +20, Yellow Hue -10 to -15 toward orange
- Color Grading: warm highlights + shadows (H 40–50 sat 10–20 + H 30–40 sat 5–10)
- Linear Gradient with warm gold overlay at sun direction, Dehaze -10 for atmospheric glow

**Foliage naturalization:** Green Sat -10 to -20 (digital greens are too neon). Green Hue +20 to +40 for summer lush, or -10 to -20 for forest moody. Yellow adjustments massively affect foliage — Yellow Hue -10 to -20 shifts leaves toward autumn orange.

**Aurora/night sky:** Dehaze +5 to +15 only (higher cranks contrast and saturation aggressively). Clarity +10 to +25 for banding definition. Saturation -5 to -10 first, compensate with Vibrance +10 to +20. Use Linear Gradient with Magenta Tint +10 to +20 on foreground snow to neutralize green aurora reflection.

### D. Niche Creative Look Recipes

**Cyberpunk / Blade Runner:**
```
Exposure: -0.50  |  Contrast: +45  |  Highlights: -65
Shadows: +40  |  Whites: +30  |  Blacks: -40
Clarity: +55  |  Dehaze: +45  |  Saturation: -15
HSL: Green H-90/S-90, Yellow S-80, Magenta S+55
Color Grading (Blending 70): Shd H230/S22, Hi H315/S22
Grain: Amount 45, Size 40, Roughness 65
```

**1980s VHS / Synthwave:**
```
Contrast: +32  |  Highlights: -90  |  Shadows: +50
Blacks: -40  |  Clarity: -23  |  Dehaze: -15
Color Grading (Blending 50): Shd H200/S22, Hi H310/S32, Bal +30
HSL: Red H+20/S+20, Green H-45/S-60, Aqua S+28, Magenta S+33
Grain: Amount 45, Size 42, Roughness 70
```
Negative Clarity and Dehaze are the defining moves — they create the analog bloom and VHS fog. Negative Texture (-25 to -40) adds channel misalignment degradation.

**Wong Kar-Wai / Doyle Green:**
```
Exposure: -0.40  |  Contrast: +25  |  Highlights: -50
Shadows: +20  |  Blacks: -40  |  Clarity: -10
HSL: Green H-50/S+32/L-20, Orange S-12, Magenta S+32
Color Grading (Blending 50): Shd H170/S20, Hi H190/S12, Bal -15
```
The green shadow shift (H170) is the defining move. Orange Sat -12 protects skin from green cast contamination. Three variants exist: Chungking Express (mid contrast), Fallen Angels (extreme +35-50 contrast), In the Mood for Love (warm amber shadows, gentler).

**Bleach Bypass (Saving Private Ryan / Seven):**
```
Exposure: -0.50  |  Contrast: +70  |  Highlights: -65
Shadows: -40  |  Whites: +15  |  Blacks: -50
Clarity: +45  |  Dehaze: +20
HSL: Red -30, Orange -25, Yellow -35, Green -40, Aqua -45, Blue -20, Purple -35, Magenta -40
Color Grading (Blending 50): Shd H225/S10, Hi H45/S7
Grain: Amount 41-45, Size 40
```
Real bleach bypass reduces saturation MORE in highlights than shadows — channel-specific desaturation matters more than global Saturation. Clarity abuse is the #1 mistake — contrast first, clarity second.

**Wes Anderson Pastel:**
```
Exposure: +0.25  |  Contrast: -30  |  Highlights: -60
Shadows: +45  |  Whites: +15  |  Blacks: +28
Clarity: -25  |  Dehaze: -15  |  Saturation: -12
HSL: Orange H-10/S-15/L+10, Green H+15/S-20, Blue S-20, Magenta H+10/S+5
Color Grading (Blending 70): Shd H200/S12, Hi H45/S8
```
The lifted black point in the tone curve is 70% of the look. Shoot slightly overexposed (+0.3 to +1.0 EV). "If your image doesn't work at -30 clarity, it's not the right image."

### E. Pro Workflow & Preset Creation Rules

**What makes a preset sellable** (from top YouTube creators):
1. Must look dramatically different from unedited RAW at one click
2. Must work across fair, medium, and dark skin tones — skin tone failure is the #1 complaint in reviews
3. Test on golden hour, overcast, indoor tungsten, and flash
4. Include multiple strength variants ("Preset +" and "Preset -")
5. Exclude crop, exposure, WB, spot removal, and local adjustments when saving
6. Professional naming — descriptive not gimmicky. "Warm Golden Hour" sells better than "Sunshine Explosion"
7. Include DNG/mobile versions — this doubled sales for many creators

**The "Influencer Preset" Formula** (the dominant Instagram look):
1. Adobe Color or Adobe Portrait profile
2. Medium-contrast S-curve
3. Warm split tone: Highlights warm (~H40), Shadows teal (~H220)
4. HSL: desaturate greens (-10 to -30), push greens toward yellow (+20 to +40), boost orange luminance (+10)
5. Slight vignette (-10 to -15)
6. Dial preset Amount to 70–85% — 100% often overwhelms

**Keyboard shortcuts every pro uses:**
| Key | Function |
|-----|----------|
| R | Crop tool |
| Q | Spot healing |
| K | Adjustment brush |
| M / Shift+M | Linear / Radial Gradient |
| `\` | Toggle before/after |
| `'` | Invert gradient direction |
| Cmd/Ctrl+Shift+C/V | Copy/Paste settings |
| Cmd/Ctrl+' | Create Virtual Copy |

### F. Pro Secrets & Hidden Features

**Profile selection is the foundation** — never leave it at Adobe Standard:

| Profile | Best For |
|---------|----------|
| Adobe Standard | Neutral base for cinematic grades |
| Adobe Neutral | Flattest base for building looks from scratch |
| Adobe Portrait | Softer skin tone rendering |
| Adobe Landscape | Punchy outdoors (poor base for moody looks) |
| Adobe Vivid | Never use as grading base (too saturated) |
| Camera-specific profiles | Revive colors Adobe Standard loses — always try these first |

**Dehaze's hidden talents:** Negative Dehaze (-10 to -25) adds atmospheric "fog" — essential for VHS, Wes Anderson pastels, and cinematic dream looks. Positive Dehaze at +30–60 on cyberpunk creates neon glow bloom. B&W Dehaze caps at 5–15 max (beyond = harsh and unnatural).

**RGB channel curves** (pro landscape colorist technique): Lift highlights in Red channel slightly left → warm cast in highlights without touching WB. Drop highlights in Blue channel → added yellow in highlights. "This is how pros warm a sky without touching white balance at all."

**The "Visual Helper" trick** (Vlad Moldovean): Create a preset that applies Saturation -100 at 200% over entire image. Toggle on/off to edit luminance without color perception bias. Yellow feels brighter than blue at the same luminance — this eliminates that illusion for precise exposure balancing.

**Clarity/Texture/Dehaze distinction:**
| Slider | Radius | What It Does |
|--------|--------|-------------|
| Texture | 5–15 px | Edge contrast at finest details — skin pores, fabric |
| Clarity | 30–100 px | Midtone contrast — builds structure, lightens near-dark edges |
| Dehaze | Multi-scale | Darkens near-light areas, cuts atmospheric haze |

For B&W portraits: Texture +10–15 is safer than global Sharpening. For landscapes: use Clarity + Texture stacked in small amounts rather than one maxed slider.

**Settings pros avoid:**
1. Calibration panel for film presets — global primary shifts cascade chaos (exception: Canon Color Science)
2. `|Vibrance − Saturation| > 5` — creates the "B&W with one color" selective-color bug
3. HSL saturation > |60| — nukes color channels into mathematical collapse
4. WB in film presets — shifts cascade through entire pipeline before HSL operates
5. Texture + Clarity + Dehaze simultaneously maxed — all frequency bands amplified = over-processed
6. Presets at 100% strength — Furoore: "Apply your preset, dial back to 70–85%"
7. Saturation slider for B&W conversion — produces flat, low-contrast B&W; always use B&W button + B&W Mix tab instead

## XIII. Preset Portability & Survivability

### Design for the 95th Percentile Display

Most users are NOT calibrated. A preset must survive on: D65 white point, gamma 2.2, 120 cd/m² brightness, sRGB gamut.

| Slider | Impact of Uncalibrated Display | Mitigation |
|--------|-------------------------------|------------|
| HSL Sat ±40+ | Looks radically different warm vs. cool monitors | Cap at ±40 for broad distribution |
| Blacks < -30 | Crushed black rectangle on dim/low-contrast screens | Floor at -30 |
| Temperature/Tint | Color casts amplify 2–3× under partial eye adaptation | Avoid unless defining |
| Shadow detail | First thing lost on bad monitors | Always test at 80 cd/m² |
| Grain Amount > 60 | Looks like compression artifacts on some panels | Stay below 60 for general-purpose |

### Gamut Survivability

Saturated reds and blues are the first colors clipped when moving from wide-gamut to sRGB. A preset with heavily boosted red/blue saturation (> +40) that looks "rich" on a P3 display will look clipped and flat on sRGB. For presets targeting broad distribution, keep saturation values conservative — let the ColorGrade wheels add richness, not HSL extremes.

### Print Survivability

Print gamuts are narrower than sRGB. If you want a preset to survive the print workflow:
1. Avoid saturating reds above +30 and blues above +25
2. Never push Blacks below -25 (print black points are significantly lighter than emissive displays)
3. Test against a FOGRA39 soft-proofing profile before finalizing

### The White Point Adaptation Problem

ICC v4 profiles assume full adaptation to display white point. But human white-point adaptation takes 10–15 minutes. A user who just opened their laptop sees your preset through *partial adaptation* — color casts appear 2–3× stronger than intended. This is the primary reason to avoid Temperature/Tint in presets. A "subtle warm cast" (+200K) on a calibrated monitor looks like a +500K error on a cold-start laptop.

## XIV. Competitive Strategy & Preset Viability

### The Open-Source Moat

No comprehensive open-source XMP preset collection currently exists on GitHub. This project's combination of 48 presets across 4 categories, fully documented with `research/` directories containing film datasheets, community recipes, and aesthetic characteristics — all published as open-source — is unique in the market.

### What AI Can't Do (Yet)

- **Film chemistry reconstruction**: AI has no access to the spectral sensitivity curves of Kodak Portra 400 or the dye coupler chemistry of Kodachrome K-14. This project's `research/` directory documents these reference data points.
- **Provenance**: AI editing tools are black boxes. Photographers who want to understand AND modify their look need documented presets, not opaque AI profiles.
- **Subtlety**: AI models gravitate toward population averages. The specific, restrained character of a Portra 400 preset (8–15 attributes in the originals) is the opposite of AI-style "correct everything" editing.

### The Profile-to-Preset Bridge

The market is shifting from slider presets to DCP-based profiles. The strongest preset packs combine both: a DCP profile for the foundation (accurate color rendering from the sensor), and an XMP preset for the creative look (HSL, Color Grading, Grain). This project's presets can evolve in this direction by referencing specific camera profiles in the `crs:Look` block.

### Mobile & Video Cross-Compatibility

Smartphone computational pipelines (Apple ProRAW, Google HDR+) produce fundamentally different starting points than dedicated cameras. Video LUT formats (CUBE, 3DL) are needed alongside XMP for cross-media workflows. A preset pack with matched photo XMP + video LUT versions has a competitive moat few offer.

## XV. The 10 Commandments of XMP Preset Design

All distilled rules in one place:

1. **ProcessVersion 15.4 always** — PV6 reduces banding in HSL adjustments
2. **Look block mandatory** — Missing = flat, washed-out rendering
3. **No Calibration** (except Canon Color Science) — Redefines primaries, cascading chaos
4. **No Temperature/Tint** unless defining — WB shifts cascade through entire pipeline
5. **Vibrance within 5 of Saturation** — Larger gap = selective-color bug
6. **HSL Sat capped at ±60** — Beyond = channel destruction + demosaic artifact amplification
7. **Grain > 0 → Sharpness ≤ 10, Clarity/Texture/Dehaze = 0** — Sharpening grain = jagged noise
8. **Tone Curve carries contrast; Clarity is seasoning** — Durand bilateral filter principle
9. **8–15 attributes > 55–68 attributes** — Small, single-purpose adjustments compose better
10. **Test on 3 image types minimum** — Chevreul's simultaneous contrast means a preset's behavior is image-dependent

## XVI. References (Whitepaper + YouTube Archive)

The `research/whitepapers/` directory contains 36 reference documents organized by domain:

- **Adobe Tech** (5): DNG spec, Camera Raw pipeline, profiles, grain/vignette, demosaicing, tone curves
- **Color Science** (5): CIECAM02, ICC color management, OkLab, Delta E, digital color spaces
- **Film Emulation** (5): ACES overview + LMTs + use cases, Dehancer grain, ARRI Textures + LogC
- **HDR/Tone Mapping** (4): Reinhard/Durand/Mantiuk operators, PQ/HLG, computational photography, local contrast
- **Industry Trends** (4): AI editing market 2025, photography trends, digital market impact, tools landscape
- **Display/Calibration** (4): Monitor calibration, color accuracy, print workflow, HDR wide gamut
- **RAW Pipelines** (4): Demosaicing (Bayer/X-Trans), noise reduction, color science, lens correction
- **Grading Theory** (4): Primary/secondary grading, color theory, ACES + LUTs, split-toning theory

### YouTube / Pro Creator Sources
Techniques in Section XI are synthesized from the following channels and their most-viewed tutorials:

| Creator | Subscribers | Known For |
|---------|------------|-----------|
| Peter McKinnon | 5.9M+ | Tone curves, cinematic color grading, preset creation |
| Mango Street | 1M+ | Cinematic looks, teal & orange, color grading wheels, Blade Runner |
| Jamie Windsor | 800K+ | Film emulation, B&W techniques, grain authenticity |
| Julia Trotti | 200K+ | Portrait editing, Portra-style presets, HSL mastery |
| Evan Ranft | 400K+ | Workflow optimization, virtual copies, batch editing |
| Jessica Kobeissi | 1M+ | Portrait editing, skin tone protection |
| Anita Sadowska | 500K+ | Skin retouching, negative Clarity technique |
| Sean Tucker | 500K+ | B&W philosophy, tonal intention, contrast discipline |
| Chris Hau | 500K+ | Cinematic color grading, teal/orange formulas |
| North Borders | 500K+ | Creative grading, dark/moody looks |
| 7th Era | 400K+ | Moody editing, night photography, PNW style |
| Pat Kay | 200K+ | Color theory, grading wheel mastery, HSL deep dives |
| Mark Denney | 400K+ | Landscape editing, basic panel workflow |
| Anthony Morganti | 200K+ | Slider education, Texture/Clarity/Dehaze distinctions |
| Jeff Ascough (via Fstoppers) | — | B&W printing philosophy, contrast layering |
| Vlad Moldovean | — | Luminosity-masked grain, visual helper technique |
| ExpertPhotography / Shotkit | — | Comprehensive tutorial articles, B&W mixer |
| Presets.io | — | Film emulation recipes, moody editing guides |
| dPS (Digital Photography School) | — | Landscape techniques, aurora editing, batch workflow |

Consult these before making slider decisions that interact with sensor physics, display calibration, or print output.
