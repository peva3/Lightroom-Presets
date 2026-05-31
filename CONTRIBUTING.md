# Contributing

Thanks for helping grow this preset collection. The goal is to keep things simple — each preset is a single `.xmp` file anyone can drag into Lightroom.

## Adding a New Preset

1. **Create the preset in Lightroom.** Tune it on a well-exposed RAW photo. Avoid baking in exposure, white balance, or crop adjustments that are shot-specific.
2. **Export as `.xmp`.** In the Develop module, click the `+` on the Presets panel header, choose *Create Preset*, give it a descriptive name, and export.
3. **Match the naming convention.** Use a descriptive name that conveys the film stock or look:
   - `Film Stock Name.xmp` — e.g., `Kodak Portra 400.xmp`
   - `Descriptive Look Name.xmp` — e.g., `Cinematic Teal and Orange.xmp`
4. **Place the file in the repo root.** All presets live flat in the top-level directory.

## Editing an Existing Preset

1. **Apply the preset in Lightroom** to a neutral reference image.
2. **Tweak the settings** in the Develop module. Document what you changed and why in your PR description.
3. **Right-click the preset** in the Presets panel, choose *Update with Current Settings*.
4. **Re-export the `.xmp`** and replace the existing file in the repo.

## README Updates

When adding or editing a preset, update `README.md` following the existing format:

```markdown
### Preset Name

*One-line vibe description — what it feels like and where it came from.*

A short paragraph about the inspiration, the film stock, or the look it's chasing.

**Settings:**
| Panel | Adjustments |
|---|---|
| Light | ... |
| Color | ... |
| HSL | ... |
| Effects | ... |
```

Add the preset to the Quick Reference table at the bottom of the README as well.

## Guidelines

- **Test on multiple images.** Make sure the preset works across different lighting conditions, not just the photo you tuned it on.
- **No shot-specific adjustments.** Don't include Exposure, White Balance, or Crop in the preset unless it's fundamental to the look (e.g., Cinestill 800T pushing WB toward tungsten).
- **Document your reference.** In your PR, mention what film stock, reference photo, or aesthetic you were targeting.
- **One preset per PR** unless they're part of a related set.
- **Keep it friendly.** These presets are shared for free — be open to feedback and iteration.

## Submitting

1. Fork the repo.
2. Create a branch: `git checkout -b preset/my-new-preset`
3. Add your `.xmp` file and update `README.md`.
4. Commit: `git commit -m "Add Preset Name"`
5. Push and open a pull request with a description of the look and your reference.

## Questions?

Open an issue or start a discussion on the repo. Happy to help dial in settings.
