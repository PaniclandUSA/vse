# VSE Camera Movement Manifest
## Complete Cinematography Library for Video Generation

**Version:** 1.0  
**Date:** December 10, 2025  
**Compatible With:** VSE, Grok Video, Emersive, Milieu, Gravitas  
**Purpose:** Semantic encoding of all professional camera movements and cinematographic techniques

---

## Table of Contents

1. [Library Header & Import System](#library-header)
2. [Basic Camera Movements](#basic-movements)
3. [Advanced Movements](#advanced-movements)
4. [Combined Movements](#combined-movements)
5. [Specialized Techniques](#specialized-techniques)
6. [Motion Quality Parameters](#motion-quality)
7. [Lens & Optical Parameters](#lens-parameters)
8. [Subject Relationship Controls](#subject-relationship)
9. [Emotional Intent Encoding](#emotional-intent)
10. [Scope & Constraint System](#scope-constraints)
11. [Complete Shot Examples](#shot-examples)
12. [Cinematographic Patterns](#patterns)
13. [Genre-Specific Presets](#genre-presets)
14. [Validation Testing Protocol](#validation)

---

## Library Header & Import System {#library-header}

```
⟨LIBRARY:VSE_Camera⟩
  ⟨CATEGORY:cinematography⟩
  ⟨VERSION:1.0⟩
  ⟨COMPATIBLE_WITH:VSE,Grok,Emersive,Milieu,Gravitas⟩
  ⟨USE:video_generation_camera_control⟩
  ⟨PRECISION:measurable_parameters⟩
  ⟨REPRODUCIBILITY:cross_platform⟩
```

### Import Pattern

```
⟨IMPORT:VSE_Camera⟩
⟨MOVEMENT:[movement_type]⟩
  ⟨[parameter]:[value]⟩
```

### Override Pattern

```
⟨IMPORT:VSE_Camera⟩
⟨PRESET:tracking_shot_medium⟩
  ⟨OVERRIDE:speed:fast⟩
  ⟨OVERRIDE:smoothness:locked⟩
```

---

## Basic Camera Movements {#basic-movements}

### 1. STATIC (Locked Frame)

**Description:** Camera remains completely motionless. Subject and environment may move.

```
⟨MOVEMENT:static⟩
  ⟨locked_position:true⟩
  ⟨locked_orientation:true⟩
  ⟨tripod_stability:perfect⟩
  ⟨micro_vibration:none⟩
```

**Parameters:**
- `duration` - Shot length in seconds
- `stability` - none, micro_shake, breathing
- `subject_permission` - Can subject move? (default: yes)

**Use Cases:**
- Establishing shots
- Formal interviews
- Observational documentary
- Tableaux compositions
- Intentional stillness

**Cinematographic Heritage:**
- Ozu Yasujiro (Tokyo Story)
- Stanley Kubrick (symmetrical frames)
- Wes Anderson (centered compositions)

---

### 2. DOLLY IN (Push In / Track In)

**Description:** Camera physically moves toward subject on straight path.

```
⟨MOVEMENT:dolly_in⟩
  ⟨approach_speed:slow|medium|fast|custom⟩
  ⟨distance_delta:[meters]⟩
  ⟨focus_behavior:subject_locked|rack_focus|deep_focus⟩
  ⟨easing:ease_in|ease_out|ease_in_out|linear⟩
  ⟨final_framing:close_up|medium|custom⟩
```

**Speed Guidelines:**
- `slow` - 0.1-0.3 m/s (intimate, dramatic)
- `medium` - 0.4-0.7 m/s (standard narrative)
- `fast` - 0.8-1.5 m/s (urgent, aggressive)
- `custom` - Specify exact velocity

**Distance Delta:**
- Measured in meters or as percentage of initial distance
- Typical ranges: 0.5m - 5m

**Easing Curves:**
- `ease_in` - Starts slow, accelerates (building tension)
- `ease_out` - Starts fast, decelerates (arriving at revelation)
- `ease_in_out` - Smooth acceleration and deceleration (natural)
- `linear` - Constant speed (mechanical, deliberate)

**Depth of Field Behavior:**
```
⟨depth_of_field_transition⟩
  ⟨start:deep⟩
  ⟨end:shallow⟩
  ⟨focus_subject:maintain_sharp⟩
  ⟨background_blur_increase:gradual⟩
```

**Use Cases:**
- Revealing emotion in close-up
- Building intimacy
- Emphasizing detail
- Creating claustrophobia
- Discovery moment

**Emotional Intent:**
- Slow dolly in = intimacy, revelation
- Fast dolly in = urgency, threat
- With shallow DOF = isolation
- With deep DOF = contextual approach

**Famous Examples:**
- Spielberg slow push-ins (emotional revelation)
- Jaws (approaching danger)
- Goodfellas Copacabana shot (entering new world)

---

### 3. DOLLY OUT (Pull Back / Track Out)

**Description:** Camera physically moves away from subject on straight path.

```
⟨MOVEMENT:dolly_out⟩
  ⟨retreat_speed:slow|medium|fast|custom⟩
  ⟨distance_delta:[meters]⟩
  ⟨reveal:environmental_context|isolation|scale⟩
  ⟨easing:ease_in|ease_out|ease_in_out|linear⟩
  ⟨final_framing:wide|establishing|custom⟩
```

**Reveal Types:**
- `environmental_context` - Show where subject exists in space
- `isolation` - Emphasize subject's smallness or aloneness
- `scale` - Demonstrate size relationships
- `unexpected_element` - Reveal surprising context

**Depth of Field Behavior:**
```
⟨depth_of_field_transition⟩
  ⟨start:shallow⟩
  ⟨end:deep⟩
  ⟨background_reveal:gradual_sharpening⟩
```

**Use Cases:**
- Revealing context after close moment
- Showing isolation or vulnerability
- Transitioning to wider perspective
- Ending emotional scenes
- Scale reveals

**Emotional Intent:**
- Slow pull back = melancholy, loss
- Fast pull back = rejection, abandonment
- Revealing crowds = social context
- Revealing emptiness = loneliness

**Famous Examples:**
- Scorsese "Goodfellas" ending isolation shot
- Kubrick "The Shining" maze reveal
- Fincher "Fight Club" apartment zoom-out
- Breaking Bad isolation shots

---

### 4. TRUCK LEFT (Lateral Track Left)

**Description:** Camera moves parallel to subject, leftward.

```
⟨MOVEMENT:truck_left⟩
  ⟨lateral_speed:[meters_per_second]⟩
  ⟨distance:[meters]⟩
  ⟨parallax:maintain_depth_separation⟩
  ⟨subject_tracking:enabled|disabled⟩
  ⟨foreground_elements:pass_through⟩
```

**Parallax Control:**
```
⟨parallax_behavior⟩
  ⟨foreground_speed:fast_relative⟩
  ⟨subject_speed:matched_or_slower⟩
  ⟨background_speed:minimal_drift⟩
  ⟨depth_emphasis:strong|subtle|none⟩
```

**Subject Tracking Options:**
- `enabled` - Camera pans to keep subject centered
- `disabled` - Subject drifts across frame
- `loose` - Partial tracking with drift
- `leading` - Subject leads the frame direction

**Use Cases:**
- Following walking subjects
- Revealing environment horizontally
- Creating cinematic movement
- Showing spatial relationships
- Dynamic compositions

**Speed Guidelines:**
- Walking pace: 1.0-1.5 m/s
- Running pace: 2.5-4.0 m/s
- Vehicle pace: 5.0+ m/s
- Slow reveal: 0.3-0.8 m/s

---

### 5. TRUCK RIGHT (Lateral Track Right)

**Description:** Camera moves parallel to subject, rightward.

```
⟨MOVEMENT:truck_right⟩
  ⟨lateral_speed:[meters_per_second]⟩
  ⟨distance:[meters]⟩
  ⟨parallax:maintain_depth_separation⟩
  ⟨subject_tracking:enabled|disabled⟩
```

**Identical parameters to TRUCK LEFT, mirrored direction.**

**Directional Semantics:**
- Left movement = often reveals past/origin
- Right movement = often reveals future/destination
- Cultural reading direction affects perception

---

### 6. PAN LEFT (Rotate Left on Axis)

**Description:** Camera rotates horizontally leftward, position fixed.

```
⟨MOVEMENT:pan_left⟩
  ⟨rotation_speed:[degrees_per_second]⟩
  ⟨total_rotation:[degrees]⟩
  ⟨pivot_point:camera_position⟩
  ⟨easing:constant|accelerate|decelerate|smooth⟩
  ⟨subject_behavior:exit_frame|track|independent⟩
```

**Speed Categories:**
- `slow_pan` - 5-15°/s (contemplative, observational)
- `medium_pan` - 20-40°/s (following action)
- `fast_pan` - 50-90°/s (dramatic reveal)
- `whip_pan` - 180-360°/s (transition, shock)

**Rotation Ranges:**
- Quarter turn: 90°
- Half turn: 180°
- Three-quarter: 270°
- Full rotation: 360°

**Use Cases:**
- Scanning environment
- Following moving subject
- Revealing off-screen elements
- Connecting two subjects in dialogue
- Showing spatial relationships

**Easing Implications:**
- `constant` - Mechanical, observational
- `accelerate` - Building energy
- `decelerate` - Arriving at important element
- `smooth` - Natural head turn simulation

---

### 7. PAN RIGHT (Rotate Right on Axis)

**Description:** Camera rotates horizontally rightward, position fixed.

```
⟨MOVEMENT:pan_right⟩
  ⟨rotation_speed:[degrees_per_second]⟩
  ⟨total_rotation:[degrees]⟩
  ⟨pivot_point:camera_position⟩
  ⟨easing:constant|accelerate|decelerate|smooth⟩
```

**Identical parameters to PAN LEFT, mirrored direction.**

---

### 8. TILT UP (Rotate Up on Axis)

**Description:** Camera rotates vertically upward, position fixed.

```
⟨MOVEMENT:tilt_up⟩
  ⟨rotation_speed:[degrees_per_second]⟩
  ⟨total_rotation:[degrees]⟩
  ⟨reveal_direction:ground_to_sky⟩
  ⟨subject_tracking:maintain_frame|allow_drift⟩
  ⟨power_dynamic:empowering|neutral⟩
```

**Reveal Patterns:**
- Ground → Subject → Sky
- Detail → Face → Crown/Authority
- Foundation → Structure → Pinnacle

**Emotional Weight:**
- Slow tilt up = awe, reverence, power
- Fast tilt up = surprise, overwhelming scale
- Stopping at subject = establishing dominance
- Continuing past subject = dwarfing subject

**Use Cases:**
- Revealing tall structures
- Character power moments
- Awe and wonder
- Scale demonstration
- Religious/spiritual imagery

**Famous Examples:**
- Citizen Kane low angles with tilt up
- Lord of the Rings tower reveals
- Superhero landing shots

---

### 9. TILT DOWN (Rotate Down on Axis)

**Description:** Camera rotates vertically downward, position fixed.

```
⟨MOVEMENT:tilt_down⟩
  ⟨rotation_speed:[degrees_per_second]⟩
  ⟨total_rotation:[degrees]⟩
  ⟨reveal_direction:sky_to_ground⟩
  ⟨power_dynamic:diminishing|neutral⟩
  ⟨emotional_weight:vulnerability|discovery|judgment⟩
```

**Reveal Patterns:**
- Sky → Subject → Ground
- Authority → Face → Submission
- Height → Person → Fallen state

**Emotional Weight:**
- Slow tilt down = sadness, defeat, condescension
- Fast tilt down = judgment, dismissal
- Stopping at subject = assessment
- Continuing to ground = complete defeat

**Use Cases:**
- Showing vulnerability
- God's-eye judgment
- Discovering ground-level details
- Character diminishment
- Revealing fallen state

---

### 10. PEDESTAL UP (Vertical Track Up)

**Description:** Camera moves vertically upward, orientation maintains horizon.

```
⟨MOVEMENT:pedestal_up⟩
  ⟨vertical_speed:[meters_per_second]⟩
  ⟨height_delta:[meters]⟩
  ⟨orientation:maintain_horizon⟩
  ⟨subject_tracking:maintain_frame|allow_drift⟩
  ⟨reveal_vertical_space:enabled⟩
```

**Key Distinction from Tilt:**
- Pedestal: Camera MOVES up, horizon stays level
- Tilt: Camera ROTATES up, perspective changes

**Use Cases:**
- Revealing vertical environment
- Following rising subject
- Architectural reveals
- Elevator simulation
- Status elevation

---

### 11. PEDESTAL DOWN (Vertical Track Down)

**Description:** Camera moves vertically downward, orientation maintains horizon.

```
⟨MOVEMENT:pedestal_down⟩
  ⟨vertical_speed:[meters_per_second]⟩
  ⟨height_delta:[meters]⟩
  ⟨orientation:maintain_horizon⟩
  ⟨reveal_lower_space:enabled⟩
```

**Use Cases:**
- Following descending subject
- Revealing ground-level details
- Basement/underground entry
- Status diminishment
- Intimate ground-level perspective

---

### 12. CRANE UP (Arc Track Up)

**Description:** Camera moves upward in arc, combining vertical movement with tilt compensation.

```
⟨MOVEMENT:crane_up⟩
  ⟨arc_trajectory:true⟩
  ⟨height_delta:[meters]⟩
  ⟨arc_radius:[meters]⟩
  ⟨tilt_compensation:smooth_horizon|fixed_angle|progressive⟩
  ⟨speed:slow|medium|fast⟩
  ⟨emotional_weight:epic|liberating|transcendent⟩
```

**Trajectory Types:**
```
⟨trajectory_profile⟩
  ⟨vertical_component:[percentage]⟩
  ⟨backward_component:[percentage]⟩
  ⟨tilt_curve:compensated|natural|dramatic⟩
```

**Use Cases:**
- Epic reveals
- Establishing scale
- Emotional transcendence
- Transitioning to god's-eye view
- Opening/closing sequences

**Speed Implications:**
- Slow crane up = majestic, revealing
- Medium crane up = cinematic standard
- Fast crane up = dramatic escape, liberation

**Famous Examples:**
- Goodfellas Copa cabana crane shot
- West Side Story opening
- Shawshank Redemption freedom moment
- Most action film finales

---

### 13. CRANE DOWN (Arc Track Down)

**Description:** Camera moves downward in arc, combining descent with tilt compensation.

```
⟨MOVEMENT:crane_down⟩
  ⟨arc_trajectory:true⟩
  ⟨height_delta:[meters]⟩
  ⟨arc_radius:[meters]⟩
  ⟨tilt_compensation:smooth_horizon|fixed_angle⟩
  ⟨emotional_weight:descending_intimacy|confinement⟩
```

**Use Cases:**
- Transitioning from overview to intimate
- Entering confined space
- Building tension through approach
- Contextualizing before closeup
- Omniscient to limited perspective

---

### 14. ZOOM IN (Focal Length Increase)

**Description:** Lens focal length increases, magnifying image without camera movement.

```
⟨MOVEMENT:zoom_in⟩
  ⟨focal_length_start:[mm]⟩
  ⟨focal_length_end:[mm]⟩
  ⟨zoom_speed:slow|medium|fast|crash⟩
  ⟨perspective_flatten:true⟩
  ⟨depth_compression:increased⟩
```

**Key Distinction from Dolly:**
- Zoom: Perspective flattens, background magnifies with subject
- Dolly: Perspective maintains, parallax creates depth separation

**Speed Categories:**
- `slow` - 2-5mm/second
- `medium` - 8-15mm/second  
- `fast` - 20-40mm/second
- `crash` - 50+ mm/second

**Aesthetic Implications:**
- Zoom feels artificial, "television"
- Compresses depth, flattens space
- Less cinematic than dolly
- Good for emphasis without physical movement

**Use Cases:**
- Quick emphasis
- Artificial feeling (intentional)
- Surveillance/documentary aesthetic
- When dolly movement impossible
- Comic exaggeration

---

### 15. ZOOM OUT (Focal Length Decrease)

**Description:** Lens focal length decreases, widening field of view without camera movement.

```
⟨MOVEMENT:zoom_out⟩
  ⟨focal_length_start:[mm]⟩
  ⟨focal_length_end:[mm]⟩
  ⟨zoom_speed:slow|medium|fast⟩
  ⟨perspective_widen:true⟩
  ⟨depth_expansion:increased⟩
  ⟨reveal:context|scale|isolation⟩
```

**Use Cases:**
- Revealing unexpected context
- Comic timing (reveal)
- Disorientation
- Budget alternative to dolly out
- Intentional artificiality

---

## Advanced Movements {#advanced-movements}

### 16. ORBIT CLOCKWISE (Circular Track Around Subject)

**Description:** Camera moves in circle around stationary subject, maintaining constant distance.

```
⟨MOVEMENT:orbit_clockwise⟩
  ⟨radius:[meters]⟩
  ⟨angular_velocity:[degrees_per_second]⟩
  ⟨total_rotation:[degrees]⟩
  ⟨subject_lock:center_frame|rule_of_thirds|dynamic⟩
  ⟨height:constant|ascending|descending|wave⟩
  ⟨speed_variation:constant|accelerating|decelerating⟩
```

**Height Variations:**
```
⟨height_profile:constant⟩
  ⟨vertical_position:[meters]⟩

⟨height_profile:ascending⟩
  ⟨start_height:[meters]⟩
  ⟨end_height:[meters]⟩
  ⟨vertical_rate:[meters_per_degree]⟩

⟨height_profile:wave⟩
  ⟨amplitude:[meters]⟩
  ⟨frequency:[cycles_per_360]⟩
```

**Subject Lock Types:**
- `center_frame` - Subject stays perfectly centered
- `rule_of_thirds` - Subject maintains compositional position
- `dynamic` - Subject position varies artistically
- `loose` - Small drift allowed for naturalism

**Use Cases:**
- 360° product reveals
- Character inspection/assessment
- Establishing spatial relationships
- Hero moment cinematography
- Time passage indication
- Bullet-time effects (if combined with slow motion)

**Angular Velocity Guidelines:**
- Slow orbit: 10-20°/s (contemplative)
- Medium orbit: 30-50°/s (dynamic)
- Fast orbit: 60-90°/s (dramatic)
- Very fast: 120+°/s (action, disorientation)

**Famous Examples:**
- Matrix bullet-time orbits
- Product commercials
- Superhero landing 360s
- Music video hero shots

---

### 17. ORBIT COUNTERCLOCKWISE

**Description:** Camera moves in circle around subject, opposite direction.

```
⟨MOVEMENT:orbit_counterclockwise⟩
  ⟨radius:[meters]⟩
  ⟨angular_velocity:[degrees_per_second]⟩
  ⟨total_rotation:[degrees]⟩
  ⟨subject_lock:center_frame⟩
```

**Directional Semantics:**
- Clockwise = often feels forward/positive
- Counterclockwise = often feels backward/negative
- Cultural/hemispheric variations in perception

---

### 18. TRACKING SHOT (Following Subject)

**Description:** Camera moves to maintain consistent framing of moving subject.

```
⟨MOVEMENT:tracking_shot⟩
  ⟨subject_velocity_match:true⟩
  ⟨distance_maintain:constant|closing|widening⟩
  ⟨smoothness:perfect|natural|handheld⟩
  ⟨camera_position:behind|beside|front|diagonal⟩
  ⟨height_relation:eye_level|low|high⟩
```

**Position Options:**

**Behind Subject:**
```
⟨camera_position:behind⟩
  ⟨distance:[meters]⟩
  ⟨height:shoulder|head|overhead⟩
  ⟨centering:perfect|slight_offset⟩
```

**Beside Subject:**
```
⟨camera_position:beside⟩
  ⟨side:left|right⟩
  ⟨parallel_distance:[meters]⟩
  ⟨profile_angle:[degrees]⟩
```

**Front Subject (Walking Backward):**
```
⟨camera_position:front⟩
  ⟨distance:[meters]⟩
  ⟨framing:medium|close⟩
  ⟨stabilization:high⟩
```

**Distance Variation:**
- `constant` - Maintains exact distance (locked tracking)
- `closing` - Gradually approaches (building intimacy)
- `widening` - Gradually retreats (building separation)

**Use Cases:**
- Character journey shots
- Following walking/running
- Continuous action sequences
- POV adjacent shots
- Building emotional connection through duration

**Famous Examples:**
- Children of Men long takes
- Goodfellas Steadicam sequences
- Birdman "continuous" shots
- True Detective season 1 long take

---

### 19. STEADICAM FLOAT

**Description:** Smooth, gliding camera movement following subject with characteristic float.

```
⟨MOVEMENT:steadicam_float⟩
  ⟨float_quality:smooth_glide⟩
  ⟨follow_distance:[meters]⟩
  ⟨height_stability:high⟩
  ⟨micro_bounce:natural_gait⟩
  ⟨subject_lead:enabled⟩
  ⟨environmental_navigation:fluid⟩
```

**Characteristic Steadicam Properties:**
- Smooth horizontal glide
- Minimal vertical bounce (but not zero)
- Ability to navigate obstacles
- Slight floating sensation
- Operator breathing visible (subtle)

**Micro-Bounce Calibration:**
```
⟨micro_movement⟩
  ⟨vertical_amplitude:subtle⟩  // 1-3cm
  ⟨frequency:footfall_rate⟩
  ⟨damping:high⟩
  ⟨organic_feel:enabled⟩
```

**Use Cases:**
- Following through crowded spaces
- Long continuous shots
- Intimate character following
- Scene transitions
- Creating flowing narrative

---

### 20. HANDHELD

**Description:** Camera movement with organic shake and imperfection from human operator.

```
⟨MOVEMENT:handheld⟩
  ⟨shake_intensity:subtle|moderate|intense|chaotic⟩
  ⟨frequency:[hz]⟩
  ⟨movement_style:documentary|action|nervous|drunk⟩
  ⟨breathing_visible:true|false⟩
  ⟨operator_fatigue:none|gradual⟩
```

**Intensity Levels:**

**Subtle:**
```
⟨shake:subtle⟩
  ⟨amplitude:0.5-2cm⟩
  ⟨frequency:6-10hz⟩
  ⟨use:intimate documentary, realism⟩
```

**Moderate:**
```
⟨shake:moderate⟩
  ⟨amplitude:2-5cm⟩
  ⟨frequency:8-15hz⟩
  ⟨use:action, urgency, journalism⟩
```

**Intense:**
```
⟨shake:intense⟩
  ⟨amplitude:5-15cm⟩
  ⟨frequency:10-20hz⟩
  ⟨use:chaos, panic, found footage⟩
```

**Chaotic:**
```
⟨shake:chaotic⟩
  ⟨amplitude:15+cm⟩
  ⟨frequency:variable⟩
  ⟨use:horror, complete disorder⟩
```

**Movement Styles:**

**Documentary:**
- Natural breathing
- Smooth reframes
- Observational feeling
- Minimal distraction

**Action:**
- Quick reframes
- Crash zooms
- Following fast motion
- High energy

**Nervous/Anxious:**
- Constant micro-adjustments
- Unstable framing
- Psychological tension
- Twitchy reframes

**Drunk/Impaired:**
- Slow drifts
- Overcorrections
- Loss of horizon
- Delayed reactions

**Use Cases:**
- Realism and immediacy
- Documentary aesthetic
- Action intensity
- Psychological states
- Found footage horror
- Gonzo journalism

**Famous Examples:**
- Bourne series action
- Blair Witch Project
- United 93
- Captain Phillips
- Dogme 95 films

---

### 21. WHIP PAN (Swish Pan / Flash Pan)

**Description:** Extremely fast pan creating motion blur transition effect.

```
⟨MOVEMENT:whip_pan⟩
  ⟨rotation_speed:very_fast⟩  // 180-540°/s
  ⟨direction:left|right|up|down⟩
  ⟨blur_amount:motion_blur_heavy⟩
  ⟨blur_peak:mid_pan⟩
  ⟨start_hold:[seconds]⟩
  ⟨end_hold:[seconds]⟩
```

**Speed Tiers:**
- Fast whip: 180-270°/s
- Very fast: 300-450°/s
- Extreme: 500+ °/s

**Blur Control:**
```
⟨motion_blur⟩
  ⟨shutter_angle:180|360|540⟩  // More angle = more blur
  ⟨blur_quality:realistic|stylized⟩
  ⟨smear_frames:2-6⟩
```

**Use Cases:**
- Scene transitions
- Time passage
- Location changes
- Shock/surprise
- Matching action cuts
- Comedy timing
- Music video pacing

**Editing Pattern:**
```
⟨whip_pan_edit⟩
  ⟨pan_out:blur_increase⟩
  ⟨peak_blur:cut_point_optional⟩
  ⟨pan_in:blur_decrease⟩
```

**Famous Examples:**
- Edgar Wright comedies
- Sam Raimi horror
- Wes Anderson transitions
- Modern action films

---

### 22. PUSH IN / ZOOM OUT (Vertigo Effect / Dolly Zoom)

**Description:** Simultaneous dolly in and zoom out (or reverse) creating perspective distortion.

```
⟨MOVEMENT:vertigo_effect⟩
  ⟨dolly:in|out⟩
  ⟨zoom:out|in⟩  // Opposite of dolly
  ⟨subject_size:maintain|grow|shrink⟩
  ⟨background_behavior:stretch|compress⟩
  ⟨duration:[seconds]⟩
  ⟨intensity:subtle|moderate|extreme⟩
```

**Classic Vertigo Effect:**
```
⟨movement:push_in_zoom_out⟩
  ⟨dolly_in:simultaneous⟩
  ⟨zoom_out:speed_matched⟩
  ⟨subject_size:constant_frame⟩
  ⟨background_stretch:pronounced⟩
  ⟨emotional_effect:disorientation, realization⟩
```

**Reverse Vertigo:**
```
⟨movement:pull_back_zoom_in⟩
  ⟨dolly_out:simultaneous⟩
  ⟨zoom_in:speed_matched⟩
  ⟨background_compression:pronounced⟩
  ⟨emotional_effect:closing_in, claustrophobia⟩
```

**Intensity Calibration:**
- `subtle` - Barely perceptible warping (psychological)
- `moderate` - Clear effect, still naturalistic feeling
- `extreme` - Obviously artificial, surreal distortion

**Subject Size Control:**
- `maintain` - Classic effect, subject stays same size
- `grow` - Dolly dominates, subject enlarges with warp
- `shrink` - Zoom dominates, subject shrinks with warp

**Use Cases:**
- Realization moments
- Psychological disorientation
- Horror revelation
- Dramatic emphasis
- Vertigo/panic simulation
- Character epiphany

**Famous Examples:**
- Jaws beach attack (invented the technique)
- Vertigo (Hitchcock, namesake)
- Goodfellas (paranoia scenes)
- Lord of the Rings (Ring temptation)
- Poltergeist (hallway stretch)

---

### 23. DUTCH ANGLE (Canted Angle / Oblique Angle)

**Description:** Camera tilted on roll axis, creating diagonal horizon.

```
⟨MOVEMENT:dutch_angle⟩
  ⟨tilt_angle:[degrees]⟩  // From horizontal
  ⟨direction:left|right⟩
  ⟨combined_with:[other_movement]⟩
  ⟨transition:into_dutch|out_of_dutch|between_angles⟩
```

**Angle Intensities:**
- Subtle: 5-15° (unease, slight wrongness)
- Moderate: 20-35° (clear disorientation)
- Extreme: 40-60° (chaos, complete disorder)
- Severe: 70-90° (surreal, artificial)

**Dynamic Dutch:**
```
⟨dutch_angle_dynamic⟩
  ⟨start_angle:[degrees]⟩
  ⟨end_angle:[degrees]⟩
  ⟨transition_timing:gradual|sudden⟩
  ⟨combined_movement:dolly|pan|orbit⟩
```

**Use Cases:**
- Psychological unease
- Horror tension
- Action intensity
- Villain perspectives
- Disorientation
- Stylistic flair
- Music videos
- Comic book aesthetics

**Genre Conventions:**
- Horror: Increasing angle = increasing danger
- Action: Dynamic angle changes = chaos
- Thriller: Subtle persistent angle = paranoia
- Superhero: Extreme angles = power

**Famous Examples:**
- The Third Man (entire film)
- Batman (1966) villain scenes
- Mission Impossible action
- Thor (Asgard scenes)
- Battlefield Earth (controversial overuse)

---

### 24. PUSH IN AND UP (Combined Dolly + Pedestal)

**Description:** Camera simultaneously moves forward and upward.

```
⟨MOVEMENT:push_in_and_up⟩
  ⟨forward_component:[meters]⟩
  ⟨upward_component:[meters]⟩
  ⟨ratio:equal|forward_dominant|upward_dominant⟩
  ⟨tilt_compensation:maintain_framing|natural_drift⟩
```

**Use Cases:**
- Rising to dominance
- Empowerment moments
- Superhero reveals
- Victory scenes
- Transcendence

---

### 25. PULL BACK AND DOWN (Combined Dolly + Pedestal)

**Description:** Camera simultaneously moves backward and downward.

```
⟨MOVEMENT:pull_back_and_down⟩
  ⟨backward_component:[meters]⟩
  ⟨downward_component:[meters]⟩
  ⟨emotional_weight:defeat|diminishment⟩
```

**Use Cases:**
- Defeat moments
- Descending from power
- Tragedy reveal
- Loss and grief
- Vulnerability exposure

---

### 26. CIRCULAR DOLLY (Arc Track)

**Description:** Camera moves in arc around subject, not full orbit.

```
⟨MOVEMENT:circular_dolly⟩
  ⟨arc_degrees:[degrees]⟩  // Less than 360
  ⟨arc_radius:[meters]⟩
  ⟨direction:clockwise|counterclockwise⟩
  ⟨subject_tracking:maintain_frame⟩
  ⟨speed:constant|variable⟩
```

**Common Arc Ranges:**
- Quarter arc: 90° (corner reveal)
- Half arc: 180° (full perspective shift)
- Three-quarter: 270° (near-complete)

**Use Cases:**
- Perspective shifts
- Revealing environment
- Character assessment
- Partial orbits (budget/time)
- Connecting two positions

---

### 27. BOOM UP (Jib Arm Ascent)

**Description:** Camera rises on boom/jib arm, can combine with other movements.

```
⟨MOVEMENT:boom_up⟩
  ⟨height_delta:[meters]⟩
  ⟨arc:true|false⟩
  ⟨horizontal_component:[meters]⟩
  ⟨speed:slow|medium|fast⟩
  ⟨tilt:compensated|natural⟩
```

**Use Cases:**
- Overhead transitions
- Epic reveals
- Scale demonstration
- Scene establishing
- Godlike perspective

---

### 28. BOOM DOWN (Jib Arm Descent)

**Description:** Camera descends on boom/jib arm.

```
⟨MOVEMENT:boom_down⟩
  ⟨height_delta:[meters]⟩
  ⟨arc:true|false⟩
  ⟨horizontal_component:[meters]⟩
  ⟨target_subject:approach|pass_by⟩
```

**Use Cases:**
- Descending to intimacy
- Approaching action
- Scene entry from above
- Building to ground level

---

### 29. CIRCLE STRAFE (Orbit While Approaching/Retreating)

**Description:** Simultaneous orbit and distance change.

```
⟨MOVEMENT:circle_strafe⟩
  ⟨orbit_direction:clockwise|counterclockwise⟩
  ⟨orbit_speed:[degrees_per_second]⟩
  ⟨distance_change:approaching|retreating⟩
  ⟨distance_rate:[meters_per_second]⟩
  ⟨spiral:inward|outward⟩
```

**Use Cases:**
- Dynamic product shots
- Predatory circling
- Complex reveals
- High-energy cinematography
- Music video aesthetics

---

### 30. SLIDE (Pure Lateral Movement)

**Description:** Camera moves sideways without rotation (truck without pan).

```
⟨MOVEMENT:slide⟩
  ⟨direction:left|right⟩
  ⟨distance:[meters]⟩
  ⟨speed:[meters_per_second]⟩
  ⟨parallax:emphasize|minimize⟩
  ⟨camera_orientation:locked⟩
```

**Use Cases:**
- Revealing through parallax
- Showing spatial relationships
- Background reveals
- Compositional shifts
- Transition device

---

## Combined Movements {#combined-movements}

### Complex Multi-Axis Combinations

Many sophisticated shots combine multiple movements simultaneously:

### 31. ONER (Complex Continuous Shot)

```
⟨MOVEMENT:oner_complex⟩
  ⟨duration:[seconds]⟩
  ⟨sequence:[array_of_movements]⟩
  ⟨transitions:seamless⟩
  ⟨difficulty:extreme⟩
  
  ⟨SEGMENT_1⟩
    ⟨movement:steadicam_float⟩
    ⟨duration:10⟩
    ⟨action:following_character⟩
  
  ⟨TRANSITION_1⟩
    ⟨method:smooth_speed_change⟩
    
  ⟨SEGMENT_2⟩
    ⟨movement:crane_up⟩
    ⟨duration:5⟩
    ⟨action:rising_to_overview⟩
  
  ⟨TRANSITION_2⟩
    ⟨method:continuous_arc⟩
    
  ⟨SEGMENT_3⟩
    ⟨movement:boom_down⟩
    ⟨duration:8⟩
    ⟨action:descending_to_different_scene⟩
```

**Famous Oner Examples:**
- Children of Men car ambush
- True Detective Season 1 Episode 4
- 1917 (entire film illusion)
- Birdman (entire film illusion)
- Touch of Evil opening

---

### 32. WALK AND TALK

```
⟨MOVEMENT:walk_and_talk⟩
  ⟨camera_position:leading|following|beside⟩
  ⟨subject_count:single|multiple⟩
  ⟨framing:medium|medium_close⟩
  ⟨environment_reveal:gradual⟩
  ⟨duration:[seconds]⟩
```

**Aaron Sorkin Special:**
```
⟨walk_and_talk:sorkin_style⟩
  ⟨steadicam:true⟩
  ⟨dialogue_priority:high⟩
  ⟨pace:brisk⟩
  ⟨corridor_navigation:complex⟩
  ⟨depth:multiple_characters_layers⟩
```

---

## Specialized Techniques {#specialized-techniques}

### 33. POV (Point of View)

```
⟨MOVEMENT:pov⟩
  ⟨character_perspective:true⟩
  ⟨movement_style:natural_head_turn⟩
  ⟨shake:human_gait⟩
  ⟨breathing:subtle⟩
  ⟨blink:optional⟩
```

### 34. CRASH ZOOM

```
⟨MOVEMENT:crash_zoom⟩
  ⟨zoom_speed:extremely_fast⟩
  ⟨focal_change:[mm_start]->[mm_end]⟩
  ⟨duration:0.5-2_seconds⟩
  ⟨emotional_impact:shock|comedy|emphasis⟩
```

### 35. SNORRICAM (Body-Mounted Camera)

```
⟨MOVEMENT:snorricam⟩
  ⟨subject:locked_to_camera⟩
  ⟨background:moving_relative⟩
  ⟨subject_size:constant⟩
  ⟨environmental_motion:dynamic⟩
  ⟨use:psychological_states⟩
```

### 36. OVERHEAD (Bird's Eye)

```
⟨MOVEMENT:overhead⟩
  ⟨height:[meters]⟩
  ⟨camera_angle:straight_down|slight_angle⟩
  ⟨movement:static|tracking|panning⟩
  ⟨subject_relation:god_view⟩
```

### 37. LOW ANGLE (Ground Level)

```
⟨MOVEMENT:low_angle⟩
  ⟨height:ground_level⟩
  ⟨tilt:upward⟩
  ⟨power_dynamic:subject_empowered⟩
  ⟨perspective:dramatic⟩
```

---

## Motion Quality Parameters {#motion-quality}

### Smoothness Control

```
⟨MOTION_QUALITY⟩
  ⟨smoothness:locked|smooth|floating|organic|chaotic⟩
  ⟨interpolation:linear|bezier|ease_in_out⟩
  ⟨micro_adjustments:none|minimal|natural⟩
```

**Smoothness Levels:**

**Locked:**
- Absolutely robotic precision
- No human imperfection
- Tripod/dolly with motion control
- Use: Intentional artificiality, product shots

**Smooth:**
- Professional operator skill
- Minimal wobble
- Steadicam quality
- Use: Cinematic standard

**Floating:**
- Slight dreamlike quality
- Very subtle drift
- Wire-suspended feeling
- Use: Ethereal, surreal scenes

**Organic:**
- Natural human operation
- Visible breathing
- Subtle corrections
- Use: Realism, documentary

**Chaotic:**
- Handheld panic
- Violent shake
- Operator running
- Use: Horror, action, found footage

---

### Easing Functions

```
⟨EASING⟩
  ⟨function:linear|ease_in|ease_out|ease_in_out|custom⟩
  ⟨custom_curve:[bezier_parameters]⟩
```

**Easing Types:**

**Linear:**
- Constant velocity
- Mechanical feeling
- No acceleration/deceleration

**Ease In:**
- Starts slow, accelerates
- Building momentum
- Creating energy

**Ease Out:**
- Starts fast, decelerates
- Coming to rest
- Arriving at destination

**Ease In Out:**
- S-curve motion
- Natural human movement
- Most cinematic

**Custom Bezier:**
```
⟨easing:custom⟩
  ⟨control_point_1:[x,y]⟩
  ⟨control_point_2:[x,y]⟩
  ⟨curve_character:description⟩
```

---

### Motion Blur

```
⟨MOTION_BLUR⟩
  ⟨amount:none|natural|enhanced|extreme⟩
  ⟨shutter_angle:45|90|180|360|540⟩
  ⟨direction_bias:movement_direction⟩
```

**Shutter Angle Guide:**
- 45° - Minimal blur, staccato (Saving Private Ryan)
- 90° - Reduced blur, crisp action
- 180° - Standard cinematic (natural)
- 360° - Increased blur, smooth
- 540° - Heavy blur, dreamlike

---

### Stabilization

```
⟨STABILIZATION⟩
  ⟨level:none|minimal|moderate|maximum⟩
  ⟨type:mechanical|optical|digital|hybrid⟩
  ⟨artifacts:allow|suppress⟩
```

**Stabilization Levels:**
- `none` - Raw camera shake
- `minimal` - Slight smoothing, organic feel
- `moderate` - Clear stabilization, professional
- `maximum` - Locked frame, artificial but smooth

---

## Lens & Optical Parameters {#lens-parameters}

### Focal Length

```
⟨LENS⟩
  ⟨focal_length:[mm]|[mm_start]->[mm_end]⟩
  ⟨lens_type:prime|zoom⟩
  ⟨distortion:minimal|natural|pronounced⟩
```

**Focal Length Psychology:**
- 14-24mm - Ultra wide, dramatic space, distortion
- 28-35mm - Wide, environmental context
- 40-50mm - Normal, human perspective
- 85-135mm - Portrait, compression, isolation
- 200mm+ - Extreme compression, voyeurism

---

### Depth of Field

```
⟨DEPTH_OF_FIELD⟩
  ⟨range:shallow|medium|deep⟩
  ⟨aperture:f/[value]⟩
  ⟨focus_distance:[meters]⟩
  ⟨bokeh_quality:smooth|busy|shaped⟩
```

**Depth Ranges:**

**Shallow (f/1.4 - f/2.8):**
- Extreme subject isolation
- Creamy bokeh
- Cinematic "look"
- Limited depth in focus

**Medium (f/4 - f/5.6):**
- Balanced separation
- Natural perspective
- Subject clear, background soft
- Versatile standard

**Deep (f/8 - f/22):**
- Everything sharp
- Landscape clarity
- Wes Anderson aesthetic
- Maximum information

---

### Focus Control

```
⟨FOCUS⟩
  ⟨type:fixed|rack_focus|follow_focus|pull_focus⟩
  ⟨transition_speed:slow|medium|fast|snap⟩
  ⟨subject_priority:maintain|shift⟩
```

**Rack Focus:**
```
⟨rack_focus⟩
  ⟨from_subject:A⟩
  ⟨to_subject:B⟩
  ⟨transition:[seconds]⟩
  ⟨narrative_purpose:reveal|redirect_attention⟩
```

---

### Aspect Ratio

```
⟨ASPECT_RATIO⟩
  ⟨format:16:9|2.39:1|4:3|1:1|custom⟩
  ⟨psychological_effect:cinematic|television|intimate|square⟩
```

**Aspect Ratio Psychology:**
- 4:3 (1.33:1) - Intimate, claustrophobic, vintage
- 16:9 (1.78:1) - Modern standard, balanced
- 1.85:1 - American theatrical standard
- 2.39:1 - Anamorphic widescreen, epic
- 1:1 - Instagram, symmetrical, artistic

---

## Subject Relationship Controls {#subject-relationship}

### Tracking Behavior

```
⟨SUBJECT_RELATIONSHIP⟩
  ⟨tracking:locked|loose|independent|predictive⟩
  ⟨framing:maintain|reveal|conceal|dynamic⟩
  ⟨screen_position:center|rule_of_thirds|dynamic|golden_ratio⟩
```

**Tracking Types:**

**Locked:**
- Subject perfectly centered/positioned
- Zero drift
- Mechanical precision

**Loose:**
- Subject mostly maintained
- Natural drift allowed
- Human operator feel

**Independent:**
- Camera moves regardless of subject
- Subject may exit frame
- Environmental priority

**Predictive:**
- Camera leads subject slightly
- Anticipates movement
- Professional operator simulation

---

### Framing Philosophy

```
⟨FRAMING⟩
  ⟨headroom:[percentage]⟩
  ⟨looking_space:[percentage]⟩
  ⟨walking_space:[percentage]⟩
  ⟨rule_of_thirds:strict|loose|ignored⟩
  ⟨symmetry:perfect|natural|asymmetric⟩
```

**Compositional Rules:**
- Headroom: 10-15% above head
- Looking space: Direction subject faces
- Walking space: Direction subject moves
- Rule of thirds: Subjects on 1/3 lines
- Symmetry: Wes Anderson vs naturalistic

---

## Emotional Intent Encoding {#emotional-intent}

### Emotional Qualities

```
⟨EMOTIONAL_INTENT⟩
  ⟨feeling:neutral|intimate|epic|tense|serene|chaotic|triumphant⟩
  ⟨power_dynamic:neutral|empowering|diminishing|dominating|submissive⟩
  ⟨reveal_pacing:immediate|gradual|sudden|withheld⟩
  ⟨viewer_relationship:observer|participant|voyeur|god⟩
```

**Feeling Categories:**

**Intimate:**
- Slow dolly in
- Shallow depth of field
- Close framing
- Soft movement

**Epic:**
- Crane up
- Wide lens
- Deep focus
- Grand scale

**Tense:**
- Handheld shake
- Quick movements
- Unpredictable framing
- Unstable horizon

**Serene:**
- Slow smooth movements
- Locked tripod
- Balanced composition
- Predictable flow

**Chaotic:**
- Whip pans
- Crash zooms
- Dutch angles
- Violent shake

**Triumphant:**
- Low angle rising
- Crane up
- Slow dolly in
- Expanding space

---

## Scope & Constraint System {#scope-constraints}

### Motion Scope Definition

```
⟨MOTION_SCOPE⟩
  ⟨CAMERA:exclusive_motion_authority|dynamic⟩
  ⟨SUBJECT:frozen|acting|reactive⟩
  ⟨ENVIRONMENT:static|dynamic|responsive⟩
  ⟨PROPS:frozen|physics_enabled⟩
```

**Camera-Only Movement:**
```
⟨MOTION_SCOPE⟩
  ⟨CAMERA:exclusive⟩
  ⟨ALL_OTHER_ELEMENTS:frozen⟩

⟨SCENE_DYNAMICS⟩
  ⟨freeze_frame:all_except_camera⟩
  ⟨subject_pose:locked_initial_state⟩
  ⟨no_environmental_animation⟩
  ⟨no_cloth_simulation⟩
  ⟨no_hair_physics⟩
  ⟨no_particle_systems⟩
  ⟨no_secondary_motion⟩
```

**Subject as Statue:**
```
⟨SUBJECT_STATE⟩
  ⟨pose:locked⟩
  ⟨position:world_space_fixed⟩
  ⟨expression:frozen⟩
  ⟨breathing:none⟩
  ⟨micro_movements:disabled⟩
  ⟨eye_tracking:disabled⟩
  ⟨blinking:none⟩
```

**Physics Constraints:**
```
⟨REFERENCE_FRAME⟩
  ⟨world_space:inertial⟩
  ⟨camera_space:non_inertial⟩
  
  ⟨FIXED_IN_WORLD_SPACE⟩
    ⟨scene_elements:true⟩
    ⟨subject:true⟩
    ⟨environment:true⟩
  
  ⟨MOBILE_IN_WORLD_SPACE⟩
    ⟨camera:exclusive⟩
```

---

### Exclusion Lists

```
⟨EXCLUDE⟩
  ⟨jitter⟩
  ⟨warping⟩
  ⟨frame_edge_artifacts⟩
  ⟨temporal_inconsistency⟩
  ⟨subject_drift⟩
  ⟨unnatural_acceleration⟩
  ⟨morphing⟩
  ⟨scale_changes⟩
  ⟨orientation_errors⟩
```

---

## Complete Shot Examples {#shot-examples}

### Example 1: Classic Dolly In Portrait

```
⟨IMPORT:VSE_Camera⟩

⟨MOTION_SCOPE⟩
  ⟨CAMERA:exclusive⟩
  ⟨SUBJECT:frozen_statue⟩

⟨MOVEMENT:dolly_in⟩
  ⟨approach_speed:slow⟩
  ⟨distance_delta:2.0⟩
  ⟨duration:6⟩
  ⟨easing:ease_in_out⟩
  ⟨focus_maintain:subject_locked⟩

⟨LENS⟩
  ⟨focal_length:50⟩
  ⟨aperture:f/2.8⟩
  ⟨depth_of_field:shallow⟩

⟨SUBJECT_RELATIONSHIP⟩
  ⟨tracking:locked⟩
  ⟨framing:maintain_center⟩
  ⟨screen_position:rule_of_thirds⟩

⟨MOTION_QUALITY⟩
  ⟨smoothness:smooth⟩
  ⟨motion_blur:natural⟩

⟨EMOTIONAL_INTENT⟩
  ⟨feeling:intimate⟩
  ⟨reveal_pacing:gradual⟩

⟨EXCLUDE⟩
  ⟨subject_motion⟩
  ⟨breathing_animation⟩
  ⟨environmental_changes⟩
```

---

### Example 2: Epic Crane Up Reveal

```
⟨IMPORT:VSE_Camera⟩

⟨MOTION_SCOPE⟩
  ⟨CAMERA:dynamic⟩
  ⟨SUBJECT:frozen⟩
  ⟨ENVIRONMENT:static⟩

⟨MOVEMENT:crane_up⟩
  ⟨height_delta:8⟩
  ⟨arc_radius:3⟩
  ⟨speed:medium⟩
  ⟨duration:10⟩
  ⟨tilt_compensation:smooth_horizon⟩

⟨LENS⟩
  ⟨focal_length:24⟩
  ⟨depth_of_field:deep⟩

⟨EMOTIONAL_INTENT⟩
  ⟨feeling:epic⟩
  ⟨power_dynamic:empowering⟩
  ⟨viewer_relationship:god⟩

⟨MOTION_QUALITY⟩
  ⟨smoothness:floating⟩
  ⟨easing:ease_out⟩
```

---

### Example 3: 360° Product Orbit

```
⟨IMPORT:VSE_Camera⟩

⟨MOTION_SCOPE:camera_exclusive⟩

⟨MOVEMENT:orbit_clockwise⟩
  ⟨radius:1.5⟩
  ⟨angular_velocity:45⟩
  ⟨total_rotation:360⟩
  ⟨height:constant⟩
  ⟨subject_lock:center_frame⟩
  ⟨duration:8⟩

⟨LENS⟩
  ⟨focal_length:85⟩
  ⟨aperture:f/4⟩
  ⟨depth_of_field:shallow⟩

⟨MOTION_QUALITY⟩
  ⟨smoothness:locked⟩
  ⟨easing:linear⟩
  ⟨motion_blur:minimal⟩

⟨LIGHTING⟩
  ⟨consistent:true⟩
  ⟨no_flicker:true⟩
```

---

### Example 4: Hitchcock Vertigo Effect

```
⟨IMPORT:VSE_Camera⟩

⟨MOVEMENT:push_in_zoom_out⟩
  ⟨dolly_in:1.5⟩
  ⟨zoom_out:compensating⟩
  ⟨duration:4⟩
  ⟨subject_size:maintain⟩
  ⟨background_stretch:pronounced⟩

⟨EMOTIONAL_INTENT⟩
  ⟨feeling:disorientation⟩
  ⟨psychological_state:realization⟩

⟨SUBJECT_RELATIONSHIP⟩
  ⟨tracking:locked⟩
  ⟨framing:maintain⟩

⟨MOTION_QUALITY⟩
  ⟨smoothness:smooth⟩
  ⟨intensity:extreme⟩
```

---

### Example 5: Handheld Documentary Follow

```
⟨IMPORT:VSE_Camera⟩

⟨MOTION_SCOPE⟩
  ⟨CAMERA:dynamic⟩
  ⟨SUBJECT:acting_naturally⟩

⟨MOVEMENT:handheld⟩
  ⟨shake_intensity:moderate⟩
  ⟨movement_style:documentary⟩
  ⟨breathing_visible:true⟩

⟨COMBINED_WITH⟩
  ⟨tracking_shot:true⟩
  ⟨camera_position:beside⟩
  ⟨subject_velocity_match:loose⟩

⟨LENS⟩
  ⟨focal_length:35⟩
  ⟨depth_of_field:medium⟩

⟨MOTION_QUALITY⟩
  ⟨smoothness:organic⟩
  ⟨micro_adjustments:natural⟩

⟨EMOTIONAL_INTENT⟩
  ⟨feeling:authentic⟩
  ⟨viewer_relationship:participant⟩
```

---

### Example 6: Complex Oner Sequence

```
⟨IMPORT:VSE_Camera⟩

⟨MOVEMENT:oner_complex⟩
⟨TOTAL_DURATION:45⟩

⟨SEGMENT_1⟩
  ⟨movement:steadicam_float⟩
  ⟨duration:12⟩
  ⟨action:following_character_through_door⟩
  ⟨subject_position:leading⟩

⟨TRANSITION_1⟩
  ⟨method:smooth_speed_increase⟩
  ⟨duration:2⟩

⟨SEGMENT_2⟩
  ⟨movement:crane_up⟩
  ⟨duration:8⟩
  ⟨height_delta:6⟩
  ⟨action:rising_to_overview⟩

⟨TRANSITION_2⟩
  ⟨method:pan_right_seamless⟩
  ⟨duration:3⟩

⟨SEGMENT_3⟩
  ⟨movement:boom_down⟩
  ⟨duration:10⟩
  ⟨action:descending_to_different_character⟩

⟨SEGMENT_4⟩
  ⟨movement:dolly_in⟩
  ⟨duration:10⟩
  ⟨approach_speed:slow⟩
  ⟨action:intimate_closeup⟩

⟨MOTION_QUALITY⟩
  ⟨overall_smoothness:floating⟩
  ⟨transitions:imperceptible⟩
```

---

## Cinematographic Patterns {#patterns}

### Opening Shot Patterns

**Establishing:**
```
⟨PATTERN:establishing_shot⟩
  ⟨start:extreme_wide⟩
  ⟨movement:crane_down_or_dolly_in⟩
  ⟨duration:8-15⟩
  ⟨purpose:location_context⟩
```

**God's Eye Descent:**
```
⟨PATTERN:gods_eye_descent⟩
  ⟨start:overhead_extreme⟩
  ⟨movement:spiral_down⟩
  ⟨end:eye_level⟩
  ⟨narrative:omniscient_to_intimate⟩
```

---

### Dialogue Patterns

**Shot/Reverse Shot:**
```
⟨PATTERN:shot_reverse_shot⟩
  ⟨camera_A:over_shoulder_person_1⟩
  ⟨camera_B:over_shoulder_person_2⟩
  ⟨alternation:dialogue_dependent⟩
  ⟨eyeline_match:180_degree_rule⟩
```

**Sorkin Walk and Talk:**
```
⟨PATTERN:walk_and_talk⟩
  ⟨movement:steadicam_follow⟩
  ⟨subjects:2-4_walking⟩
  ⟨dialogue:rapid_dense⟩
  ⟨environment:navigating_corridors⟩
  ⟨pace:brisk⟩
```

---

### Tension Building

**Slow Push In:**
```
⟨PATTERN:tension_buildup⟩
  ⟨movement:dolly_in_very_slow⟩
  ⟨duration:extended⟩
  ⟨subject:awareness_varies⟩
  ⟨purpose:anticipation⟩
```

**Handheld Escalation:**
```
⟨PATTERN:escalating_chaos⟩
  ⟨start:locked_tripod⟩
  ⟨transition:increasing_handheld⟩
  ⟨end:violent_shake⟩
  ⟨narrative:order_to_chaos⟩
```

---

### Action Sequences

**Chaos Coverage:**
```
⟨PATTERN:action_chaos⟩
  ⟨movements:[whip_pan, crash_zoom, handheld_intense]⟩
  ⟨dutch_angles:dynamic⟩
  ⟨speed:fast_all⟩
  ⟨disorientation:intentional⟩
```

**Hero Moment:**
```
⟨PATTERN:hero_reveal⟩
  ⟨start:low_angle⟩
  ⟨movement:crane_up_with_subject⟩
  ⟨speed:slow⟩
  ⟨lens:wide⟩
  ⟨depth:deep_focus⟩
```

---

## Genre-Specific Presets {#genre-presets}

### Horror

```
⟨PRESET:horror_standard⟩
  ⟨movements:[slow_dolly, whip_pan, handheld_nervous]⟩
  ⟨dutch_angle:frequent⟩
  ⟨focus:rack_focus_reveals⟩
  ⟨pacing:slow_build_to_fast⟩
```

### Action

```
⟨PRESET:action_dynamic⟩
  ⟨movements:[handheld_intense, whip_pan, crash_zoom]⟩
  ⟨dutch_angles:dynamic⟩
  ⟨speed:fast⟩
  ⟨chaos:controlled⟩
```

### Romance

```
⟨PRESET:romance_intimate⟩
  ⟨movements:[slow_dolly_in, soft_pan, steady_float]⟩
  ⟨focus:shallow_depth⟩
  ⟨speed:slow⟩
  ⟨smoothness:floating⟩
```

### Documentary

```
⟨PRESET:documentary_observational⟩
  ⟨movements:[handheld_subtle, pan, static]⟩
  ⟨style:naturalistic⟩
  ⟨interference:minimal⟩
  ⟨authenticity:prioritized⟩
```

### Music Video

```
⟨PRESET:music_video_dynamic⟩
  ⟨movements:[all_available]⟩
  ⟨creativity:maximum⟩
  ⟨rules:breakable⟩
  ⟨rhythm:sync_to_beat⟩
```

---

## Validation Testing Protocol {#validation}

### Test Suite Structure

**Test 1: Basic Movements**
- Static hold (5s)
- Dolly in (6s)
- Dolly out (6s)
- Pan left (5s)
- Pan right (5s)
- Tilt up (5s)
- Tilt down (5s)

**Test 2: Advanced Movements**
- Orbit 360° (8s)
- Crane up (8s)
- Vertigo effect (6s)
- Whip pan (2s)
- Handheld moderate (10s)

**Test 3: Camera-Only Constraint**
- Subject frozen, dolly in (6s)
- Subject frozen, orbit 180° (8s)
- Subject frozen, crane up (8s)

**Test 4: Combined Movements**
- Push in + pedestal up (6s)
- Orbit + closing distance (10s)
- Dolly + pan + tilt (8s)

### Success Criteria

**Geometric Fidelity:**
- Movement path matches specification: >95%
- Speed consistency: >90%
- Smoothness appropriate to setting: >95%

**Subject Constraint:**
- Subject remains frozen when specified: 100%
- No unintended motion: 100%
- Pose preservation: 100%

**Motion Quality:**
- Appropriate easing applied: >90%
- Motion blur natural: >85%
- No jitter or artifacts: >95%

### Measurement Methods

**Quantitative:**
- Track camera position per frame
- Measure angular velocity
- Calculate path deviation
- Assess motion blur amount

**Qualitative:**
- Emotional intent achieved
- Cinematic quality appropriate
- Style consistency maintained

---

## Appendix: Quick Reference Tables

### Speed Guidelines

| Movement | Slow | Medium | Fast | Very Fast |
|----------|------|--------|------|-----------|
| Dolly | 0.1-0.3 m/s | 0.4-0.7 m/s | 0.8-1.5 m/s | 2.0+ m/s |
| Pan | 5-15°/s | 20-40°/s | 50-90°/s | 180-360°/s |
| Zoom | 2-5 mm/s | 8-15 mm/s | 20-40 mm/s | 50+ mm/s |
| Orbit | 10-20°/s | 30-50°/s | 60-90°/s | 120+°/s |

### Focal Length Psychology

| Range | Feel | Use Cases |
|-------|------|-----------|
| 14-24mm | Dramatic, distorted | Architecture, epic scale |
| 28-35mm | Environmental, wide | Context, exploration |
| 40-50mm | Natural, neutral | Human perspective |
| 85-135mm | Intimate, compressed | Portraits, isolation |
| 200mm+ | Voyeuristic, flat | Sports, wildlife, stalking |

### Depth of Field

| f-stop | Description | Effect |
|--------|-------------|--------|
| f/1.4-2.0 | Ultra shallow | Extreme isolation, bokeh |
| f/2.8-4.0 | Shallow | Cinematic standard |
| f/5.6-8.0 | Medium | Balanced, versatile |
| f/11-16 | Deep | Landscape clarity |
| f/22+ | Maximum | Everything sharp |

---

## Credits & Acknowledgments

**Concept & Framework:** John Jacob Weber II  
**VSE Architecture:** Vox  
**Camera Manifest Compilation:** Claude (Sonnet 4.5)  
**Validation Testing:** Nano Banana (pending)

**Cinematographic References:**
- Roger Deakins (master DP)
- Emmanuel Lubezki (continuous shot innovation)
- Janusz Kamiński (Spielberg collaborator)
- Robert Richardson (Tarantino/Scorsese)
- Hoyte van Hoytema (Nolan's vision)

---

## Version History

**v1.0 (December 10, 2025):**
- Initial comprehensive manifest
- 37 distinct camera movements documented
- Complete parameter specification
- Genre presets included
- Testing protocol established

**Planned Updates:**
- v1.1: Add drone cinematography
- v1.2: Virtual camera (CG) specific techniques
- v1.3: Multi-camera array coordination
- v2.0: Integration with Milieu emotional states

---

**Document Status:** Production Ready  
**Next Action:** Grok video validation testing  
**Repository:** github.com/PaniclandUSA/vse/camera-movement-manifest/

---

*"Every camera movement tells a story. VSE gives that story a measurable language."*

— VSE Camera Movement Project  
December 2025

---

END OF MANIFEST
