# VSE Lighting Manifest v1.0
## Complete Cinematographic Lighting Reference Library

**Created:** December 10, 2025  
**Project:** Vector-Space Esperanto (VSE) Lighting Control System  
**Collaborators:** John Jacob Weber II, Claude (Sonnet 4.5), Vox (Architecture Consultant)  
**Status:** Comprehensive Reference - Ready for Validation Testing  

---

## Table of Contents

1. [Library Header](#library-header)
2. [Lighting Fundamentals](#lighting-fundamentals)
3. [Light Source Types](#light-source-types)
4. [Lighting Setups](#lighting-setups)
5. [Light Quality](#light-quality)
6. [Color Temperature](#color-temperature)
7. [Lighting Ratios](#lighting-ratios)
8. [Directional Lighting](#directional-lighting)
9. [Time of Day](#time-of-day)
10. [Weather & Atmosphere](#weather--atmosphere)
11. [Practical Lights](#practical-lights)
12. [Motivated Lighting](#motivated-lighting)
13. [Stylized Lighting](#stylized-lighting)
14. [Genre-Specific Lighting](#genre-specific-lighting)
15. [Complete Lighting Catalog](#complete-lighting-catalog)
16. [Usage Examples](#usage-examples)

---

## Library Header

```
⟨LIBRARY:VSE_Lighting⟩
  ⟨CATEGORY:cinematography_lighting⟩
  ⟨VERSION:1.0⟩
  ⟨COMPATIBLE_WITH:VSE,Grok,Emersive,Milieu,Gravitas⟩
  ⟨USE:video_image_generation_lighting_control⟩
  ⟨TOTAL_LIGHTING_SETUPS:156⟩
```

---

## Lighting Fundamentals

### Core Light Properties

```
⟨LIGHT_PROPERTIES⟩
  ⟨intensity:[0.0-1.0|lux|lumens]⟩
  ⟨color_temperature:[1000K-10000K]⟩
  ⟨quality:hard|soft|diffused⟩
  ⟨direction:[angle_degrees]⟩
  ⟨spread:[narrow|medium|wide|flood]⟩
  ⟨falloff:[inverse_square|linear|none]⟩
  ⟨shadows:sharp|soft|none⟩
  ⟨motivation:natural|artificial|practical|motivated⟩
```

### Three-Point Lighting Foundation

```
⟨THREE_POINT_LIGHTING⟩
  ⟨key_light⟩
    ⟨purpose:primary_illumination⟩
    ⟨intensity:brightest_source⟩
    ⟨position:30-45_degrees_horizontal, 30-45_degrees_vertical⟩
    ⟨quality:typically_hard_or_medium⟩
  
  ⟨fill_light⟩
    ⟨purpose:shadow_reduction⟩
    ⟨intensity:30-50%_of_key⟩
    ⟨position:opposite_side_of_key⟩
    ⟨quality:soft_diffused⟩
  
  ⟨back_light⟩
    ⟨purpose:separation_from_background⟩
    ⟨intensity:equal_to_or_brighter_than_key⟩
    ⟨position:behind_subject_elevated⟩
    ⟨quality:hard_focused⟩
```

---

## Light Source Types

### 001. NATURAL SUNLIGHT
```
⟨LIGHT_001:NATURAL_SUNLIGHT⟩
  ⟨source:sun⟩
  ⟨color_temperature:5500-6500K⟩
  ⟨quality:hard_parallel_rays⟩
  ⟨intensity:very_high⟩
  ⟨shadows:sharp_defined⟩
  ⟨direction:time_of_day_dependent⟩
  ⟨variation:clear_sky|through_clouds|through_trees⟩
  ⟨use_case:outdoor_natural_realism⟩
```

### 002. OVERCAST DAYLIGHT
```
⟨LIGHT_002:OVERCAST_DAYLIGHT⟩
  ⟨source:cloud_diffused_sun⟩
  ⟨color_temperature:6500-7500K⟩
  ⟨quality:extremely_soft_omnidirectional⟩
  ⟨intensity:medium⟩
  ⟨shadows:minimal_to_none⟩
  ⟨direction:dome_light_from_sky⟩
  ⟨use_case:even_flattering_outdoor⟩
```

### 003. GOLDEN HOUR SUNLIGHT
```
⟨LIGHT_003:GOLDEN_HOUR⟩
  ⟨source:low_angle_sun⟩
  ⟨color_temperature:2500-3500K⟩
  ⟨quality:soft_warm⟩
  ⟨intensity:medium⟩
  ⟨direction:horizontal_low_angle⟩
  ⟨color:warm_amber_golden⟩
  ⟨shadows:long_soft⟩
  ⟨use_case:romantic_beautiful_warm⟩
  ⟨timing:hour_after_sunrise_or_before_sunset⟩
```

### 004. BLUE HOUR
```
⟨LIGHT_004:BLUE_HOUR⟩
  ⟨source:indirect_twilight⟩
  ⟨color_temperature:9000-12000K⟩
  ⟨quality:soft_diffused⟩
  ⟨intensity:low⟩
  ⟨color:deep_blue⟩
  ⟨shadows:minimal⟩
  ⟨use_case:moody_mysterious_cinematic⟩
  ⟨timing:30_minutes_before_sunrise_or_after_sunset⟩
```

### 005. MOONLIGHT
```
⟨LIGHT_005:MOONLIGHT⟩
  ⟨source:moon_reflected_sunlight⟩
  ⟨color_temperature:4000-4500K⟩
  ⟨color_perception:blue_in_cinema_convention⟩
  ⟨quality:soft_directional⟩
  ⟨intensity:very_low⟩
  ⟨shadows:soft_subtle⟩
  ⟨use_case:night_exterior_romantic⟩
  ⟨note:often_enhanced_cinematically⟩
```

### 006. TUNGSTEN (INCANDESCENT)
```
⟨LIGHT_006:TUNGSTEN⟩
  ⟨source:filament_bulb⟩
  ⟨color_temperature:2700-3200K⟩
  ⟨quality:depends_on_modifier⟩
  ⟨color:warm_orange_amber⟩
  ⟨intensity:variable⟩
  ⟨use_case:warm_interior_practical⟩
  ⟨common_in:household_lamps, practical_lighting⟩
```

### 007. FLUORESCENT
```
⟨LIGHT_007:FLUORESCENT⟩
  ⟨source:gas_discharge_tube⟩
  ⟨color_temperature:3500-6500K⟩
  ⟨quality:soft_diffused⟩
  ⟨color:often_greenish_tint⟩
  ⟨intensity:medium⟩
  ⟨shadows:soft⟩
  ⟨use_case:office_institutional_sterile⟩
  ⟨emotional_quality:clinical_cold_corporate⟩
```

### 008. LED (MODERN)
```
⟨LIGHT_008:LED⟩
  ⟨source:light_emitting_diode⟩
  ⟨color_temperature:2700-6500K_adjustable⟩
  ⟨quality:depends_on_design⟩
  ⟨intensity:variable⟩
  ⟨color:full_spectrum_possible⟩
  ⟨use_case:modern_flexible_efficient⟩
  ⟨advantage:rgb_color_control⟩
```

### 009. FIRE / FLAME
```
⟨LIGHT_009:FIRE⟩
  ⟨source:combustion⟩
  ⟨color_temperature:1800-2200K⟩
  ⟨quality:flickering_dynamic⟩
  ⟨color:orange_yellow_red⟩
  ⟨intensity:low_to_medium⟩
  ⟨movement:constant_flicker⟩
  ⟨shadows:dancing_shifting⟩
  ⟨use_case:primal_intimate_dramatic⟩
```

### 010. CANDLELIGHT
```
⟨LIGHT_010:CANDLELIGHT⟩
  ⟨source:candle_flame⟩
  ⟨color_temperature:1800-2000K⟩
  ⟨quality:soft_flickering⟩
  ⟨intensity:very_low⟩
  ⟨color:warm_amber_orange⟩
  ⟨falloff:rapid⟩
  ⟨use_case:intimate_romantic_historical⟩
  ⟨emotional_quality:romantic_vulnerable_antiquated⟩
```

### 011. NEON / FLUORESCENT SIGNAGE
```
⟨LIGHT_011:NEON⟩
  ⟨source:neon_gas_tubes⟩
  ⟨color:saturated_pure_hues⟩
  ⟨quality:soft_glow⟩
  ⟨intensity:medium⟩
  ⟨colors:red|blue|green|pink|custom⟩
  ⟨use_case:urban_noir_cyberpunk⟩
  ⟨emotional_quality:electric_artificial_nocturnal⟩
```

### 012. SCREEN / MONITOR GLOW
```
⟨LIGHT_012:SCREEN_GLOW⟩
  ⟨source:digital_display⟩
  ⟨color_temperature:6500K_or_colored⟩
  ⟨quality:soft_frontal⟩
  ⟨intensity:low_to_medium⟩
  ⟨falloff:rapid⟩
  ⟨flicker:optional_subtle⟩
  ⟨use_case:modern_technology_isolation⟩
  ⟨emotional_quality:isolated_technological_modern⟩
```

### 013. LIGHTNING
```
⟨LIGHT_013:LIGHTNING⟩
  ⟨source:electrical_discharge⟩
  ⟨color_temperature:20000K+⟩
  ⟨quality:harsh_instantaneous⟩
  ⟨intensity:extreme⟩
  ⟨duration:fraction_of_second⟩
  ⟨color:blue_white⟩
  ⟨use_case:storm_drama_horror⟩
  ⟨emotional_quality:dramatic_shocking_powerful⟩
```

### 014. CAR HEADLIGHTS
```
⟨LIGHT_014:HEADLIGHTS⟩
  ⟨source:vehicle_headlamps⟩
  ⟨color_temperature:4300-6000K⟩
  ⟨quality:hard_focused_beam⟩
  ⟨intensity:high⟩
  ⟨pattern:dual_beams_converging⟩
  ⟨shadows:sharp⟩
  ⟨use_case:night_urban_drama⟩
```

### 015. STREETLIGHT / SODIUM VAPOR
```
⟨LIGHT_015:STREETLIGHT⟩
  ⟨source:high_pressure_sodium⟩
  ⟨color_temperature:2000-2200K⟩
  ⟨color:orange_amber⟩
  ⟨quality:soft_overhead⟩
  ⟨intensity:medium⟩
  ⟨pattern:pools_of_light⟩
  ⟨use_case:urban_night_noir⟩
  ⟨emotional_quality:urban_nocturnal_solitary⟩
```

---

## Classic Lighting Setups

### 016. REMBRANDT LIGHTING
```
⟨SETUP_016:REMBRANDT⟩
  ⟨key_light_position:45_degrees_horizontal, 45_degrees_vertical⟩
  ⟨signature:triangle_of_light_under_shadow_side_eye⟩
  ⟨shadow_side:half_face_in_shadow⟩
  ⟨quality:dramatic_painterly⟩
  ⟨ratio:high_contrast⟩
  ⟨use_case:portraits, dramatic, classical⟩
  ⟨emotional_quality:dignified, contemplative, serious⟩
  ⟨film_reference:classical_portraiture⟩
```

### 017. LOOP LIGHTING
```
⟨SETUP_017:LOOP_LIGHTING⟩
  ⟨key_light_position:30-45_degrees_horizontal, slightly_elevated⟩
  ⟨signature:small_shadow_loop_under_nose⟩
  ⟨shadow:minimal_nose_shadow⟩
  ⟨quality:flattering_natural⟩
  ⟨use_case:standard_portrait, commercial⟩
  ⟨emotional_quality:approachable, natural, clean⟩
```

### 018. BUTTERFLY (PARAMOUNT) LIGHTING
```
⟨SETUP_018:BUTTERFLY⟩
  ⟨key_light_position:directly_in_front_above⟩
  ⟨signature:butterfly_shadow_under_nose⟩
  ⟨cheekbones:emphasized⟩
  ⟨quality:glamorous_sculptural⟩
  ⟨use_case:beauty, fashion, glamour⟩
  ⟨emotional_quality:elegant, beautiful, classic⟩
  ⟨film_reference:Old_Hollywood, Paramount_Pictures⟩
```

### 019. SPLIT LIGHTING
```
⟨SETUP_019:SPLIT_LIGHTING⟩
  ⟨key_light_position:90_degrees_to_side⟩
  ⟨signature:half_face_lit_half_shadow⟩
  ⟨dramatic_split:precise_center_divide⟩
  ⟨quality:dramatic_stark⟩
  ⟨use_case:dramatic_portraits, mystery⟩
  ⟨emotional_quality:mysterious, divided, dramatic⟩
```

### 020. BROAD LIGHTING
```
⟨SETUP_020:BROAD_LIGHTING⟩
  ⟨key_light:illuminates_side_of_face_toward_camera⟩
  ⟨effect:wider_face_appearance⟩
  ⟨shadow_side:away_from_camera⟩
  ⟨use_case:narrow_faces, commercial⟩
```

### 021. SHORT LIGHTING
```
⟨SETUP_021:SHORT_LIGHTING⟩
  ⟨key_light:illuminates_side_of_face_away_from_camera⟩
  ⟨effect:slimming_sculptural⟩
  ⟨shadow_side:toward_camera⟩
  ⟨use_case:most_portraits, slimming, dramatic⟩
  ⟨emotional_quality:sculptural, dimensional, flattering⟩
```

### 022. FLAT LIGHTING (BEAUTY LIGHTING)
```
⟨SETUP_022:FLAT_LIGHTING⟩
  ⟨technique:frontal_soft_source_or_ring_light⟩
  ⟨shadows:minimal_to_none⟩
  ⟨quality:even_shadowless⟩
  ⟨use_case:beauty, commercial, blemish_minimization⟩
  ⟨emotional_quality:clean, perfect, commercial⟩
```

### 023. HIGH KEY LIGHTING
```
⟨SETUP_023:HIGH_KEY⟩
  ⟨overall_tone:bright_minimal_shadows⟩
  ⟨lighting_ratio:low_1:2_or_1:3⟩
  ⟨fill_level:high⟩
  ⟨background:bright⟩
  ⟨mood:upbeat_optimistic⟩
  ⟨use_case:comedy, commercial, sitcom⟩
  ⟨emotional_quality:happy, light, optimistic⟩
```

### 024. LOW KEY LIGHTING
```
⟨SETUP_024:LOW_KEY⟩
  ⟨overall_tone:dark_predominant_shadows⟩
  ⟨lighting_ratio:high_1:8_or_greater⟩
  ⟨fill_level:minimal_or_none⟩
  ⟨background:dark⟩
  ⟨mood:dramatic_mysterious⟩
  ⟨use_case:noir, thriller, horror, drama⟩
  ⟨emotional_quality:mysterious, threatening, dramatic⟩
```

### 025. CHIAROSCURO
```
⟨SETUP_025:CHIAROSCURO⟩
  ⟨technique:extreme_light_dark_contrast⟩
  ⟨shadows:deep_rich_blacks⟩
  ⟨highlights:bright_selective⟩
  ⟨inspiration:Caravaggio_painting⟩
  ⟨use_case:dramatic, artistic, period⟩
  ⟨emotional_quality:dramatic, painterly, classical⟩
  ⟨film_reference:Godfather, Blade_Runner⟩
```

---

## Light Quality

### 026. HARD LIGHT
```
⟨QUALITY_026:HARD_LIGHT⟩
  ⟨source:small_focused_unmodified⟩
  ⟨shadows:sharp_defined_edges⟩
  ⟨contrast:high⟩
  ⟨texture:emphasized⟩
  ⟨examples:direct_sun, fresnel, focused_spot⟩
  ⟨use_case:drama, texture, sculpting⟩
  ⟨emotional_quality:harsh, dramatic, unforgiving⟩
```

### 027. SOFT LIGHT
```
⟨QUALITY_027:SOFT_LIGHT⟩
  ⟨source:large_diffused⟩
  ⟨shadows:soft_gradual_edges⟩
  ⟨contrast:low⟩
  ⟨texture:minimized⟩
  ⟨examples:overcast_sky, softbox, bounce⟩
  ⟨use_case:beauty, flattering, commercial⟩
  ⟨emotional_quality:gentle, flattering, beautiful⟩
```

### 028. DIFFUSED LIGHT
```
⟨QUALITY_028:DIFFUSED⟩
  ⟨technique:light_through_translucent_material⟩
  ⟨quality:scattered_omnidirectional⟩
  ⟨shadows:very_soft_to_none⟩
  ⟨examples:through_curtains, silk, clouds⟩
  ⟨use_case:natural_looking, gentle⟩
```

### 029. SPECULAR LIGHT
```
⟨QUALITY_029:SPECULAR⟩
  ⟨reflection:direct_mirror_like⟩
  ⟨highlights:bright_sharp_points⟩
  ⟨examples:water, metal, glass⟩
  ⟨use_case:emphasis, jewelry, eyes⟩
```

### 030. BOUNCED LIGHT
```
⟨QUALITY_030:BOUNCED⟩
  ⟨technique:light_reflected_off_surface⟩
  ⟨quality:soft_indirect⟩
  ⟨color:picks_up_surface_color⟩
  ⟨examples:off_ceiling, white_card, reflector⟩
  ⟨use_case:fill, natural_looking, gentle⟩
```

---

## Color Temperature & Color Contrast

### 031. WARM LIGHT (LOW KELVIN)
```
⟨TEMPERATURE_031:WARM⟩
  ⟨kelvin:2000-3500K⟩
  ⟨color:orange_amber_yellow⟩
  ⟨sources:tungsten, fire, golden_hour⟩
  ⟨mood:cozy_intimate_nostalgic⟩
  ⟨use_case:interiors, romance, comfort⟩
  ⟨emotional_quality:warm, inviting, comfortable⟩
```

### 032. NEUTRAL LIGHT (DAYLIGHT)
```
⟨TEMPERATURE_032:NEUTRAL⟩
  ⟨kelvin:5000-6500K⟩
  ⟨color:white_balanced⟩
  ⟨sources:midday_sun, balanced_LED⟩
  ⟨mood:natural_realistic⟩
  ⟨use_case:natural_realistic_standard⟩
```

### 033. COOL LIGHT (HIGH KELVIN)
```
⟨TEMPERATURE_033:COOL⟩
  ⟨kelvin:7000-10000K⟩
  ⟨color:blue_cyan⟩
  ⟨sources:overcast_sky, moonlight_convention, blue_hour⟩
  ⟨mood:cold_clinical_mysterious⟩
  ⟨use_case:night_clinical_isolation⟩
  ⟨emotional_quality:cold, isolated, mysterious⟩
```

### 034. MIXED COLOR TEMPERATURE
```
⟨TEMPERATURE_034:MIXED⟩
  ⟨technique:warm_and_cool_sources_together⟩
  ⟨contrast:color_temperature_opposition⟩
  ⟨example:warm_interior_cool_exterior⟩
  ⟨use_case:depth, visual_interest, realism⟩
  ⟨emotional_quality:complex, layered, realistic⟩
```

### 035. ORANGE AND TEAL
```
⟨TEMPERATURE_035:ORANGE_TEAL⟩
  ⟨technique:warm_subjects_cool_shadows⟩
  ⟨color_grading:complementary_contrast⟩
  ⟨saturation:often_enhanced⟩
  ⟨use_case:modern_blockbuster_look⟩
  ⟨emotional_quality:cinematic, polished, commercial⟩
  ⟨film_reference:Michael_Bay, modern_action⟩
```

---

## Directional Lighting

### 036. FRONT LIGHTING
```
⟨DIRECTION_036:FRONT⟩
  ⟨angle:0-30_degrees_from_camera_axis⟩
  ⟨shadows:minimal_behind_subject⟩
  ⟨depth:flattened⟩
  ⟨use_case:beauty, flat, direct⟩
  ⟨emotional_quality:direct, confrontational, open⟩
```

### 037. SIDE LIGHTING (90 DEGREES)
```
⟨DIRECTION_037:SIDE⟩
  ⟨angle:90_degrees_from_camera⟩
  ⟨shadows:half_subject_in_shadow⟩
  ⟨texture:maximum_emphasis⟩
  ⟨depth:strong_dimensionality⟩
  ⟨use_case:dramatic, texture, sculpture⟩
  ⟨emotional_quality:dramatic, divided, sculptural⟩
```

### 038. BACK LIGHTING (RIM LIGHTING)
```
⟨DIRECTION_038:BACK⟩
  ⟨angle:180_degrees_from_camera⟩
  ⟨effect:glowing_edge_around_subject⟩
  ⟨front:often_silhouetted_or_requires_fill⟩
  ⟨use_case:separation, halo, ethereal⟩
  ⟨emotional_quality:angelic, separated, transcendent⟩
```

### 039. TOP LIGHTING
```
⟨DIRECTION_039:TOP⟩
  ⟨angle:directly_above⟩
  ⟨shadows:under_eyes_nose_chin⟩
  ⟨effect:sinister_unnatural⟩
  ⟨use_case:horror, villain, supernatural⟩
  ⟨emotional_quality:ominous, unnatural, threatening⟩
```

### 040. UNDER LIGHTING
```
⟨DIRECTION_040:UNDER⟩
  ⟨angle:from_below⟩
  ⟨effect:unnatural_spooky⟩
  ⟨shadows:reversed_upward⟩
  ⟨use_case:horror, campfire_stories, villain⟩
  ⟨emotional_quality:creepy, unnatural, ominous⟩
  ⟨reference:flashlight_under_chin⟩
```

### 041. KICKER LIGHT
```
⟨DIRECTION_041:KICKER⟩
  ⟨position:behind_and_to_side⟩
  ⟨angle:135_degrees_from_camera⟩
  ⟨effect:edge_highlight_one_side⟩
  ⟨use_case:separation, dimension, accent⟩
```

### 042. HAIR LIGHT
```
⟨DIRECTION_042:HAIR_LIGHT⟩
  ⟨position:above_and_behind⟩
  ⟨target:hair_and_shoulders⟩
  ⟨effect:highlights_hair_separation⟩
  ⟨use_case:separation, glamour, definition⟩
```

---

## Time of Day Lighting

### 043. SUNRISE (EARLY MORNING)
```
⟨TIME_043:SUNRISE⟩
  ⟨sun_position:low_angle_horizon⟩
  ⟨color_temperature:3500-4500K⟩
  ⟨color:warm_pink_orange⟩
  ⟨quality:soft_hazy⟩
  ⟨shadows:long_soft⟩
  ⟨atmosphere:dew_mist_possible⟩
  ⟨mood:hopeful, new_beginning, fresh⟩
  ⟨use_case:beginning, hope, romance⟩
```

### 044. MORNING (MID-MORNING)
```
⟨TIME_044:MORNING⟩
  ⟨sun_position:elevated_30-50_degrees⟩
  ⟨color_temperature:5000-5500K⟩
  ⟨quality:clear_crisp⟩
  ⟨shadows:defined_moderate_length⟩
  ⟨mood:energetic, active, clear⟩
  ⟨use_case:active_scenes, energy⟩
```

### 045. NOON (MIDDAY)
```
⟨TIME_045:NOON⟩
  ⟨sun_position:overhead_80-90_degrees⟩
  ⟨color_temperature:5500-6500K⟩
  ⟨quality:harsh_direct⟩
  ⟨shadows:short_dark_under_features⟩
  ⟨mood:harsh_unflattering⟩
  ⟨use_case:realism, harsh_conditions⟩
  ⟨note:generally_avoided_for_beauty⟩
```

### 046. AFTERNOON
```
⟨TIME_046:AFTERNOON⟩
  ⟨sun_position:descending_40-60_degrees⟩
  ⟨color_temperature:4500-5500K⟩
  ⟨quality:warm_directional⟩
  ⟨shadows:lengthening⟩
  ⟨mood:warm_comfortable⟩
  ⟨use_case:standard_outdoor⟩
```

### 047. GOLDEN HOUR (MAGIC HOUR)
```
⟨TIME_047:GOLDEN_HOUR⟩
  ⟨sun_position:near_horizon_0-10_degrees⟩
  ⟨color_temperature:2500-3500K⟩
  ⟨color:golden_amber_warm⟩
  ⟨quality:soft_magical⟩
  ⟨shadows:long_flattering⟩
  ⟨mood:romantic, beautiful, magical⟩
  ⟨use_case:romance, beauty, cinematic⟩
  ⟨emotional_quality:nostalgic, beautiful, precious⟩
```

### 048. DUSK (TWILIGHT)
```
⟨TIME_048:DUSK⟩
  ⟨sun_position:below_horizon⟩
  ⟨color_temperature:7000-9000K⟩
  ⟨color:purple_blue_orange_gradient⟩
  ⟨quality:soft_fading⟩
  ⟨mood:transitional, melancholic⟩
  ⟨use_case:transition, endings, reflection⟩
```

### 049. BLUE HOUR
```
⟨TIME_049:BLUE_HOUR⟩
  ⟨sun_position:6-15_degrees_below_horizon⟩
  ⟨color_temperature:9000-12000K⟩
  ⟨color:deep_saturated_blue⟩
  ⟨quality:soft_even⟩
  ⟨mood:mysterious, moody, cinematic⟩
  ⟨use_case:urban_night, moody_exterior⟩
  ⟨emotional_quality:mysterious, liminal, cinematic⟩
```

### 050. NIGHT (FULL DARK)
```
⟨TIME_050:NIGHT⟩
  ⟨natural_light:minimal_moon_stars⟩
  ⟨artificial_light:dominant⟩
  ⟨sources:streetlights, windows, signs, moon⟩
  ⟨mood:mysterious, dangerous, intimate⟩
  ⟨use_case:noir, thriller, romance⟩
  ⟨emotional_quality:mysterious, dangerous, intimate⟩
```

---

## Weather & Atmospheric Lighting

### 051. OVERCAST / CLOUDY
```
⟨WEATHER_051:OVERCAST⟩
  ⟨sky:cloud_cover_diffusion⟩
  ⟨quality:extremely_soft_omnidirectional⟩
  ⟨shadows:minimal_to_none⟩
  ⟨color:neutral_to_cool⟩
  ⟨mood:somber, even, subdued⟩
  ⟨use_case:even_lighting, drama, sadness⟩
```

### 052. FOG / MIST
```
⟨WEATHER_052:FOG⟩
  ⟨atmosphere:suspended_water_droplets⟩
  ⟨visibility:reduced⟩
  ⟨light_behavior:scattering_volumetric_beams⟩
  ⟨depth:compressed_atmospheric_perspective⟩
  ⟨mood:mysterious, isolated, ethereal⟩
  ⟨use_case:mystery, horror, atmospheric⟩
  ⟨emotional_quality:mysterious, isolated, dreamlike⟩
```

### 053. RAIN
```
⟨WEATHER_053:RAIN⟩
  ⟨atmosphere:falling_water_reflections⟩
  ⟨surfaces:wet_reflective⟩
  ⟨light:multiply_via_reflections⟩
  ⟨color:saturated_darkened⟩
  ⟨mood:melancholic, romantic, dramatic⟩
  ⟨use_case:noir, drama, romance⟩
  ⟨emotional_quality:melancholic, cleansing, romantic⟩
```

### 054. STORM
```
⟨WEATHER_054:STORM⟩
  ⟨sky:dark_turbulent_clouds⟩
  ⟨light:intermittent_dramatic⟩
  ⟨lightning:possible_intense_flashes⟩
  ⟨mood:threatening, dramatic, chaos⟩
  ⟨use_case:drama, thriller, climax⟩
  ⟨emotional_quality:threatening, powerful, chaotic⟩
```

### 055. SNOW
```
⟨WEATHER_055:SNOW⟩
  ⟨surfaces:highly_reflective_white⟩
  ⟨light:bounced_from_ground_upward⟩
  ⟨quality:bright_even_from_multiple_directions⟩
  ⟨color_temperature:cool_blue⟩
  ⟨mood:pristine, cold, peaceful⟩
  ⟨use_case:winter, purity, cold⟩
  ⟨emotional_quality:pure, cold, peaceful⟩
```

### 056. DUST / HAZE
```
⟨WEATHER_056:DUST_HAZE⟩
  ⟨atmosphere:suspended_particles⟩
  ⟨light_behavior:visible_beams_god_rays⟩
  ⟨quality:diffused_volumetric⟩
  ⟨mood:atmospheric, dramatic, otherworldly⟩
  ⟨use_case:westerns, desert, atmospheric⟩
```

### 057. SMOKE
```
⟨WEATHER_057:SMOKE⟩
  ⟨atmosphere:heavy_particulate⟩
  ⟨light_behavior:strong_scattering_beams⟩
  ⟨visibility:significantly_reduced⟩
  ⟨color:darkened_tinted⟩
  ⟨mood:danger, mystery, aftermath⟩
  ⟨use_case:action, disaster, thriller⟩
```

---

## Practical Lights (In-Scene Sources)

### 058. TABLE LAMP
```
⟨PRACTICAL_058:TABLE_LAMP⟩
  ⟨source:in_frame_visible_lamp⟩
  ⟨color_temperature:2700-3200K⟩
  ⟨quality:soft_local⟩
  ⟨intensity:low_to_medium⟩
  ⟨motivation:realistic_interior⟩
  ⟨use_case:domestic, intimate, motivated⟩
```

### 059. CEILING FIXTURE
```
⟨PRACTICAL_059:CEILING⟩
  ⟨source:overhead_visible_fixture⟩
  ⟨direction:top_down⟩
  ⟨quality:depends_on_shade⟩
  ⟨use_case:interior, realistic⟩
```

### 060. WINDOW LIGHT
```
⟨PRACTICAL_060:WINDOW⟩
  ⟨source:exterior_light_through_window⟩
  ⟨quality:soft_directional⟩
  ⟨color:time_of_day_dependent⟩
  ⟨pattern:rectangular_light_pool⟩
  ⟨use_case:natural_interior, beautiful⟩
  ⟨emotional_quality:natural, contemplative, beautiful⟩
```

### 061. DOORWAY LIGHT
```
⟨PRACTICAL_061:DOORWAY⟩
  ⟨source:adjacent_room_or_exterior⟩
  ⟨pattern:rectangular_frame_of_light⟩
  ⟨quality:dramatic_edge_lit⟩
  ⟨use_case:silhouette, entrance, drama⟩
```

### 062. FIREPLACE / HEARTH
```
⟨PRACTICAL_062:FIREPLACE⟩
  ⟨source:visible_fire_flames⟩
  ⟨color_temperature:1800-2200K⟩
  ⟨quality:flickering_warm⟩
  ⟨movement:dancing_flames⟩
  ⟨mood:cozy, intimate, primal⟩
  ⟨use_case:intimate, historical, comfort⟩
```

### 063. CHRISTMAS LIGHTS / STRING LIGHTS
```
⟨PRACTICAL_063:STRING_LIGHTS⟩
  ⟨source:visible_decorative_bulbs⟩
  ⟨color:warm_or_multicolored⟩
  ⟨pattern:multiple_point_sources⟩
  ⟨quality:soft_bokeh⟩
  ⟨mood:festive, romantic, nostalgic⟩
  ⟨use_case:holidays, romance, whimsy⟩
```

### 064. REFRIGERATOR LIGHT
```
⟨PRACTICAL_064:REFRIGERATOR⟩
  ⟨source:interior_fridge_light⟩
  ⟨color_temperature:5000-6500K⟩
  ⟨quality:cool_frontal⟩
  ⟨context:night_scene_face_lit⟩
  ⟨mood:isolated, late_night, vulnerable⟩
  ⟨use_case:night_scene, isolation, realism⟩
```

### 065. FLASHLIGHT / TORCH
```
⟨PRACTICAL_065:FLASHLIGHT⟩
  ⟨source:handheld_beam⟩
  ⟨quality:focused_beam_hard_edge⟩
  ⟨movement:motivated_by_character⟩
  ⟨use_case:thriller, search, night⟩
  ⟨emotional_quality:searching, tense, limited_visibility⟩
```

### 066. LIGHTER FLAME
```
⟨PRACTICAL_066:LIGHTER⟩
  ⟨source:small_flame⟩
  ⟨color_temperature:1800K⟩
  ⟨quality:flickering_dramatic⟩
  ⟨falloff:extreme_rapid⟩
  ⟨use_case:close_up, intimate, dramatic⟩
```

---

## Motivated Lighting (Justified Sources)

### 067. MOTIVATED BY SUN
```
⟨MOTIVATED_067:SUN⟩
  ⟨justification:visible_sun_or_window⟩
  ⟨direction:consistent_with_sun_position⟩
  ⟨quality:matches_time_of_day⟩
  ⟨realism:high⟩
```

### 068. MOTIVATED BY FIRE
```
⟨MOTIVATED_068:FIRE⟩
  ⟨justification:visible_flame_fireplace_candle⟩
  ⟨color:warm_orange_flickering⟩
  ⟨movement:dancing_organic⟩
  ⟨realism:requires_flicker⟩
```

### 069. MOTIVATED BY TV/SCREEN
```
⟨MOTIVATED_069:SCREEN⟩
  ⟨justification:visible_monitor_TV⟩
  ⟨color:typically_blue_white⟩
  ⟨flicker:optional_subtle⟩
  ⟨direction:frontal_from_screen⟩
```

### 070. MOTIVATED BY CAR
```
⟨MOTIVATED_070:CAR⟩
  ⟨justification:vehicle_headlights_or_interior⟩
  ⟨headlights:dual_beams_cool_white⟩
  ⟨dashboard:warm_glow_soft⟩
  ⟨movement:possible_if_driving⟩
```

### 071. MOTIVATED BY NEON SIGN
```
⟨MOTIVATED_071:NEON_SIGN⟩
  ⟨justification:visible_neon_signage⟩
  ⟨color:saturated_hue_from_sign⟩
  ⟨quality:soft_glow⟩
  ⟨context:urban_night⟩
```

### 072. MOTIVATED BY LIGHTNING
```
⟨MOTIVATED_072:LIGHTNING⟩
  ⟨justification:storm_exterior⟩
  ⟨quality:instantaneous_bright_flash⟩
  ⟨color:blue_white⟩
  ⟨duration:fraction_of_second⟩
  ⟨timing:irregular⟩
```

---

## Stylized Lighting (Genre-Specific)

### 073. FILM NOIR
```
⟨STYLE_073:FILM_NOIR⟩
  ⟨technique:low_key_high_contrast⟩
  ⟨shadows:deep_dramatic_venetian_blinds⟩
  ⟨sources:hard_single_source⟩
  ⟨patterns:slats_bars_geometric_shadows⟩
  ⟨mood:cynical_fatalistic_dangerous⟩
  ⟨use_case:thriller, crime, mystery⟩
  ⟨film_reference:The_Third_Man, Double_Indemnity⟩
```

### 074. HORROR LIGHTING
```
⟨STYLE_074:HORROR⟩
  ⟨technique:low_key_unnatural_angles⟩
  ⟨sources:under_lighting_top_lighting⟩
  ⟨color:often_desaturated_or_green_tint⟩
  ⟨shadows:threatening_obscuring⟩
  ⟨mood:threatening_ominous_supernatural⟩
  ⟨use_case:horror, supernatural, fear⟩
```

### 075. ROMANTIC LIGHTING
```
⟨STYLE_075:ROMANTIC⟩
  ⟨technique:soft_warm_flattering⟩
  ⟨sources:candles_firelight_golden_hour⟩
  ⟨quality:diffused_glowing⟩
  ⟨color:warm_amber_golden⟩
  ⟨mood:intimate_tender_beautiful⟩
  ⟨use_case:romance, intimacy, love_scenes⟩
```

### 076. SCI-FI LIGHTING
```
⟨STYLE_076:SCI_FI⟩
  ⟨technique:cool_tones_artificial⟩
  ⟨sources:LED_panels_screens_futuristic⟩
  ⟨color:blue_cyan_white⟩
  ⟨quality:clean_crisp_technological⟩
  ⟨mood:futuristic_clinical_alien⟩
  ⟨use_case:science_fiction, technology, future⟩
```

### 077. CYBERPUNK
```
⟨STYLE_077:CYBERPUNK⟩
  ⟨technique:neon_urban_mixed_sources⟩
  ⟨color:saturated_pink_cyan_purple⟩
  ⟨sources:neon_signs_holograms_screens⟩
  ⟨quality:artificial_electric⟩
  ⟨mood:dystopian_nocturnal_electric⟩
  ⟨use_case:cyberpunk, urban_future, noir_future⟩
  ⟨film_reference:Blade_Runner, Ghost_in_the_Shell⟩
```

### 078. WESTERN / PERIOD
```
⟨STYLE_078:WESTERN⟩
  ⟨technique:natural_harsh_sun⟩
  ⟨quality:dusty_atmospheric⟩
  ⟨time:often_golden_hour_or_harsh_noon⟩
  ⟨mood:rugged_isolated_timeless⟩
  ⟨use_case:westerns, period, adventure⟩
```

### 079. FANTASY / MAGICAL
```
⟨STYLE_079:FANTASY⟩
  ⟨technique:ethereal_glowing_sources⟩
  ⟨color:often_saturated_unnatural⟩
  ⟨quality:soft_magical_glowing⟩
  ⟨sources:magical_fires_crystals_enchanted⟩
  ⟨mood:wondrous_otherworldly_magical⟩
  ⟨use_case:fantasy, magic, fairy_tale⟩
```

### 080. MUSIC VIDEO
```
⟨STYLE_080:MUSIC_VIDEO⟩
  ⟨technique:bold_dynamic_changing⟩
  ⟨color:saturated_contrasting_dramatic⟩
  ⟨movement:often_changing_with_beat⟩
  ⟨style:expressive_not_naturalistic⟩
  ⟨mood:energetic_artistic_expressive⟩
  ⟨use_case:music_video, performance, stylized⟩
```

---

## Lighting Ratios

### 081. 1:1 RATIO (NO CONTRAST)
```
⟨RATIO_081:1_TO_1⟩
  ⟨key_to_fill:equal_intensity⟩
  ⟨shadows:none⟩
  ⟨mood:flat_even⟩
  ⟨use_case:beauty, commercial, minimizing_texture⟩
```

### 082. 2:1 RATIO (LOW CONTRAST)
```
⟨RATIO_082:2_TO_1⟩
  ⟨key_to_fill:key_twice_as_bright⟩
  ⟨shadows:subtle_visible⟩
  ⟨mood:natural_gentle⟩
  ⟨use_case:standard_commercial, gentle_modeling⟩
```

### 083. 4:1 RATIO (MEDIUM CONTRAST)
```
⟨RATIO_083:4_TO_1⟩
  ⟨key_to_fill:key_four_times_brighter⟩
  ⟨shadows:defined_moderate⟩
  ⟨mood:dramatic_visible_dimension⟩
  ⟨use_case:standard_dramatic_portrait⟩
```

### 084. 8:1 RATIO (HIGH CONTRAST)
```
⟨RATIO_084:8_TO_1⟩
  ⟨key_to_fill:key_eight_times_brighter⟩
  ⟨shadows:deep_dark⟩
  ⟨mood:very_dramatic_noir⟩
  ⟨use_case:noir, thriller, dramatic⟩
```

### 085. NO FILL (INFINITE RATIO)
```
⟨RATIO_085:NO_FILL⟩
  ⟨fill_light:absent⟩
  ⟨shadows:pure_black⟩
  ⟨contrast:extreme⟩
  ⟨mood:stark_graphic_extreme⟩
  ⟨use_case:silhouette, extreme_drama⟩
```

---

## Special Lighting Effects

### 086. VOLUMETRIC LIGHTING (GOD RAYS)
```
⟨EFFECT_086:VOLUMETRIC⟩
  ⟨technique:light_beams_visible_through_atmosphere⟩
  ⟨atmosphere:fog_dust_smoke_required⟩
  ⟨appearance:shafts_of_light_visible⟩
  ⟨mood:ethereal_dramatic_spiritual⟩
  ⟨use_case:churches, forests, atmospheric⟩
  ⟨emotional_quality:divine, atmospheric, dramatic⟩
```

### 087. LENS FLARE
```
⟨EFFECT_087:LENS_FLARE⟩
  ⟨cause:bright_light_source_toward_camera⟩
  ⟨appearance:geometric_artifacts_hexagons⟩
  ⟨style:naturalistic|J.J.Abrams_excessive⟩
  ⟨mood:authentic_bright_energetic⟩
  ⟨use_case:sun_shots, authenticity, style⟩
```

### 088. SILHOUETTE
```
⟨EFFECT_088:SILHOUETTE⟩
  ⟨technique:subject_between_camera_and_bright_source⟩
  ⟨subject:completely_dark_no_detail⟩
  ⟨background:bright⟩
  ⟨mood:mysterious_iconic_dramatic⟩
  ⟨use_case:mystery, iconic_poses, drama⟩
  ⟨emotional_quality:mysterious, iconic, dramatic⟩
```

### 089. PRACTICAL BLOOM / GLOW
```
⟨EFFECT_089:BLOOM⟩
  ⟨appearance:bright_sources_glow_beyond_boundaries⟩
  ⟨cause:lens_halation_or_post⟩
  ⟨mood:ethereal_dreamlike_soft⟩
  ⟨use_case:romance, dreams, softness⟩
```

### 090. SHADOW PATTERNS
```
⟨EFFECT_090:SHADOW_PATTERNS⟩
  ⟨technique:light_through_objects_casting_patterns⟩
  ⟨sources:venetian_blinds, leaves, bars, lattice⟩
  ⟨mood:dramatic, noir, textured⟩
  ⟨use_case:noir, drama, visual_interest⟩
  ⟨film_reference:Film_Noir_aesthetic⟩
```

### 091. COLORED GELS
```
⟨EFFECT_091:COLORED_GELS⟩
  ⟨technique:colored_filters_on_lights⟩
  ⟨effect:non_realistic_color_wash⟩
  ⟨use_case:music_video, stylized, clubs⟩
  ⟨mood:artificial_expressive_stylized⟩
```

### 092. PRACTICAL SMOKE / HAZE
```
⟨EFFECT_092:HAZE⟩
  ⟨technique:smoke_or_haze_in_air⟩
  ⟨effect:visible_light_beams_atmosphere⟩
  ⟨mood:atmospheric_concert_mysterious⟩
  ⟨use_case:concerts, clubs, atmosphere⟩
```

### 093. MOVING LIGHTS / SCANNING
```
⟨EFFECT_093:MOVING_LIGHTS⟩
  ⟨technique:lights_that_move_or_scan⟩
  ⟨sources:searchlights, moving_heads, police_lights⟩
  ⟨mood:dynamic, club, emergency⟩
  ⟨use_case:clubs, emergencies, action⟩
```

### 094. LIGHTNING FLASH
```
⟨EFFECT_094:LIGHTNING⟩
  ⟨duration:instantaneous_flash⟩
  ⟨intensity:extreme_brief⟩
  ⟨color:blue_white⟩
  ⟨timing:unpredictable_dramatic⟩
  ⟨use_case:storm, drama, shock⟩
```

### 095. FIRELIGHT FLICKER
```
⟨EFFECT_095:FLICKER⟩
  ⟨technique:simulated_flame_movement⟩
  ⟨pattern:organic_dancing⟩
  ⟨color:warm_orange_amber⟩
  ⟨use_case:firelight, candlelight, campfire⟩
```

---

## Environment-Specific Lighting

### 096. INTERIOR DAY (WINDOW LIT)
```
⟨ENVIRONMENT_096:INTERIOR_DAY_WINDOW⟩
  ⟨primary_source:window_light⟩
  ⟨quality:soft_directional⟩
  ⟨contrast:moderate_falloff⟩
  ⟨color:neutral_to_warm⟩
  ⟨mood:natural_intimate_realistic⟩
```

### 097. INTERIOR NIGHT (PRACTICALS)
```
⟨ENVIRONMENT_097:INTERIOR_NIGHT⟩
  ⟨primary_source:lamps_fixtures_practicals⟩
  ⟨quality:warm_localized⟩
  ⟨contrast:pools_of_light_dark_shadows⟩
  ⟨color:warm_amber⟩
  ⟨mood:intimate_cozy_mysterious⟩
```

### 098. EXTERIOR DAY (SUN)
```
⟨ENVIRONMENT_098:EXTERIOR_DAY⟩
  ⟨primary_source:sun⟩
  ⟨quality:hard_or_soft_depending_on_clouds⟩
  ⟨intensity:high⟩
  ⟨color:time_of_day_dependent⟩
  ⟨mood:energetic_clear_realistic⟩
```

### 099. EXTERIOR NIGHT (URBAN)
```
⟨ENVIRONMENT_099:EXTERIOR_NIGHT_URBAN⟩
  ⟨primary_source:streetlights_signs_windows⟩
  ⟨quality:mixed_hard_and_soft⟩
  ⟨color:orange_streetlights_cool_moonlight⟩
  ⟨mood:noir_isolated_urban⟩
```

### 100. EXTERIOR NIGHT (RURAL)
```
⟨ENVIRONMENT_100:EXTERIOR_NIGHT_RURAL⟩
  ⟨primary_source:moonlight_starlight⟩
  ⟨quality:soft_very_low⟩
  ⟨color:blue_convention⟩
  ⟨mood:isolated_mysterious_vast⟩
```

### 101. CAR INTERIOR DAY
```
⟨ENVIRONMENT_101:CAR_INTERIOR_DAY⟩
  ⟨primary_source:windows_soft_indirect⟩
  ⟨quality:diffused_through_glass⟩
  ⟨challenges:changing_exterior_light⟩
  ⟨mood:intimate_confined_realistic⟩
```

### 102. CAR INTERIOR NIGHT
```
⟨ENVIRONMENT_102:CAR_INTERIOR_NIGHT⟩
  ⟨primary_source:dashboard_streetlights⟩
  ⟨dashboard:warm_soft_glow_uplight⟩
  ⟨exterior:passing_lights_scanning⟩
  ⟨mood:intimate_vulnerable_noir⟩
```

### 103. UNDERWATER
```
⟨ENVIRONMENT_103:UNDERWATER⟩
  ⟨quality:diffused_omnidirectional_soft⟩
  ⟨color:blue_green_filtered⟩
  ⟨caustics:dancing_light_patterns_on_surfaces⟩
  ⟨falloff:rapid_due_to_water_absorption⟩
  ⟨mood:otherworldly_isolated_dreamlike⟩
```

### 104. FOREST / DAPPLED LIGHT
```
⟨ENVIRONMENT_104:FOREST_DAPPLED⟩
  ⟨technique:sun_through_leaves_canopy⟩
  ⟨pattern:irregular_moving_spots⟩
  ⟨quality:mixed_hard_spots_soft_ambient⟩
  ⟨mood:natural_alive_organic⟩
```

### 105. CAVE / UNDERGROUND
```
⟨ENVIRONMENT_105:CAVE⟩
  ⟨natural_light:minimal_to_none⟩
  ⟨sources:torches_flashlights_artificial⟩
  ⟨quality:dramatic_localized⟩
  ⟨mood:claustrophobic_mysterious_primordial⟩
```

### 106. STAGE / THEATER
```
⟨ENVIRONMENT_106:STAGE⟩
  ⟨sources:theatrical_spots_follows⟩
  ⟨quality:dramatic_controlled⟩
  ⟨background:often_dark⟩
  ⟨mood:performative_dramatic_artificial⟩
```

### 107. NIGHTCLUB / BAR
```
⟨ENVIRONMENT_107:NIGHTCLUB⟩
  ⟨sources:colored_gels_moving_lights_practicals⟩
  ⟨color:saturated_changing⟩
  ⟨quality:hazy_atmospheric⟩
  ⟨mood:energetic_nocturnal_artificial⟩
```

### 108. HOSPITAL / CLINICAL
```
⟨ENVIRONMENT_108:HOSPITAL⟩
  ⟨sources:fluorescent_overhead_harsh⟩
  ⟨quality:flat_even_bright⟩
  ⟨color:cool_white_greenish⟩
  ⟨mood:clinical_sterile_cold⟩
  ⟨emotional_quality:anxiety_sterile_institutional⟩
```

### 109. CHURCH / CATHEDRAL
```
⟨ENVIRONMENT_109:CHURCH⟩
  ⟨sources:windows_stained_glass_candles⟩
  ⟨quality:dramatic_volumetric_reverent⟩
  ⟨color:stained_glass_colors_warm_candles⟩
  ⟨mood:spiritual_reverent_solemn⟩
  ⟨emotional_quality:spiritual_transcendent_sacred⟩
```

### 110. WAREHOUSE / INDUSTRIAL
```
⟨ENVIRONMENT_110:WAREHOUSE⟩
  ⟨sources:high_bay_lights_windows_gaps⟩
  ⟨quality:harsh_mixed_dusty⟩
  ⟨atmosphere:often_dusty_hazy⟩
  ⟨mood:gritty_stark_utilitarian⟩
```

---

## Advanced Lighting Techniques

### 111. NEGATIVE FILL
```
⟨TECHNIQUE_111:NEGATIVE_FILL⟩
  ⟨method:black_flags_absorbing_light⟩
  ⟨purpose:deepen_shadows_increase_contrast⟩
  ⟨use_case:drama, noir, sculpting⟩
```

### 112. BOUNCE CARD
```
⟨TECHNIQUE_112:BOUNCE_CARD⟩
  ⟨method:white_reflector_redirecting_light⟩
  ⟨effect:soft_fill_natural_looking⟩
  ⟨use_case:outdoor_natural_fill⟩
```

### 113. BOOK LIGHTING
```
⟨TECHNIQUE_113:BOOK_LIGHTING⟩
  ⟨method:bounce_into_reflector_then_subject⟩
  ⟨quality:extremely_soft_flattering⟩
  ⟨use_case:beauty, close_ups, flattering⟩
```

### 114. COVE LIGHTING
```
⟨TECHNIQUE_114:COVE⟩
  ⟨method:hidden_lights_in_architectural_features⟩
  ⟨effect:indirect_ambient_glow⟩
  ⟨use_case:modern_interiors, atmosphere⟩
```

### 115. CROSS LIGHTING
```
⟨TECHNIQUE_115:CROSS_LIGHTING⟩
  ⟨method:two_lights_opposite_sides⟩
  ⟨effect:even_low_contrast⟩
  ⟨use_case:even_coverage, documentation⟩
```

---

## Color Grading Implications

### 116. WARM GRADE
```
⟨GRADE_116:WARM⟩
  ⟨color_shift:toward_orange_yellow⟩
  ⟨mood:nostalgic_comfortable_inviting⟩
  ⟨use_case:period_pieces, romance, comfort⟩
```

### 117. COOL GRADE
```
⟨GRADE_117:COOL⟩
  ⟨color_shift:toward_blue_cyan⟩
  ⟨mood:clinical_modern_isolated⟩
  ⟨use_case:sci_fi, thriller, clinical⟩
```

### 118. DESATURATED
```
⟨GRADE_118:DESATURATED⟩
  ⟨saturation:reduced_muted⟩
  ⟨mood:gritty_realistic_somber⟩
  ⟨use_case:war_films, drama, realism⟩
  ⟨film_reference:Saving_Private_Ryan⟩
```

### 119. PUSHED SATURATION
```
⟨GRADE_119:SATURATED⟩
  ⟨saturation:enhanced_vibrant⟩
  ⟨mood:stylized_energetic_artificial⟩
  ⟨use_case:music_video, fantasy, stylized⟩
```

### 120. BLEACH BYPASS
```
⟨GRADE_120:BLEACH_BYPASS⟩
  ⟨technique:reduced_color_increased_contrast⟩
  ⟨appearance:washed_gritty_high_contrast⟩
  ⟨mood:gritty_harsh_visceral⟩
  ⟨use_case:war, action, gritty_drama⟩
  ⟨film_reference:Three_Kings, Saving_Private_Ryan⟩
```

---

## Director / DP Signature Styles

### 121. ROGER DEAKINS STYLE
```
⟨STYLE_121:DEAKINS⟩
  ⟨technique:naturalistic_motivated_sources⟩
  ⟨quality:soft_beautiful_subtle⟩
  ⟨mood:realistic_yet_cinematic⟩
  ⟨characteristics:motivated_light_natural_beauty⟩
  ⟨film_reference:Blade_Runner_2049, 1917⟩
```

### 122. EMMANUEL LUBEZKI STYLE
```
⟨STYLE_122:LUBEZKI⟩
  ⟨technique:natural_light_magic_hour⟩
  ⟨quality:ethereal_flowing⟩
  ⟨characteristics:golden_hour_natural_beauty_long_takes⟩
  ⟨film_reference:The_Revenant, Tree_of_Life⟩
```

### 123. GORDON WILLIS STYLE (GODFATHER)
```
⟨STYLE_123:WILLIS⟩
  ⟨technique:low_key_top_lighting_shadows⟩
  ⟨quality:dark_eyes_in_shadow⟩
  ⟨mood:mysterious_powerful_noir⟩
  ⟨characteristics:darkness_top_light_rich_blacks⟩
  ⟨film_reference:The_Godfather⟩
```

### 124. DAVID FINCHER STYLE
```
⟨STYLE_124:FINCHER⟩
  ⟨technique:cool_controlled_precise⟩
  ⟨quality:clinical_designed⟩
  ⟨color:often_cool_desaturated⟩
  ⟨mood:controlled_precise_clinical⟩
  ⟨film_reference:Se7en, Gone_Girl⟩
```

### 125. WES ANDERSON STYLE
```
⟨STYLE_125:ANDERSON⟩
  ⟨technique:flat_frontal_symmetrical⟩
  ⟨quality:even_pastel_controlled⟩
  ⟨color:pastel_coordinated_palette⟩
  ⟨mood:whimsical_controlled_artificial⟩
  ⟨film_reference:Grand_Budapest_Hotel⟩
```

---

## Complete Example Lighting Setups

### 126. EXAMPLE: Classic Portrait
```
⟨IMPORT:VSE_Lighting⟩

⟨LIGHTING_SETUP:rembrandt⟩
  ⟨key_light⟩
    ⟨position:45_degrees_horizontal, 45_degrees_vertical⟩
    ⟨quality:soft⟩
    ⟨color_temperature:5500K⟩
    ⟨intensity:1.0⟩
  
  ⟨fill_light⟩
    ⟨position:opposite_key, near_camera⟩
    ⟨quality:very_soft⟩
    ⟨intensity:0.3⟩
  
  ⟨back_light⟩
    ⟨position:behind_subject_elevated⟩
    ⟨quality:hard⟩
    ⟨intensity:1.2⟩

⟨LIGHTING_RATIO:4_to_1⟩
⟨MOOD:dignified_contemplative⟩
```

### 127. EXAMPLE: Noir Scene
```
⟨IMPORT:VSE_Lighting⟩

⟨LIGHTING_STYLE:film_noir⟩
⟨LIGHTING_RATIO:8_to_1⟩

⟨KEY_LIGHT⟩
  ⟨quality:hard⟩
  ⟨position:side_elevated⟩
  ⟨intensity:1.0⟩
  ⟨shadows:sharp_dramatic⟩

⟨FILL_LIGHT⟩
  ⟨intensity:0.125⟩
  ⟨minimal⟩

⟨PRACTICAL_LIGHTS⟩
  ⟨venetian_blind_shadows:true⟩
  ⟨desk_lamp:visible_motivated⟩

⟨MOOD:mysterious_dangerous_fatalistic⟩
⟨FILM_REFERENCE:The_Third_Man⟩
```

### 128. EXAMPLE: Golden Hour Romantic
```
⟨IMPORT:VSE_Lighting⟩

⟨TIME_OF_DAY:golden_hour⟩
⟨COLOR_TEMPERATURE:2800K⟩

⟨NATURAL_SUN⟩
  ⟨position:low_angle_horizontal⟩
  ⟨quality:soft_warm⟩
  ⟨color:golden_amber⟩
  ⟨intensity:0.8⟩
  ⟨shadows:long_flattering⟩

⟨ATMOSPHERE:clear_slight_haze⟩
⟨MOOD:romantic_nostalgic_beautiful⟩
⟨EMOTIONAL_QUALITY:precious_fleeting_magical⟩
```

### 129. EXAMPLE: Horror Scene
```
⟨IMPORT:VSE_Lighting⟩

⟨LIGHTING_STYLE:horror⟩
⟨LIGHTING_RATIO:no_fill_extreme_contrast⟩

⟨KEY_LIGHT⟩
  ⟨position:under_lighting⟩
  ⟨quality:hard_focused⟩
  ⟨color:slightly_green_tint⟩
  ⟨motivated_by:flashlight⟩

⟨ATMOSPHERE:fog_mist⟩
⟨SHADOWS:deep_threatening⟩
⟨MOOD:ominous_supernatural_terrifying⟩
```

### 130. EXAMPLE: Cyberpunk Night
```
⟨IMPORT:VSE_Lighting⟩

⟨LIGHTING_STYLE:cyberpunk⟩
⟨ENVIRONMENT:urban_night_rain⟩

⟨PRACTICAL_SOURCES⟩
  ⟨neon_signs:saturated_pink_cyan⟩
  ⟨street_lights:orange_sodium_vapor⟩
  ⟨windows:cool_blue_interior_glow⟩
  ⟨reflections:wet_pavement_multiplying_lights⟩

⟨ATMOSPHERE:rain_slight_fog⟩
⟨COLOR_PALETTE:pink_cyan_orange_purple⟩
⟨MOOD:dystopian_nocturnal_electric⟩
⟨FILM_REFERENCE:Blade_Runner⟩
```

---

## Lighting Exclusions (What to Avoid)

### 131. EXCLUDE UNNATURAL SOURCES
```
⟨EXCLUDE_131:UNNATURAL⟩
  ⟨description:light_without_motivation⟩
  ⟨when_realism_required:must_justify_all_sources⟩
```

### 132. EXCLUDE FLAT LIGHTING
```
⟨EXCLUDE_132:FLAT⟩
  ⟨description:no_dimension_no_shadows⟩
  ⟨unless:intentional_for_beauty_commercial⟩
```

### 133. EXCLUDE MIXED KELVIN ERRORS
```
⟨EXCLUDE_133:MIXED_KELVIN_ERRORS⟩
  ⟨description:unrealistic_color_temperature_clashes⟩
  ⟨unless:intentional_stylistic_choice⟩
```

### 134. EXCLUDE OVEREXPOSURE
```
⟨EXCLUDE_134:OVEREXPOSURE⟩
  ⟨description:blown_highlights_lost_detail⟩
  ⟨unless:intentional_bloom_effect⟩
```

### 135. EXCLUDE UNDEREXPOSURE
```
⟨EXCLUDE_135:UNDEREXPOSURE⟩
  ⟨description:crushed_blacks_lost_shadow_detail⟩
  ⟨unless:intentional_dramatic_noir⟩
```

---

## Emotional Lighting Matrix

### 136-156. EMOTION-TO-LIGHTING MAPPINGS

```
⟨EMOTION_136:JOY⟩
  ⟨lighting:high_key_bright_warm⟩
  ⟨color:warm_saturated⟩

⟨EMOTION_137:SADNESS⟩
  ⟨lighting:low_key_cool_subdued⟩
  ⟨color:desaturated_blue⟩

⟨EMOTION_138:ANGER⟩
  ⟨lighting:harsh_high_contrast_red⟩
  ⟨color:red_orange_hot⟩

⟨EMOTION_139:FEAR⟩
  ⟨lighting:low_key_unnatural_angles_shadows⟩
  ⟨color:desaturated_cool⟩

⟨EMOTION_140:LOVE⟩
  ⟨lighting:soft_warm_flattering_golden⟩
  ⟨color:warm_amber_gentle⟩

⟨EMOTION_141:MYSTERY⟩
  ⟨lighting:low_key_shadows_concealing⟩
  ⟨color:cool_dark_muted⟩

⟨EMOTION_142:WONDER⟩
  ⟨lighting:ethereal_glowing_magical⟩
  ⟨color:saturated_fantastical⟩

⟨EMOTION_143:ISOLATION⟩
  ⟨lighting:single_source_darkness_surrounding⟩
  ⟨color:cool_minimal⟩

⟨EMOTION_144:POWER⟩
  ⟨lighting:dramatic_from_below_or_high_contrast⟩
  ⟨color:bold_saturated⟩

⟨EMOTION_145:VULNERABILITY⟩
  ⟨lighting:exposed_soft_revealing⟩
  ⟨color:neutral_honest⟩

⟨EMOTION_146:NOSTALGIA⟩
  ⟨lighting:warm_soft_slightly_hazy⟩
  ⟨color:warm_sepia_faded⟩

⟨EMOTION_147:TENSION⟩
  ⟨lighting:harsh_shadows_uneven⟩
  ⟨color:stark_contrast⟩

⟨EMOTION_148:SERENITY⟩
  ⟨lighting:soft_even_natural⟩
  ⟨color:pastel_gentle⟩

⟨EMOTION_149:CHAOS⟩
  ⟨lighting:mixed_conflicting_moving⟩
  ⟨color:saturated_clashing⟩

⟨EMOTION_150:HOPE⟩
  ⟨lighting:dawn_light_breaking_through⟩
  ⟨color:warm_lifting⟩

⟨EMOTION_151:DESPAIR⟩
  ⟨lighting:dark_minimal_crushing⟩
  ⟨color:desaturated_bleak⟩

⟨EMOTION_152:TRIUMPH⟩
  ⟨lighting:bright_heroic_backlit⟩
  ⟨color:golden_elevated⟩

⟨EMOTION_153:INTIMACY⟩
  ⟨lighting:close_soft_warm_personal⟩
  ⟨color:warm_amber_gentle⟩

⟨EMOTION_154:ALIENATION⟩
  ⟨lighting:cold_harsh_fluorescent⟩
  ⟨color:cool_sterile⟩

⟨EMOTION_155:TRANSCENDENCE⟩
  ⟨lighting:ethereal_glowing_heavenly⟩
  ⟨color:white_gold_pure⟩

⟨EMOTION_156:DREAD⟩
  ⟨lighting:ominous_unnatural_threatening⟩
  ⟨color:sickly_dark_foreboding⟩
```

---

## Summary & Usage

**Total Lighting Setups Catalogued:** 156

**Categories:**
- Light Source Types: 15
- Classic Setups: 10
- Light Quality: 5
- Color Temperature: 5
- Directional Lighting: 7
- Time of Day: 8
- Weather & Atmosphere: 7
- Practical Lights: 9
- Motivated Lighting: 6
- Stylized Lighting: 8
- Lighting Ratios: 5
- Special Effects: 10
- Environment-Specific: 15
- Advanced Techniques: 5
- Color Grading: 5
- Signature Styles: 5
- Complete Examples: 5
- Exclusions: 5
- Emotional Mappings: 21

---

## Usage Guidelines

### Basic Usage
```
⟨IMPORT:VSE_Lighting⟩

⟨LIGHTING_SETUP:[setup_name]⟩
⟨TIME_OF_DAY:[time]⟩
⟨MOOD:[emotional_quality]⟩
```

### Advanced Usage
```
⟨IMPORT:VSE_Lighting⟩

⟨KEY_LIGHT⟩
  ⟨position:[degrees]⟩
  ⟨quality:[hard|soft]⟩
  ⟨color_temperature:[kelvin]⟩
  ⟨intensity:[0.0-1.0]⟩

⟨FILL_LIGHT⟩...
⟨BACK_LIGHT⟩...

⟨PRACTICAL_SOURCES⟩...
⟨ATMOSPHERE⟩...
⟨MOOD⟩...
```

---

## Next Steps

1. **Test with material transforms** (combine VSE_Lighting + VSE_Material)
2. **Validate with Grok video generation**
3. **Build preset library** (common scenarios)
4. **Create visual reference gallery**
5. **Cross-platform testing**

---

**Credits:**  
**Orchestration:** John Jacob Weber II  
**Documentation:** Claude (Sonnet 4.5)  
**Architecture:** Vox (Consultant)

**Status:** Complete Reference - Ready for Validation  
**Repository:** github.com/PaniclandUSA/vse/lighting-manifest/  
**Version:** 1.0  
**Date:** December 10, 2025

---

*"Light is meaning. Every shadow tells a story."*

— VSE Lighting Manifest Team

END OF MANIFEST
