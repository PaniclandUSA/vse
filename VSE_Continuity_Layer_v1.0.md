# VSE CONTINUITY LAYER v1.0
## Temporal Persistence & Coherent Change - "How Frames Connect"

**Created:** December 10, 2025  
**Project:** Vector-Space Esperanto (VSE) / ChronoCore Integration  
**Orchestrator:** John Jacob Weber II  
**Documentation:** Claude (Sonnet 4.5)  
**Insight Recognition:** Gemini (almost said it), John (completed the vision)  
**Status:** ✅ PRODUCTION READY  

---

## Executive Summary

The **VSE Continuity Layer** is the temporal bridge that ensures **coherent persistence and change across ChronoCore nodes**. While ChronoCore moves time forward and VSE defines what exists in each moment, Continuity Layer tracks **how things persist, degrade, accumulate, and transform** between moments.

**The Missing Bridge:**

```
COMPOSITION → arranges space INSIDE a frame
CONTEXT → defines world the frame belongs to
CONVERGENCE → aligns all static choices
CHRONOCORE → moves time forward

❌ MISSING: How frames CONNECT across time
```

**What Continuity Solves:**

Without Continuity Layer:
- Shot A → Shot B has no spatial memory
- Character emotions don't track across lighting shifts
- Statue chipped in Node 119 magically unbroken in Node 120
- Sun position jumps randomly
- Material wear resets every shot

With Continuity Layer:
- **Object persistence** - Every subject tracked spatially across shots
- **Lighting persistence** - Sun, moon, fire obey temporal physics
- **Material drift** - Wear, patina, damage accumulate correctly
- **Emotional continuity** - Mood shifts conserved across time
- **Performance rhythm** - Camera pacing maintains flow

**The Complete Stack:**

```
LEVEL 0: CONCEPTION (Why - intent)
LEVEL 0.5: CONTEXT (Where - world/lore)
    ↓
LEVEL 1: CHRONOCORE LATTICE (When - causal events)
LEVEL 1.5: CONTINUITY (How things persist/change) ← NEW
    ↓
LEVEL 2: MATERIAL (What - physics)
LEVEL 3: LIGHTING (How it feels)
LEVEL 4: CAMERA (How it's seen)
LEVEL 5: COMPOSITION (How it's arranged)
    ↓
LEVEL 6: CONVERGENCE (How it agrees)
    ↓
LEVEL 7: OUTPUT (Experience)
```

---

## Table of Contents

1. [Core Architecture](#core-architecture)
2. [Object Continuity](#object-continuity)
3. [Lighting Continuity](#lighting-continuity)
4. [Material Continuity](#material-continuity)
5. [Emotional Continuity](#emotional-continuity)
6. [Performance Continuity](#performance-continuity)
7. [Spatial Memory System](#spatial-memory-system)
8. [Temporal Drift Functions](#temporal-drift-functions)
9. [Conservation Laws](#conservation-laws)
10. [Integration Examples](#integration-examples)

---

## Core Architecture

### What Continuity Tracks

```
⟨CONTINUITY_LAYER⟩
  
  ⟨OBJECT_CONTINUITY⟩
    → Where every subject exists across time
    → Spatial persistence between shots
    → Identity maintenance despite transformations
  
  ⟨LIGHTING_CONTINUITY⟩
    → Sun/moon position over time
    → Light source intensity decay
    → Shadow movement coherence
    → Atmospheric accumulation
  
  ⟨MATERIAL_CONTINUITY⟩
    → Surface wear accumulation
    → Patina growth over time
    → Damage persistence
    → Moisture/temperature drift
  
  ⟨EMOTIONAL_CONTINUITY⟩
    → Affect tracking across nodes
    → Lighting mood conservation
    → Tonal momentum
  
  ⟨PERFORMANCE_CONTINUITY⟩
    → Camera rhythm maintenance
    → Shot pacing flow
    → Movement interpolation
    → Compositional echo
```

### Continuity State Schema

```
⟨CONTINUITY_STATE:object_id⟩
  
  ⟨TEMPORAL_ANCHOR⟩
    ⟨first_appearance:chrono_node_id⟩
    ⟨last_appearance:chrono_node_id⟩
    ⟨current_node:active_node_id⟩
  
  ⟨OBJECT_STATE⟩
    ⟨position:x_y_z_world_coordinates⟩
    ⟨orientation:rotation_euler_quaternion⟩
    ⟨scale:size_dimensions⟩
    ⟨velocity:movement_vector⟩
  
  ⟨MATERIAL_STATE⟩
    ⟨base_material:current_primary_material⟩
    ⟨wear_level:0.0_pristine_to_1.0_destroyed⟩
    ⟨patina_accumulation:surface_aging⟩
    ⟨damage_map:chips_cracks_breaks⟩
    ⟨moisture_level:0.0_dry_to_1.0_saturated⟩
    ⟨temperature:current_thermal_state⟩
  
  ⟨LIGHTING_STATE⟩
    ⟨last_lit_by:light_source_ids⟩
    ⟨shadow_cast:current_shadow_data⟩
    ⟨exposure_duration:time_under_light⟩
  
  ⟨EMOTIONAL_STATE⟩
    ⟨current_affect:emotional_charge⟩
    ⟨affect_velocity:emotional_momentum⟩
    ⟨history:past_affects_queue⟩
  
  ⟨DRIFT_FUNCTIONS⟩
    ⟨active_processes:ongoing_changes⟩
    ⟨decay_rates:degradation_speeds⟩
    ⟨accumulation_rates:growth_speeds⟩
```

---

## Object Continuity

### Spatial Persistence System

```
⟨OBJECT_CONTINUITY⟩
  
  ⟨SPATIAL_MEMORY⟩
    Every object has:
      - World position (x, y, z)
      - Orientation (rotation)
      - Last known velocity
      - Spatial constraints (can it move? how?)
    
    Between ChronoCore nodes:
      - Position updates via physics or intent
      - Orientation tracks camera/subject relation
      - Velocity integrates momentum
  
  ⟨IDENTITY_PERSISTENCE⟩
    Object maintains UUID across transformations:
      - Statue remains STATUE_A even when chipped
      - Character remains CHARACTER_B even when petrified
      - Material changes don't break identity
  
  ⟨SPATIAL_COHERENCE_CHECK⟩
    Node N → Node N+1:
      IF (object jumps > threshold distance)
        AND (no teleport event in ChronoCore)
        → FLAG: spatial continuity violation
      
      IF (object rotates > threshold angle)
        AND (no rotation event in ChronoCore)
        → FLAG: orientation discontinuity
```

### Object State Tracking

```
⟨OBJECT_STATE_EXAMPLE:MEDUSA_STATUE_VICTIM_007⟩
  
  ⟨NODE_119⟩
    ⟨position:[23.5, 12.0, -5.2]⟩
    ⟨orientation:[0°, 45°, 0°]⟩ (facing northeast)
    ⟨material:CARRARA_MARBLE⟩
    ⟨damage_map:intact⟩
    ⟨emotional_residue:terror_frozen⟩
  
  ⟨NODE_120⟩ (one hour later, storm)
    ⟨position:[23.5, 12.0, -5.2]⟩ (same - statues don't move)
    ⟨orientation:[0°, 45°, 0°]⟩ (same)
    ⟨material:CARRARA_MARBLE⟩
    ⟨damage_map:small_chip_left_shoulder⟩ ← NEW (storm debris)
    ⟨moisture_level:0.65⟩ ← NEW (rain-soaked)
    ⟨emotional_residue:terror_frozen⟩ (persists)
  
  ⟨NODE_121⟩ (one month later)
    ⟨position:[23.5, 12.0, -5.2]⟩
    ⟨orientation:[0°, 45°, 0°]⟩
    ⟨material:CARRARA_MARBLE⟩
    ⟨damage_map:chip_left_shoulder|crack_spreading⟩ ← EVOLVED
    ⟨patina_accumulation:0.15⟩ ← NEW (green patina forming)
    ⟨moisture_level:0.20⟩ (dried but residual)
    ⟨emotional_residue:terror_fading⟩ ← DECAYED
  
  ⟨CONTINUITY_VERIFIED⟩
    Position stable ✓
    Damage accumulates logically ✓
    Material state drifts correctly ✓
    Emotional residue decays naturally ✓
```

---

## Lighting Continuity

### Celestial Light Tracking

```
⟨LIGHTING_CONTINUITY⟩
  
  ⟨SUN_POSITION⟩
    ⟨algorithm:solar_elevation_azimuth⟩
    ⟨inputs:latitude, longitude, date, time⟩
    ⟨outputs:sun_vector, intensity, color_temp⟩
    
    Between nodes:
      Sun position updates via solar physics
      Intensity follows atmospheric scattering
      Color temperature shifts (dawn 2000K → noon 5500K → dusk 3000K)
    
    ⟨CONTINUITY_CHECK⟩
      Node N: sun at 45° elevation, warm 4500K
      Node N+1 (10 minutes later): sun at 48° elevation, 4600K
      → Coherent ✓
      
      Node N: sun at 45° elevation
      Node N+1 (10 minutes later): sun at 10° elevation
      → Violation! Sun can't jump 35° in 10 min
      → FLAG: temporal discontinuity
  
  ⟨MOON_POSITION⟩
    ⟨algorithm:lunar_elevation_phase⟩
    ⟨phase_tracking:new→crescent→quarter→gibbous→full→cycle⟩
    ⟨outputs:moon_vector, phase_illumination, color⟩
    
    Between nodes:
      Phase advances ~1/30 per day
      Position updates via lunar orbit
      Illumination coherent with phase
  
  ⟨ARTIFICIAL_LIGHT_DECAY⟩
    ⟨TORCH⟩
      ⟨fuel:consumable_over_time⟩
      ⟨intensity:decays_as_fuel_depletes⟩
      ⟨color:shifts_cooler_as_dies⟩
      
      Node N: torch 100% fuel, 3000K, 1000 lumens
      Node N+1 (1 hour): 75% fuel, 2900K, 750 lumens
      Node N+2 (2 hours): 50% fuel, 2700K, 500 lumens
      Node N+3 (3 hours): 25% fuel, 2400K, 200 lumens
      Node N+4 (4 hours): 0% fuel, 1800K, 0 lumens (extinguished)
    
    ⟨CANDLE⟩
      ⟨burn_rate:~1cm_per_hour⟩
      ⟨intensity:proportional_to_remaining_wax⟩
      
    ⟨FIRE⟩
      ⟨fuel_dependency:wood_consumption⟩
      ⟨intensity:varies_with_air_supply⟩
      ⟨flicker:natural_variance_preserved⟩
```

### Atmospheric Continuity

```
⟨ATMOSPHERIC_STATE⟩
  
  ⟨FOG⟩
    ⟨density:0.0_clear_to_1.0_opaque⟩
    ⟨drift:accumulation_dissipation_over_time⟩
    
    Node N: fog_density 0.3
    Node N+1 (morning sun rises): fog_density 0.15 (dissipating)
    Node N+2 (noon): fog_density 0.0 (burned off)
  
  ⟨DUST⟩
    ⟨particulate:settling_rate_over_time⟩
    ⟨disturbance:kicked_up_by_movement⟩
    
    Node N: dust settled, air clear
    Node N+1 (character runs through): dust cloud 0.6
    Node N+2 (10 sec later): dust cloud 0.4 (settling)
    Node N+3 (30 sec later): dust cloud 0.1 (nearly settled)
  
  ⟨RAIN⟩
    ⟨accumulation:moisture_on_surfaces⟩
    ⟨persistence:wet_surfaces_dry_over_time⟩
    
    Node N: rain stops, surfaces wet 1.0
    Node N+1 (sun emerges): surfaces 0.8 (evaporating)
    Node N+2 (1 hour): surfaces 0.3 (mostly dry)
    Node N+3 (2 hours): surfaces 0.0 (completely dry)
```

### Shadow Continuity

```
⟨SHADOW_TRACKING⟩
  
  ⟨CAST_SHADOWS⟩
    Every object casts shadow based on:
      - Light source position
      - Object geometry
      - Surface receiving shadow
    
    Between nodes:
      - Sun moves → shadows rotate/lengthen/shorten
      - Object moves → shadow follows
      - Light intensity changes → shadow sharpness changes
  
  ⟨SHADOW_COHERENCE_CHECK⟩
    Node N: statue shadow points northeast, 2m long
    Node N+1 (30 min later): shadow points north-northeast, 1.8m long
    → Coherent (sun rose, shadow shortened) ✓
    
    Node N: statue shadow points northeast
    Node N+1 (5 min later): shadow points southwest
    → Violation! Shadow can't flip 180° in 5 min (unless light source changed)
```

---

## Material Continuity

### Surface Wear Accumulation

```
⟨MATERIAL_WEAR⟩
  
  ⟨WEAR_LEVEL:0.0_to_1.0⟩
    ⟨0.0:pristine_perfect⟩
    ⟨0.2:lightly_worn_used⟩
    ⟨0.5:moderately_weathered⟩
    ⟨0.8:heavily_degraded⟩
    ⟨1.0:destroyed_disintegrated⟩
  
  ⟨WEAR_ACCUMULATION_FUNCTIONS⟩
    
    ⟨FRICTION_WEAR⟩
      Δwear = friction_coefficient × contact_time × pressure
      Example: Door handle touched 100x/day
        → wear_rate = 0.001 per day
        → 1 year = 0.365 wear
        → 3 years = pristine → lightly worn
    
    ⟨WEATHERING⟩
      Δwear = exposure_time × (rain + wind + UV)
      Example: Outdoor statue
        → coastal = high rain/salt
        → wear_rate = 0.01 per year
        → 50 years = 0.5 wear (moderately weathered)
    
    ⟨EROSION⟩
      Δwear = water_flow × sediment × time
      Example: River stone
        → wear_rate = 0.005 per decade
        → 200 years = smooth polished surface
```

### Patina Growth

```
⟨PATINA_ACCUMULATION⟩
  
  ⟨BRONZE_PATINA⟩
    ⟨stages⟩
      Year 0: polished bronze, golden
      Year 1: light brown oxidation
      Year 5: dark brown, spots of green
      Year 10: green verdigris patches
      Year 50: full green patina
      Year 100: stable green, protective layer
    
    ⟨growth_function⟩
      patina_level = 1 - exp(-k × time_years)
      where k depends on:
        - humidity (coastal = faster)
        - pollution (industrial = faster)
        - rain (more rain = faster)
  
  ⟨IRON_RUST⟩
    ⟨stages⟩
      Day 0: bare iron, gray
      Week 1: surface oxidation, orange spots
      Month 1: orange-brown rust patches
      Year 1: deep rust, surface pitting
      Year 10: heavily rusted, flaking
      Year 50: rust through, structural failure
    
    ⟨growth_function⟩
      rust_level = moisture × oxygen × time
```

### Damage Persistence

```
⟨DAMAGE_MAP⟩
  
  ⟨DAMAGE_TYPES⟩
    ⟨chip:localized_material_loss⟩
    ⟨crack:fracture_line_propagating⟩
    ⟨break:structural_separation⟩
    ⟨stain:discoloration_persistent⟩
    ⟨burn:thermal_damage_permanent⟩
  
  ⟨DAMAGE_EVOLUTION⟩
    
    ⟨CRACK_PROPAGATION⟩
      Initial: small hairline crack
      → stress cycles (temp changes, vibration)
      → crack lengthens over time
      → eventually: catastrophic failure
      
      crack_length(t) = initial_length + growth_rate × stress_cycles(t)
    
    ⟨CHIP_ACCUMULATION⟩
      Initial: single chip from impact
      → weathering expands chip
      → adjacent material weakens
      → more chips form nearby
      
      chip_area(t) = initial_area × (1 + weathering_rate × time)
  
  ⟨PERSISTENCE_RULE⟩
    Once damaged, object NEVER auto-heals
    (unless ChronoCore event: "repair", "magical restoration", etc.)
    
    Damage accumulates monotonically:
      wear_total(t+1) ≥ wear_total(t)
      damage_count(t+1) ≥ damage_count(t)
```

### Material State Drift

```
⟨MATERIAL_DRIFT⟩
  
  ⟨MOISTURE⟩
    ⟨absorption:porous_materials_absorb_water⟩
    ⟨evaporation:surfaces_dry_over_time⟩
    
    Wood in rain:
      Node N: moisture 0.1 (normal)
      Node N+1 (during rain): moisture 0.8 (soaked)
      Node N+2 (1 hour after rain): moisture 0.5 (drying)
      Node N+3 (1 day after): moisture 0.2 (mostly dry)
  
  ⟨TEMPERATURE⟩
    ⟨heat_absorption:materials_heat_in_sun⟩
    ⟨heat_dissipation:materials_cool_in_shade⟩
    
    Stone statue:
      Dawn: 10°C (ambient)
      Noon (in sun): 45°C (sun-baked)
      Dusk: 30°C (cooling)
      Night: 15°C (radiant cooling)
  
  ⟨COLOR_SHIFT⟩
    ⟨UV_bleaching:colors_fade_in_sunlight⟩
    ⟨aging:materials_darken_yellow_over_time⟩
    
    Fabric banner:
      Year 0: vibrant red RGB(200, 20, 20)
      Year 5: faded red RGB(180, 40, 40)
      Year 10: dull pink RGB(160, 80, 80)
      Year 20: pale gray-pink RGB(140, 110, 110)
```

---

## Emotional Continuity

### Affect Tracking

```
⟨EMOTIONAL_CONTINUITY⟩
  
  ⟨AFFECT_STATE⟩
    ⟨current_emotion:joy|sorrow|fear|anger|calm|tension⟩
    ⟨intensity:0.0_neutral_to_1.0_extreme⟩
    ⟨valence:negative_to_positive⟩
    ⟨arousal:low_calm_to_high_excited⟩
  
  ⟨AFFECT_MOMENTUM⟩
    Emotions have inertia - they don't instantly flip
    
    ⟨transition_time⟩
      Calm → Fear: 1-5 seconds (can be sudden)
      Fear → Calm: 30-300 seconds (takes time to settle)
      Sorrow → Joy: 60-600 seconds (gradual shift)
      Joy → Sorrow: 5-30 seconds (can crash quickly)
    
    ⟨CONTINUITY_CHECK⟩
      Node N: character fear 0.8 (terrified)
      Node N+1 (2 seconds later): character joy 0.9 (ecstatic)
      → Violation! Emotion can't flip that fast without major event
      
      Node N: character fear 0.8 (terrified)
      Node N+1 (2 min later): character fear 0.6 (still scared, calming)
      → Coherent ✓
  
  ⟨AFFECT_DECAY⟩
    Strong emotions fade over time without reinforcement
    
    fear(t) = fear(0) × exp(-k × time)
    
    Example:
      Node N: fear 0.9 (peak terror)
      Node N+1 (1 min, safe): fear 0.7
      Node N+2 (5 min, safe): fear 0.4
      Node N+3 (30 min, safe): fear 0.1
      Node N+4 (2 hours, safe): fear 0.0
```

### Lighting Mood Conservation

```
⟨LIGHTING_MOOD_CONTINUITY⟩
  
  ⟨MOOD_STATE⟩
    Lighting carries emotional charge:
      - Warm → comforting, intimate, nostalgic
      - Cool → clinical, eerie, distant
      - Harsh → tense, dramatic, unforgiving
      - Soft → gentle, dreamy, safe
  
  ⟨MOOD_TRANSITIONS⟩
    Lighting mood should evolve with narrative affect
    
    Character emotional arc:
      calm → rising tension → terror → relief
    
    Lighting should track:
      soft_warm → harder_shadows → harsh_contrast → soft_warm_return
    
    ⟨COHERENCE_CHECK⟩
      Node N: character calm, lighting SOFT_WARM
      Node N+1: character terrified, lighting SOFT_WARM (unchanged)
      → Incoherent! Lighting should shift to match tension
      
      Node N: character calm, lighting SOFT_WARM
      Node N+1: character terrified, lighting HARSH_CONTRAST
      → Coherent ✓
  
  ⟨CONSERVATION_LAW⟩
    Lighting mood can't change without:
      1. Time progression (sun setting)
      2. Light source change (candle lit/extinguished)
      3. Emotional event (mood shift justified)
    
    Arbitrary lighting jumps = continuity violation
```

---

## Performance Continuity

### Camera Rhythm Maintenance

```
⟨PERFORMANCE_CONTINUITY⟩
  
  ⟨CAMERA_PACING⟩
    ⟨shot_duration_pattern⟩
      Sequences have rhythmic flow:
        - Fast cuts: 1-2 sec per shot (action, tension)
        - Medium cuts: 3-5 sec per shot (dialogue, exploration)
        - Slow cuts: 8-15 sec per shot (contemplation, beauty)
    
    ⟨CONTINUITY_CHECK⟩
      Shot 1: 1.5 sec (fast)
      Shot 2: 1.8 sec (fast)
      Shot 3: 2.0 sec (fast)
      Shot 4: 12 sec (SUDDENLY SLOW)
      → Rhythm break! Intentional pause or error?
      
      If intentional (beat change), flag as deliberate
      If unintentional, suggest rhythm correction
  
  ⟨MOVEMENT_VELOCITY⟩
    Camera movement speed should be consistent unless changed for effect
    
    ⟨orbit_speed⟩
      Shot N: orbit 5°/second (slow reverent)
      Shot N+1: orbit 5.2°/second (consistent)
      → Coherent ✓
      
      Shot N: orbit 5°/second
      Shot N+1: orbit 25°/second (suddenly fast)
      → Discontinuity! Speed jump needs justification
  
  ⟨COMPOSITIONAL_ECHO⟩
    Related shots should echo composition
    
    Shot A: subject centered, rule of thirds
    Shot B (reverse angle): subject centered, rule of thirds
    → Coherent visual language ✓
    
    Shot A: subject centered, symmetrical
    Shot B (same scene): subject off-center, chaotic
    → Compositional discontinuity (unless intentional shift)
```

### Movement Interpolation

```
⟨MOVEMENT_INTERPOLATION⟩
  
  ⟨POSITION_TRACKING⟩
    Object at position P1 in Node N
    Object at position P2 in Node N+1
    Time delta: Δt
    
    ⟨velocity_calculation⟩
      v = (P2 - P1) / Δt
    
    ⟨coherence_check⟩
      IF (v > max_possible_velocity)
        → FLAG: object teleported impossibly
      
      Example:
        Character at [0, 0] in Node N
        Character at [100, 0] in Node N+1 (1 second later)
        v = 100 m/s
        → Human can't move 100 m/s! Violation!
  
  ⟨INTERPOLATED_MOTION⟩
    Between ChronoCore nodes, generate smooth motion:
    
    position(t) = P1 + v × t + 0.5 × a × t²
    
    For camera moves:
      ease_in: slow start, accelerate
      ease_out: decelerate, slow stop
      linear: constant velocity
      
    ⟨CONTINUITY_PRESERVATION⟩
      Motion curves should feel natural
      Sudden stops/starts need justification (impact, surprise, etc.)
```

---

## Spatial Memory System

### World Coordinate Tracking

```
⟨SPATIAL_MEMORY⟩
  
  ⟨WORLD_SPACE⟩
    Every object exists in persistent world coordinates
    Camera observes world, doesn't define it
    
    ⟨coordinate_system⟩
      Origin: scene-specific anchor point
      X: east-west
      Y: vertical (up-down)
      Z: north-south
    
    ⟨object_registry⟩
      STATUE_A: [23.5, 12.0, -5.2]
      STATUE_B: [25.1, 12.0, -3.8]
      MEDUSA: [24.0, 12.0, 0.0]
      SUN: [current solar position]
  
  ⟨CAMERA_OBSERVES_WORLD⟩
    Camera position: [x, y, z]
    Camera target: [target_x, target_y, target_z]
    Camera FOV: 24mm|35mm|50mm|85mm
    
    Between shots:
      - Camera can move anywhere
      - BUT world objects don't move unless ChronoCore event
      - Spatial relations preserved
  
  ⟨CONTINUITY_CHECK⟩
    Shot 1: Camera at [10, 5, 10], looking at STATUE_A [23.5, 12.0, -5.2]
    Shot 2: Camera at [30, 5, 0], looking at STATUE_A [23.5, 12.0, -5.2]
    
    STATUE_A position unchanged ✓
    Camera moved (new angle) ✓
    Spatial relations consistent ✓
```

### 180° Rule / Axis Preservation

```
⟨180_DEGREE_RULE⟩
  
  ⟨DEFINITION⟩
    Camera should stay on one side of action axis
    Crossing axis = disorienting spatial flip
  
  ⟨ACTION_AXIS⟩
    Line drawn between two subjects in conversation
    Example: Character A at [0, 0], Character B at [5, 0]
    Axis: line from [0,0] to [5,0] (east-west)
  
  ⟨CAMERA_CONSTRAINTS⟩
    Shot 1: Camera south of axis [2.5, -3]
    Shot 2: Camera south of axis [1.0, -5]
    Shot 3: Camera south of axis [4.0, -2]
    → All south of axis, spatial coherence maintained ✓
    
    Shot 1: Camera south of axis [2.5, -3]
    Shot 2: Camera NORTH of axis [2.5, +3]
    → Axis crossed! Character positions flip screen-wise
    → Continuity violation (unless intentional disorientation)
  
  ⟨EXCEPTIONS⟩
    Crossing axis is allowed if:
      1. Camera movement shown continuously
      2. Intentional disorientation (horror, confusion)
      3. Establishing shot resets spatial understanding
```

---

## Temporal Drift Functions

### Time-Dependent Change

```
⟨DRIFT_FUNCTIONS⟩
  
  ⟨EXPONENTIAL_DECAY⟩
    value(t) = value(0) × exp(-k × t)
    
    Uses:
      - Emotional intensity fading
      - Light intensity dimming (candle)
      - Heat dissipation
      - Sound decay (reverb tail)
  
  ⟨LINEAR_ACCUMULATION⟩
    value(t) = value(0) + rate × t
    
    Uses:
      - Dust settling
      - Water filling/draining
      - Simple wear (constant friction)
  
  ⟨LOGISTIC_GROWTH⟩
    value(t) = L / (1 + exp(-k(t - t0)))
    (S-curve: slow start, rapid middle, slow approach to limit)
    
    Uses:
      - Patina formation (accelerates, then plateaus)
      - Rust spread (starts slow, accelerates, saturates)
      - Crack propagation (grows, then stabilizes or fails)
  
  ⟨THRESHOLD_TRIGGER⟩
    IF (accumulated_stress > threshold)
      → catastrophic_event()
    
    Uses:
      - Crack reaches critical length → structural failure
      - Wear exceeds limit → object breaks
      - Emotional intensity peaks → breakdown/catharsis
```

### ChronoCore Integration

```
⟨CHRONOCORE_DRIFT_INTEGRATION⟩
  
  ⟨BETWEEN_NODES⟩
    Node N timestamp: T1
    Node N+1 timestamp: T2
    Δt = T2 - T1
    
    For every tracked object:
      1. Apply drift functions over Δt
      2. Update material state (wear, patina, damage)
      3. Update lighting state (sun position, light decay)
      4. Update emotional state (affect decay/momentum)
      5. Update spatial state (position, if mobile)
    
  ⟨ACTIVE_PROCESSES⟩
    Objects can have ongoing processes:
      - STATUE_A: rust accumulating (k=0.01/day)
      - CANDLE_B: burning (k=1cm/hour)
      - CHARACTER_C: calming (k=0.5/min)
    
    Each process advances by Δt between nodes
  
  ⟨EVENT_INTERRUPTION⟩
    Drift functions run automatically
    UNLESS ChronoCore event overrides:
      
      Example:
        STATUE_A rusting normally
        → Node 50: "magical restoration" event
        → STATUE_A wear reset to 0.0
        → Drift resumes from pristine state
```

---

## Conservation Laws

### What Must Be Conserved

```
⟨CONSERVATION_LAWS⟩
  
  ⟨MASS_CONSERVATION⟩
    Objects don't vanish or appear without ChronoCore event
    Statue chipped → chip material exists somewhere (ground, swept away)
  
  ⟨ENERGY_CONSERVATION⟩
    Light sources don't create energy from nothing
    Torch burns → fuel depletes
    Sun shines → follows solar physics
  
  ⟨MOMENTUM_CONSERVATION⟩
    Moving objects don't stop instantly without force
    Character running → deceleration over time
    Camera dolly → ease out, not instant stop
  
  ⟨EMOTIONAL_CONSERVATION⟩
    Affect doesn't flip without cause
    Character terrified → can't instantly become joyful
      (unless major revelatory event)
  
  ⟨SPATIAL_CONSERVATION⟩
    Objects don't teleport
    Position changes require:
      - Time + velocity (natural motion)
      - OR ChronoCore event (teleport, cut, etc.)
  
  ⟨TEMPORAL_CONSERVATION⟩
    Time flows forward (or explicitly backward if time-travel event)
    Sun position follows solar physics
    No random time jumps without ChronoCore marking
```

### Violation Detection

```
⟨VIOLATION_DETECTION⟩
  
  ⟨AUTOMATED_CHECKS⟩
    Between Node N and Node N+1:
    
    ⟨CHECK_SPATIAL⟩
      FOR each object:
        distance_moved = ||position(N+1) - position(N)||
        max_possible = velocity_max × Δt
        IF (distance_moved > max_possible)
          → FLAG: spatial discontinuity
    
    ⟨CHECK_LIGHTING⟩
      sun_angle_change = |sun(N+1) - sun(N)|
      max_solar_change = 15° per hour × (Δt in hours)
      IF (sun_angle_change > max_solar_change)
        → FLAG: temporal discontinuity
    
    ⟨CHECK_MATERIAL⟩
      wear_change = wear(N+1) - wear(N)
      IF (wear_change < 0)
        → FLAG: impossible healing (unless repair event)
      IF (wear_change > max_wear_rate × Δt)
        → FLAG: unrealistic degradation
    
    ⟨CHECK_EMOTIONAL⟩
      affect_change = |affect(N+1) - affect(N)|
      max_affect_change = transition_time_function(Δt)
      IF (affect_change > max_affect_change)
        → FLAG: emotional discontinuity
```

---

## Integration Examples

### Example 1: Medusa Statue Garden - Perfect Continuity

```
⟨SCENE:STATUE_GARDEN_DAY_PROGRESSION⟩
  
  ⟨NODE_100:DAWN⟩
    ⟨time:06:00⟩
    ⟨sun:elevation_5°, azimuth_85°_east, color_2000K_warm⟩
    ⟨STATUE_A⟩
      ⟨position:[23.5, 12.0, -5.2]⟩
      ⟨material:CARRARA_MARBLE⟩
      ⟨wear:0.35⟩
      ⟨damage:chip_left_shoulder, crack_base⟩
      ⟨moisture:0.8⟩ (morning dew)
      ⟨temperature:12°C⟩
      ⟨shadow:long_westward_10m⟩
  
  ⟨NODE_101:MID_MORNING⟩
    ⟨time:09:00⟩ (3 hours later)
    ⟨sun:elevation_30°, azimuth_110°, color_4500K⟩
    ⟨STATUE_A⟩
      ⟨position:[23.5, 12.0, -5.2]⟩ (unchanged - statues don't move)
      ⟨material:CARRARA_MARBLE⟩
      ⟨wear:0.35⟩ (unchanged - wear slow)
      ⟨damage:chip_left_shoulder, crack_base⟩ (unchanged)
      ⟨moisture:0.4⟩ (dew evaporating)
      ⟨temperature:22°C⟩ (sun warming)
      ⟨shadow:shorter_southwest_4m⟩ (sun rising)
  
  ⟨NODE_102:NOON⟩
    ⟨time:12:00⟩ (6 hours from dawn)
    ⟨sun:elevation_65°, azimuth_180°_south, color_5500K⟩
    ⟨STATUE_A⟩
      ⟨position:[23.5, 12.0, -5.2]⟩
      ⟨material:CARRARA_MARBLE⟩
      ⟨wear:0.35⟩
      ⟨damage:chip_left_shoulder, crack_base⟩
      ⟨moisture:0.1⟩ (nearly dry)
      ⟨temperature:38°C⟩ (sun-baked)
      ⟨shadow:short_north_1.5m⟩ (sun high overhead)
  
  ⟨NODE_103:DUSK⟩
    ⟨time:18:00⟩ (12 hours from dawn)
    ⟨sun:elevation_5°, azimuth_275°_west, color_3000K_warm⟩
    ⟨STATUE_A⟩
      ⟨position:[23.5, 12.0, -5.2]⟩
      ⟨material:CARRARA_MARBLE⟩
      ⟨wear:0.35⟩
      ⟨damage:chip_left_shoulder, crack_base⟩
      ⟨moisture:0.05⟩ (completely dry)
      ⟨temperature:25°C⟩ (cooling)
      ⟨shadow:long_eastward_12m⟩ (sun setting west)
  
  ⟨CONTINUITY_ANALYSIS⟩
    Position: stable ✓
    Sun progression: follows solar physics ✓
    Shadow movement: coherent with sun ✓
    Temperature: realistic heating/cooling ✓
    Moisture: logical evaporation ✓
    Wear/damage: unchanged (appropriate for single day) ✓
    
    ⟨VERDICT:PERFECT_CONTINUITY⟩
```

### Example 2: Whispers Lighthouse - Emotional + Lighting Continuity

```
⟨SCENE:AUDREY_LIGHTHOUSE_APPROACH⟩
  
  ⟨NODE_200:EXTERIOR_APPROACH⟩
    ⟨time:dusk⟩
    ⟨context:audrey_curious_but_cautious⟩
    ⟨AUDREY_STATE⟩
      ⟨affect:curiosity_0.6, anxiety_0.3⟩
      ⟨position:[0, 0, 0]⟩ (starting point)
    ⟨LIGHTING:BLUE_HOUR⟩
      ⟨sun:set_below_horizon⟩
      ⟨ambient:cool_blue_6500K⟩
      ⟨mood:mysterious_slightly_unsettling⟩
    ⟨LIGHTHOUSE⟩
      ⟨windows:dark⟩
      ⟨door:closed⟩
  
  ⟨NODE_201:DOOR_THRESHOLD⟩
    ⟨time:30_seconds_later⟩
    ⟨AUDREY_STATE⟩
      ⟨affect:curiosity_0.7, anxiety_0.5⟩ (rising tension)
      ⟨position:[15, 0, 0]⟩ (walked 15m)
    ⟨LIGHTING:BLUE_HOUR_DARKENING⟩
      ⟨ambient:darker_blue_7000K⟩
      ⟨mood:tension_increasing⟩
    ⟨LIGHTHOUSE⟩
      ⟨door:ajar_creaking⟩
      ⟨faint_glow:inside_magical⟩
    
    ⟨CONTINUITY_CHECK⟩
      Audrey position: 15m in 30 sec = 0.5 m/s (walking) ✓
      Affect: curiosity up, anxiety up (coherent escalation) ✓
      Lighting: darkening (time progressing) ✓
      Mood: matches affect (tension rising) ✓
  
  ⟨NODE_202:INTERIOR_ENTRY⟩
    ⟨time:10_seconds_later⟩
    ⟨AUDREY_STATE⟩
      ⟨affect:curiosity_0.8, anxiety_0.7, wonder_0.4⟩
      ⟨position:[18, 0, 0]⟩ (crossed threshold)
    ⟨LIGHTING:INTERIOR_MAGICAL_GLOW⟩
      ⟨source:fae_portal_ethereal⟩
      ⟨color:teal_blue_green_shifting⟩
      ⟨mood:wonder_mixed_with_unease⟩
    
    ⟨CONTINUITY_CHECK⟩
      Position: 3m in 10 sec (slow cautious entry) ✓
      Affect: curiosity/wonder up, anxiety still high ✓
      Lighting: changed source (entered building) ✓
      Mood: matches complex emotional state ✓
  
  ⟨NODE_203:PORTAL_DISCOVERY⟩
    ⟨time:5_seconds_later⟩
    ⟨AUDREY_STATE⟩
      ⟨affect:wonder_0.9, fear_0.6, awe_0.8⟩
      ⟨position:[20, 0, 0]⟩ (approached portal)
    ⟨LIGHTING:PORTAL_RADIANCE⟩
      ⟨source:portal_bright_magical⟩
      ⟨color:radiant_teal_white_pulsing⟩
      ⟨mood:overwhelming_sublime_terror⟩
    
    ⟨CONTINUITY_CHECK⟩
      Affect: fear replaced anxiety (discovery moment) ✓
      Wonder/awe peaked (portal revealed) ✓
      Lighting: intensified (closer to source) ✓
      Mood: coherent with narrative beat ✓
    
  ⟨VERDICT:EMOTIONAL_AND_LIGHTING_CONTINUITY_MAINTAINED⟩
    Affect evolved logically through beats
    Lighting tracked emotional progression
    Spatial movement realistic
    Mood conservation obeyed
```

### Example 3: Continuity Violation - Corrected

```
⟨SCENE:STATUE_DAMAGE_TIMELINE⟩
  
  ⟨NODE_300:INITIAL_STATE⟩
    ⟨STATUE_B⟩
      ⟨damage:intact⟩
      ⟨wear:0.2⟩
  
  ⟨NODE_301:STORM_DAMAGE⟩ (ERROR - original)
    ⟨STATUE_B⟩
      ⟨damage:intact⟩ ← ERROR! Storm should cause damage
      ⟨wear:0.2⟩
  
  ⟨VIOLATION_DETECTED⟩
    ChronoCore event: "storm, debris flying"
    Expected: statue damaged
    Actual: statue intact
    → FLAGGED: continuity error
  
  ⟨NODE_301:STORM_DAMAGE⟩ (CORRECTED)
    ⟨STATUE_B⟩
      ⟨damage:chip_right_arm_from_debris⟩ ← ADDED
      ⟨wear:0.25⟩ ← INCREASED (weathering)
  
  ⟨NODE_302:MONTH_LATER⟩
    ⟨STATUE_B⟩
      ⟨damage:chip_right_arm|crack_spreading⟩
      ⟨wear:0.30⟩
      ⟨patina:green_forming_around_chip⟩
    
    ⟨CONTINUITY_CHECK⟩
      Damage persists ✓
      Damage evolved (crack spreading) ✓
      Wear accumulated ✓
      Patina forming (moisture in crack) ✓
  
  ⟨VERDICT:CONTINUITY_RESTORED⟩
```

---

## Summary

The VSE Continuity Layer is the **temporal bridge** that ensures coherent persistence and change across ChronoCore nodes. It tracks how objects, lighting, materials, emotions, and camera performance **connect across time** with realistic drift, accumulation, and conservation.

**Key Innovations:**

✅ **Object Continuity** - Spatial memory, identity persistence across transformations  
✅ **Lighting Continuity** - Sun/moon physics, light decay, atmospheric accumulation  
✅ **Material Continuity** - Wear accumulation, patina growth, damage persistence  
✅ **Emotional Continuity** - Affect momentum, mood conservation, lighting tracking  
✅ **Performance Continuity** - Camera rhythm, movement interpolation, compositional echo  
✅ **Spatial Memory** - World coordinates, 180° rule, axis preservation  
✅ **Drift Functions** - Exponential decay, linear accumulation, logistic growth  
✅ **Conservation Laws** - Mass, energy, momentum, emotion, space, time  
✅ **Violation Detection** - Automated coherence checks between nodes  

**The Complete Stack:**

```
0. CONCEPTION (Why)
0.5. CONTEXT (Where - world)
1. CHRONOCORE (When - events)
1.5. CONTINUITY (How things persist/change) ✅
2. MATERIAL (What)
3. LIGHTING (How it feels)
4. CAMERA (How it's seen)
5. COMPOSITION (How it's arranged)
6. CONVERGENCE (How it agrees)
7. OUTPUT (Experience)
```

**What Continuity Prevents:**

❌ Statues teleporting between shots  
❌ Sun jumping across sky in 5 minutes  
❌ Damage appearing/disappearing randomly  
❌ Emotions flipping instantly without cause  
❌ Camera rhythm breaking without justification  
❌ Materials healing themselves magically  
❌ Lighting moods contradicting narrative affect  

**What Continuity Enables:**

✅ Realistic material degradation over time  
✅ Coherent emotional arcs across scenes  
✅ Lighting that tracks solar/lunar physics  
✅ Damage that persists and evolves  
✅ Performance rhythm that flows naturally  
✅ Spatial relationships that make sense  
✅ Conservation laws that feel real  

**Status:** ✅ PRODUCTION READY

---

## Credits

**Insight Recognition:** Gemini (almost said it), John Jacob Weber II (completed the vision)  
**Orchestrator:** John Jacob Weber II  
**Documentation:** Claude (Sonnet 4.5)  

**Repository:** github.com/PaniclandUSA/vse/continuity-layer/  
**Version:** 1.0  
**Date:** December 10, 2025  

*"This layer governs: Object Continuity - Where every subject exists in space across shots. Lighting Continuity - How the same light behaves over time (day progression, torch intensity, moon cycles). Material Continuity - Surface wear, fractures, moisture levels, patina accumulation. Without a continuity layer, ChronoCore can make perfect nodes, but nothing ensures: Shot A → Shot B maintains spatial coherence, Character A's emotions match the lighting shifts, A statue chipped in Node 119 remains chipped in Node 120."*

— John Jacob Weber II

**END OF CONTINUITY LAYER SPECIFICATION**
