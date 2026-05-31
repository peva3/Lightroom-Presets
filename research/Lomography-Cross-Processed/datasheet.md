# Cross-Processing Datasheet: E-6 Film in C-41 Chemistry

## Overview

**Cross-processing** (Xpro) is the deliberate development of photographic film in chemistry intended for a different film type. The most common form is processing E-6 slide/reversal film in C-41 color negative chemistry. This produces a negative image on a colorless (non-orange-masked) base with wild, unpredictable color shifts.

## The Two Film Systems

### E-6 (Slide/Reversal Film) — Normal Process

E-6 film is designed to produce a **positive transparency** (slide). The normal E-6 process has 6 chemical baths:

| Step | Bath | Time | Temp | Function |
|------|------|------|------|----------|
| 1 | First Developer (B&W) | 6 min | 38°C | Creates a **negative silver image** in each layer — this is the critical contrast-control step |
| 2 | First Wash | 2 min | 36-39°C | Stops first developer |
| 3 | Reversal Bath | 2 min | 24-39°C | Chemically fogs remaining unexposed silver halide (or uses light) |
| 4 | Color Developer (CD-3) | 6 min | 38°C | Develops the fogged silver halide → forms positive silver image + **oxidized developer couples with dye couplers** in each layer to form color dyes |
| 5 | Pre-Bleach / Conditioner | 2 min | 24-39°C | Contains formaldehyde (historically) as dye preservative; EDTA to kick off bleach |
| 6 | Bleach | 6 min | 33-39°C | Converts all metallic silver → silver bromide |
| 7 | Fixer | 4 min | 33-39°C | Removes all silver halide, leaving only dye image |
| 8 | Final Wash + Stabilizer | — | — | Surfactant + antifungal |

**Key point**: E-6 film has dye couplers designed to form dyes during the **color developer** step (step 4), acting on the **reversed** (fogged) silver halide — producing a positive image.

### C-41 (Color Negative Film) — Normal Process

C-41 film is designed to produce a **negative** on an orange-masked base. Steps:

| Step | Bath | Time | Temp | Function |
|------|------|------|------|----------|
| 1 | Color Developer (CD-4) | 3:15 | 37.8°C | Develops exposed silver → oxidized developer couples with dye couplers → forms negative dye image |
| 2 | Bleach | 6:30 | 24-41°C | Converts metallic silver → silver halide |
| 3 | Wash | 3:15 | 37.8°C | — |
| 4 | Fixer | 6:30 | 24-41°C | Removes silver halide |
| 5 | Wash | 3:15 | 37.8°C | — |
| 6 | Stabilizer | 1:30 | 24-41°C | Wetting agent, anti-fungal |

**Key difference**: C-41 uses **CD-4** developing agent; E-6 uses **CD-3**. C-41 film has an orange mask (from residual couplers in unexposed areas) to compensate for dye deficiencies.

## What Happens When E-6 Film Meets C-41 Chemistry

### The Chemical Collision

When E-6 slide film is processed in C-41 chemistry, several critical things happen:

1. **No First Developer / No Reversal Step**: The C-41 process lacks a separate B&W first developer and a reversal/fogging bath. The film goes straight into the C-41 color developer.

2. **Single Developer Step**: The C-41 color developer (CD-4) acts on ALL silver halide in the film — both exposed and unexposed. With normal E-6, the first developer creates a negative silver image and the reversal bath + color developer creates the positive dye image. Without the first developer, the C-41 color developer develops all silver indiscriminately.

3. **Wrong Developing Agent**: E-6 dye couplers are designed to react with oxidized **CD-3** (the E-6 color developing agent). C-41 uses **CD-4**, which is a different paraphenylene diamine variant. The dye couplers still react, but with different efficiency and coupling kinetics — producing **shifted, unpredictable colors**.

4. **Missing Formaldehyde Stabilizer**: E-6 films rely on formaldehyde in the pre-bleach/final rinse to stabilize dyes. C-41 stabilizer lacks formaldehyde (since ~1990s). This means cross-processed E-6 films may have reduced dye stability and archival properties.

5. **No Orange Mask**: Because E-6 film has a clear base (no orange mask like C-41 film), the resulting negative has a clear/colorless base. This contributes to the high-contrast, saturated look.

6. **Increased Contrast**: The C-41 developer develops more aggressively than E-6's first developer, and without the contrast-controlling first developer step, cross-processed film shows dramatically increased contrast.

7. **Color Shifts — The Science**: Each dye layer (cyan, magenta, yellow) in E-6 film was designed for CD-3 coupling. When CD-4 reacts with these couplers instead, the coupling efficiency differs per layer. Typically:
   - **Yellow layer** (blue-sensitive): couples inefficiently → weak yellows
   - **Magenta layer** (green-sensitive): shifts toward purple/magenta
   - **Cyan layer** (red-sensitive): shifts toward cyan/green/teal
   - Result: Shadows go **purple/blue** (dominant magenta + cyan layers), highlights go **yellow-green** (weak yellow + shifted cyan)

### Processing Notes

- **Temperature**: Despite E-6 normally requiring tight 38°C tolerance, cross-processing in C-41 at standard 37.8°C works — the C-41 developer is more forgiving.
- **Push Processing**: Many photographers push E-6 film 1-2 stops when cross-processing to compensate for the increased density and contrast.
- **Film Speed**: Generally, shoot at box speed or overexpose by 1/3 to 1 stop. Velvia 50 is often shot at ISO 40 or 50. Provia 100F at ISO 80-100.
- **Scanning**: Since the result is a negative on clear base, it scans easily — no orange mask removal needed. This is a major advantage.

## C-41 Film in E-6 Chemistry (Reverse Xpro)

The less common reverse process: C-41 negative film processed in E-6 chemistry produces a **positive image** with:
- Strong **green cast** (from the orange mask not being removed properly)
- Lower contrast than normal
- Muted, pastel-like colors
- The orange base of the C-41 film remains visible, giving everything a warm/amber tint

## Summary of Key Chemical Differences

| Property | E-6 (Normal) | C-41 (Normal) | E-6 in C-41 (Xpro) |
|----------|-------------|---------------|---------------------|
| Color developer | CD-3 | CD-4 | CD-4 on CD-3 couplers |
| Reversal step | Yes (chemical or light) | N/A | Missing → wrong image structure |
| First developer | Yes (B&W, controls contrast) | No | Missing → high contrast |
| Dye stabilizer | Formaldehyde | Surfactant only | No formaldehyde → less stable |
| Film base | Clear | Orange mask | Clear (E-6 base stays clear) |
| Result | Positive transparency | Negative | Negative on clear base |
| Color | Accurate | Corrected via orange mask | Wildly shifted, saturated |

## Sources
- Wikipedia: Cross processing, E-6 process, C-41 process
- Kodak Publication Z-119 (E-6), Z-131 (C-41)
- Practical experience from the analog photography community
