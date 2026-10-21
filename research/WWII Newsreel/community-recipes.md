# WWII Newsreel Lightroom Preset — Community Recipes & Settings

Ranges for a 1940s newsreel frame, derived from release-print characteristics and from film-restoration practice rather than from a single published grade.

## Reference Looks

The primary reference is archival: NARA's Universal Newsreel holdings and the BFI's nitrate collection, both of which publish frames that show how hard and grainy a release print is compared with the negative. Film-restoration colourists describe the same target from the other side: when a scan of a dupe negative is "corrected" back toward the original, contrast and grain come *down*, which tells you how much of the look is generation loss. War-film grades in modern cinema — desaturated, blue-shadowed, hard-contrast — are a recognisable shorthand but a different object: they are usually designed to look like a memory of the footage rather than like the footage. Pick one target and stay on it.

## Slider Starting Points

| Panel | Range | Contribution |
|---|---|---|
| Exposure | −0.4 to 0 | Dense print, made for projection through carbon arc |
| Contrast | +20 to +40 | Dupe-generation build-up |
| Highlights | −60 to −35 | Holds the shoulder; newsreel highlights are hot |
| Shadows | −20 to 0 | Negative values block up the blacks like a release print |
| Whites | 0 to +10 | Keeps a spark in the speculars |
| Blacks | −30 to −15 | −30 is the hard floor; beyond it is a digital hole |
| Clarity | 0 | Zero while grain is active |
| Texture | 0 | Same |
| Dehaze | 0 | No atmospheric modelling here; grain is the texture |
| Saturation | −55 to −35 | Global mute is mandatory |
| Vibrance | −5 to 0 | Positive Vibrance produces instant selective colour |
| HSL saturation | −50 to −35 per hue | One silver axis; no surviving accent hue |
| Color Grade — highlights | Hue 200–220°, Sat 0–8 | Cool silver, lightly |
| Color Grade — shadows | Hue 200–230°, Sat 5–12 | Cool shadows; keep saturation low |
| Grain | Amount 40–55, Size 30–38, Rough 60–75 | Dupe grain — coarse and structured |
| Vignette | −30 to −15 | Projection falloff and fast lenses |

## Common Mistakes

- **Treating the blue cast as historical.** Release prints were neutral to warm. Blue is a modern convention; use it knowingly and keep saturation under ~10.
- **Crushing past −30.** `Blacks` below −30 collapses into a rectangle on uncalibrated displays, and the texture that makes the look dies with it.
- **Pushing Dehaze positive.** It removes the veiling and sharpens grain into noise.
- **Sharpening over grain.** `Sharpness` above 10 with `GrainAmount` 50 turns every particle into a ringing edge.
- **Clean, high-resolution sharpness.** A release print is soft by modern standards; positive Clarity or Texture breaks the illusion immediately.
- **Ignoring the midtones.** The era's darkness is in the shadow *weight*, not in a global exposure cut; underexposing to get "mood" loses faces.

## See Also

- [WWII Newsreel characteristics](characteristics.md)
- [Dust Bowl Documentary](../Dust%20Bowl%20Documentary/) — the same period, warmer and softer.
- [Dramatic Monochrome](../Dramatic-Monochrome/) — the modern look this preset is often confused with.
