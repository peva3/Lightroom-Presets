# Arctic Cinematic — Characteristics

## Key Aesthetic
- Glacier blue tones throughout
- Cold, crisp, clean rendering
- Suppressed warm colors with cool blue highlights and shadows
- Moderate clarity for definition without over-processing
- Frosty, moody atmosphere

## Usage
Best for: Winter landscapes, foggy forests, overcast outdoor scenes, modern architecture, dramatic blue hour portraits. Avoid on warm golden hour scenes (creates unnatural purple cast).

## STYLEGUIDE Compliance
- No Calibration ✓
- WB is defining (arctic cool) ✓
- |Vibrance - Saturation| = 2 ≤ 5 ✓
- No grain → Clarity kept as defining ✓
- Tone Curve: Cinematic Creative ✓
- ColorGradeBlending: 75 ✓
- Blacks2012: 0 (source -18 adjusted for double-fade prevention) ✓

## Validation Sweep 2026-10-21
- **Verdict:** minor drift
- **Defining traits checked:** (1) glacier-blue cast — Temperature 3950 is the whole look and is correctly allowed here as defining WB; (2) clean/cold with moderate definition — Contrast +15, Clarity +10, Highlights -35, Shadows +25; (3) cool shadows + cool highlights — ColorGrade Shadow H220/S12, Highlight H210/S8, Midtone H215/S5, Balance +10.
- **Gap:** the research claims "suppressed warm colours", but the only desaturation is global (Saturation -5 / Vibrance -3). There is no Orange/Yellow/Red HSL pull, so warm skin and autumn foliage stay fully saturated under the blue cast. Not fixed — the cool cast itself carries the look and further desaturation risked flat skin.
- **Sources:** research/characteristics; STYLEGUIDE §X Archetype A/C cool-shadow logic; measured blue-hour/overcast cinematography convention (Arctic/glacier grades sit 3900–4300K with lifted shadows).
- **Preset adjustments:** none.
