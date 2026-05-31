# Community Recipes — Making Sony RAWs Look Like Canon

> Reddit communities (r/SonyAlpha, r/postprocessing, r/Lightroom) are full of attempts to emulate Canon color science on Sony files. This document catalogs the recurring strategies, calibration settings, and DIY approaches shared by the community.

---

## Strategy 1: Use Camera-Matching Profiles (Free, Built-In)

### The Sony "ST" Profile Discovery
The simplest and most overlooked approach: switch from Adobe Color to Sony's camera-matching profiles in Lightroom's Profile Browser.

- Navigate to: **Profile Browser → Camera Matching → Sony ST (Standard)**
- The ST profile renders skin tones with more red/magenta warmth — closer to Canon's signature than Adobe Color.
- Vectorscope analysis by u/Rndmized (r/SonyAlpha) confirmed ST shifts skin tones toward red/magenta which is visibly closer to Canon's rendering.
- u/Supsti_1 (A6700 shooter): *"When I switch from Adobe Color to Sony ST, the issue basically disappears. Skin tones look more natural and balanced, without that green cast."*

**Other Sony camera-matching profiles:**
- **PT** (Portrait): Softens contrast, warm skin bias — good starting point for Canon emulation
- **FL** (Film Look): Added warmth and character — newer bodies only (A7IV+)
- **SH** (Soft High-key): Bright, airy rendering — popular for wedding/lifestyle
- **NT** (Neutral): Flat starting point, good for building custom looks
- **IN** (Indoor): Warmer rendering for interior lighting

**Caveat:** Only available on newer Sony bodies. Older cameras (A7III, A7RIII) have the older "Camera Matching" names like "Camera Standard" instead.

---

## Strategy 2: Lightroom Calibration Panel Adjustments

### Known Calibration Slider Values
From u/Reptiles_SHH on r/SonyAlpha, who reverse-engineered A1II profiles for A7V bodies:

```
Red Primary:
  Hue: -8
  Saturation: 0

Green Primary:
  Hue: -10
  Saturation: -22

Blue Primary:
  Hue: 0
  Saturation: +6
```

These values were computed via a Python optimization script that matched A1II ST profile colors to an A7V image — they effectively shift Sony's rendering closer to Canon-like warmth.

### General Calibration Heuristics (Community Consensus)

For pushing Sony toward Canon:
- **Red Hue:** Shift slightly negative (-5 to -15) — pushes reds toward magenta
- **Green Hue:** Shift negative (-5 to -15) — warms up foliage and reduces green cast
- **Green Saturation:** Reduce (-10 to -25) — tames Sony's green channel
- **Blue Saturation:** Slight positive (+5 to +15) — enriches skies
- **Red Saturation:** Slight positive (+5 to +10) — boosts skin warmth

**Important:** Calibration sliders apply to the entire image base and interact differently per body. Values that work for A7III won't perfectly translate to A7IV or A7RV.

### White Balance Baseline Shift
Many users recommend setting a permanent WB bias in Lightroom's import preset:
- **Temp:** +200 to +400K warmer than as-shot
- **Tint:** +3 to +8 toward magenta

In-camera equivalent: *"AWB tilted to B0.5 M0.5 or whatever"* — u/szewc, r/SonyAlpha. This shifts the starting point toward Canon-like warmth before any profile is applied.

---

## Strategy 3: Custom DCP Profiles via dcpTool

### The Approach
The most technically sophisticated community approach involves creating custom DCP (DNG Camera Profile) files:

1. Obtain a DCP profile from a Canon body (or from Cobalt/Color Fidelity)
2. Use [dcpTool](https://sourceforge.net/projects/dcptool/) to decompile: `dcptool -d input.dcp output.xml`
3. Edit the XML — change `<UniqueCameraModelRestriction>` to match your Sony body
4. Recompile: `dcptool -c edited.xml new.dcp`
5. Import into Lightroom

### Notable Implementations

**ALPH47's Fujifilm Emulation (r/SonyAlpha):**
- User ALPH47 spent "weeks and months" reverse-engineering Fujifilm GFX profiles for Sony bodies
- Built calibrated DCP base profiles for A7RV, A7III, A7RIII, A7IV, A7C
- Required shooting reference targets with controlled lighting
- Results: 99% match to GFX output (difference attributed to lens characteristics)
- Profiles offered: Provia, Velvia, Astia, Classic Chrome, Classic Neg, Nostalgic Neg, Pro Neg Hi/Std

**A7V Profile Hack (r/SonyAlpha):**
- When A7V launched without Lightroom camera-matching profiles, u/Reptiles_SHH discovered A1II profiles worked as a close match
- Used dcpTool to change camera model restriction from "Sony ILCE-1M2" to "Sony ILCE-7M5"
- Process documented step-by-step for Windows users
- Additional calibration adjustments applied on top for exact matching

---

## Strategy 4: In-Camera Tweaks (JPEG/SOOC)

### Sony Creative Looks (A7IV and newer)
- **FL** with AWB shifted warm: Frequently recommended as closest to Canon SOOC
- **SH** (Soft High-key): Popular for portrait shooters wanting bright, Canon-like skintones
- Customize contrast (-1 or -2), saturation (+1), and sharpness to taste

### Sony Picture Profiles (All bodies)
- PP1-PP10 can be configured for stills shooting
- Some users shoot HLG2 (PP10) for wider dynamic range with muted tones
- Veres Deni Alex (popular YouTuber) provides specific PP settings for Canon/Fuji emulation

### WB Shift (All bodies)
- In-camera AWB priority: Set to "AWB-W" (White priority) for warmer rendering
- Manual WB shift: +1 Amber, +0.5 Magenta grid position

---

## Strategy 5: HSL and Color Grading (Manual)

### HSL Adjustments for Canon-Like Skin
Reddit user u/Alert-Ad-6284 shared a Canon-matched Sony A7III edit in r/postprocessing (61 upvotes), describing their multi-step approach:
- Calibration panel adjustments (see Strategy 2)
- HSL panel: increase orange luminance slightly, shift red hue toward orange, increase red/orange/yellow saturation modestly
- Mask different areas of the image with different color temperatures
- Add contrast selectively to separate subject from background

### General HSL Consensus for Canon Emulation

| Color | Hue Shift | Saturation | Luminance |
|---|---|---|---|
| Red | +5 to +15 toward orange | +5 to +15 | 0 to +10 |
| Orange | 0 to -5 | +10 to +20 | +10 to +20 |
| Yellow | 0 to -5 toward orange | +5 to +10 | 0 |
| Green | +10 to +20 toward yellow | -10 to -20 | 0 to -10 |
| Aqua | 0 | 0 to -10 | 0 |
| Blue | 0 to -5 | +5 to +10 | -5 to -15 |

### Color Grading Wheels
- **Shadows:** Subtle warm tint (orange/amber at low saturation)
- **Midtones:** Neutral to slightly warm
- **Highlights:** Slightly warm (golden hour effect)

---

## Strategy 6: Use a ColorChecker Passport

### Professional Approach
Multiple Reddit threads reference using X-Rite/Calibrite ColorChecker Passport:
1. Shoot the chart under your working light
2. Use Lightroom plugin to generate a custom camera profile
3. This creates a calibrated, neutral starting point
4. From neutral, add warmth and magenta bias intentionally

**Cost:** ~$100 for the hardware
**Benefit:** Camera-specific color accuracy, eliminates sensor-to-sensor variance

From u/aCuria on r/SonyAlpha: *"If you really want to dial the colors in, then get a chip chart and apply the correction in Lightroom or Capture One."*

---

## Community Consensus: What Doesn't Work

### Generic Cross-Brand Presets
- Applying a Canon preset designed for CR2/CR3 files directly to Sony ARW files produces unpredictable results.
- Different sensor CFA (Color Filter Array) characteristics mean the same slider values produce different outputs.
- Presets that work on Canon R5 files will NOT translate correctly to Sony A7IV files.

### Simple Temperature/Tint Adjustments Alone
- Warming WB helps but doesn't address the underlying tonal differences.
- Users report that temperature adjustments alone create "uncanny valley" skin — warm but still flat.

### "Just Shoot JPEG" with Default Settings
- Sony's default JPEG engine on older bodies (pre-A7IV) doesn't compare favorably to Canon's.
- Newer bodies with Creative Looks (FL, SH) partially close this gap.

---

## Quick-Start: The 5-Minute Canon-Emulation Setup

1. **Import preset:** Set default profile to Camera Matching → Sony ST (or Standard)
2. **WB bias:** Temp +300, Tint +5 in import preset
3. **Calibration:** Red Hue -8, Green Hue -10, Green Sat -20
4. **HSL:** Orange Sat +15, Orange Lum +10
5. Adjust per scene, save as a preset for batch application

This won't be perfect but provides a substantially closer starting point than Adobe Color defaults.

---

*Sources: r/SonyAlpha threads (specifically u/Supsti_1's ST profile discovery, u/Reptiles_SHH's A7V dcpTool hack, u/Alert-Ad-6284's Canon match post, u/ALPH47's Fuji emulation project), r/postprocessing threads, community discussion*
