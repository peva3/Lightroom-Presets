# Pushed CineStill 800T — Characteristics

## Film Background
Based on Kodak Vision3 500T motion picture film (5219) with Remjet layer removed for C-41 processing. When push-processed 2 stops (EI 3200), the film exhibits:
- Increased apparent grain size and roughness
- Higher contrast with compressed dynamic range
- More extreme color crossover (tungsten balance in daylight creates strong blue cast)
- Enhanced halation (light piping through film base without Remjet anti-halation layer)

## Key Aesthetic
- Concert/night photography variant
- Strong tungsten blue cast in shadows
- Warm orange highlights from pushed color crossover
- Heavy, textured grain
- Bloom/glow from halation effect
- Dramatic light rendering for gig photography and urban night scenes

## STYLEGUIDE Compliance
- No Calibration ✓
- |Vibrance - Saturation| = 3 ≤ 5 ✓
- WB is defining (tungsten-balanced film look) ✓
- HSL ≤ ±60 ✓
- Grain → Sharpness=10, LuminanceSmoothing=0 ✓
- Tone Curve: Cinematic Creative ✓
- ColorGradeBlending: 75 ✓
- Blacks2012: 0 (double-fade prevention) ✓
## Validation Sweep 2026-10-21
- **Verdict:** accurate
- **Defining traits checked:** tungsten-blue shadow cast vs warm halation highlights; 2-stop push grain; bloom; crushed night blacks
- **Sources:** Fuji X Weekly recipe with 7700K WB (community-recipes.md); CineStill 800T halation references
- **Preset adjustments:** none. WB 7700/Tint +15 comes straight from the documented recipe; shadow 200 sat 18 + highlight 40 sat 12 recreate the tungsten/halation split; Grain 55/45 is appropriate for a 2-stop push. Clarity -10 with heavy grain is a deliberate halation-bloom deviation from the grain rule.
