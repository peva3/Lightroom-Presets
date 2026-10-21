# Golden Grid Architecture Lightroom Preset — Aesthetic Characteristics

Golden Grid Architecture is a warm, contrasty architectural photography Lightroom preset designed for golden-hour building and cityscape shots. It emphasizes structural geometry ("grid") through deep shadows, lifted midtones, and selective warm color boosting.

## Key Visual Traits

- **Very warm white balance** (6500K / Tint +15) — pushes amber/magenta toward warm golden tones
- **High contrast** (+30) with an S-curve that lifts the black point to 5% (0,5) — filmic matte shadows without crushing
- **Moderate highlight rolloff** (-20, shadows +15) — retains detail in bright architecture while opening up dark areas
- **Selective orange/yellow saturation** (+25/+15) with green suppression (-20) — warm brick, stone, and sunset tones pop while foliage recedes
- **Orange luminance boost** (+10) — skin-friendly for street-level architectural shots with people
- **Strong vignette** (-35/40/60) — frames the composition, draws eye to center
- **Sharpened architecture** via Clarity +10, Dehaze +15, Texture +5 — brings out material texture without digital harshness
- **Warm highlight color grade** (H45/S5, Blending 75) — subtle golden sheen on bright areas
- **No grain** — clean rendering for crisp architectural lines

## Ideal Subjects

- Urban architectural exteriors (skyscrapers, bridges, historic buildings)
- Golden-hour cityscapes and skyline shots
- Warm-toned building materials (brick, sandstone, terracotta)
- Street-level architecture with mixed warm/cool lighting
- Interior architectural details with warm ambient light

## Tone Curve

Custom 5-point S-curve with lifted blacks:
- `0, 5` — lifted black point (matte film shadow)
- `45, 35` — shadow compression
- `128, 128` — midtone anchor
- `192, 200` — gentle highlight lift
- `255, 255` — white point

## Lightroom Panel Breakdown

| Panel | Setting | Value |
|-------|---------|-------|
| WB | Temperature | 6500K |
| WB | Tint | +15 |
| Basic | Exposure | +0.45 |
| Basic | Contrast | +30 |
| Basic | Highlights | -20 |
| Basic | Shadows | +15 |
| Basic | Whites | +20 |
| Basic | Blacks | -15 |
| Presence | Clarity | +10 |
| Presence | Dehaze | +15 |
| Presence | Texture | +5 |
| Presence | Vibrance | +20 |
| Presence | Saturation | +5 |
| HSL Hue | Yellow | -10 |
| HSL Sat | Orange | +25 |
| HSL Sat | Yellow | +15 |
| HSL Sat | Green | -20 |
| HSL Lum | Orange | +10 |
| HSL Lum | Yellow | +5 |
| ColorGrade | Highlights | H45/S5 |
| ColorGrade | Blending | 75 |
| Effects | Vignette | -35/40/60 |
| Profile | Adobe Color | — |

## Comparison to Similar Presets

| Trait | Golden Grid | Savanna Golden | Outback Red Earth |
|-------|------------|----------------|-------------------|
| WB | 6500K/+15 | +700 (warm) | +800 (very warm) |
| Contrast | +30 | +25 | +30 |
| Exposure | +0.45 | -0.05 | -0.15 |
| Vignette | -35 | none | none |
| Tone Curve | S-curve (0,5) | Cinematic (0,20) | Cinematic (0,20) |
| Orange Sat | +25 | +25 | +25 |
| Green Sat | -20 | +10 | -25 |
| Clarity/Dehaze | +10/+15 | +10/+10 | +20/+15 |

## Validation Sweep 2026-10-21
- **Verdict:** minor drift
- **Defining traits checked:** Kelvin 6500, Tint +15, Ex +0.45, Contrast +30, Highlights -20, Shadows +15, Whites +20, Blacks -15, Clarity +10, Texture +5, Dehaze +15, Vibrance +10, Saturation +5; YellowHue -10, OrangeSat +25, YellowSat +15, GreenSat -20, OrangeLum +10, YellowLum +5; highlight H45/S5, blending 75; calibration none; PV 15.4, Color, Adobe Color Look; custom contrast curve. Aerial golden-hour city identity is present (Kelvin 6500, Tint +15, OrangeSat +25, vignette -35, custom contrast curve 0,5 / 45,35 / 128,128 / 192,200 / 255,255). Tint +15 is a visible magenta bias on concrete and glass; on pure architecture deliverables it will read as a cast. Advisory: Tint +15 -> +6 keeps the gold without the magenta. Left unchanged: the preset is a stylised aerial look, not a documentation preset.
- **Sources:** whitepaper `research/whitepapers/lightroom-xmp-attribute-reference.md`; STYLEGUIDE.md sec. VI (pitfall: tint vs. warm temperature); architecture/aerial community recipes.
- **Preset adjustments:** none
