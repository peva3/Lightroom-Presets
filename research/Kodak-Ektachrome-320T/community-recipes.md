# Kodak Ektachrome 320T — Community Recipes

## Source: Extrapolation from STYLEGUIDE + tungsten slide characteristics

### Rationale
This preset synthesizes:
1. **STYLEGUIDE Cross-Processed E6→C41 formula** (Section IV — green/magenta crossover)
2. **Tungsten-balanced slide characteristics** (blue cast from 3200K balance in daylight/scan)
3. **Ektachrome color palette** (slightly cool, clean, moderate saturation)

No single Fuji X Weekly recipe exists for cross-processed tungsten slide film. This is a synthesis preset.

### Fuji → Lightroom Translation
| Element | LR Attribute | Value | Source |
|---|---|---|---|
| Xpro Contrast | Contrast2012 | +30 | E6→C41 standard contrast boost |
| Highlight Rolloff | Highlights2012 | -45 | Shoulder compression for high gamma |
| Shadow Lift | Shadows2012 | +15 | Some shadow detail recovery |
| Tungsten Blue | Blue Sat +15 | HSL | Tungsten balance boosts blue perception |
| Xpro Green | Green Sat -15 | HSL | Green shift from C-41 processing |
| Skin Cooling | Orange/Red Sat -10 | HSL | Tungsten + xpro cools skin tones |
| Xpro Grading | CG S:220/M:120/H:330 | Color Grade | Blue shadows + green mids + magenta highs |
| Grain | Amount 35 / Size 30 / Freq 55 | Grain panel | Slide + xpro = emphasized grain |

### Key Design Decisions
1. **Blending at 50** per Color-Negative category (though xpro typically uses 40, the category rule takes precedence)
2. **Contrast +30**: High but not extreme — the cross-processed effect comes more from color shifts than contrast alone
3. **Three-way color grade**: The defining characteristic. Blue shadows (tungsten), green midtones (xpro crossover), magenta highlights (complementary crossover)
4. **Blue Sat +15**: Amplifies the tungsten blue cast that distinguishes this from E6 daylight xpro
5. **No WB**: Per STYLEGUIDE — the blue/magenta/green color shifts are achieved entirely through Color Grading + HSL
6. **Blacks at -15**: Some crush for the slide film DMax character, but not extreme

### Comparison to Existing Cross-Processed E6→C41 Preset
| Aspect | Ektachrome 320T | Cross-Processed E6-C41 (existing) |
|---|---|---|
| Balance | Tungsten (3200K) | Daylight (5500K) |
| Shadow color | Blue (H220) | Green-cyan (H160) |
| Midtone color | Yellow-green (H120) | Yellow-green (H70) |
| Highlight color | Magenta (H330) | Magenta (H320) |
| Blue saturation | Boosted (+15) | Not specifically boosted |
| Overall cast | Cool blue-dominant | Green-magenta dominant |
| Contrast | +30 | Similar range |
