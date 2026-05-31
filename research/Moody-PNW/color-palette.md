# Moody PNW Color Palette & Theory

> The specific color manipulations that create the dark, brooding PNW forest aesthetic.

---

## Source Colors (Natural PNW Palette)

The unedited PNW landscape contains these base colors:

| Element | Natural Color | Hex (approx) |
|---|---|---|
| Douglas fir / hemlock | Deep muted green | `#2D4A2C` to `#3B5E38` |
| Wet bark / trunks | Dark brown-grey | `#3A3028` to `#4A3C30` |
| Moss / lichen | Yellow-green | `#5A6B30` to `#6B7B3A` |
| Fog / mist | Cool grey-white | `#CBD0D4` to `#DCE0E4` |
| Overcast sky | Cool blue-grey | `#8A95A5` to `#9DA8B5` |
| Forest floor | Muted brown/orange | `#5A4028` to `#6B4C30` |
| Ferns | Mid green | `#406030` to `#4E703A` |
| Coastal water (grey day) | Dark teal-grey | `#3A5058` to `#45606A` |
| Sea stacks / rock | Dark grey-brown | `#4A4238` to `#585048` |
| Waterfalls / streams | Cool white/cyan highlights | `#E0E8F0` |

---

## Target Colors (After Moody PNW Grade)

### Primary Palette: Dark Teal Greens

The foundational color. Natural greens are shifted from true green toward teal (cyan-green) territory while being heavily desaturated and darkened.

| Name | Hex | Use |
|---|---|---|
| Deep Forest Teal | `#1A2A20` | Shadows in foliage, darkest greens |
| Crushed Evergreen | `#2A3A2A` | Midtone greens, main forest body |
| Moss Green | `#3A4A30` | Highlight greens, wet surfaces |
| Dark Pine | `#1E2E1E` | Background trees, vignette areas |
| Coastal Teal | `#253035` | Water in overcast light, shadows |

**LR technique**: Green Hue +40 to +60 (shifts toward yellow, but combined with blue calibration creates teal territory), Green Saturation -60 to -90, Green Luminance +30 to +50.

### Secondary Palette: Muted Earth Tones

Warm earth colors are desaturated and luminance-boosted to create subtle warmth without vibrancy. These anchor the image and prevent it from feeling monochromatic.

| Name | Hex | Use |
|---|---|---|
| Wet Bark Brown | `#4A3828` | Tree trunks, roots |
| Faded Fern | `#5A5A30` | Dried ferns, forest floor |
| Muted Clay | `#5A4A3A` | Earth, trails, soil |
| Dull Amber | `#6A5030` | Autumn leaves, warm accents |
| Shadow Earth | `#3A2A20` | Dark forest floor |

**LR technique**: Orange Hue 0, Orange Saturation -10 to -20, Orange Luminance +50 to +80. Yellow Saturation -20 to -40. Red Saturation -20 to -30.

### Tertiary Palette: Misty Atmospheric Colors

The cool, hazy colors that define the mood — fog, mist, overcast sky, distant mountains. These colors live in the highlights and midtones.

| Name | Hex | Use |
|---|---|---|
| Fog Grey | `#C8D0D8` | Mist, fog banks, atmosphere |
| Cold Blue-Grey | `#8898A8` | Overcast sky, distant mountains |
| Misty Cyan | `#98A8B0` | Diffuse light through fog |
| Shadow Blue | `#405060` | Cool shadows, rainy atmosphere |
| Highlight Teal | `#88A098` | Light catching wet foliage |

**LR technique**: Temperature -5 to -15, Tint -3 to -10 (green shift). Split toning: green/teal highlights at +5 to +10 saturation, cool blue-purple shadows at +5 to +10 saturation. Calibration: Blue Hue shifted significantly (turns greens teal), Blue Saturation increased.

### Accent Colors: Reserved Highlights

The small bright spots that create depth and focal interest. Used sparingly.

| Name | Hex | Use |
|---|---|---|
| Fog Glow White | `#E8E8E0` | Light piercing fog, waterfalls |
| Warm Highlight | `#D8D0B0` | Rare sunlight, warm accent |
| Water Reflection | `#D0D8D8` | Wet surfaces, stream highlights |

---

## Color Theory Breakdown

### The Green Problem

Natural green in photos reads as "healthy, vibrant, happy." Moody PNW needs the opposite. The solution is three-fold:

1. **Desaturate heavily** — -60 to -90 on green saturation
2. **Shift hue toward yellow** — +40 to +60 on green hue slider (this moves bright "spring" green toward muted "moss" green)
3. **Use calibration to further alter** — dropping blue primary hue in the Calibration tab shifts all greens toward a teal/orange palette. This is the "secret" color science trick.

### The Yellow Connection

Green hue shifts push into yellow territory. Yellow MUST also be controlled or the image looks sickly. The solution is yellow desaturation (-20 to -40) to match the muted green palette.

### The Teal-Orange Dynamic

At its core, Moody PNW uses a **subtle teal-orange split**:
- Cool teal/blue-green in the shadows and overall cast
- Muted warm earth tones (orange-brown, not orange-bright) in the ground/trunk colors
- This creates color contrast without saturation — warm vs cool rather than color vs color

### The Luminance Strategy

A key insight from the community: desaturated colors feel darker. To compensate:
- Orange luminance is pushed +50 to +80 (keeps earth tones visible against dark greens)
- Green luminance is raised +30 to +50 (prevents foliage from becoming black holes)
- Blue luminance raised slightly (maintains atmosphere visibility)

### The Calibration Tab "Secret"

Mentioned explicitly by thephlog (981-upvote tutorial) and implied in others:

> "I dropped the blue hues dramatically [in Calibration tab] to give the green tones a nice red/orange colour and then increased its saturation."

The Calibration tab affects color at the sensor level BEFORE the HSL sliders process them. This is why it's so powerful — it fundamentally shifts the color relationships in ways HSL alone cannot achieve. Dropping Blue Primary Hue is the single most impactful move for the Moody PNW green shift.

### Global Saturation

- Vibrance: typically untouched or slightly reduced
- Global Saturation: -30 to -60
- This pulls EVERYTHING down uniformly, then selective luminance boosts bring back specific elements

---

## Color Wheel Summary

```
                    COOL TEAL (dominant)
                          ↑
                          |
      FOG GREY ← — — — — + — — — — — → MUTED EARTH
                          |
                          ↓
                    SHADOW BLUE
```

The eye tracks from the cool overall cast (teal-green) through the atmospheric fog (grey) to the warm grounding (muted earth tones). The darkest shadows are cool blue, not warm black.

---

## Key Color Formulas (Quick Reference)

| Effect | Sliders |
|---|---|
| Crush greens (the core look) | Green Saturation -70, Green Hue +50, Green Lum +30 |
| Faded forest floor | Orange Lum +60, Orange Sat -15, Yellow Sat -30 |
| Brooding atmosphere | Temp -10, Tint -5, Dehaze +10 |
| Misty glow | Highlights -50, Whites +25, Radial filter: -Clarity +Exposure |
| Teal shift | Calibration: Blue Hue -30 to -60, Blue Sat +10 to +30 |
| Faded blacks | Tone curve: Lift shadow point 0.5-1.0 stops |
| Cool shadows | Split Tone Highlights: warm, Shadows: cool blue (+5-10 Sat each) |

---

## Inspirational References

The color palette draws from these real-world PNW references:
- **Olympic National Park** rainforest valleys in overcast light
- **Oregon Coast** sea stacks in morning fog
- **Columbia River Gorge** waterfalls on grey days
- **Mount Rainier** seen through mist and cloud layers
- **Vancouver Island** old-growth temperate rainforest
