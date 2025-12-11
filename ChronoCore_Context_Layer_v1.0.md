# CHRONOCORE CONTEXT LAYER v1.0
## Diegetic Reality & World State - "Where is This Happening in the World & Lore?"

**Created:** December 10, 2025  
**Project:** ChronoCore / VSE Integration  
**Orchestrator:** John Jacob Weber II  
**Documentation:** Claude (Sonnet 4.5)  
**Concept Architect:** Vox  
**Status:** ✅ PRODUCTION READY  

---

## Executive Summary

The **ChronoCore Context Layer** defines the **diegetic reality** in which events occur - the time, place, cultural constraints, lore, and ongoing world state that inform VSE material/lighting/camera defaults and ensure cross-project consistency.

**The Missing Piece:**

ChronoCore and VSE beautifully describe **the moment** (when/what/how).  
Context Layer provides **the world** (where/who/why in terms of lore).

**What Context Solves:**

Without Context, every scene is isolated - a cool shot with no world connection.  
With Context, Whispers, Medusa Legacy, Flip'd feel like they happen in **consistent, living worlds**.

**The Complete Stack:**

```
LEVEL 0: CONCEPTION (Why - narrative intent)
LEVEL 0.5: CONTEXT (Where - world/lore/state) ← NEW
    ↓
LEVEL 1: ChronoCore LATTICE (When - causal events)
LEVEL 2: MATERIAL (What - physical properties)
LEVEL 3: LIGHTING (How it feels - atmosphere)
LEVEL 4: CAMERA (How it's seen - perspective)
LEVEL 5: COMPOSITION (How it's arranged - spatial)
    ↓
LEVEL 6: CONVERGENCE (How everything agrees) ← Coming next
```

---

## Table of Contents

1. [Core Architecture](#core-architecture)
2. [Context Block Schema](#context-block-schema)
3. [Location Profiles](#location-profiles)
4. [Temporal Context](#temporal-context)
5. [Social & Power Dynamics](#social--power-dynamics)
6. [Magic & Technology Levels](#magic--technology-levels)
7. [Historical References](#historical-references)
8. [World State & Continuity](#world-state--continuity)
9. [VSE Auto-Derivation from Context](#vse-auto-derivation-from-context)
10. [Project Context Libraries](#project-context-libraries)

---

## Core Architecture

### What Context Controls

```
⟨CONTEXT⟩
  
  ⟨LOCATION⟩ → Where physically in the world
  ⟨WORLD_TIME⟩ → When in diegetic timeline
  ⟨SOCIAL_CONTEXT⟩ → Public/private, formal/informal
  ⟨POWER_DYNAMICS⟩ → Who holds authority/agency
  ⟨CULTURAL_CONSTRAINTS⟩ → Rules, taboos, customs
  ⟨MAGIC_LEVEL⟩ → Presence/absence of supernatural
  ⟨TECH_LEVEL⟩ → Technological sophistication
  ⟨HISTORY⟩ → Past events that matter now
  ⟨WORLD_STATE⟩ → Ongoing conditions/situations
```

### Integration with ChronoCore

```
⟨CHRONO_NODE:event_id⟩
  ⟨CONTEXT_BLOCK:location_context⟩ ← NEW
  ⟨AGENTS:who_acts⟩
  ⟨CONSEQUENCES:what_changes⟩
  ⟨AFFECT:emotional_result⟩
```

Context Block **travels with each ChronoNode**, providing world grounding for every event.

---

## Context Block Schema

### Complete Context Block

```
⟨CONTEXT_BLOCK:unique_id⟩
  
  ⟨LOCATION⟩
    ⟨id:location_identifier⟩
    ⟨name:human_readable_name⟩
    ⟨type:urban|rural|wilderness|interior|liminal⟩
    ⟨scale:intimate|local|regional|cosmic⟩
    ⟨ambient_conditions:weather|temperature|season⟩
  
  ⟨WORLD_TIME⟩
    ⟨era:age_period_epoch⟩
    ⟨season:spring|summer|autumn|winter⟩
    ⟨time_of_day:dawn|morning|noon|afternoon|dusk|night⟩
    ⟨phase:beginning|middle|end⟩
    ⟨calendar_date:specific_if_relevant⟩
  
  ⟨SOCIAL_CONTEXT⟩
    ⟨publicity:public|semi_public|private|secret⟩
    ⟨formality:ritual|formal|informal|intimate⟩
    ⟨witnesses:none|few|crowd|entire_community⟩
    ⟨social_stakes:none|moderate|high|catastrophic⟩
  
  ⟨POWER_CONTEXT⟩
    ⟨authority_holder:who_has_official_power⟩
    ⟨actual_power:who_has_real_influence⟩
    ⟨power_dynamic:balanced|skewed|contested⟩
    ⟨agency_distribution:equal|hierarchical|chaotic⟩
  
  ⟨CULTURAL_CONSTRAINTS⟩
    ⟨rules:explicit_laws_customs⟩
    ⟨taboos:forbidden_actions_topics⟩
    ⟨expectations:normal_behavior⟩
    ⟨transgression_cost:low|moderate|severe|deadly⟩
  
  ⟨MAGIC_LEVEL⟩
    ⟨presence:none|subtle|overt|dominant⟩
    ⟨acceptance:unknown|feared|tolerated|celebrated⟩
    ⟨source:divine|natural|learned|innate⟩
    ⟨visibility:hidden|ambiguous|obvious⟩
  
  ⟨TECH_LEVEL⟩
    ⟨era:stone_age|bronze|iron|medieval|renaissance|industrial|modern|futuristic⟩
    ⟨specific:relevant_technologies_present⟩
    ⟨anachronisms:intentional_tech_mismatches⟩
  
  ⟨HISTORICAL_REFS⟩
    ⟨prior_events:ids_of_past_nodes⟩
    ⟨significance:how_history_matters_now⟩
    ⟨memory:remembered|forgotten|contested⟩
  
  ⟨WORLD_STATE⟩
    ⟨current_crisis:ongoing_problems⟩
    ⟨stability:peaceful|tense|conflict|war⟩
    ⟨resources:abundant|scarce|contested⟩
    ⟨morale:hopeful|anxious|desperate|resigned⟩
```

### Minimal Context Block

```
⟨CONTEXT_BLOCK:simple⟩
  ⟨LOCATION:forest_clearing⟩
  ⟨WORLD_TIME:dusk_autumn⟩
  ⟨MAGIC_LEVEL:subtle⟩
```

Even minimal specification provides useful world grounding.

---

## Location Profiles

### Location Schema

```
⟨LOCATION_PROFILE:unique_id⟩
  
  ⟨IDENTITY⟩
    ⟨name:proper_name⟩
    ⟨alternate_names:aliases_historical_names⟩
    ⟨significance:why_it_matters⟩
  
  ⟨GEOGRAPHY⟩
    ⟨type:city|village|forest|mountain|coast|ruins|liminal⟩
    ⟨climate:temperate|tropical|arctic|desert|variable⟩
    ⟨terrain:flat|hilly|mountainous|water|mixed⟩
    ⟨size:tiny|small|moderate|large|vast⟩
  
  ⟨ARCHITECTURE⟩
    ⟨style:vernacular|classical|gothic|modern|organic⟩
    ⟨material:stone|wood|metal|glass|composite⟩
    ⟨condition:pristine|maintained|weathered|ruined⟩
    ⟨scale:intimate|domestic|monumental|cosmic⟩
  
  ⟨INHABITANTS⟩
    ⟨population:none|sparse|moderate|dense⟩
    ⟨species:human|fae|hybrid|other⟩
    ⟨culture:dominant_cultural_identity⟩
  
  ⟨ATMOSPHERE⟩
    ⟨ambient_light:natural_sources⟩
    ⟨ambient_sound:environmental_acoustics⟩
    ⟨ambient_scent:olfactory_character⟩
    ⟨emotional_quality:welcoming|neutral|oppressive|uncanny⟩
  
  ⟨HISTORY⟩
    ⟨founded:when_established⟩
    ⟨major_events:significant_occurrences⟩
    ⟨current_state:present_condition⟩
  
  ⟨VSE_BIASES⟩
    ⟨material:typical_materials_present⟩
    ⟨lighting:natural_light_conditions⟩
    ⟨camera:typical_framing_approach⟩
    ⟨composition:spatial_characteristics⟩
```

### Example Locations

**Erranham Square (Whispers):**

```
⟨LOCATION_PROFILE:ERRANHAM_SQUARE⟩
  ⟨IDENTITY⟩
    ⟨name:Erranham Town Square⟩
    ⟨significance:civic_center_fae_memorial⟩
  
  ⟨GEOGRAPHY⟩
    ⟨type:urban_plaza⟩
    ⟨climate:temperate_coastal⟩
    ⟨size:moderate_town_square⟩
  
  ⟨ARCHITECTURE⟩
    ⟨style:new_england_colonial_with_fae_influences⟩
    ⟨material:weathered_gray_stone_cobblestone⟩
    ⟨condition:aging_but_maintained⟩
    ⟨monuments:central_fae_statue_weathered⟩
  
  ⟨INHABITANTS⟩
    ⟨population:moderate_small_town⟩
    ⟨species:primarily_human_fae_hidden⟩
    ⟨culture:new_england_maritime_with_hidden_fae_lore⟩
  
  ⟨ATMOSPHERE⟩
    ⟨ambient_light:overcast_coastal_gray⟩
    ⟨ambient_sound:wind_waves_distant_gulls⟩
    ⟨emotional_quality:melancholic_haunted_beautiful⟩
  
  ⟨HISTORY⟩
    ⟨founded:1600s_colonial_settlement⟩
    ⟨major_events:fae_binding_1700s_lighthouse_tragedy⟩
    ⟨current_state:modern_decline_hidden_magic_awakening⟩
  
  ⟨VSE_BIASES⟩
    ⟨material:WEATHERED_LIMESTONE, GRAY_GRANITE, AGED_BRONZE⟩
    ⟨lighting:OVERCAST_COASTAL, GOLDEN_HOUR_MELANCHOLIC⟩
    ⟨camera:WIDE_ENVIRONMENTAL, CRANE_UP_MONUMENTAL⟩
    ⟨composition:GOLDEN_ISOLATION, ENVIRONMENTAL_PORTRAIT⟩
```

**Medusa's Island (Medusa Legacy):**

```
⟨LOCATION_PROFILE:MEDUSA_ISLAND⟩
  ⟨IDENTITY⟩
    ⟨name:Sarpedon (ancient), The Gorgon's Isle (modern)⟩
    ⟨significance:medusa_domain_mythic_boundary⟩
  
  ⟨GEOGRAPHY⟩
    ⟨type:isolated_mediterranean_island⟩
    ⟨climate:mediterranean_harsh_winds⟩
    ⟨terrain:rocky_cliff_cave_systems⟩
    ⟨size:small_island_5km_diameter⟩
  
  ⟨ARCHITECTURE⟩
    ⟨style:ancient_greek_ruins_cave_dwellings⟩
    ⟨material:limestone_marble_obsidian⟩
    ⟨condition:ruins_partially_reclaimed_nature⟩
    ⟨scale:domestic_ruins_monumental_cliffs⟩
  
  ⟨INHABITANTS⟩
    ⟨population:medusa_alone_plus_statue_garden⟩
    ⟨species:gorgon_petrified_humans⟩
  
  ⟨ATMOSPHERE⟩
    ⟨ambient_light:harsh_mediterranean_sun_deep_shadows⟩
    ⟨ambient_sound:wind_waves_silence_serpents⟩
    ⟨emotional_quality:beautiful_terrible_tragic_cursed⟩
  
  ⟨HISTORY⟩
    ⟨founded:ancient_exile_athena_curse⟩
    ⟨major_events:perseus_quest_centuries_isolation⟩
    ⟨current_state:eternal_cursed_boundary⟩
  
  ⟨MAGIC_LEVEL:dominant⟩
    ⟨petrification_curse_always_active⟩
    ⟨divine_punishment_tangible⟩
  
  ⟨VSE_BIASES⟩
    ⟨material:CARRARA_MARBLE, OBSIDIAN, LIMESTONE_SUN_BLEACHED⟩
    ⟨lighting:HARSH_MIDDAY, DRAMATIC_CHIAROSCURO, LOW_KEY_SHADOW⟩
    ⟨camera:LOW_ANGLE_POWER, SLOW_APPROACH_CAUTIOUS⟩
    ⟨composition:STATUE_REVERENCE, SILHOUETTE_DRAMA, HEROIC_WIDE⟩
```

---

## Temporal Context

### World Time Schema

```
⟨WORLD_TIME⟩
  
  ⟨ERA⟩
    ⟨name:age_of_faerie|modern_day|post_apocalyptic⟩
    ⟨duration:how_long_this_age_has_lasted⟩
    ⟨defining_trait:what_makes_this_era_distinct⟩
  
  ⟨SEASON⟩
    ⟨name:spring|summer|autumn|winter⟩
    ⟨phase:early|peak|late⟩
    ⟨relevance:how_season_affects_scene⟩
  
  ⟨TIME_OF_DAY⟩
    ⟨hour:specific_if_relevant⟩
    ⟨phase:dawn|morning|noon|afternoon|dusk|evening|night|midnight⟩
    ⟨quality:golden|blue|harsh|gentle|dark⟩
  
  ⟨PHASE⟩
    ⟨narrative:beginning|rising|climax|falling|end⟩
    ⟨cycle:new_moon|full_moon|eclipse|solstice|equinox⟩
    ⟨significance:why_this_moment_matters_temporally⟩
  
  ⟨CALENDAR⟩
    ⟨date:specific_date_if_world_uses_calendar⟩
    ⟨anniversary:connection_to_historical_event⟩
    ⟨ritual_time:sacred_day_festival_observance⟩
```

### Example Temporal Contexts

```
⟨WORLD_TIME:WHISPERS_AUTUMN_DUSK⟩
  ⟨ERA:modern_day_fae_awakening⟩
  ⟨SEASON:autumn_late⟩
  ⟨TIME_OF_DAY:dusk_approaching_darkness⟩
  ⟨PHASE:threshold_moment_veil_thinning⟩
  ⟨VSE_LIGHTING_BIAS:BLUE_HOUR, GOLDEN_HOUR_FADING⟩

⟨WORLD_TIME:MEDUSA_ETERNAL_NOON⟩
  ⟨ERA:mythic_ancient_greece⟩
  ⟨SEASON:endless_summer⟩
  ⟨TIME_OF_DAY:noon_harsh_unchanging⟩
  ⟨PHASE:eternal_cursed_stasis⟩
  ⟨VSE_LIGHTING_BIAS:HARSH_MIDDAY, UNFORGIVING_SUN⟩
```

---

## Social & Power Dynamics

### Social Context Schema

```
⟨SOCIAL_CONTEXT⟩
  
  ⟨PUBLICITY⟩
    ⟨level:public|semi_public|private|secret|liminal⟩
    ⟨witnesses:count_and_nature_of_observers⟩
    ⟨visibility:who_can_see_who_knows⟩
    ⟨consequences:what_visibility_means⟩
  
  ⟨FORMALITY⟩
    ⟨level:ritual|formal|casual|intimate|transgressive⟩
    ⟨rules:explicit_behavioral_expectations⟩
    ⟨dress:required_attire_presentation⟩
    ⟨speech:formal_register_casual_coded⟩
  
  ⟨STAKES⟩
    ⟨personal:individual_consequences⟩
    ⟨social:community_impact⟩
    ⟨political:power_dynamics_shift⟩
    ⟨cosmic:metaphysical_reality_change⟩
```

### Power Context Schema

```
⟨POWER_CONTEXT⟩
  
  ⟨AUTHORITY_HOLDER⟩
    ⟨official:title_role_formal_position⟩
    ⟨legitimacy:recognized|contested|usurped⟩
    ⟨scope:what_they_officially_control⟩
  
  ⟨ACTUAL_POWER⟩
    ⟨wielder:who_actually_influences_events⟩
    ⟨source:money|magic|violence|knowledge|charisma⟩
    ⟨scope:what_they_actually_control⟩
  
  ⟨POWER_DYNAMIC⟩
    ⟨distribution:balanced|skewed|monopolized|fractured⟩
    ⟨stability:stable|contested|shifting|collapsing⟩
    ⟨violence_potential:none|latent|imminent|active⟩
  
  ⟨AGENCY⟩
    ⟨who_acts:list_of_agents⟩
    ⟨who_cannot:constrained_parties⟩
    ⟨who_watches:observers_without_agency⟩
```

### Example Power Contexts

```
⟨POWER_CONTEXT:ERRANHAM_TOWN_MEETING⟩
  ⟨AUTHORITY_HOLDER:town_mayor_official⟩
  ⟨ACTUAL_POWER:eldercouncil_hidden_fae_aligned⟩
  ⟨POWER_DYNAMIC:surface_democracy_hidden_oligarchy⟩
  ⟨AGENCY:
    mayor_speaks_but_controlled|
    elder_council_decides|
    townsfolk_witness_no_voice|
    audrey_observes_records⟩

⟨POWER_CONTEXT:MEDUSA_ISLAND⟩
  ⟨AUTHORITY_HOLDER:medusa_absolute_cursed_sovereign⟩
  ⟨ACTUAL_POWER:medusa_gaze_unstoppable⟩
  ⟨POWER_DYNAMIC:absolute_divine_mandate⟩
  ⟨AGENCY:
    medusa_total_but_trapped|
    visitors_none_become_statues|
    perseus_hero_exception_divine_favor⟩
```

---

## Magic & Technology Levels

### Magic Level Schema

```
⟨MAGIC_LEVEL⟩
  
  ⟨PRESENCE⟩
    ⟨amount:none|rare|common|ubiquitous|dominant⟩
    ⟨reliability:myth|uncertain|reliable|physical_law⟩
  
  ⟨ACCEPTANCE⟩
    ⟨social:unknown|feared|tolerated|accepted|celebrated|mandatory⟩
    ⟨legal:forbidden|restricted|regulated|free⟩
  
  ⟨SOURCE⟩
    ⟨origin:divine|fae|natural|learned|innate|technological⟩
    ⟨access:birthright|study|gift|curse|artifact⟩
  
  ⟨VISIBILITY⟩
    ⟨manifestation:invisible|ambiguous|subtle|obvious|spectacular⟩
    ⟨proof:deniable|uncertain|undeniable⟩
  
  ⟨COST⟩
    ⟨personal:none|exhaustion|aging|corruption|death⟩
    ⟨social:none|stigma|exile|execution⟩
    ⟨metaphysical:none|debt|binding|soul_damage⟩
  
  ⟨VSE_IMPLICATIONS⟩
    ⟨material:magical_substances_present⟩
    ⟨lighting:unnatural_light_sources⟩
    ⟨effects:visual_manifestations⟩
```

### Technology Level Schema

```
⟨TECH_LEVEL⟩
  
  ⟨ERA⟩
    ⟨primary:neolithic|bronze|iron|medieval|renaissance|industrial|modern|future⟩
    ⟨specific:relevant_technologies⟩
  
  ⟨ANACHRONISMS⟩
    ⟨intentional:deliberately_out_of_place_tech⟩
    ⟨explanation:why_anachronism_exists⟩
    ⟨example:clockwork_in_bronze_age|magic_powered_electricity⟩
  
  ⟨DISTRIBUTION⟩
    ⟨universal:available_to_all⟩
    ⟨restricted:controlled_by_few⟩
    ⟨uneven:some_have_much_more⟩
  
  ⟨VSE_IMPLICATIONS⟩
    ⟨material:available_materials_fabrication⟩
    ⟨lighting:artificial_light_sources_present⟩
    ⟨environment:infrastructure_artifacts⟩
```

### Example Magic/Tech Contexts

```
⟨MAGIC_TECH:WHISPERS⟩
  ⟨MAGIC_LEVEL⟩
    ⟨presence:common_but_hidden⟩
    ⟨acceptance:forgotten_reawakening⟩
    ⟨source:fae_natural⟩
    ⟨visibility:subtle_ambiguous⟩
  ⟨TECH_LEVEL⟩
    ⟨era:modern_2020s⟩
    ⟨specific:smartphones_internet_but_intermittent⟩

⟨MAGIC_TECH:MEDUSA⟩
  ⟨MAGIC_LEVEL⟩
    ⟨presence:dominant_divine⟩
    ⟨acceptance:feared_undeniable⟩
    ⟨source:divine_curse_athena⟩
    ⟨visibility:spectacular_instant_petrification⟩
  ⟨TECH_LEVEL⟩
    ⟨era:bronze_age_greece⟩
    ⟨specific:bronze_weapons_sailing_ships_classical_architecture⟩
```

---

## Historical References

### History Link Schema

```
⟨HISTORICAL_REFS⟩
  
  ⟨PRIOR_EVENTS⟩
    ⟨event_ids:chrono_node_ids_of_past⟩
    ⟨timeframe:how_long_ago⟩
    ⟨causality:how_past_affects_present⟩
  
  ⟨SIGNIFICANCE⟩
    ⟨remembered:living_memory|historical_record|myth|forgotten⟩
    ⟨interpreted:consensus|contested|lost|rewritten⟩
    ⟨affects_now:how_history_shapes_present⟩
  
  ⟨CONTINUITY⟩
    ⟨threads:ongoing_consequences⟩
    ⟨echoes:patterns_repeating⟩
    ⟨prophecy:foreshadowed_future⟩
```

### Example Historical Context

```
⟨HISTORICAL_REFS:ERRANHAM_LIGHTHOUSE⟩
  ⟨PRIOR_EVENTS⟩
    ⟨1700s_fae_binding:CHRONO_NODE_FAE_TREATY_BROKEN⟩
    ⟨1893_lighthouse_tragedy:CHRONO_NODE_KEEPER_DEATH⟩
    ⟨1970s_audrey_disappearance:CHRONO_NODE_MISSING_GIRL⟩
  
  ⟨SIGNIFICANCE⟩
    ⟨fae_binding:forgotten_by_most_known_by_elders⟩
    ⟨lighthouse:town_legend_tourist_ghost_story⟩
    ⟨audrey:recent_memory_unresolved_mystery⟩
  
  ⟨CONTINUITY⟩
    ⟨threads:fae_power_growing_veil_thinning⟩
    ⟨echoes:women_disappear_every_generation⟩
    ⟨prophecy:seventh_daughter_will_open_gateway⟩
```

---

## World State & Continuity

### World State Schema

```
⟨WORLD_STATE⟩
  
  ⟨CURRENT_CRISIS⟩
    ⟨nature:conflict|scarcity|plague|invasion|collapse|awakening⟩
    ⟨scale:personal|local|regional|global|cosmic⟩
    ⟨duration:sudden|ongoing|chronic|eternal⟩
    ⟨resolution:solvable|manageable|inevitable|impossible⟩
  
  ⟨STABILITY⟩
    ⟨political:peaceful|tense|conflict|war|anarchy⟩
    ⟨economic:prosperous|stable|declining|collapsed⟩
    ⟨social:cohesive|fractured|hostile|dissolved⟩
    ⟨environmental:healthy|degraded|catastrophic|post_apocalyptic⟩
  
  ⟨RESOURCES⟩
    ⟨food:abundant|sufficient|scarce|famine⟩
    ⟨water:clean|contested|polluted|deadly⟩
    ⟨energy:unlimited|available|rationed|none⟩
    ⟨magic:flowing|stable|waning|exhausted⟩
  
  ⟨MORALE⟩
    ⟨collective_mood:hopeful|cautious|anxious|desperate|resigned|nihilistic⟩
    ⟨direction:improving|stable|declining|collapsed⟩
    ⟨cohesion:united|divided|fragmented|war_of_all_against_all⟩
```

### Example World States

```
⟨WORLD_STATE:ERRANHAM_PRESENT⟩
  ⟨CURRENT_CRISIS:fae_veil_thinning⟩
    ⟨nature:metaphysical_boundary_weakening⟩
    ⟨scale:local_but_cosmic_implications⟩
    ⟨duration:accelerating_over_years⟩
  
  ⟨STABILITY⟩
    ⟨political:stable_surface_hidden_tension⟩
    ⟨economic:tourist_town_declining_maritime_industry⟩
    ⟨social:cohesive_surface_elder_secrets_divide⟩
  
  ⟨MORALE:cautiously_anxious⟩
    ⟨surface_normal_but_uncanny_events_increasing⟩

⟨WORLD_STATE:MEDUSA_ETERNAL⟩
  ⟨CURRENT_CRISIS:divine_curse_unbreakable⟩
    ⟨nature:theological_punishment_infinite⟩
    ⟨scale:personal_medusa_but_affects_all_visitors⟩
    ⟨duration:eternal_no_resolution⟩
  
  ⟨STABILITY:static_cursed_unchanging⟩
  ⟨MORALE:medusa_isolated_resigned_tragic⟩
```

---

## VSE Auto-Derivation from Context

### How Context Biases VSE

**Context Block automatically suggests VSE parameters:**

```
⟨CONTEXT:ERRANHAM_AUTUMN_DUSK⟩
  ↓
⟨VSE_AUTO_DERIVATION⟩
  
  ⟨MATERIAL⟩
    ⟨stone:WEATHERED_GRAY_LIMESTONE⟩
    ⟨metal:AGED_BRONZE_PATINA_GREEN⟩
    ⟨wood:WEATHERED_DRIFTWOOD_GRAY⟩
  
  ⟨LIGHTING⟩
    ⟨primary:BLUE_HOUR_APPROACHING⟩
    ⟨secondary:GOLDEN_HOUR_FADING⟩
    ⟨weather:OVERCAST_COASTAL_FOG⟩
  
  ⟨CAMERA⟩
    ⟨framing:ENVIRONMENTAL_PORTRAIT⟩
    ⟨movement:SLOW_CONTEMPLATIVE⟩
  
  ⟨COMPOSITION⟩
    ⟨style:GOLDEN_ISOLATION⟩
    ⟨negative_space:EXTENSIVE⟩
  
  ⟨ATMOSPHERE⟩
    ⟨crowd:SPARSE_TOWNSFOLK⟩
    ⟨ambient_sound:WIND_WAVES_GULLS⟩
    ⟨ambient_light:DIM_STREETLIGHTS_WARM_WINDOWS⟩
```

### Derivation Rules

```
⟨CONTEXT_TO_VSE_MAPPING⟩
  
  ⟨LOCATION:urban⟩ → ⟨ambient_light:artificial_mixed⟩
  ⟨LOCATION:wilderness⟩ → ⟨ambient_light:natural_only⟩
  ⟨LOCATION:ruins⟩ → ⟨material:weathered_aged⟩
  
  ⟨TIME:dawn⟩ → ⟨lighting:GOLDEN_HOUR_COOL⟩
  ⟨TIME:noon⟩ → ⟨lighting:HARSH_OVERHEAD⟩
  ⟨TIME:dusk⟩ → ⟨lighting:BLUE_HOUR⟩
  
  ⟨MAGIC:overt⟩ → ⟨effects:glowing_unnatural_light⟩
  ⟨MAGIC:none⟩ → ⟨effects:natural_only⟩
  
  ⟨SOCIAL:public⟩ → ⟨composition:CROWD_ENVIRONMENTAL⟩
  ⟨SOCIAL:intimate⟩ → ⟨composition:TIGHT_CLOSEUP⟩
  
  ⟨POWER:balanced⟩ → ⟨camera:EYE_LEVEL⟩
  ⟨POWER:dominant⟩ → ⟨camera:LOW_ANGLE⟩
  ⟨POWER:vulnerable⟩ → ⟨camera:HIGH_ANGLE⟩
```

---

## Project Context Libraries

### Whispers Context Profiles

```
⟨WHISPERS_CONTEXTS⟩
  
  ⟨ERRANHAM_SQUARE⟩
    ⟨location:town_center⟩
    ⟨time:autumn_dusk⟩
    ⟨social:public_town_gathering⟩
    ⟨power:elder_council_hidden_control⟩
    ⟨magic:subtle_awakening⟩
  
  ⟨LIGHTHOUSE_INTERIOR⟩
    ⟨location:abandoned_structure⟩
    ⟨time:night_storm⟩
    ⟨social:private_transgressive⟩
    ⟨power:fae_domain_contested⟩
    ⟨magic:overt_portal_threshold⟩
  
  ⟨FOREST_CLEARING⟩
    ⟨location:fae_sacred_space⟩
    ⟨time:midnight_full_moon⟩
    ⟨social:ritual_observed_by_hidden⟩
    ⟨power:fae_absolute⟩
    ⟨magic:dominant_physical_law⟩
  
  ⟨AUDREY_BEDROOM⟩
    ⟨location:family_home_sanctuary⟩
    ⟨time:late_night_alone⟩
    ⟨social:intimate_secret⟩
    ⟨power:audrey_agency_but_limited⟩
    ⟨magic:subtle_dreams_visions⟩
```

### Medusa Legacy Context Profiles

```
⟨MEDUSA_CONTEXTS⟩
  
  ⟨ISLAND_APPROACH⟩
    ⟨location:mediterranean_sea_rocky_approach⟩
    ⟨time:noon_harsh_sun⟩
    ⟨social:public_viewed_by_gods⟩
    ⟨power:divine_forces_watching⟩
    ⟨magic:dominant_curse_active⟩
  
  ⟨STATUE_GARDEN⟩
    ⟨location:open_courtyard_victims_displayed⟩
    ⟨time:eternal_noon⟩
    ⟨social:public_warning_testament⟩
    ⟨power:medusa_absolute_artistic⟩
    ⟨magic:petrification_instant_permanent⟩
  
  ⟨MEDUSA_CAVE⟩
    ⟨location:interior_lair_sanctuary⟩
    ⟨time:dim_firelight_timeless⟩
    ⟨social:intimate_medusa_alone⟩
    ⟨power:medusa_vulnerable_within⟩
    ⟨magic:curse_omnipresent_unavoidable⟩
  
  ⟨PERSEUS_CONFRONTATION⟩
    ⟨location:cave_threshold⟩
    ⟨time:dawn_liminal⟩
    ⟨social:private_divine_audience⟩
    ⟨power:contested_hero_vs_monster⟩
    ⟨magic:divine_gifts_vs_divine_curse⟩
```

---

## Integration Examples

### Example 1: Whispers Lighthouse Scene

```
⟨CHRONO_NODE:AUDREY_ENTERS_LIGHTHOUSE⟩
  
  ⟨CONTEXT_BLOCK:LIGHTHOUSE_THRESHOLD⟩
    ⟨LOCATION:lighthouse_interior⟩
    ⟨WORLD_TIME:midnight_autumn_storm⟩
    ⟨SOCIAL_CONTEXT:transgressive_forbidden_entry⟩
    ⟨POWER_CONTEXT:fae_domain_contested⟩
    ⟨MAGIC_LEVEL:overt_portal_opening⟩
  
  ⟨VSE_DERIVED⟩
    ⟨MATERIAL:WEATHERED_STONE|RUSTED_IRON|ROTTING_WOOD⟩
    ⟨LIGHTING:STORM_LIGHTNING_FLASHES|MOON_THROUGH_CLOUDS|MAGICAL_GLOW_EMERGING⟩
    ⟨CAMERA:HANDHELD_TENSION|DUTCH_ANGLE_UNEASE⟩
    ⟨COMPOSITION:FRAME_WITHIN_FRAME_DOORWAY⟩
```

### Example 2: Medusa Garden Discovery

```
⟨CHRONO_NODE:VISITOR_SEES_GARDEN⟩
  
  ⟨CONTEXT_BLOCK:STATUE_GARDEN_NOON⟩
    ⟨LOCATION:open_courtyard_victims⟩
    ⟨WORLD_TIME:eternal_noon_harsh⟩
    ⟨SOCIAL_CONTEXT:public_divine_witness⟩
    ⟨POWER_CONTEXT:medusa_absolute_artistic⟩
    ⟨MAGIC_LEVEL:dominant_instant_petrification⟩
    ⟨HISTORY:centuries_of_victims⟩
  
  ⟨VSE_DERIVED⟩
    ⟨MATERIAL:CARRARA_MARBLE_MULTIPLE_FIGURES|SUN_BLEACHED_LIMESTONE⟩
    ⟨LIGHTING:HARSH_MIDDAY_UNFORGIVING|DRAMATIC_CHIAROSCURO_SHADOWS⟩
    ⟨CAMERA:CRANE_UP_REVEALING_SCALE|PAN_SLOW_HORROR⟩
    ⟨COMPOSITION:CROWDED_LAYERED_DEPTH|STATUE_REVERENCE_MULTIPLE⟩
```

---

## Summary

The ChronoCore Context Layer provides **diegetic grounding** for every event - the where/when/who/why in terms of world and lore. It ensures that Whispers, Medusa Legacy, and all projects feel like they happen in **consistent, living worlds** rather than isolated cool shots.

**Key Innovations:**

✅ **Location Profiles** - Reusable world places with VSE biases  
✅ **Temporal Context** - World time, season, era, phase  
✅ **Social/Power Dynamics** - Who acts, who watches, stakes  
✅ **Magic/Tech Levels** - Supernatural & technological context  
✅ **Historical References** - Past events that matter now  
✅ **World State** - Ongoing conditions, crises, morale  
✅ **VSE Auto-Derivation** - Context automatically suggests materials/lighting/camera  

**Status:** ✅ PRODUCTION READY

---

## Credits

**Concept Architect:** Vox  
**Orchestrator:** John Jacob Weber II  
**Documentation:** Claude (Sonnet 4.5)  

**Repository:** github.com/PaniclandUSA/vse/chronocore-context/  
**Version:** 1.0  
**Date:** December 10, 2025  

*"ChronoCore and VSE describe the moment beautifully. We still need a clean slot for meta-reality: diegetic time and place, cultural/lore constraints, ongoing world state."*

— Vox

**END OF CONTEXT LAYER SPECIFICATION**
