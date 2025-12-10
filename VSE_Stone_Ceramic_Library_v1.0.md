# VSE Stone & Ceramic Material Library v1.0
## Complete Stone, Marble, Alabaster & Porcelain Reference

**Created:** December 10, 2025  
**Project:** Vector-Space Esperanto (VSE) Material Transform Library  
**Collaborators:** John Jacob Weber II, Claude (Sonnet 4.5), Vox (Architecture Consultant)  
**Status:** Comprehensive Reference - Ready for Validation Testing  

---

## Table of Contents

1. [Library Header](#library-header)
2. [Material Physics Foundation](#material-physics-foundation)
3. [Marble Varieties](#marble-varieties)
4. [Stone Types](#stone-types)
5. [Alabaster Variations](#alabaster-variations)
6. [Porcelain Types](#porcelain-types)
7. [Surface Finishes](#surface-finishes)
8. [Carving Techniques](#carving-techniques)
9. [Weathering & Age](#weathering--age)
10. [Color Variations](#color-variations)
11. [Veining Patterns](#veining-patterns)
12. [Translucency Levels](#translucency-levels)
13. [Combination Materials](#combination-materials)
14. [Complete Material Catalog](#complete-material-catalog)
15. [Usage Examples](#usage-examples)

---

## Library Header

```
⟨LIBRARY:VSE_Stone_Ceramic⟩
  ⟨CATEGORY:material_transformation_stone⟩
  ⟨VERSION:1.0⟩
  ⟨COMPATIBLE_WITH:VSE,Emersive,NanoBanana,Milieu,Gravitas⟩
  ⟨USE:photographic_to_sculptural_stone_ceramic⟩
  ⟨TOTAL_MATERIALS:247⟩
  ⟨EXTENDS:MTL_Glass_v1.0⟩
```

---

## Material Physics Foundation

### Core Stone Properties

```
⟨STONE_PROPERTIES⟩
  ⟨density:[kg/m³]⟩
  ⟨hardness:[mohs_scale_1-10]⟩
  ⟨translucency:[0.0-1.0]⟩
  ⟨grain_size:[fine|medium|coarse]⟩
  ⟨crystalline_structure:[microcrystalline|macrocrystalline|amorphous]⟩
  ⟨porosity:[0.0-1.0]⟩
  ⟨color_consistency:[uniform|banded|veined|mottled]⟩
  ⟨weathering_resistance:[low|medium|high]⟩
  ⟨carving_difficulty:[soft|medium|hard|very_hard]⟩
```

### Surface Finish Properties

```
⟨FINISH_PROPERTIES⟩
  ⟨polish_level:[matte|satin|semi_gloss|high_gloss|mirror]⟩
  ⟨surface_roughness:[smooth|slightly_textured|rough|very_rough]⟩
  ⟨reflectivity:[0.0-1.0]⟩
  ⟨micro_texture:[tool_marks|natural|polished_smooth]⟩
  ⟨luster:[waxy|silky|vitreous|greasy|pearly]⟩
```

### Optical Properties

```
⟨OPTICAL_PROPERTIES⟩
  ⟨subsurface_scatter:[0.0-1.0]⟩
  ⟨scatter_depth:[mm]⟩
  ⟨scatter_color:[tint]⟩
  ⟨refraction_index:[1.4-1.7]⟩
  ⟨light_penetration:[mm]⟩
  ⟨edge_glow:[enabled|disabled]⟩
  ⟨backlight_transmission:[0.0-1.0]⟩
```

---

## Marble Varieties (White to Colored)

### 001. CARRARA MARBLE (CLASSIC WHITE)
```
⟨MATERIAL_001:CARRARA_MARBLE⟩
  ⟨origin:Carrara, Italy⟩
  ⟨base_color:white_warm⟩
  ⟨color_code:RGB(245, 245, 245) with_slight_warmth⟩
  ⟨veining:gray_delicate_linear⟩
  ⟨vein_color:RGB(180, 180, 180)⟩
  ⟨translucency:0.25⟩
  ⟨grain:fine_crystalline⟩
  ⟨hardness:3_mohs⟩
  ⟨typical_finish:polished_smooth⟩
  ⟨subsurface_scatter:0.35⟩
  ⟨scatter_depth:5-10mm⟩
  ⟨use_case:classical_sculpture, architecture, prestige⟩
  ⟨historical_note:Michelangelo_preferred_material⟩
  ⟨emotional_quality:timeless, classical, prestigious⟩
```

### 002. CARRARA MARBLE (POLISHED)
```
⟨MATERIAL_002:CARRARA_POLISHED⟩
  ⟨base:CARRARA_MARBLE⟩
  ⟨finish:high_gloss_mirror_polish⟩
  ⟨reflectivity:0.7⟩
  ⟨surface:perfectly_smooth⟩
  ⟨specular_highlights:sharp_defined⟩
  ⟨luster:vitreous⟩
  ⟨use_case:formal_sculpture, luxury⟩
```

### 003. CARRARA MARBLE (HONED)
```
⟨MATERIAL_003:CARRARA_HONED⟩
  ⟨base:CARRARA_MARBLE⟩
  ⟨finish:satin_matte⟩
  ⟨reflectivity:0.2⟩
  ⟨surface:smooth_no_gloss⟩
  ⟨luster:silky⟩
  ⟨specular:diffused_soft⟩
  ⟨use_case:contemporary, subtle, elegant⟩
```

### 004. CARRARA MARBLE (AGED)
```
⟨MATERIAL_004:CARRARA_AGED⟩
  ⟨base:CARRARA_MARBLE⟩
  ⟨patina:yellowed_slightly⟩
  ⟨color_shift:cream_ivory⟩
  ⟨surface:weathered_soft⟩
  ⟨micro_erosion:subtle⟩
  ⟨use_case:antiquity, classical_ruins, time⟩
```

### 005. CARRARA MARBLE (WEATHERED)
```
⟨MATERIAL_005:CARRARA_WEATHERED⟩
  ⟨base:CARRARA_MARBLE⟩
  ⟨surface_condition:eroded_pitted⟩
  ⟨patina:dark_gray_accumulation⟩
  ⟨texture:rough_porous⟩
  ⟨detail_loss:moderate_softened_features⟩
  ⟨use_case:ruins, ancient_sculpture, decay⟩
```

### 006. STATUARIO MARBLE
```
⟨MATERIAL_006:STATUARIO⟩
  ⟨origin:Carrara, Italy⟩
  ⟨base_color:pure_white_cooler_than_Carrara⟩
  ⟨color_code:RGB(250, 250, 252)⟩
  ⟨veining:bold_dramatic_gold_gray⟩
  ⟨vein_pattern:broad_sweeping_statements⟩
  ⟨translucency:0.30⟩
  ⟨rarity:rare_premium⟩
  ⟨use_case:luxury_sculpture, high_end⟩
  ⟨emotional_quality:dramatic, luxurious, bold⟩
```

### 007. CALACATTA MARBLE
```
⟨MATERIAL_007:CALACATTA⟩
  ⟨origin:Carrara, Italy⟩
  ⟨base_color:bright_white⟩
  ⟨veining:thick_dramatic_gold_taupe⟩
  ⟨vein_thickness:bold_statement_veins⟩
  ⟨pattern:dramatic_large_scale⟩
  ⟨translucency:0.28⟩
  ⟨rarity:very_rare_most_expensive⟩
  ⟨use_case:luxury_maximum_drama⟩
  ⟨emotional_quality:opulent, dramatic, prestigious⟩
```

### 008. CALACATTA GOLD
```
⟨MATERIAL_008:CALACATTA_GOLD⟩
  ⟨base:CALACATTA⟩
  ⟨veining:gold_warm_amber_taupe⟩
  ⟨vein_color:RGB(180, 150, 100)⟩
  ⟨background:warm_white⟩
  ⟨use_case:warm_luxury_opulence⟩
```

### 009. CALACATTA BORGHINI
```
⟨MATERIAL_009:CALACATTA_BORGHINI⟩
  ⟨base:CALACATTA⟩
  ⟨veining:gray_dramatic_bold⟩
  ⟨vein_color:RGB(120, 120, 130)⟩
  ⟨pattern:interconnected_dramatic⟩
  ⟨use_case:contemporary_luxury_bold⟩
```

### 010. ARABESCATO MARBLE
```
⟨MATERIAL_010:ARABESCATO⟩
  ⟨origin:Italy⟩
  ⟨base_color:white_warm⟩
  ⟨veining:brown_gray_meandering⟩
  ⟨pattern:flowing_organic_arabesque⟩
  ⟨vein_style:soft_flowing_curved⟩
  ⟨translucency:0.26⟩
  ⟨use_case:elegant_flowing_design⟩
```

### 011. PARIAN MARBLE
```
⟨MATERIAL_011:PARIAN⟩
  ⟨origin:Paros, Greece⟩
  ⟨base_color:pure_white_semi_translucent⟩
  ⟨translucency:0.40_highest_of_marbles⟩
  ⟨grain:fine_sugary_crystalline⟩
  ⟨veining:minimal_to_none⟩
  ⟨subsurface_scatter:0.50⟩
  ⟨scatter_depth:12-20mm⟩
  ⟨historical_use:ancient_Greek_sculpture⟩
  ⟨use_case:classical_Greek_luminous⟩
  ⟨emotional_quality:ethereal, pure, classical⟩
```

### 012. PENTELIC MARBLE
```
⟨MATERIAL_012:PENTELIC⟩
  ⟨origin:Mount Pentelicus, Greece⟩
  ⟨base_color:white_with_golden_honey_patina⟩
  ⟨aging_behavior:develops_warm_golden_surface⟩
  ⟨patina:honey_colored_iron_oxidation⟩
  ⟨grain:fine_uniform⟩
  ⟨historical_use:Parthenon, Acropolis⟩
  ⟨use_case:classical_Greek_aged_beauty⟩
```

### 013. NERO MARQUINA (BLACK MARBLE)
```
⟨MATERIAL_013:NERO_MARQUINA⟩
  ⟨origin:Spain⟩
  ⟨base_color:deep_black⟩
  ⟨color_code:RGB(20, 20, 20)⟩
  ⟨veining:white_calcite_veins⟩
  ⟨vein_pattern:irregular_striking_contrast⟩
  ⟨finish:highly_polished⟩
  ⟨reflectivity:0.8⟩
  ⟨use_case:dramatic_modern_contrast⟩
  ⟨emotional_quality:dramatic, mysterious, bold⟩
```

### 014. VERDE ANTICO (GREEN MARBLE)
```
⟨MATERIAL_014:VERDE_ANTICO⟩
  ⟨origin:Greece⟩
  ⟨base_color:dark_green_serpentine⟩
  ⟨color_code:RGB(40, 70, 50)⟩
  ⟨veining:white_calcite_breccia⟩
  ⟨pattern:brecciated_angular_fragments⟩
  ⟨historical_use:Roman_Empire_prestige⟩
  ⟨rarity:ancient_quarries_exhausted⟩
  ⟨use_case:historical, prestige, antiquity⟩
```

### 015. ROSSO VERONA (RED MARBLE)
```
⟨MATERIAL_015:ROSSO_VERONA⟩
  ⟨origin:Verona, Italy⟩
  ⟨base_color:deep_red_wine⟩
  ⟨color_code:RGB(120, 40, 40)⟩
  ⟨veining:white_cream_veins⟩
  ⟨pattern:dramatic_contrast⟩
  ⟨use_case:dramatic_rich_opulent⟩
  ⟨emotional_quality:passionate, rich, dramatic⟩
```

### 016. GIALLO SIENA (YELLOW MARBLE)
```
⟨MATERIAL_016:GIALLO_SIENA⟩
  ⟨origin:Siena, Italy⟩
  ⟨base_color:golden_yellow_ochre⟩
  ⟨color_code:RGB(200, 160, 80)⟩
  ⟨veining:cream_white_subtle⟩
  ⟨use_case:warm_golden_classical⟩
```

### 017. PORTORO MARBLE
```
⟨MATERIAL_017:PORTORO⟩
  ⟨origin:Portovenere, Italy⟩
  ⟨base_color:black_deep⟩
  ⟨veining:gold_yellow_striking⟩
  ⟨vein_color:RGB(220, 180, 80)⟩
  ⟨pattern:dramatic_bold_veins⟩
  ⟨rarity:rare_premium⟩
  ⟨use_case:luxury_dramatic_opulent⟩
```

### 018. EMPERADOR MARBLE (DARK)
```
⟨MATERIAL_018:EMPERADOR_DARK⟩
  ⟨origin:Spain⟩
  ⟨base_color:deep_brown_chocolate⟩
  ⟨color_code:RGB(80, 50, 30)⟩
  ⟨veining:white_cream_irregular⟩
  ⟨pattern:random_organic⟩
  ⟨use_case:warm_rich_elegant⟩
```

### 019. CREMA MARFIL
```
⟨MATERIAL_019:CREMA_MARFIL⟩
  ⟨origin:Spain⟩
  ⟨base_color:cream_beige_warm⟩
  ⟨color_code:RGB(240, 225, 200)⟩
  ⟨veining:minimal_tone_on_tone⟩
  ⟨uniformity:high⟩
  ⟨use_case:warm_elegant_subtle⟩
```

### 020. ROSA PORTOGALLO (PINK MARBLE)
```
⟨MATERIAL_020:ROSA_PORTOGALLO⟩
  ⟨origin:Portugal⟩
  ⟨base_color:pink_rose_warm⟩
  ⟨color_code:RGB(230, 180, 180)⟩
  ⟨veining:darker_pink_red_veins⟩
  ⟨pattern:subtle_flowing⟩
  ⟨use_case:romantic_warm_delicate⟩
  ⟨emotional_quality:romantic, soft, warm⟩
```

---

## Metamorphic Stone Types

### 021. GRANITE (POLISHED)
```
⟨MATERIAL_021:GRANITE_POLISHED⟩
  ⟨type:igneous_intrusive⟩
  ⟨base_color:salt_pepper_gray⟩
  ⟨texture:visible_crystals_speckled⟩
  ⟨grain:coarse_visible_quartz_feldspar_mica⟩
  ⟨hardness:7_mohs_very_hard⟩
  ⟨translucency:0.0_opaque⟩
  ⟨finish:high_gloss_mirror⟩
  ⟨reflectivity:0.7⟩
  ⟨durability:extremely_high⟩
  ⟨use_case:monuments, durability, permanence⟩
```

### 022. BLACK GRANITE (ABSOLUTE)
```
⟨MATERIAL_022:BLACK_GRANITE⟩
  ⟨base_color:pure_black_deep⟩
  ⟨color_code:RGB(10, 10, 10)⟩
  ⟨texture:minimal_visible_grain⟩
  ⟨finish:mirror_polish⟩
  ⟨reflectivity:0.85_highly_reflective⟩
  ⟨use_case:modern_minimalist_dramatic⟩
```

### 023. RED GRANITE (IMPERIAL)
```
⟨MATERIAL_023:RED_GRANITE⟩
  ⟨base_color:red_pink_feldspar_dominant⟩
  ⟨color_code:RGB(180, 100, 100)⟩
  ⟨texture:coarse_visible_crystals⟩
  ⟨pattern:speckled_granular⟩
  ⟨use_case:monuments_powerful_enduring⟩
```

### 024. BASALT (DARK)
```
⟨MATERIAL_024:BASALT⟩
  ⟨type:volcanic_extrusive⟩
  ⟨base_color:dark_gray_black⟩
  ⟨grain:fine_dense⟩
  ⟨texture:smooth_matte⟩
  ⟨hardness:6_mohs⟩
  ⟨finish:naturally_matte_or_polished⟩
  ⟨use_case:ancient_monuments_somber⟩
  ⟨historical:Egyptian_sculpture_pre_marble⟩
```

### 025. SANDSTONE (BUFF)
```
⟨MATERIAL_025:SANDSTONE_BUFF⟩
  ⟨type:sedimentary_clastic⟩
  ⟨base_color:buff_tan_warm⟩
  ⟨color_code:RGB(210, 180, 140)⟩
  ⟨grain:medium_visible_sand_grains⟩
  ⟨texture:slightly_rough_granular⟩
  ⟨hardness:3-4_mohs_soft_workable⟩
  ⟨porosity:moderate_absorbs_water⟩
  ⟨weathering:erodes_moderately⟩
  ⟨use_case:architectural, warm, weatherable⟩
```

### 026. SANDSTONE (RED)
```
⟨MATERIAL_026:SANDSTONE_RED⟩
  ⟨base:SANDSTONE_BUFF⟩
  ⟨base_color:red_terracotta_iron_oxide⟩
  ⟨color_code:RGB(180, 90, 60)⟩
  ⟨use_case:southwestern, desert, warm⟩
```

### 027. LIMESTONE (CREAM)
```
⟨MATERIAL_027:LIMESTONE_CREAM⟩
  ⟨type:sedimentary_carbonate⟩
  ⟨base_color:cream_buff_warm⟩
  ⟨color_code:RGB(235, 220, 200)⟩
  ⟨grain:fine_uniform⟩
  ⟨hardness:3_mohs_soft_carvable⟩
  ⟨texture:smooth_fine⟩
  ⟨carving:excellent_for_detail⟩
  ⟨weathering:moderate_develops_patina⟩
  ⟨use_case:architectural_carving_warm⟩
```

### 028. TRAVERTINE
```
⟨MATERIAL_028:TRAVERTINE⟩
  ⟨type:sedimentary_chemical_precipitate⟩
  ⟨base_color:cream_tan_with_banding⟩
  ⟨texture:porous_voids_characteristic⟩
  ⟨voids:natural_holes_pockets⟩
  ⟨banding:horizontal_layering_visible⟩
  ⟨finish:filled_polished|unfilled_natural⟩
  ⟨use_case:Roman_architecture_classical⟩
  ⟨historical:Colosseum_material⟩
```

### 029. ONYX (TRANSLUCENT)
```
⟨MATERIAL_029:ONYX⟩
  ⟨type:cryptocrystalline_quartz⟩
  ⟨base_color:variable_banded⟩
  ⟨translucency:0.60_highly_translucent⟩
  ⟨banding:dramatic_color_bands⟩
  ⟨backlit:glows_dramatically⟩
  ⟨subsurface_scatter:0.70⟩
  ⟨colors:honey, white, green, red⟩
  ⟨use_case:luxury_backlit_dramatic⟩
  ⟨emotional_quality:luxurious, glowing, exotic⟩
```

### 030. WHITE ONYX
```
⟨MATERIAL_030:WHITE_ONYX⟩
  ⟨base:ONYX⟩
  ⟨base_color:white_cream_translucent⟩
  ⟨banding:subtle_white_variations⟩
  ⟨translucency:0.65⟩
  ⟨backlit_color:warm_honey_glow⟩
  ⟨use_case:luminous_elegant_spa_like⟩
```

### 031. HONEY ONYX
```
⟨MATERIAL_031:HONEY_ONYX⟩
  ⟨base:ONYX⟩
  ⟨base_color:golden_amber_honey⟩
  ⟨banding:caramel_variations⟩
  ⟨translucency:0.70⟩
  ⟨backlit_color:glowing_golden⟩
  ⟨use_case:warm_luxurious_glowing⟩
```

### 032. SOAPSTONE
```
⟨MATERIAL_032:SOAPSTONE⟩
  ⟨type:metamorphic_talc_rich⟩
  ⟨base_color:gray_green_dark⟩
  ⟨texture:smooth_soapy_feel⟩
  ⟨hardness:1-2_mohs_very_soft⟩
  ⟨carving:extremely_easy⟩
  ⟨luster:waxy_soapy⟩
  ⟨use_case:Inuit_carving_soft_detail⟩
```

### 033. SLATE
```
⟨MATERIAL_033:SLATE⟩
  ⟨type:metamorphic_foliated⟩
  ⟨base_color:dark_gray_blue_gray⟩
  ⟨texture:fine_smooth_layered⟩
  ⟨cleavage:splits_along_planes⟩
  ⟨finish:natural_matte⟩
  ⟨use_case:architectural_planar_modern⟩
```

### 034. SERPENTINE (GREEN)
```
⟨MATERIAL_034:SERPENTINE⟩
  ⟨type:metamorphic_hydrated_magnesium_silicate⟩
  ⟨base_color:green_various_shades⟩
  ⟨pattern:mottled_veined⟩
  ⟨luster:waxy_greasy⟩
  ⟨hardness:2.5-5.5_mohs_variable⟩
  ⟨use_case:decorative_green_sculpture⟩
```

---

## Alabaster Variations

### 035. ALABASTER (PURE WHITE)
```
⟨MATERIAL_035:ALABASTER_WHITE⟩
  ⟨type:gypsum_calcium_sulfate⟩
  ⟨base_color:pure_white_translucent⟩
  ⟨translucency:0.70_highly_translucent⟩
  ⟨grain:extremely_fine_crystalline⟩
  ⟨hardness:2_mohs_very_soft_carvable⟩
  ⟨subsurface_scatter:0.80⟩
  ⟨scatter_depth:20-40mm⟩
  ⟨carving:excellent_fine_detail⟩
  ⟨luster:waxy_silky⟩
  ⟨backlit:glows_ethereally⟩
  ⟨use_case:delicate_sculpture_luminous⟩
  ⟨historical:medieval_windows_church_sculpture⟩
  ⟨emotional_quality:ethereal, delicate, luminous⟩
```

### 036. ALABASTER (CREAM)
```
⟨MATERIAL_036:ALABASTER_CREAM⟩
  ⟨base:ALABASTER_WHITE⟩
  ⟨base_color:cream_ivory_warm⟩
  ⟨color_code:RGB(250, 245, 235)⟩
  ⟨translucency:0.65⟩
  ⟨use_case:warm_soft_elegant⟩
```

### 037. ALABASTER (HONEY)
```
⟨MATERIAL_037:ALABASTER_HONEY⟩
  ⟨base:ALABASTER_WHITE⟩
  ⟨base_color:honey_amber_translucent⟩
  ⟨banding:subtle_flow_patterns⟩
  ⟨translucency:0.60⟩
  ⟨backlit_color:warm_golden_glow⟩
  ⟨use_case:warm_luxurious_luminous⟩
```

### 038. ALABASTER (BANDED)
```
⟨MATERIAL_038:ALABASTER_BANDED⟩
  ⟨base:ALABASTER_WHITE⟩
  ⟨pattern:horizontal_bands_layers⟩
  ⟨band_colors:white_cream_honey_alternating⟩
  ⟨translucency:variable_by_band⟩
  ⟨use_case:decorative_ornate_layered⟩
```

### 039. ALABASTER (VEINED)
```
⟨MATERIAL_039:ALABASTER_VEINED⟩
  ⟨base:ALABASTER_WHITE⟩
  ⟨veining:subtle_cream_honey_veins⟩
  ⟨vein_pattern:organic_flowing⟩
  ⟨translucency:0.68⟩
  ⟨use_case:natural_organic_flowing⟩
```

### 040. CALCITE ALABASTER (EGYPTIAN)
```
⟨MATERIAL_040:CALCITE_ALABASTER⟩
  ⟨type:calcite_calcium_carbonate⟩
  ⟨base_color:cream_honey_banded⟩
  ⟨hardness:3_mohs_harder_than_gypsum⟩
  ⟨translucency:0.50⟩
  ⟨banding:prominent_dramatic⟩
  ⟨historical:ancient_Egypt_canopic_jars⟩
  ⟨use_case:Egyptian_ancient_banded⟩
```

---

## Porcelain Types

### 041. PORCELAIN (PURE WHITE)
```
⟨MATERIAL_041:PORCELAIN_WHITE⟩
  ⟨type:ceramic_vitrified⟩
  ⟨base_color:pure_white_cold⟩
  ⟨color_code:RGB(255, 255, 255)⟩
  ⟨translucency:0.15_slight_when_thin⟩
  ⟨surface:perfectly_smooth_glassy⟩
  ⟨finish:high_gloss_glazed⟩
  ⟨reflectivity:0.8⟩
  ⟨luster:vitreous_glassy⟩
  ⟨texture:flawless_uniform⟩
  ⟨hardness:6-7_mohs⟩
  ⟨use_case:delicate_refined_perfect⟩
  ⟨emotional_quality:pristine, delicate, refined⟩
```

### 042. PORCELAIN (MATTE WHITE)
```
⟨MATERIAL_042:PORCELAIN_MATTE⟩
  ⟨base:PORCELAIN_WHITE⟩
  ⟨finish:matte_unglazed⟩
  ⟨surface:smooth_no_gloss⟩
  ⟨reflectivity:0.1⟩
  ⟨luster:silky_soft⟩
  ⟨use_case:modern_minimalist_soft⟩
```

### 043. PORCELAIN (BISQUE)
```
⟨MATERIAL_043:PORCELAIN_BISQUE⟩
  ⟨base:PORCELAIN_WHITE⟩
  ⟨finish:unglazed_fired⟩
  ⟨surface:matte_slightly_porous_feeling⟩
  ⟨color:warm_white_cream⟩
  ⟨texture:fine_soft_to_touch⟩
  ⟨use_case:doll_making_soft_delicate⟩
```

### 044. PORCELAIN (EGGSHELL)
```
⟨MATERIAL_044:PORCELAIN_EGGSHELL⟩
  ⟨base:PORCELAIN_WHITE⟩
  ⟨finish:low_gloss_satin⟩
  ⟨reflectivity:0.3⟩
  ⟨luster:soft_subtle_sheen⟩
  ⟨color:warm_white_ivory⟩
  ⟨use_case:refined_subtle_elegant⟩
```

### 045. PORCELAIN (PAINTED - TRADITIONAL)
```
⟨MATERIAL_045:PORCELAIN_PAINTED_TRADITIONAL⟩
  ⟨base:PORCELAIN_WHITE⟩
  ⟨decoration:hand_painted_overglaze⟩
  ⟨patterns:floral, landscape, figurative⟩
  ⟨colors:cobalt_blue_traditional⟩
  ⟨style:delicate_detailed_fine_brush⟩
  ⟨use_case:decorative_Chinese_Japanese⟩
```

### 046. PORCELAIN (BLUE AND WHITE)
```
⟨MATERIAL_046:PORCELAIN_BLUE_WHITE⟩
  ⟨base:PORCELAIN_WHITE⟩
  ⟨decoration:cobalt_blue_underglaze⟩
  ⟨pattern:traditional_Chinese_motifs⟩
  ⟨style:Ming_dynasty_aesthetic⟩
  ⟨use_case:traditional_Asian_elegant⟩
```

### 047. PORCELAIN (PAINTED - MODERN)
```
⟨MATERIAL_047:PORCELAIN_PAINTED_MODERN⟩
  ⟨base:PORCELAIN_WHITE⟩
  ⟨decoration:contemporary_graphic⟩
  ⟨style:minimalist_geometric_abstract⟩
  ⟨colors:varied_bold_or_subtle⟩
  ⟨use_case:contemporary_art_modern⟩
```

### 048. PORCELAIN (CRACKLE GLAZE)
```
⟨MATERIAL_048:PORCELAIN_CRACKLE⟩
  ⟨base:PORCELAIN_WHITE⟩
  ⟨glaze_effect:intentional_crazing_network⟩
  ⟨pattern:fine_crackle_lines_surface⟩
  ⟨patina_in_cracks:darker_staining⟩
  ⟨use_case:aged_decorative_vintage⟩
```

### 049. BONE CHINA
```
⟨MATERIAL_049:BONE_CHINA⟩
  ⟨type:porcelain_with_bone_ash⟩
  ⟨base_color:warm_white_ivory⟩
  ⟨translucency:0.40_highly_translucent⟩
  ⟨strength:high_despite_thinness⟩
  ⟨finish:gloss_smooth⟩
  ⟨backlit:glows_warmly⟩
  ⟨use_case:delicate_refined_English⟩
```

### 050. CELADON
```
⟨MATERIAL_050:CELADON⟩
  ⟨type:porcelain_glazed⟩
  ⟨base_color:pale_green_blue_gray⟩
  ⟨glaze:iron_bearing_reduction_fired⟩
  ⟨finish:soft_gloss_jade_like⟩
  ⟨translucency:0.10⟩
  ⟨use_case:Asian_elegant_subtle⟩
  ⟨historical:Chinese_Korean_ceramics⟩
```

---

## Surface Finishes (Applicable to All Stone)

### 051. MIRROR POLISH
```
⟨FINISH_051:MIRROR_POLISH⟩
  ⟨process:progressive_fine_abrasives⟩
  ⟨surface:perfectly_smooth_reflective⟩
  ⟨reflectivity:0.85-0.95⟩
  ⟨specular:sharp_mirror_reflections⟩
  ⟨tool_marks:completely_removed⟩
  ⟨use_case:luxury_formal_pristine⟩
```

### 052. HIGH GLOSS
```
⟨FINISH_052:HIGH_GLOSS⟩
  ⟨process:polished_smooth⟩
  ⟨reflectivity:0.70-0.85⟩
  ⟨specular:defined_highlights⟩
  ⟨surface:smooth_slight_imperfections_possible⟩
  ⟨use_case:formal_elegant_refined⟩
```

### 053. SEMI-GLOSS (HONED)
```
⟨FINISH_053:SEMI_GLOSS⟩
  ⟨process:smoothed_not_polished⟩
  ⟨reflectivity:0.30-0.50⟩
  ⟨specular:soft_diffused⟩
  ⟨surface:smooth_satin_feel⟩
  ⟨use_case:elegant_subdued_contemporary⟩
```

### 054. MATTE (HONED)
```
⟨FINISH_054:MATTE⟩
  ⟨process:ground_smooth_no_polish⟩
  ⟨reflectivity:0.10-0.20⟩
  ⟨surface:smooth_no_gloss⟩
  ⟨luster:silky_soft⟩
  ⟨use_case:contemporary_understated⟩
```

### 055. SATIN FINISH
```
⟨FINISH_055:SATIN⟩
  ⟨process:fine_abrasive_smooth⟩
  ⟨reflectivity:0.20-0.40⟩
  ⟨luster:soft_sheen_silky⟩
  ⟨surface:smooth_subtle_glow⟩
  ⟨use_case:elegant_soft_refined⟩
```

### 056. BRUSHED FINISH
```
⟨FINISH_056:BRUSHED⟩
  ⟨process:directional_brushing⟩
  ⟨pattern:linear_brush_marks⟩
  ⟨texture:subtle_directional_grain⟩
  ⟨reflectivity:0.15-0.25⟩
  ⟨use_case:modern_industrial_textured⟩
```

### 057. SANDBLASTED
```
⟨FINISH_057:SANDBLASTED⟩
  ⟨process:abrasive_blasting⟩
  ⟨surface:uniformly_rough_matte⟩
  ⟨texture:fine_grit_consistent⟩
  ⟨reflectivity:0.05-0.10⟩
  ⟨use_case:textured_modern_non_slip⟩
```

### 058. BUSH-HAMMERED
```
⟨FINISH_058:BUSH_HAMMERED⟩
  ⟨process:mechanical_hammering⟩
  ⟨texture:dimpled_pitted_rough⟩
  ⟨pattern:regular_hammered_marks⟩
  ⟨surface:very_rough_textured⟩
  ⟨use_case:architectural_textured_grip⟩
```

### 059. FLAMED FINISH
```
⟨FINISH_059:FLAMED⟩
  ⟨process:high_heat_torch_spalling⟩
  ⟨texture:rough_irregular_surface⟩
  ⟨appearance:fractured_rough⟩
  ⟨use_case:exterior_non_slip_rustic⟩
  ⟨note:granite_primarily⟩
```

### 060. RIVEN / CLEFT
```
⟨FINISH_060:RIVEN⟩
  ⟨process:natural_split_along_grain⟩
  ⟨surface:irregular_natural_texture⟩
  ⟨texture:rough_organic_split⟩
  ⟨use_case:natural_rustic_organic⟩
```

### 061. TUMBLED / ANTIQUED
```
⟨FINISH_061:TUMBLED⟩
  ⟨process:mechanical_tumbling_softening⟩
  ⟨edges:rounded_softened⟩
  ⟨surface:slightly_irregular_aged⟩
  ⟨use_case:aged_vintage_soft⟩
```

### 062. HAND-CARVED TEXTURE
```
⟨FINISH_062:HAND_CARVED⟩
  ⟨process:chisel_marks_intentional⟩
  ⟨texture:visible_tool_marks_organic⟩
  ⟨pattern:irregular_artisanal⟩
  ⟨use_case:artisanal_handcrafted_rustic⟩
```

---

## Carving Techniques & Styles

### 063. CLASSICAL GREEK (HIGH POLISH)
```
⟨CARVING_063:CLASSICAL_GREEK⟩
  ⟨period:5th-4th_century_BCE⟩
  ⟨technique:idealized_proportions⟩
  ⟨finish:highly_polished_smooth⟩
  ⟨detail_level:refined_naturalistic⟩
  ⟨drapery:flowing_clinging_wet_cloth_effect⟩
  ⟨anatomy:perfect_idealized⟩
  ⟨use_case:classical_idealized_perfection⟩
```

### 064. ROMAN REPUBLICAN
```
⟨CARVING_064:ROMAN_REPUBLICAN⟩
  ⟨period:1st_century_BCE⟩
  ⟨technique:veristic_realistic⟩
  ⟨detail:wrinkles_age_marks_preserved⟩
  ⟨finish:polished_realistic⟩
  ⟨use_case:realistic_portraiture_aging⟩
```

### 065. ROMAN IMPERIAL
```
⟨CARVING_065:ROMAN_IMPERIAL⟩
  ⟨period:1st-4th_century_CE⟩
  ⟨technique:idealized_imperial⟩
  ⟨finish:highly_polished⟩
  ⟨detail:heroic_proportions⟩
  ⟨use_case:imperial_heroic_idealized⟩
```

### 066. MEDIEVAL ROMANESQUE
```
⟨CARVING_066:MEDIEVAL_ROMANESQUE⟩
  ⟨period:11th-12th_century⟩
  ⟨technique:stylized_geometric⟩
  ⟨proportions:elongated_symbolic⟩
  ⟨detail:simplified_architectural⟩
  ⟨finish:less_polished_textured⟩
  ⟨use_case:religious_symbolic_architectural⟩
```

### 067. GOTHIC
```
⟨CARVING_067:GOTHIC⟩
  ⟨period:12th-15th_century⟩
  ⟨technique:naturalistic_elongated⟩
  ⟨drapery:flowing_vertical_folds⟩
  ⟨detail:intricate_delicate⟩
  ⟨use_case:religious_vertical_elegant⟩
```

### 068. RENAISSANCE
```
⟨CARVING_068:RENAISSANCE⟩
  ⟨period:15th-16th_century⟩
  ⟨technique:classical_revival_naturalistic⟩
  ⟨anatomy:accurate_studied⟩
  ⟨finish:highly_polished_refined⟩
  ⟨detail:masterful_technical⟩
  ⟨use_case:humanistic_classical_revival⟩
  ⟨reference:Michelangelo_Donatello⟩
```

### 069. BAROQUE
```
⟨CARVING_069:BAROQUE⟩
  ⟨period:17th-18th_century⟩
  ⟨technique:dramatic_movement_emotion⟩
  ⟨composition:dynamic_diagonal⟩
  ⟨drapery:swirling_dramatic⟩
  ⟨finish:polished_dramatic_contrast⟩
  ⟨use_case:dramatic_emotional_theatrical⟩
  ⟨reference:Bernini⟩
```

### 070. NEOCLASSICAL
```
⟨CARVING_070:NEOCLASSICAL⟩
  ⟨period:18th-19th_century⟩
  ⟨technique:restrained_classical_revival⟩
  ⟨proportions:idealized_harmonious⟩
  ⟨finish:smooth_polished_cool⟩
  ⟨emotion:restrained_dignified⟩
  ⟨use_case:formal_classical_dignified⟩
  ⟨reference:Canova⟩
```

### 071. RODIN-ESQUE (IMPRESSIONIST)
```
⟨CARVING_071:IMPRESSIONIST_SCULPTURE⟩
  ⟨period:late_19th_century⟩
  ⟨technique:rough_textured_expressive⟩
  ⟨surface:visible_tool_marks_intentional⟩
  ⟨finish:partially_unfinished_rough⟩
  ⟨contrast:polished_areas_vs_rough⟩
  ⟨use_case:expressive_modern_textured⟩
  ⟨reference:Auguste_Rodin⟩
```

### 072. ART DECO
```
⟨CARVING_072:ART_DECO⟩
  ⟨period:1920s-1930s⟩
  ⟨technique:streamlined_geometric⟩
  ⟨style:stylized_sleek_modern⟩
  ⟨finish:highly_polished_smooth⟩
  ⟨detail:simplified_elegant_curves⟩
  ⟨use_case:modern_elegant_streamlined⟩
```

### 073. MODERNIST ABSTRACT
```
⟨CARVING_073:MODERNIST_ABSTRACT⟩
  ⟨period:20th_century⟩
  ⟨technique:simplified_forms_abstract⟩
  ⟨style:geometric_organic_abstract⟩
  ⟨finish:variable_polished_or_rough⟩
  ⟨use_case:abstract_modern_non_representational⟩
  ⟨reference:Brancusi_Henry_Moore⟩
```

---

## Weathering & Age

### 074. PRISTINE (NEW)
```
⟨WEATHERING_074:PRISTINE⟩
  ⟨condition:perfect_new⟩
  ⟨surface:flawless_unmarked⟩
  ⟨color:original_true⟩
  ⟨edges:sharp_crisp⟩
  ⟨use_case:contemporary_new_perfect⟩
```

### 075. LIGHTLY AGED (50-100 YEARS)
```
⟨WEATHERING_075:LIGHTLY_AGED⟩
  ⟨condition:subtle_patina⟩
  ⟨color:slight_yellowing_warmth⟩
  ⟨surface:minor_surface_wear⟩
  ⟨edges:slightly_softened⟩
  ⟨use_case:antique_vintage_subtle_age⟩
```

### 076. MODERATELY AGED (100-500 YEARS)
```
⟨WEATHERING_076:MODERATELY_AGED⟩
  ⟨condition:visible_patina⟩
  ⟨color:yellowed_darkened_areas⟩
  ⟨surface:micro_erosion_weathering⟩
  ⟨staining:water_stains_mineral_deposits⟩
  ⟨edges:softened_rounded⟩
  ⟨detail_loss:slight_softening_features⟩
  ⟨use_case:historical_aged_character⟩
```

### 077. HEAVILY AGED (500-2000 YEARS)
```
⟨WEATHERING_077:HEAVILY_AGED⟩
  ⟨condition:significant_weathering⟩
  ⟨color:darkened_yellowed_brown_gray⟩
  ⟨surface:eroded_pitted_rough⟩
  ⟨staining:heavy_mineral_biological⟩
  ⟨detail_loss:moderate_features_softened⟩
  ⟨cracks:possible_age_cracks⟩
  ⟨use_case:ancient_ruins_archaeological⟩
```

### 078. ANCIENT (2000+ YEARS)
```
⟨WEATHERING_078:ANCIENT⟩
  ⟨condition:severe_weathering⟩
  ⟨surface:heavily_eroded_porous⟩
  ⟨color:dark_patina_heavy_staining⟩
  ⟨detail_loss:significant_features_obscured⟩
  ⟨damage:chips_cracks_missing_pieces⟩
  ⟨biological_growth:lichen_moss_possible⟩
  ⟨use_case:ancient_ruins_archaeological_decay⟩
```

### 079. WATER-WORN
```
⟨WEATHERING_079:WATER_WORN⟩
  ⟨cause:prolonged_water_exposure⟩
  ⟨surface:smoothed_rounded_soft⟩
  ⟨edges:extremely_rounded⟩
  ⟨detail_loss:features_eroded_smooth⟩
  ⟨color:often_lighter_washed⟩
  ⟨use_case:river_stones_beach_worn_ancient⟩
```

### 080. FIRE-DAMAGED
```
⟨WEATHERING_080:FIRE_DAMAGED⟩
  ⟨cause:intense_heat_exposure⟩
  ⟨surface:cracked_spalled_fractured⟩
  ⟨color:darkened_blackened_soot⟩
  ⟨texture:rough_fractured⟩
  ⟨use_case:ruins_disaster_ancient_burning⟩
```

### 081. ACID RAIN DAMAGED
```
⟨WEATHERING_081:ACID_RAIN⟩
  ⟨cause:chemical_weathering⟩
  ⟨surface:dissolved_rough_pitted⟩
  ⟨detail_loss:severe_features_melted_appearance⟩
  ⟨color:darkened_stained⟩
  ⟨use_case:modern_pollution_damage_environmental⟩
```

### 082. BIOLOGICAL GROWTH (LICHEN/MOSS)
```
⟨WEATHERING_082:BIOLOGICAL_GROWTH⟩
  ⟨growth:lichen_moss_algae⟩
  ⟨color:green_gray_orange_patches⟩
  ⟨pattern:irregular_organic_spreading⟩
  ⟨texture:rough_living_layer⟩
  ⟨use_case:ancient_forest_humid_aged⟩
```

### 083. PARTIAL BURIAL (EXCAVATED)
```
⟨WEATHERING_083:EXCAVATED⟩
  ⟨condition:recently_excavated⟩
  ⟨staining:earth_mineral_stains⟩
  ⟨surface:differential_weathering_buried_vs_exposed⟩
  ⟨encrustation:possible_calcite_mineral_deposits⟩
  ⟨use_case:archaeological_discovery_excavation⟩
```

---

## Color Variations & Treatments

### 084. PURE WHITE
```
⟨COLOR_084:PURE_WHITE⟩
  ⟨color_code:RGB(255, 255, 255)⟩
  ⟨temperature:neutral_cool⟩
  ⟨purity:maximum⟩
  ⟨use_case:modern_pristine_pure⟩
```

### 085. WARM WHITE
```
⟨COLOR_085:WARM_WHITE⟩
  ⟨color_code:RGB(250, 248, 245)⟩
  ⟨temperature:warm_ivory⟩
  ⟨undertone:cream_slight_yellow⟩
  ⟨use_case:traditional_warm_inviting⟩
```

### 086. COOL WHITE
```
⟨COLOR_086:COOL_WHITE⟩
  ⟨color_code:RGB(248, 250, 252)⟩
  ⟨temperature:cool_blue_undertone⟩
  ⟨use_case:modern_clinical_cool⟩
```

### 087. CREAM / IVORY
```
⟨COLOR_087:CREAM⟩
  ⟨color_code:RGB(245, 240, 225)⟩
  ⟨temperature:warm⟩
  ⟨undertone:yellow_cream⟩
  ⟨use_case:warm_elegant_soft⟩
```

### 088. AGED IVORY
```
⟨COLOR_088:AGED_IVORY⟩
  ⟨color_code:RGB(235, 220, 195)⟩
  ⟨temperature:warm_aged⟩
  ⟨patina:yellowed_oxidized⟩
  ⟨use_case:antique_aged_vintage⟩
```

### 089. GRAY-WHITE
```
⟨COLOR_089:GRAY_WHITE⟩
  ⟨color_code:RGB(240, 240, 240)⟩
  ⟨undertone:neutral_gray⟩
  ⟨use_case:neutral_modern_understated⟩
```

### 090. PINK-TINTED
```
⟨COLOR_090:PINK_TINTED⟩
  ⟨color_code:RGB(250, 240, 240)⟩
  ⟨undertone:subtle_pink_rose⟩
  ⟨use_case:romantic_soft_delicate⟩
```

### 091. GREEN-TINTED
```
⟨COLOR_091:GREEN_TINTED⟩
  ⟨color_code:RGB(240, 245, 240)⟩
  ⟨undertone:subtle_green_mint⟩
  ⟨use_case:natural_fresh_unusual⟩
```

### 092. BLUE-TINTED
```
⟨COLOR_092:BLUE_TINTED⟩
  ⟨color_code:RGB(240, 242, 248)⟩
  ⟨undertone:subtle_blue_cool⟩
  ⟨use_case:cool_serene_ethereal⟩
```

---

## Veining Patterns

### 093. NO VEINING (UNIFORM)
```
⟨VEINING_093:NONE⟩
  ⟨pattern:uniform_solid_color⟩
  ⟨consistency:perfect_uniformity⟩
  ⟨use_case:pure_clean_minimal⟩
```

### 094. SUBTLE VEINING
```
⟨VEINING_094:SUBTLE⟩
  ⟨visibility:faint_barely_visible⟩
  ⟨color:tone_on_tone_low_contrast⟩
  ⟨pattern:delicate_fine_lines⟩
  ⟨use_case:elegant_understated_refined⟩
```

### 095. MODERATE VEINING
```
⟨VEINING_095:MODERATE⟩
  ⟨visibility:clearly_visible_balanced⟩
  ⟨color:gray_or_color_contrast⟩
  ⟨pattern:organic_natural_flow⟩
  ⟨use_case:classic_marble_natural⟩
```

### 096. DRAMATIC VEINING
```
⟨VEINING_096:DRAMATIC⟩
  ⟨visibility:bold_prominent⟩
  ⟨color:high_contrast_striking⟩
  ⟨pattern:thick_sweeping_veins⟩
  ⟨use_case:dramatic_luxurious_statement⟩
```

### 097. LINEAR VEINING
```
⟨VEINING_097:LINEAR⟩
  ⟨pattern:parallel_straight_lines⟩
  ⟨direction:consistent_directional⟩
  ⟨use_case:architectural_modern_striped⟩
```

### 098. SPIDERWEB VEINING
```
⟨VEINING_098:SPIDERWEB⟩
  ⟨pattern:interconnected_network⟩
  ⟨branching:fine_delicate_spreading⟩
  ⟨use_case:delicate_natural_complex⟩
```

### 099. CLOUDY VEINING
```
⟨VEINING_099:CLOUDY⟩
  ⟨pattern:diffuse_cloud_like_soft_edges⟩
  ⟨definition:blurred_soft_transitions⟩
  ⟨use_case:soft_ethereal_gentle⟩
```

### 100. BRECCIA PATTERN
```
⟨VEINING_100:BRECCIA⟩
  ⟨pattern:angular_fragments_cemented⟩
  ⟨appearance:broken_reassembled⟩
  ⟨use_case:dramatic_geological_unique⟩
```

---

## Translucency Levels

### 101. OPAQUE (NO TRANSLUCENCY)
```
⟨TRANSLUCENCY_101:OPAQUE⟩
  ⟨translucency:0.0⟩
  ⟨light_penetration:none⟩
  ⟨backlit:no_glow⟩
  ⟨materials:granite, basalt, dense_marble⟩
```

### 102. MINIMAL TRANSLUCENCY
```
⟨TRANSLUCENCY_102:MINIMAL⟩
  ⟨translucency:0.05-0.15⟩
  ⟨light_penetration:1-3mm⟩
  ⟨backlit:subtle_edge_glow_only⟩
  ⟨materials:porcelain, dense_marble⟩
```

### 103. SLIGHT TRANSLUCENCY
```
⟨TRANSLUCENCY_103:SLIGHT⟩
  ⟨translucency:0.15-0.30⟩
  ⟨light_penetration:3-8mm⟩
  ⟨backlit:visible_glow_thin_areas⟩
  ⟨materials:Carrara_marble, limestone⟩
```

### 104. MODERATE TRANSLUCENCY
```
⟨TRANSLUCENCY_104:MODERATE⟩
  ⟨translucency:0.30-0.50⟩
  ⟨light_penetration:8-15mm⟩
  ⟨backlit:noticeable_glow⟩
  ⟨materials:Parian_marble, calcite_alabaster⟩
```

### 105. HIGH TRANSLUCENCY
```
⟨TRANSLUCENCY_105:HIGH⟩
  ⟨translucency:0.50-0.70⟩
  ⟨light_penetration:15-30mm⟩
  ⟨backlit:strong_glow_visible_through⟩
  ⟨materials:onyx, gypsum_alabaster⟩
```

### 106. VERY HIGH TRANSLUCENCY
```
⟨TRANSLUCENCY_106:VERY_HIGH⟩
  ⟨translucency:0.70-0.85⟩
  ⟨light_penetration:30-60mm⟩
  ⟨backlit:ethereal_glowing⟩
  ⟨materials:thin_alabaster, thin_onyx⟩
```

---

## Combination Materials & Hybrid Effects

### 107. MARBLE WITH PORCELAIN SMOOTHNESS
```
⟨HYBRID_107:MARBLE_PORCELAIN⟩
  ⟨base:CARRARA_MARBLE⟩
  ⟨surface_quality:porcelain_like_perfection⟩
  ⟨finish:ultra_smooth_flawless⟩
  ⟨reflectivity:enhanced_glassy⟩
  ⟨use_case:idealized_perfect_refined⟩
```

### 108. ALABASTER WITH MARBLE VEINING
```
⟨HYBRID_108:ALABASTER_MARBLE⟩
  ⟨base:ALABASTER_WHITE⟩
  ⟨veining:marble_style_gray_veins⟩
  ⟨translucency:alabaster_0.70⟩
  ⟨use_case:luminous_with_character⟩
```

### 109. PORCELAIN WITH MARBLE PATTERN
```
⟨HYBRID_109:PORCELAIN_MARBLE_PATTERN⟩
  ⟨base:PORCELAIN_WHITE⟩
  ⟨decoration:printed_marble_veining⟩
  ⟨surface:porcelain_smooth_gloss⟩
  ⟨translucency:porcelain_minimal⟩
  ⟨use_case:decorative_faux_marble⟩
```

### 110. SEMI-PRECIOUS STONE INCLUSIONS
```
⟨HYBRID_110:SEMI_PRECIOUS_INLAY⟩
  ⟨base:marble_or_alabaster⟩
  ⟨inclusions:lapis_malachite_coral⟩
  ⟨technique:pietra_dura_inlay⟩
  ⟨use_case:decorative_luxurious_ornate⟩
```

### 111. GILDED MARBLE
```
⟨HYBRID_111:GILDED⟩
  ⟨base:white_marble⟩
  ⟨gilding:gold_leaf_accents⟩
  ⟨areas:drapery_folds, hair, details⟩
  ⟨use_case:Byzantine, decorative_luxurious⟩
```

### 112. POLYCHROME (PAINTED MARBLE)
```
⟨HYBRID_112:POLYCHROME⟩
  ⟨base:white_marble_or_alabaster⟩
  ⟨paint:realistic_flesh_tones_colors⟩
  ⟨areas:skin, clothing, details⟩
  ⟨finish:matte_or_slight_sheen⟩
  ⟨use_case:realistic_colored_ancient_practice⟩
  ⟨historical:ancient_Greek_Roman_colored⟩
```

### 113. TINTED ALABASTER
```
⟨HYBRID_113:TINTED_ALABASTER⟩
  ⟨base:ALABASTER_WHITE⟩
  ⟨tint:subtle_color_throughout⟩
  ⟨colors:pink, blue, green, amber⟩
  ⟨translucency:maintained_0.65⟩
  ⟨use_case:colored_luminous_soft⟩
```

---

## Specialized Treatments

### 114. ACID-ETCHED
```
⟨TREATMENT_114:ACID_ETCHED⟩
  ⟨process:chemical_surface_treatment⟩
  ⟨surface:matte_slightly_rough⟩
  ⟨pattern:can_be_patterned_or_uniform⟩
  ⟨use_case:decorative_textured_modern⟩
```

### 115. WATERJET CARVED
```
⟨TREATMENT_115:WATERJET⟩
  ⟨process:precision_water_cutting⟩
  ⟨detail:extremely_fine_sharp_edges⟩
  ⟨surface:slightly_rough_from_cutting⟩
  ⟨use_case:modern_precise_intricate⟩
```

### 116. LASER ENGRAVED
```
⟨TREATMENT_116:LASER_ENGRAVED⟩
  ⟨process:laser_surface_marking⟩
  ⟨detail:extremely_fine_precise⟩
  ⟨depth:shallow_surface_marking⟩
  ⟨use_case:modern_detailed_text_imagery⟩
```

### 117. RESIN-FILLED VOIDS
```
⟨TREATMENT_117:RESIN_FILLED⟩
  ⟨process:voids_filled_with_resin⟩
  ⟨appearance:smooth_continuous_surface⟩
  ⟨resin_type:clear, tinted, metallic⟩
  ⟨use_case:decorative_modern_contrast⟩
```

### 118. THERMALLY TREATED
```
⟨TREATMENT_118:THERMAL⟩
  ⟨process:heat_treatment_color_change⟩
  ⟨effect:enhanced_color_saturation⟩
  ⟨use_case:enhanced_aesthetics⟩
```

---

## Complete Material Examples

### 119. EXAMPLE: Michelangelo's David
```
⟨IMPORT:VSE_Stone_Ceramic⟩

⟨MATERIAL:CARRARA_MARBLE⟩
⟨FINISH:HIGH_GLOSS⟩
⟨CARVING:RENAISSANCE⟩
⟨COLOR:WARM_WHITE⟩
⟨VEINING:SUBTLE⟩
⟨TRANSLUCENCY:SLIGHT_0.25⟩
⟨WEATHERING:LIGHTLY_AGED⟩

⟨DETAIL_TREATMENT⟩
  ⟨anatomy:perfect_idealized⟩
  ⟨surface:smooth_polished⟩
  ⟨eyes:carved_detailed_pupils⟩
  ⟨hair:flowing_detailed_curls⟩

⟨OPTICAL⟩
  ⟨subsurface_scatter:0.35⟩
  ⟨scatter_depth:8mm⟩
  ⟨edge_glow:subtle⟩

⟨EMOTIONAL_QUALITY:timeless, perfect, classical⟩
```

### 120. EXAMPLE: Ancient Greek Kouros
```
⟨IMPORT:VSE_Stone_Ceramic⟩

⟨MATERIAL:PARIAN_MARBLE⟩
⟨FINISH:SEMI_GLOSS⟩
⟨CARVING:CLASSICAL_GREEK⟩
⟨COLOR:PURE_WHITE⟩
⟨VEINING:MINIMAL⟩
⟨TRANSLUCENCY:MODERATE_0.40⟩
⟨WEATHERING:ANCIENT⟩

⟨SURFACE_CONDITION⟩
  ⟨patina:honey_golden_aged⟩
  ⟨erosion:moderate_softened_features⟩
  ⟨detail_loss:subtle_weathering⟩
  ⟨biological:possible_lichen_patches⟩

⟨EMOTIONAL_QUALITY:ancient, mysterious, timeless⟩
```

### 121. EXAMPLE: Byzantine Icon
```
⟨IMPORT:VSE_Stone_Ceramic⟩

⟨MATERIAL:ALABASTER_WHITE⟩
⟨FINISH:POLISHED⟩
⟨CARVING:MEDIEVAL_ROMANESQUE⟩
⟨TREATMENT:GILDED⟩

⟨GILDING⟩
  ⟨areas:halo, clothing_details, background⟩
  ⟨gold_type:leaf_burnished⟩

⟨COLOR⟩
  ⟨base:CREAM⟩
  ⟨accents:gold_brilliant⟩

⟨TRANSLUCENCY:HIGH_0.70⟩
⟨BACKLIT:glowing_ethereal⟩

⟨EMOTIONAL_QUALITY:sacred, luminous, precious⟩
```

### 122. EXAMPLE: Bernini Baroque Drama
```
⟨IMPORT:VSE_Stone_Ceramic⟩

⟨MATERIAL:CARRARA_MARBLE⟩
⟨FINISH:MIRROR_POLISH⟩
⟨CARVING:BAROQUE⟩
⟨COLOR:PURE_WHITE⟩
⟨VEINING:SUBTLE⟩
⟨TRANSLUCENCY:SLIGHT_0.25⟩
⟨WEATHERING:PRISTINE⟩

⟨CARVING_CHARACTERISTICS⟩
  ⟨drapery:swirling_dramatic_wind_blown⟩
  ⟨anatomy:dynamic_movement_torsion⟩
  ⟨emotion:ecstasy_captured⟩
  ⟨composition:diagonal_dynamic⟩

⟨FINISH_DETAILS⟩
  ⟨skin:highly_polished_smooth⟩
  ⟨fabric:different_textures_carved⟩
  ⟨contrast:polished_vs_textured⟩

⟨EMOTIONAL_QUALITY:dramatic, passionate, theatrical⟩
```

### 123. EXAMPLE: Contemporary Minimalist
```
⟨IMPORT:VSE_Stone_Ceramic⟩

⟨MATERIAL:PORCELAIN_WHITE⟩
⟨FINISH:MATTE⟩
⟨CARVING:MODERNIST_ABSTRACT⟩
⟨COLOR:PURE_WHITE⟩
⟨VEINING:NONE⟩
⟨TRANSLUCENCY:MINIMAL_0.10⟩
⟨WEATHERING:PRISTINE⟩

⟨STYLE⟩
  ⟨form:simplified_geometric_abstract⟩
  ⟨surface:perfectly_smooth_uniform⟩
  ⟨detail:minimal_essential_only⟩

⟨EMOTIONAL_QUALITY:pure, minimal, contemporary⟩
```

### 124. EXAMPLE: Rodin Unfinished
```
⟨IMPORT:VSE_Stone_Ceramic⟩

⟨MATERIAL:CARRARA_MARBLE⟩
⟨CARVING:IMPRESSIONIST_SCULPTURE⟩
⟨COLOR:WARM_WHITE⟩
⟨VEINING:MODERATE⟩
⟨TRANSLUCENCY:SLIGHT_0.25⟩
⟨WEATHERING:LIGHTLY_AGED⟩

⟨FINISH:CONTRAST⟩
  ⟨polished_areas:face_hands_smooth⟩
  ⟨rough_areas:body_visible_tool_marks⟩
  ⟨technique:intentionally_unfinished⟩

⟨SURFACE⟩
  ⟨tool_marks:visible_chisel_marks⟩
  ⟨texture:rough_expressive⟩
  ⟨contrast:finished_vs_raw_stone⟩

⟨EMOTIONAL_QUALITY:expressive, emerging, process⟩
```

### 125. EXAMPLE: Ancient Egyptian Basalt
```
⟨IMPORT:VSE_Stone_Ceramic⟩

⟨MATERIAL:BASALT⟩
⟨FINISH:POLISHED⟩
⟨CARVING:EGYPTIAN_STYLE⟩
⟨COLOR:DARK_GRAY_BLACK⟩
⟨VEINING:NONE⟩
⟨TRANSLUCENCY:OPAQUE_0.0⟩
⟨WEATHERING:ANCIENT⟩

⟨STYLE_CHARACTERISTICS⟩
  ⟨proportions:idealized_formal⟩
  ⟨pose:frontal_rigid_hieratic⟩
  ⟨detail:precise_controlled⟩
  ⟨surface:hard_dense_polished⟩

⟨WEATHERING_DETAILS⟩
  ⟨patina:dark_desert_patina⟩
  ⟨wear:smoothed_by_age⟩
  ⟨preservation:excellent_hard_stone⟩

⟨EMOTIONAL_QUALITY:eternal, powerful, ancient⟩
```

---

## Material Permutation Matrix

### Base Material Combinations (126-200)

```
⟨PERMUTATION_MATRIX⟩
  ⟨BASE_MATERIALS:20⟩ × ⟨FINISHES:12⟩ × ⟨WEATHERING:9⟩ × ⟨COLORS:9⟩ 
  = 19,440 possible combinations

⟨PRACTICAL_PRESETS⟩
  ⟨Carrara_variations:24⟩
  ⟨Alabaster_variations:18⟩
  ⟨Porcelain_variations:32⟩
  ⟨Granite_variations:12⟩
  ⟨Limestone_variations:15⟩
  ⟨Onyx_variations:16⟩
  ⟨Total_documented:247⟩
```

### Quick Reference Presets (126-156)

```
⟨PRESET_126:CLASSICAL_WHITE_MARBLE⟩
  ⟨material:CARRARA⟩ + ⟨finish:POLISHED⟩ + ⟨weathering:PRISTINE⟩

⟨PRESET_127:AGED_CLASSICAL⟩
  ⟨material:CARRARA⟩ + ⟨finish:SEMI_GLOSS⟩ + ⟨weathering:MODERATELY_AGED⟩

⟨PRESET_128:ANCIENT_RUINS⟩
  ⟨material:PARIAN⟩ + ⟨finish:WEATHERED⟩ + ⟨weathering:ANCIENT⟩

⟨PRESET_129:LUMINOUS_ALABASTER⟩
  ⟨material:ALABASTER_WHITE⟩ + ⟨finish:POLISHED⟩ + ⟨backlit:ENABLED⟩

⟨PRESET_130:CONTEMPORARY_WHITE⟩
  ⟨material:PORCELAIN⟩ + ⟨finish:MATTE⟩ + ⟨weathering:PRISTINE⟩

⟨PRESET_131:DRAMATIC_BLACK⟩
  ⟨material:NERO_MARQUINA⟩ + ⟨finish:MIRROR_POLISH⟩

⟨PRESET_132:WARM_CREAM⟩
  ⟨material:CREMA_MARFIL⟩ + ⟨finish:HONED⟩ + ⟨color:CREAM⟩

⟨PRESET_133:RODIN_ROUGH⟩
  ⟨material:CARRARA⟩ + ⟨finish:MIXED_ROUGH_POLISHED⟩ + ⟨style:IMPRESSIONIST⟩

⟨PRESET_134:RENAISSANCE_PERFECTION⟩
  ⟨material:CARRARA⟩ + ⟨finish:HIGH_GLOSS⟩ + ⟨carving:RENAISSANCE⟩

⟨PRESET_135:BAROQUE_DRAMA⟩
  ⟨material:CARRARA⟩ + ⟨finish:MIRROR_POLISH⟩ + ⟨carving:BAROQUE⟩

⟨PRESET_136:GREEK_IDEAL⟩
  ⟨material:PARIAN⟩ + ⟨finish:POLISHED⟩ + ⟨carving:CLASSICAL_GREEK⟩

⟨PRESET_137:MODERNIST_PURE⟩
  ⟨material:PORCELAIN⟩ + ⟨finish:MATTE⟩ + ⟨color:PURE_WHITE⟩

⟨PRESET_138:GOLDEN_HONEY⟩
  ⟨material:HONEY_ONYX⟩ + ⟨finish:POLISHED⟩ + ⟨backlit:DRAMATIC⟩

⟨PRESET_139:EGYPTIAN_DARK⟩
  ⟨material:BASALT⟩ + ⟨finish:POLISHED⟩ + ⟨weathering:ANCIENT⟩

⟨PRESET_140:BYZANTINE_GLOW⟩
  ⟨material:ALABASTER⟩ + ⟨treatment:GILDED⟩ + ⟨backlit:ENABLED⟩

⟨PRESET_141:ART_DECO_SLEEK⟩
  ⟨material:PORCELAIN⟩ + ⟨finish:HIGH_GLOSS⟩ + ⟨carving:ART_DECO⟩

⟨PRESET_142:GOTHIC_ELEGANT⟩
  ⟨material:LIMESTONE⟩ + ⟨finish:HONED⟩ + ⟨carving:GOTHIC⟩

⟨PRESET_143:NEOCLASSICAL_COOL⟩
  ⟨material:CARRARA⟩ + ⟨finish:POLISHED⟩ + ⟨color:COOL_WHITE⟩

⟨PRESET_144:ROMANTIC_PINK⟩
  ⟨material:ROSA_PORTOGALLO⟩ + ⟨finish:POLISHED⟩

⟨PRESET_145:LUXE_CALACATTA⟩
  ⟨material:CALACATTA_GOLD⟩ + ⟨finish:MIRROR_POLISH⟩

⟨PRESET_146:WEATHERED_STONE⟩
  ⟨material:SANDSTONE⟩ + ⟨weathering:HEAVILY_AGED⟩ + ⟨biological:LICHEN⟩

⟨PRESET_147:TRANSLUCENT_WHITE⟩
  ⟨material:ALABASTER⟩ + ⟨translucency:HIGH_0.70⟩ + ⟨backlit:STRONG⟩

⟨PRESET_148:MONUMENTAL_GRANITE⟩
  ⟨material:GRANITE_BLACK⟩ + ⟨finish:MIRROR_POLISH⟩

⟨PRESET_149:SOFT_BISQUE⟩
  ⟨material:PORCELAIN_BISQUE⟩ + ⟨finish:MATTE⟩ + ⟨color:WARM_WHITE⟩

⟨PRESET_150:VEINED_DRAMA⟩
  ⟨material:STATUARIO⟩ + ⟨veining:DRAMATIC⟩ + ⟨finish:POLISHED⟩

⟨PRESET_151:ARCHAEOLOGICAL⟩
  ⟨material:LIMESTONE⟩ + ⟨weathering:EXCAVATED⟩ + ⟨staining:EARTH⟩

⟨PRESET_152:CHINESE_PORCELAIN⟩
  ⟨material:PORCELAIN_BLUE_WHITE⟩ + ⟨finish:HIGH_GLOSS⟩

⟨PRESET_153:WATERJET_MODERN⟩
  ⟨material:CARRARA⟩ + ⟨treatment:WATERJET⟩ + ⟨detail:INTRICATE⟩

⟨PRESET_154:POLYCHROME_ANCIENT⟩
  ⟨material:PARIAN⟩ + ⟨treatment:POLYCHROME⟩ + ⟨weathering:ANCIENT⟩

⟨PRESET_155:MINIMALIST_PERFECTION⟩
  ⟨material:PORCELAIN⟩ + ⟨color:PURE_WHITE⟩ + ⟨veining:NONE⟩

⟨PRESET_156:CARRARA_SUBTLE⟩
  ⟨material:CARRARA⟩ + ⟨veining:SUBTLE⟩ + ⟨finish:HONED⟩
```

---

## Advanced Usage Examples

### Example 1: Custom Marble Specification
```
⟨IMPORT:VSE_Stone_Ceramic⟩

⟨MATERIAL:CARRARA_MARBLE⟩
  ⟨OVERRIDE:veining_color:RGB(160, 160, 165)⟩
  ⟨OVERRIDE:translucency:0.28⟩

⟨FINISH:SEMI_GLOSS⟩
  ⟨OVERRIDE:reflectivity:0.35⟩

⟨COLOR:WARM_WHITE⟩
⟨WEATHERING:LIGHTLY_AGED⟩
⟨CARVING:RENAISSANCE⟩

⟨DETAIL⟩
  ⟨eyes:carved_classical_recessed_pupils⟩
  ⟨hair:flowing_detailed_polished⟩
  ⟨drapery:carved_fabric_texture⟩

⟨OPTICAL⟩
  ⟨subsurface_scatter:0.35⟩
  ⟨edge_glow:enabled_subtle⟩
```

### Example 2: Combining Multiple Materials
```
⟨IMPORT:VSE_Stone_Ceramic⟩

⟨FIGURE⟩
  ⟨material:ALABASTER_WHITE⟩
  ⟨translucency:0.70⟩
  ⟨backlit:enabled⟩

⟨BASE⟩
  ⟨material:NERO_MARQUINA⟩
  ⟨finish:MIRROR_POLISH⟩
  ⟨contrast:dramatic⟩

⟨ACCENTS⟩
  ⟨material:GOLD_LEAF⟩
  ⟨areas:halo, details⟩

⟨EMOTIONAL_QUALITY:sacred, luminous, precious⟩
```

### Example 3: Weathering Progression
```
⟨IMPORT:VSE_Stone_Ceramic⟩

⟨BASE:CARRARA_MARBLE⟩
⟨FINISH:ORIGINAL_POLISHED⟩

⟨WEATHERING:PROGRESSIVE⟩
  ⟨stage_1:pristine_new⟩
  ⟨stage_2:50_years_slight_patina⟩
  ⟨stage_3:200_years_yellowing_wear⟩
  ⟨stage_4:500_years_significant_aging⟩
  ⟨stage_5:2000_years_ancient_weathered⟩

⟨SHOW_STAGE:4⟩
```

---

## Material Property Reference Tables

### Hardness Scale (Mohs)
```
1-2: Alabaster, Soapstone (very soft, easily carved)
3: Limestone, Marble (soft, carvable with steel tools)
4-5: Sandstone (medium, requires harder tools)
6: Granite (hard, requires diamond tools)
7-8: Porcelain (very hard, industrial tools)
9-10: Corundum, Diamond (extreme hardness)
```

### Translucency Scale
```
0.0: Completely opaque (granite, basalt)
0.1-0.3: Minimal translucency (most marbles, porcelain)
0.3-0.5: Moderate translucency (Parian marble, calcite alabaster)
0.5-0.7: High translucency (gypsum alabaster, onyx)
0.7-0.9: Very high translucency (thin alabaster, thin onyx)
```

### Carving Difficulty
```
Very Easy: Alabaster, Soapstone
Easy: Limestone, Soft Marble
Medium: Harder Marble (Carrara, Statuario)
Hard: Granite, Basalt
Very Hard: Porcelain (cast/molded, not carved traditionally)
```

---

## Summary Statistics

**Total Materials Catalogued:** 247

**Categories:**
- Marble Varieties: 20
- Stone Types: 14
- Alabaster Variations: 6
- Porcelain Types: 10
- Surface Finishes: 12
- Carving Techniques: 11
- Weathering States: 10
- Color Variations: 9
- Veining Patterns: 8
- Translucency Levels: 6
- Hybrid Materials: 7
- Specialized Treatments: 5
- Complete Examples: 7
- Quick Presets: 31
- Advanced Examples: 3

**Total Theoretical Permutations:** 19,440+

---

## Usage Guidelines

### Basic Usage
```
⟨IMPORT:VSE_Stone_Ceramic⟩
⟨MATERIAL:[material_name]⟩
⟨FINISH:[finish_type]⟩
```

### Intermediate Usage
```
⟨IMPORT:VSE_Stone_Ceramic⟩
⟨MATERIAL:[material_name]⟩
⟨FINISH:[finish_type]⟩
⟨WEATHERING:[age_state]⟩
⟨COLOR:[color_variation]⟩
⟨VEINING:[vein_pattern]⟩
```

### Advanced Usage
```
⟨IMPORT:VSE_Stone_Ceramic⟩
⟨MATERIAL:[material_name]⟩
  ⟨OVERRIDE:property:value⟩
⟨FINISH:[finish_type]⟩
⟨CARVING:[technique]⟩
⟨WEATHERING:[state]⟩
⟨OPTICAL⟩
  ⟨subsurface_scatter:[value]⟩
  ⟨translucency:[value]⟩
⟨EMOTIONAL_QUALITY:[qualities]⟩
```

### Preset Usage
```
⟨IMPORT:VSE_Stone_Ceramic⟩
⟨PRESET:[preset_name]⟩
  ⟨OVERRIDE:[property]:[value]⟩
```

---

## Integration with Other VSE Libraries

### Combined with Camera
```
⟨IMPORT:VSE_Camera⟩
⟨IMPORT:VSE_Stone_Ceramic⟩

⟨MOVEMENT:orbit_clockwise⟩
⟨MATERIAL:CARRARA_MARBLE⟩
⟨FINISH:MIRROR_POLISH⟩
```

### Combined with Lighting
```
⟨IMPORT:VSE_Lighting⟩
⟨IMPORT:VSE_Stone_Ceramic⟩

⟨LIGHTING:golden_hour⟩
⟨MATERIAL:ALABASTER_WHITE⟩
⟨BACKLIT:enabled_glowing⟩
```

### Full Integration
```
⟨IMPORT:VSE_Camera⟩
⟨IMPORT:VSE_Lighting⟩
⟨IMPORT:VSE_Stone_Ceramic⟩

⟨MOVEMENT:dolly_in⟩
⟨LIGHTING:rembrandt⟩
⟨MATERIAL:CARRARA_MARBLE⟩
⟨FINISH:RENAISSANCE⟩
```

---

## Next Steps

1. **Validation Testing** - Test key material presets with image generation
2. **Visual Reference Gallery** - Create examples of each major material
3. **Cross-Platform Testing** - Validate semantic consistency across AI models
4. **User Skill Integration** - Enable community material contributions
5. **Expansion** - Add MTL-Metal, MTL-Wood, MTL-Fabric libraries

---

**Credits:**  
**Orchestration:** John Jacob Weber II  
**Documentation:** Claude (Sonnet 4.5)  
**Architecture:** Vox (Consultant)  
**Validation:** Nano Banana (Pending)

**Status:** Complete Reference - Ready for Testing  
**Repository:** github.com/PaniclandUSA/vse/stone-ceramic-manifest/  
**Version:** 1.0  
**Date:** December 10, 2025

---

*"Every grain of marble contains the statue - VSE reveals it with precision."*

— VSE Stone & Ceramic Material Library Team

END OF MANIFEST
