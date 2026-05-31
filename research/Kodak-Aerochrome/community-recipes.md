# Kodak Aerochrome / False-Color IR — Lightroom & Community Emulation Recipes

## Core Concept

Digital emulation of Aerochrome requires **three distinct operations** applied in sequence:

1. **Channel manipulation** (swap or remap RGB channels)
2. **HSL hue shifting** (green → magenta, blue → cyan)
3. **Tonal balancing** (vegetation glow, sky depth, contrast)

No single HSL adjustment can replicate Aerochrome because the false-color mapping is fundamentally different from any HSL remap. True emulation requires channel-level manipulation.

---

## Method 1: Lightroom HSL Only (Simplified)

*Easiest, works entirely in Lightroom. Results are approximate but recognizable.*

### HSL Panel Settings

**Hue:**
| Color | Shift |
|-------|-------|
| Red | +30 to +60 |
| Orange | +15 to +30 |
| Yellow | -80 to -100 |
| Green | -100 to -130 |
| Aqua | 0 to +30 |
| Blue | -30 to -60 |
| Purple | +30 to +60 |
| Magenta | 0 to -20 |

**Saturation:**
| Color | Change |
|-------|--------|
| Red | +20 to +40 |
| Orange | +10 to +20 |
| Yellow | -30 to -60 |
| Green | -50 to -80 |
| Aqua | +20 to +40 |
| Blue | +30 to +60 |
| Purple | +20 to +40 |
| Magenta | +10 to +30 |

**Luminance:**
| Color | Change |
|-------|--------|
| Green | -20 to -40 |
| Yellow | -10 to -20 |
| Blue | -20 to -40 |
| Red | +10 to +20 |

### Key Rationale
- **Green → -100 to -130 hue**: Shifts all green vegetation into red/magenta territory. This is the single most critical slider.
- **Blue → -30 to -60 hue**: Pushes blue sky toward cyan/teal.
- **Yellow → -80 to -100 hue**: Shifts yellow-greens (sunlit grass) toward red.
- Saturation cuts on green/yellow prevent the new magenta from being overwhelming.
- Blue darkening helps water and sky shadow areas.

---

## Method 2: Photoshop Channel Mixer (Intermediate)

*More accurate than HSL-only. Requires Photoshop or similar.*

### Step 1: Red Channel Replacement
```
Red channel source:
  Red:   0%
  Green: 100%
  Blue:  0%
```
This remaps infrared-bright areas (vegetation) into the red channel, the first step to creating the magenta foliage look.

### Step 2: Green Channel Replacement
```
Green channel source:
  Red:   100%
  Green: 0%
  Blue:  0%
```

### Step 3: Blue Channel Replacement
```
Blue channel source:
  Red:   0%
  Green: 0%
  Blue:  100%
```

### Step 4: Fine-Tune with HSL
After the channel swaps, apply the Method 1 HSL adjustments to refine:
- Push resulting reds toward magenta
- Shift blues toward cyan
- Adjust saturation and luminance

---

## Method 3: Full Channel Swap + Curves (Advanced)

*Best results for accuracy. Requires Photoshop.*

### Process
1. **Duplicate background layer** × 3 (one for each channel swap)
2. **Channel Swap** using Apply Image or channel mixer:
   - Swap **Red ↔ Green** channels
   - Leave Blue channel as-is, then shift via Curves
3. **Curves adjustments per channel**:
   - **Red curve**: Lift shadows slightly, boost highlights → enhances magenta glow
   - **Green curve**: Reduce midtones → reduces green cast on non-vegetation
   - **Blue curve**: Lift highlights → pushes sky toward cyan
4. **Merge and apply HSL** (Method 1 final tuning)

### Additional Steps (Optional)
- Add a subtle **gradient map** (magenta → white → cyan) at 5-10% opacity for tonal unification
- Apply **clarity/texture +15 to +25** on vegetation areas (masked) for the IR "glow" effect
- **Vignette -15 to -20** with midpoint at 25 — Aerochrome often has natural corner darkening

---

## Method 4: LUT / Preset Approach

Several community-created presets exist:

### Popular Approaches
1. **RNI All Films 5** — includes "Aerochrome" profile (modified, not fully accurate)
2. **Really Nice Images (RNI)** custom LUTs for Capture One/Lightroom
3. **VSCO** custom profiles — none official, some community modifications
4. **Jamie Windsor's Aerochrome preset pack** — popular YouTube recipe
5. **Kodak Aerochrome LUT by PixelPeeper** — channel-swap based

### Community Notes on Presets
- Most commercial presets use a compromised approach (HSL-only or channel mixer blend)
- The best community-reviewed results come from **manual channel swaps + HSL** rather than any single preset
- No preset perfectly replicates the look — it's always a "vibe match"

---

## Method 5: Camera Calibration Panel (Lightroom)

*Hidden gem technique used by some community members.*

### Process Version: Version 5 (2012) recommended

| Slider | Green Primary | Red Primary | Blue Primary |
|--------|--------------|-------------|--------------|
| **Hue** | -50 to -70 | +40 to +60 | -40 to -60 |
| **Saturation** | +20 to +40 | +10 to +30 | +20 to +50 |

This shifts the underlying color matrix in a way that mimics false-color channel remapping to some degree.

**Combine with HSL** for more complete results.

---

## Community Workflows (from r/postprocessing, r/analog discussions)

### Workflow A: "Quick And Good Enough"
1. Start with a well-exposed base image (landscape with green vegetation)
2. Apply Camera Calibration shifts (Method 5)
3. Apply HSL panel adjustments (Method 1)
4. Add slight dehaze (-5 to -10) for the slightly diffused IR look
5. Tone curve: lift blacks slightly, slight S-curve

### Workflow B: "Channel Swap Purist"
1. Export from Lightroom to Photoshop
2. Full channel swap (Method 3)
3. Return to Lightroom
4. Final HSL tuning and local adjustments
5. Grain: +30 amount, +40 size, +50 roughness (Aerochrome has visible grain)

### Workflow C: "C-41 Cross-Process Emulation"
*For those wanting the more extreme cross-processed look (popular on r/analog)*
1. Same channel swap as Method 3
2. Increase saturation +20 to +40 globally
3. Push magenta deeper (HSL: Magenta hue -25, saturation +30)
4. Reduce overall contrast slightly
5. Add slight yellow-green shadow tint (split toning: shadows hue 55, sat 5)

---

## Vegetation Selectivity Notes

Aerochrome's most challenging aspect to emulate is **selective vegetation response**:
- Only chlorophyll-rich vegetation goes magenta
- Dead plants, brown grass, tree bark remain neutral/cream
- Digital emulation often makes *everything green* turn magenta, which looks wrong

### To improve selectivity:
- Use **luminance masks** targeting the green channel
- Apply magenta shift only to brighter greens (healthy foliage)
- Keep darker greens (evergreens, shaded areas) with a more muted shift
- Mask out brown bark, dirt patches from the shift

---

## Test Scene Recommendations
For consistent preset development:
- Landscapes with prominent green foliage, blue sky, and clouds
- Botanical gardens or parks with varied vegetation
- Scenes with both sunlit and shaded foliage
- Bodies of water visible in frame
- Avoid: urban-only scenes, mostly-brown landscapes, winter scenes without foliage

---

## Reddit Source Posts

Key discussions on emulation (r/postprocessing, r/analog, r/infraredphotography):
- Channel swap method is consistently the #1 recommended approach
- Multiple users report HSL-only is "close but not right" — missing the channel-level remapping
- The Photoshop "swap red and green channels, then adjust" recipe is cited across dozens of threads
- Jamie Windsor's YouTube tutorial referenced consistently as the most thorough public guide
- RNI Films' "Aerochrome" profile in RNI All Films 5 is the most-cited commercial preset
