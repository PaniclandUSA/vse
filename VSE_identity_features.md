⭐ VSE::IDENTITY_FEATURES v2.3 — Ontology Expansion + Preset System

Official canonical version for Vox, Claude, Grok, Gemini, and all renderer pipelines.

This module defines how identity-linked human features behave under VSE material transformation:
tattoos, scars, freckles, moles, pigmentation, and anatomical microdetails.

Includes:

Complete material behavior vocabulary

Complete microstructure vocabulary

Crystallization metal-fill expansion

Preset system for user-facing simplicity

Fully modular parameter sets for all AI renderers



---


---

## A. MATERIAL BEHAVIOR VOCABULARY

Full formalized palette

Behavior	Description

opaque	no light penetration
translucent	diffuses / scatters incoming light
transparent	clear, glass-like transmission
reflective	mirror-like, high specular reflection
iridescent	color-shifting, opal-like interference
luminous	emits soft internal glow
matte	low-reflective, diffuse scattering
glossy	smooth, high-specular sheen
metallic	conductive metallic reflectance



---

## B. MICROSTRUCTURE VOCABULARY

Defines internal material microforms

Microstructure	Description

smooth	uniform material density
cloudy	fog-like diffusion patterns
layered	stacked mineral or opal-like sheets
crystalline	structured facets and refractive nodes
fibrous	thread-like internal patterns
granular	small particulates, mineral clusters
veined	linear contrast veins
fractured	crack-like internal disruptions



---


---

## C. IDENTITY FEATURE TYPES

All identity features have independent fate controls.


---

1. Tattoos

<feature type="tattoos">
  fate = [ etched_relief | inked_subsurface | omitted ]
</feature>

Etched Relief Mode

depth_mm: 0.05–2.0               // shallow to deep carving
edge_definition: 0.0–1.0          // soft → sharp
fill_behavior: [ none | shadow | gold_inlay | pigment_inlay ]
weathering: 0.0–1.0               // pristine → ancient
surface_continuity: [ smooth | textured | fractured ]

Inked Subsurface Mode

ink_depth_mm: 0.5–3.0
clarity: 0.0–1.0                   // obscured → fully visible
diffusion: [ none | subtle | moderate | heavy ]
color_shift: [ neutral | warm | cool | desaturated | monochrome ]
interact_with_translucency: true/false
interact_with_veining: [ none | partial | full ]
gloss_interference: 0.0–1.0        // reflection masking strength

Omitted Mode

removal_completeness: 0.0–1.0
surface_memory: true/false         // faint topology ghost


---

2. Pigmented Marks (Freckles, Moles, Birthmarks)

<feature type="pigmented_marks">
  fate = [ preserved | omitted | converted_to_material_flaws ]
</feature>

Preserved Mode

render_as: [ subsurface_impurity | surface_spot | raised_inclusion ]
size_scaling: 0.5–2.0
color_inheritance: [ full | partial | none ]

Converted to Material Flaws

become: [ mineral_inclusion | vein_node | crystalline_flaw | air_pocket ]
distribution: match_original


---

3. Scars

<feature type="scars">
  fate = [ deepened | smoothed | omitted | crystallized ]
</feature>

Deepened Mode

depth_multiplier: 1.0–3.0
edge_character: [ rough | clean | fractured ]

Crystallized Mode

material_identity: opal
material_behavior: iridescent
microstructure: layered
glow_amount: 0.0–1.0
crack_intensity: 0.0–1.0
metal_fill: [ gold | silver | bronze | platinum | none ]
aesthetic_mode: kintsugi


---

4. Skin Tone Variations

<feature type="natural_discoloration">
  fate = [ preserved_as_marble_variation | unified_to_base_material | omitted ]
</feature>

Optional Behaviors

sun_exposure_memory: true/false       // tan becomes denser regions
vein_color_inheritance: true/false


---


---

## D. PRESET SYSTEM (New in v2.3)

Presets dramatically simplify user-facing control.


---

Example Presets


---

⭐ preset="ancient_relic"

Feature	Behavior

Tattoos	etched_relief (weathered)
Pigmented Marks	converted to mineral flaws
Scars	deepened, fractured edges
Discoloration	preserved_as_marble_variation


Usage:

<VSE::MATERIAL_BEHAVIOR scope="identity_features" preset="ancient_relic"/>


---

⭐ preset="kintsugi_divine"

Feature	Behavior

Tattoos	gold-filled etched relief
Scars	crystallized opal, gold veins
Pigmented Marks	subsurface impurities
Discoloration	unified to base material


Usage:

<VSE::MATERIAL_BEHAVIOR scope="identity_features" preset="kintsugi_divine"/>


---

⭐ preset="ghost_memory"

Feature	Behavior

Tattoos	omitted, faint surface_memory
Pigmented Marks	omitted
Scars	smoothed
Discoloration	omitted


Usage:

<VSE::MATERIAL_BEHAVIOR scope="identity_features" preset="ghost_memory"/>


---


---

## E. INLINE OVERRIDE SYSTEM

Presets can be adjusted without rewriting full feature blocks.

<VSE::MATERIAL_BEHAVIOR scope="identity_features" preset="kintsugi_divine">
  <override feature="tattoos">
    glow_amount = 0.9
    depth_mm = 1.2
  </override>
</VSE::MATERIAL_BEHAVIOR>


---

## F. FULL EXAMPLE IMPLEMENTATION

<VSE::material_transform>
  <material
    base="white_opal_marble"
    translucency="0.42"
    veining="warm_gold"
  />

  <VSE::MATERIAL_BEHAVIOR scope="identity_features" preset="ancient_relic">
    
    <override feature="scars">
      fate = crystallized
      glow_amount = 0.55
      metal_fill = gold
    </override>

  </VSE::MATERIAL_BEHAVIOR>
</VSE::material_transform>