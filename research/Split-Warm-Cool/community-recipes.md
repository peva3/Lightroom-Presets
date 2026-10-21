# Split Warm-Cool — Community Recipes & Reference Values

> Compiled from darkroom split-toning threads, duotone printing practice, and community
> Lightroom split-tone recipes. Values are translation targets for the ColorGrade panel.

## Recipe A: "Split sepia + selenium" (the darkroom original)
- Full sepia tone, then a short selenium bath.
- Result: honey highlights, aubergine shadows, neutral midtones. The ancestor of every
  warm/cool split preset.

## Recipe B: "Teal and orange, restrained"
- Highlights warm (≈40–50°), shadows cool (≈200–215°), low saturation.
- The restrained version of the cinematic grade; saturation is what separates "toned print"
  from "blockbuster poster".

## Recipe C: "Cool shadow / neutral highlight"
- Only the shadows tinted (blue ≈ 220°, sat 10–15), highlights left at zero.
- Reads as cold evening light rather than as a two-colour grade.

## Community consensus points
- Warm highlights + cool shadows is the canonical direction; the reverse arrangement is a
  cross-process look and should not be labelled "split tone".
- Keep per-zone saturation ≤ ~18; above that midtones lose neutrality and skin goes plastic.
- Balance at or near 0 — the crossover must sit at mid-grey for the midtones to stay clean.
- Do not stack legacy `SplitToning*` attributes on top of `ColorGrade*`; Lightroom applies both
  and the tint doubles.
- A split tone is applied to a *finished* B&W render, so contrast should stay near base — the
  colour does the work.

## Quality assessment
Consistent guidance across sources on direction, zone weighting, and saturation ceilings. The
most common failure is over-saturation, which turns a print aesthetic into a graphic effect.
