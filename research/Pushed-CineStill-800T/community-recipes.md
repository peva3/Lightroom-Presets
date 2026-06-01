# Pushed CineStill 800T — Community Recipes

## Source
Fuji X Weekly: https://fujixweekly.com/2023/07/22/pushed-cinestill-800t-fujifilm-x-t5-x-trans-v-film-simulation-recipe/

## Fuji X Weekly Recipe (X-Trans V)
- Film Simulation: Eterna Bleach Bypass
- Grain Effect: Strong, Large
- Color Chrome Effect: Strong
- Color Chrome FX Blue: Weak
- White Balance: 7700K, -9 Red & +5 Blue
- Dynamic Range: DR400
- Highlight: -0.5
- Shadow: +1.5
- Color: +3
- Sharpness: 0
- High ISO NR: -4
- Clarity: -3
- ISO: Auto, up to ISO 6400
- Exposure Compensation: -1/3 to +2/3 (typically)

## Description
Pushed CineStill 800T emulates CineStill 800T (Kodak Vision3 500T with Remjet removed) push-processed 2 stops to EI 3200. The result: more grain, more contrast, stronger halation, and more extreme color shifts than standard CineStill 800T. The "pushed" variant is particularly suited for concert/night photography. While the Fuji recipe was designed for overcast daylight, it excels at night with a diffusion filter.

## XMP Translation Notes
- WB 7700K is defining (tungsten-balanced film look); kept in XMP
- Eterna Bleach Bypass → high contrast, low saturation base
- Grain Strong/Large → Amount 55, Size 45, Roughness 65 (pushed film)
- Clarity -3 → Clarity -10 (bloom/halation approximation)
- High ISO NR -4 → LuminanceSmoothing 0 (no noise reduction)
- Sharpness 0 → Sharpness 10 (grain protection)
- Cinematic ToneCurve (0,20 / 64,55 / 128,128 / 192,196 / 255,235)
- ColorGrade: tungsten shadow blue + warm highlight orange
