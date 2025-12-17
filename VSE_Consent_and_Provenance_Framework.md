# VSE Consent and Provenance Framework

**Declarative Consent for Human Representation in Generative Systems**

---

## Document Purpose

This framework establishes a consent and provenance declaration system for human representation in AI-generated content. It separates consent (a legal/ethical property) from content (a visual property), enabling systems to enforce ethical standards without attempting to infer consent from pixels.

**Companion Documents**: 
- [VSE_non-invertible_realism-NIR.md](./VSE_non-invertible_realism-NIR.md) (Philosophical manifesto)
- [NIR_engineering_specification.md](./NIR_engineering_specification.md) (Technical implementation)

**Status**: v1.0 - Production Ready  
**Last Updated**: 2025-12-17  
**Maintainer**: Vector-Space Esperanto (VSE) Project

---

## Table of Contents

1. [Core Principle](#core-principle)
2. [Why Visual Inference Fails](#why-visual-inference-fails)
3. [The Declarative Consent Model](#the-declarative-consent-model)
4. [Alignment with Established Legal Frameworks](#alignment-with-established-legal-frameworks)
5. [VSE Consent Declaration Specification](#vse-consent-declaration-specification)
6. [Use Cases and Examples](#use-cases-and-examples)
7. [Liability Assignment](#liability-assignment)
8. [Integration with NIR](#integration-with-nir)
9. [Platform Implementation Guide](#platform-implementation-guide)
10. [FAQ](#faq)

---

## Core Principle

**Consent is not a visual property. It is a provenance property.**

Current AI safety systems attempt to infer consent by analyzing image content:
- "Does this look like a real person?"
- "Does this appear sexual?"
- "Could this be exploitative?"

These are aesthetic guesses, not ethical determinations. Consent cannot be detected from pixels—it must be declared upstream and recorded auditably.

### The Parallel to Copyright

The copyright system already solved this problem:

| Copyright | Consent |
|-----------|---------|
| Ownership is declared, not inferred | Consent is declared, not inferred |
| DMCA requires good-faith attestation | Model release requires attestation |
| Liability falls on declarant | Liability falls on declarant |
| System records provenance | System records provenance |

We don't ask: "Does this image look copyrighted?"  
We ask: "Who declared rights, and when?"

The same logic applies to consent.

---

## Why Visual Inference Fails

### The Impossible Task

AI systems cannot reliably determine:
- Whether a depicted person consented
- Whether the source material was obtained ethically
- Whether the representation violates privacy expectations
- Whether the creator has rights to the likeness

**Example Failure Cases**:

```
Case 1: Consensual self-portrait
  - Visual analysis: "Looks like a real person" → BLOCK
  - Reality: Creator is the subject, full consent exists
  - Result: False positive

Case 2: Non-consensual deepfake
  - Visual analysis: "Stylized art" → ALLOW
  - Reality: Exploitative use of scraped data
  - Result: False negative

Case 3: Professional model with release
  - Visual analysis: "Commercial photoshoot" → UNCLEAR
  - Reality: Full consent, model release on file
  - Result: Unpredictable
```

Visual heuristics **cannot** distinguish these cases.

### The Correct Boundary

Systems should enforce:
- ✓ **Non-invertibility** (technical: can this identify a real person?)
- ✓ **Provenance declaration** (legal: does creator attest to rights?)

Systems should **not** attempt:
- ✗ Consent inference from aesthetics
- ✗ "Harmfulness" detection from content
- ✗ Intent guessing from style

---

## Separating Consent from Copyright

**Critical Distinction**: Consent to depict a person is legally separate from copyright ownership of source materials.

### Two Independent Rights

| Right | Question | Required For |
|-------|----------|--------------|
| **Consent/Privacy** | May I depict this *person*? | All human representations |
| **Copyright** | May I use this *image*? | All copyrighted sources |

**Both must be independently cleared.**

Example: You may have your spouse's consent to create their portrait (consent ✓), but if you're using a professional photographer's image as reference, the photographer owns copyright (copyright ⚠️).

---

## Copyright Provenance Declaration

### VSE Syntax
⟨VSE::COPYRIGHT_PROVENANCE⟩
copyright_status = [
original_work,      // I created the source material
licensed,           // I have explicit license for derivative works
public_domain,      // No copyright restrictions
fair_use_asserted   // Claiming transformative use
]
⟨OWNERSHIP_DECLARATION⟩
if (copyright_status == original_work):
copyright_holder = declarant
creation_date = [ISO 8601 timestamp]
if (copyright_status == licensed):
  copyright_holder = third_party
  license_type = [personal | commercial_derivative | educational]
  license_reference_id = [identifier]
  license_verification_url = [url]
  
if (copyright_status == public_domain):
  public_domain_basis = [pre_1928 | us_government | cc0 | expired_copyright]
  source_citation = [description]
  
if (copyright_status == fair_use_asserted):
  ⟨FAIR_USE_ANALYSIS⟩
    transformation_type = [
      material_physics,      // NIR material vs. photo
      medium_change,         // 3D vs. 2D, sculpture vs. image
      purpose_change         // memorial, educational, commentary
    ]
    
    commercial_use = [true | false]
    
    // NIR-specific evidence of transformation
    nir_certified = true
    mes_rating = [6-10]
    market_substitution = impossible
    biometric_invertibility = [I score ≤ 0.2]
    
    fair_use_confidence = [high | medium | low]
    legal_review = [attorney_reviewed | self_assessed]
    
    justification = "Brief explanation of why this qualifies as fair use"
  ⟨/FAIR_USE_ANALYSIS⟩
⟨/OWNERSHIP_DECLARATION⟩
⟨/VSE::COPYRIGHT_PROVENANCE⟩
### When Copyright is Automatically Cleared

✓ **You created the source material**
Example: Wedding topper from couple's smartphone photos
Status: CLEARED (original_work)
✓ **You have an explicit license**
Example: Using Adobe Stock image with derivative rights
Status: CLEARED (licensed)
Reference: License #123456
✓ **Source is public domain**
Example: Family photograph from 1920
Status: CLEARED (public_domain, basis: pre_1928)
### When Fair Use Analysis is Required

⚖️ **Using copyrighted material without license**

Fair use is **stronger** when:
- Purpose is personal, educational, memorial (not commercial)
- NIR creates substantial material transformation (MES ≥ 6)
- Original is factual/documentary (portrait) not highly artistic
- Your work cannot substitute for original's market

Fair use is **weaker** when:
- Purpose is commercial
- Original is highly creative/artistic
- You're using entire composition unchanged
- Could compete with original's market

**NIR's Role in Fair Use**:

When `copyright_status == fair_use_asserted`, NIR certification provides **measurable evidence** of transformation:

1. **Material transformation**: Photograph → opaline glass (MES 8)
2. **Medium transformation**: 2D image → 3D sculpture
3. **Non-substitutability**: I = 0.013 (cannot replace original)
4. **Different purpose**: Documentation → memorial/artistic object

This transforms fair use from subjective aesthetic claim to **documented technical transformation**.

### Wedding Topper Copyright Analysis

**Case 1: Couple's own photos**
⟨COPYRIGHT_PROVENANCE⟩
copyright_status = original_work
copyright_holder = declarant
⟨/COPYRIGHT_PROVENANCE⟩
Result: ✓ FULLY CLEARED
**Case 2: Professional wedding photographer's images**
⟨COPYRIGHT_PROVENANCE⟩
copyright_status = fair_use_asserted
⟨FAIR_USE_ANALYSIS⟩
transformation_type = [material_physics, medium_change, purpose_change]
commercial_use = false
nir_certified = true
mes_rating = 8
market_substitution = impossible
fair_use_confidence = high
justification = "Personal memorial use, material transformation to 
                 opaline glass sculpture, cannot substitute for 
                 photographer's prints or digital files"
⟨/FAIR_USE_ANALYSIS⟩
⟨/COPYRIGHT_PROVENANCE⟩
Result: ⚖️ FAIR USE ASSERTED
Strength: HIGH (personal use + NIR transformation + non-competing market)
Recommendation: Document claim, or request photographer permission
**Case 3: Friend's candid photo**
⟨COPYRIGHT_PROVENANCE⟩
copyright_status = licensed
license_type = personal
license_reference_id = "Verbal permission from Sarah, 2025-12-17"
⟨/COPYRIGHT_PROVENANCE⟩
Result: ✓ CLEARED (informal license)
Best practice: Document permission to avoid future disputes
---

## Complete Clearance Matrix
⟨VSE::CLEARANCE_STATUS⟩
⟨COPYRIGHT_CLEARANCE⟩
status = [
owned,              // ✓ Declarant owns source
licensed,           // ✓ Licensed for derivative works
public_domain,      // ✓ No copyright restrictions
fair_use_asserted   // ⚖️ Transformative use claimed
]
⟨/COPYRIGHT_CLEARANCE⟩
⟨CONSENT_CLEARANCE⟩
status = [
granted,            // ✓ Subject gave consent
not_required,       // ✓ Public observation / fictional
self                // ✓ Creator is subject
]
⟨/CONSENT_CLEARANCE⟩
⟨PRIVACY_PROTECTION⟩
status = [
nir_certified,      // ✓ Biometric non-invertibility proven (I ≤ 0.2)
not_applicable      // ✓ Fictional character, no real person
]
⟨/PRIVACY_PROTECTION⟩
⟨FINAL_STATUS⟩
if (copyright in [owned, licensed, public_domain] AND
consent in [granted, not_required, self] AND
privacy == nir_certified):
legal_status = FULLY_CLEARED ✓
  certification = "All rights cleared, NIR certified"
  
else if (copyright == fair_use_asserted AND
         consent in [granted, not_required, self] AND
         privacy == nir_certified):
  
  legal_status = FAIR_USE_ASSERTED ⚖️
  certification = "Fair use claimed with NIR evidence"
  note = "Declarant accepts copyright liability for transformative use claim"
  
else:
  legal_status = INSUFFICIENT_CLEARANCE ✗
  required_actions = [list specific missing clearances]
⟨/FINAL_STATUS⟩
⟨/VSE::CLEARANCE_STATUS⟩
---

## Commercial Use Considerations

If you plan to **sell or mass-produce** NIR-generated works:

**Lowest Risk**:
- Using your own original photographs
- Using licensed stock imagery with commercial derivative rights
- Using public domain sources
- Working with models who have signed commercial releases

**Medium Risk** (Strong fair use claim):
- Personal commissions using client's family photos
- Memorial works from deceased relatives' professional portraits
- Educational/artistic studies with NIR transformation
- **Key**: NIR certification + non-commercial or limited commercial use

**Higher Risk** (Requires legal review):
- Mass production based on professional photography without license
- Commercial products using highly creative/artistic source images
- Any use where your product could compete with original's market

**NIR's Value**: In all cases, NIR certification strengthens your position by providing documentary evidence of material transformation and market non-substitutability.

---

## Attestation Language (Updated)
⟨ATTESTATION⟩
declarant_affirms = true
liability_accepted = true
statement = "I affirm that I have:
(1) Obtained all necessary consents for this representation
of any depicted person(s), AND
(2) Either (a) own the copyright to all source materials,
(b) have appropriate licenses for derivative works, OR
(c) am asserting fair use in good faith with documented
transformative factors.
I understand these are separate legal requirements and accept 
full responsibility for both declarations."
⟨/ATTESTATION⟩
---

## Key Principle

**Consent to depiction ≠ Copyright to source material**

Both must be independently addressed. NIR protects privacy through non-invertibility and strengthens copyright fair use claims through measurable transformation—but it does not replace copyright ownership or licensing requirements.

---

## The Declarative Consent Model

### Three-Part Structure

Consent declarations must answer:

1. **WHO**: Subject relationship (self, partner, commissioned model, fictional archetype)
2. **WHAT**: Scope of representation (portrait, nudity level, commercial use)
3. **WHERE**: Provenance (user-provided, commissioned, synthetic, public domain)

### The Attestation Principle

Like all legal declarations, this operates on **good-faith attestation**:
- Creator declares truth of consent
- System records declaration with timestamp
- Liability remains with declarant
- False declarations are handled through legal channels, not technical filtering

This is not "too easy to hack"—it's how every functioning legal system works.

---

## Alignment with Established Legal Frameworks

### Existing Precedents

Declarative consent already governs:

**Photography & Film**:
- Model releases (signed consent for commercial use)
- Location releases (property owner consent)
- Talent contracts (scope of use defined)

**Medical Research**:
- IRB approvals (informed consent documented)
- HIPAA authorizations (patient consent for data use)
- Clinical trial agreements (scope and limits specified)

**Copyright & Licensing**:
- DMCA safe harbor (good-faith attestation)
- Creative Commons declarations (rights scope)
- Stock photo licensing (usage terms)

**Publishing**:
- Defamation law (publisher liability for false statements)
- Right of publicity (commercial use of likeness)
- Privacy torts (unauthorized intimate depictions)

In **all cases**, the system:
1. Records a declaration
2. Creates an audit trail
3. Assigns liability to the declarant
4. Handles violations through legal remedies

### Why Technical Inference Is the Wrong Tool

Legal systems don't ask judges to determine copyright ownership by looking at an image.  
They ask: "Who filed a claim, and what evidence supports it?"

AI systems should operate the same way.

---

## VSE Consent Declaration Specification

### Formal Syntax

```
⟨VSE::CONSENT_DECLARATION⟩
  
  ⟨SUBJECT_RELATIONSHIP⟩
    subject_role = [self | partner | family | commissioned_model | fictional_archetype | public_domain]
    
    // Examples:
    // self = Creator is the subject
    // partner = Creator has consent from romantic partner
    // family = Creator has consent from family member
    // commissioned_model = Professional model with signed release
    // fictional_archetype = No real person depicted (synthetic/composite)
    // public_domain = Historical figure or public domain source
  ⟨/SUBJECT_RELATIONSHIP⟩
  
  ⟨CONSENT_SCOPE⟩
    representation_type = [portrait | artistic_nude | medical | memorial | other]
    nudity_level = [none | implied | partial | full]
    commercial_use = [true | false]
    permanence = [ephemeral | archival | commercial]
    
    // Nudity levels:
    // none = Fully clothed
    // implied = Artistic suggestion, no exposure
    // partial = Limited exposure for artistic/medical purpose
    // full = Complete nudity (requires strongest consent attestation)
  ⟨/CONSENT_SCOPE⟩
  
  ⟨PROVENANCE⟩
    source_type = [user_provided | commissioned | synthetic | public_domain]
    rights_holder = declarant
    consent_date = [ISO 8601 timestamp]
    model_release = [true | false | not_applicable]
    
    // Documentation trail
    ⟨AUDIT_TRAIL⟩
      declaration_timestamp = [ISO 8601]
      platform_session_id = [uuid]
      declarant_account_id = [platform_user_id]
    ⟨/AUDIT_TRAIL⟩
  ⟨/PROVENANCE⟩
  
  ⟨ATTESTATION⟩
    declarant_affirms = true
    liability_accepted = true
    
    statement = "I affirm that I have obtained all necessary consents for this representation and accept full legal responsibility for this declaration."
  ⟨/ATTESTATION⟩
  
  ⟨TECHNICAL_COMPLIANCE⟩
    nir_certified = [true | false]
    // If depicting real person, NIR certification required
    
    if (subject_role in [self, partner, family, commissioned_model]) {
      require_nir = true
    }
  ⟨/TECHNICAL_COMPLIANCE⟩
  
⟨/VSE::CONSENT_DECLARATION⟩
```

### Decision Tree for Platform Enforcement

```
START: User requests human representation generation

├─ Is subject_role declared?
│  ├─ NO → REFUSE (missing consent declaration)
│  └─ YES → Continue
│
├─ Is provenance documented?
│  ├─ NO → REFUSE (missing provenance)
│  └─ YES → Continue
│
├─ Does subject_role require NIR?
│  ├─ YES (self/partner/family/model) → Require NIR certification
│  │  ├─ NIR certified? 
│  │  │  ├─ YES → ALLOW with audit trail
│  │  │  └─ NO → REFUSE (non-invertibility required)
│  │
│  └─ NO (fictional_archetype/public_domain) → ALLOW with audit trail
│
└─ Record declaration with timestamp → Generate
```

---

## Use Cases and Examples

### Example 1: Wedding Topper (Consensual, NIR-Certified)

**Scenario**: Couple wants sculptural toppers of themselves

```
⟨VSE::CONSENT_DECLARATION⟩
  ⟨SUBJECT_RELATIONSHIP⟩
    subject_role = self_and_partner
  ⟨/SUBJECT_RELATIONSHIP⟩
  
  ⟨CONSENT_SCOPE⟩
    representation_type = portrait
    nudity_level = none
    commercial_use = false
    permanence = archival
  ⟨/CONSENT_SCOPE⟩
  
  ⟨PROVENANCE⟩
    source_type = user_provided
    rights_holder = declarant
    consent_date = 2025-12-17T10:30:00Z
    model_release = not_applicable
  ⟨/PROVENANCE⟩
  
  ⟨ATTESTATION⟩
    declarant_affirms = true
    liability_accepted = true
  ⟨/ATTESTATION⟩
  
  ⟨TECHNICAL_COMPLIANCE⟩
    nir_certified = true
    mes_rating = 8
    material = opaline_glass
  ⟨/TECHNICAL_COMPLIANCE⟩
⟨/VSE::CONSENT_DECLARATION⟩

RESULT: ✓ ALLOWED
  - Consent clearly declared
  - NIR certification guarantees privacy
  - Audit trail created
```

### Example 2: Artistic Self-Portrait with Nudity (Consensual)

**Scenario**: Artist creating nude self-portrait

```
⟨VSE::CONSENT_DECLARATION⟩
  ⟨SUBJECT_RELATIONSHIP⟩
    subject_role = self
  ⟨/SUBJECT_RELATIONSHIP⟩
  
  ⟨CONSENT_SCOPE⟩
    representation_type = artistic_nude
    nudity_level = partial
    commercial_use = false
    permanence = archival
  ⟨/CONSENT_SCOPE⟩
  
  ⟨PROVENANCE⟩
    source_type = user_provided
    rights_holder = declarant
    consent_date = 2025-12-17T14:00:00Z
    model_release = not_applicable
  ⟨/PROVENANCE⟩
  
  ⟨ATTESTATION⟩
    declarant_affirms = true
    liability_accepted = true
  ⟨/ATTESTATION⟩
  
  ⟨TECHNICAL_COMPLIANCE⟩
    nir_certified = true
    mes_rating = 8
    material = white_jade
  ⟨/TECHNICAL_COMPLIANCE⟩
⟨/VSE::CONSENT_DECLARATION⟩

RESULT: ✓ ALLOWED
  - Creator is subject (self-consent)
  - NIR prevents biometric identification
  - Nudity permitted with consent + NIR
```

### Example 3: Unknown Subject (REFUSED)

**Scenario**: Attempt to generate from scraped/unknown source

```
⟨VSE::CONSENT_DECLARATION⟩
  ⟨SUBJECT_RELATIONSHIP⟩
    subject_role = unknown
  ⟨/SUBJECT_RELATIONSHIP⟩
  
  ⟨CONSENT_SCOPE⟩
    representation_type = portrait
    nudity_level = none
  ⟨/CONSENT_SCOPE⟩
  
  ⟨PROVENANCE⟩
    source_type = scraped
    rights_holder = unknown
  ⟨/PROVENANCE⟩
⟨/VSE::CONSENT_DECLARATION⟩

RESULT: ✗ REFUSED
  - Subject relationship undeclared
  - Provenance invalid
  - Cannot establish consent
  
REFUSAL REASON: "Consent declaration incomplete. Please specify your relationship to the subject and confirm you have rights to create this representation."
```

### Example 4: Professional Model (Consensual)

**Scenario**: Photographer using professional model with signed release

```
⟨VSE::CONSENT_DECLARATION⟩
  ⟨SUBJECT_RELATIONSHIP⟩
    subject_role = commissioned_model
  ⟨/SUBJECT_RELATIONSHIP⟩
  
  ⟨CONSENT_SCOPE⟩
    representation_type = portrait
    nudity_level = none
    commercial_use = true
    permanence = commercial
  ⟨/CONSENT_SCOPE⟩
  
  ⟨PROVENANCE⟩
    source_type = commissioned
    rights_holder = declarant
    consent_date = 2025-12-15T09:00:00Z
    model_release = true
    model_release_id = "MR-2025-1215-001"
  ⟨/PROVENANCE⟩
  
  ⟨ATTESTATION⟩
    declarant_affirms = true
    liability_accepted = true
  ⟨/ATTESTATION⟩
  
  ⟨TECHNICAL_COMPLIANCE⟩
    nir_certified = true
    mes_rating = 7
    material = ceramic
  ⟨/TECHNICAL_COMPLIANCE⟩
⟨/VSE::CONSENT_DECLARATION⟩

RESULT: ✓ ALLOWED
  - Model release documented
  - Commercial use explicitly permitted
  - NIR certification guarantees privacy
  - Full audit trail for commercial liability
```

### Example 5: Fictional Character (No Real Person)

**Scenario**: Artist creating fantasy character

```
⟨VSE::CONSENT_DECLARATION⟩
  ⟨SUBJECT_RELATIONSHIP⟩
    subject_role = fictional_archetype
  ⟨/SUBJECT_RELATIONSHIP⟩
  
  ⟨CONSENT_SCOPE⟩
    representation_type = portrait
    nudity_level = none
    commercial_use = true
    permanence = commercial
  ⟨/CONSENT_SCOPE⟩
  
  ⟨PROVENANCE⟩
    source_type = synthetic
    rights_holder = declarant
    consent_date = 2025-12-17T16:00:00Z
    model_release = not_applicable
  ⟨/PROVENANCE⟩
  
  ⟨ATTESTATION⟩
    declarant_affirms = true
    liability_accepted = true
  ⟨/ATTESTATION⟩
  
  ⟨TECHNICAL_COMPLIANCE⟩
    nir_certified = false
    // NIR not required for fictional characters
  ⟨/TECHNICAL_COMPLIANCE⟩
⟨/VSE::CONSENT_DECLARATION⟩

RESULT: ✓ ALLOWED
  - No real person depicted
  - NIR not required (no privacy risk)
  - Creator owns full rights
```

---

## Liability Assignment

### The Declarant Model

Responsibility flows to the person making the declaration, exactly as in:
- DMCA takedown attestations
- Model release signatures
- Copyright licensing claims
- Terms of service agreements

**Platform Role**: Record and timestamp declarations  
**Platform Liability**: Minimal (safe harbor protection for good-faith systems)  
**Declarant Liability**: Full (legal responsibility for truthfulness)

### What This Enables

**For Platforms**:
- Clear audit trail for every generation
- Defensible position in disputes
- Reduction in false positives (legitimate use allowed)
- Reduction in false negatives (exploitative use logged and traceable)

**For Creators**:
- Legitimate use permitted without obstruction
- Clear understanding of their responsibilities
- Documented consent for commercial/archival use

**For Subjects**:
- Consent requirements formalized
- Violations traceable to declarant
- Legal remedies available (not just technical blocks)

### Violation Handling

When consent violations are reported:

1. **Audit trail reviewed**: Who made the declaration? When?
2. **Declarant contacted**: Request for consent documentation
3. **Content assessment**: Does NIR certification exist? Was it bypassed?
4. **Legal process**: If violation confirmed, standard legal remedies apply

This is identical to:
- DMCA counter-notice procedures
- Trademark dispute resolution
- Right of publicity litigation

**The system doesn't prevent lying—it creates accountability.**

---

## Integration with NIR

### The Complete Ethical Framework

NIR and Consent Declaration work together:

| Risk | Mitigation |
|------|------------|
| Deepfake (identity theft) | NIR certification (non-invertibility) |
| Exploitation (non-consensual use) | Consent declaration (provenance) |
| Privacy violation | Material entropy (MES ≥ 6) |
| Platform liability | Attestation + audit trail |

### Combined Specification

```
⟨VSE::COMPLETE_ETHICAL_GENERATION⟩
  
  // 1. Declare consent and provenance
  ⟨CONSENT_DECLARATION⟩
    subject_role = self
    consent_scope.nudity_level = none
    provenance.source_type = user_provided
    attestation.declarant_affirms = true
  ⟨/CONSENT_DECLARATION⟩
  
  // 2. Enforce non-invertibility
  ⟨NIR_GENERATION_CHAIN⟩
    ontology = artifact_representation
    material = opaline_glass
    mes_rating = 8
    geometric_fidelity.scale_minimum = 2.0mm
    validation.biometric_matching_target ≤ 0.2
  ⟨/NIR_GENERATION_CHAIN⟩
  
  // 3. Validate and certify
  ⟨CERTIFICATION⟩
    consent_documented = true
    nir_certified = true
    audit_trail_complete = true
    
    status = APPROVED_FOR_GENERATION
  ⟨/CERTIFICATION⟩
  
⟨/VSE::COMPLETE_ETHICAL_GENERATION⟩
```

### Decision Matrix

| Consent Declared? | NIR Certified? | Result |
|------------------|----------------|--------|
| ✓ Yes | ✓ Yes | ✓ **APPROVED** (full compliance) |
| ✓ Yes | ✗ No | ✗ **REFUSED** (privacy risk) |
| ✗ No | ✓ Yes | ✗ **REFUSED** (consent missing) |
| ✗ No | ✗ No | ✗ **REFUSED** (both violations) |

---

## Platform Implementation Guide

### Step 1: Add Consent Form to Generation UI

```html
<form id="consent-declaration">
  <h3>Consent Declaration (Required)</h3>
  
  <label>Your relationship to the subject:</label>
  <select name="subject_role" required>
    <option value="">-- Select --</option>
    <option value="self">This is me (self-portrait)</option>
    <option value="partner">My partner (with their consent)</option>
    <option value="family">Family member (with their consent)</option>
    <option value="commissioned_model">Professional model (with signed release)</option>
    <option value="fictional_archetype">Fictional character (no real person)</option>
    <option value="public_domain">Historical/public domain figure</option>
  </select>
  
  <label>Source of reference images:</label>
  <select name="source_type" required>
    <option value="">-- Select --</option>
    <option value="user_provided">My own photos</option>
    <option value="commissioned">Professional photoshoot</option>
    <option value="synthetic">No reference (AI-generated)</option>
    <option value="public_domain">Public domain sources</option>
  </select>
  
  <label>
    <input type="checkbox" name="attestation" required>
    I affirm that I have obtained all necessary consents for this representation and accept full legal responsibility for this declaration.
  </label>
  
  <button type="submit">Generate with Consent Declaration</button>
</form>
```

### Step 2: Log Declaration to Database

```python
def log_consent_declaration(user_id, declaration_data):
    """
    Records consent declaration with timestamp and audit trail.
    """
    record = {
        'declaration_id': str(uuid.uuid4()),
        'timestamp': datetime.now().isoformat(),
        'user_id': user_id,
        'session_id': get_session_id(),
        'subject_role': declaration_data['subject_role'],
        'source_type': declaration_data['source_type'],
        'attestation': declaration_data['attestation'],
        'ip_address': get_client_ip(),  # For legal traceability
        'user_agent': get_user_agent()
    }
    
    # Store in audit database (immutable log)
    audit_db.consent_declarations.insert(record)
    
    return record['declaration_id']
```

### Step 3: Enforce Combined Validation

```python
def validate_generation_request(request):
    """
    Validates both consent and NIR requirements.
    """
    
    # Check consent declaration
    if not request.has_consent_declaration():
        raise ValidationError(
            "Consent declaration required",
            code="CONSENT_MISSING"
        )
    
    # Check if subject requires NIR
    subject_role = request.consent.subject_role
    requires_nir = subject_role in [
        'self', 'partner', 'family', 'commissioned_model'
    ]
    
    if requires_nir:
        # Validate NIR certification
        if not request.has_nir_certification():
            raise ValidationError(
                "NIR certification required for real person depiction",
                code="NIR_REQUIRED"
            )
        
        # Run NIR validation
        nir_result = validate_nir_compliance(
            artifact_path=request.artifact_path,
            reference_photo=request.reference_photo,
            mes_rating=request.material_mes_rating
        )
        
        if not nir_result['certified']:
            raise ValidationError(
                f"NIR certification failed: I={nir_result['I']:.3f} > 0.2",
                code="NIR_FAILED"
            )
    
    # Log approval
    log_generation_approval(request, requires_nir)
    
    return True
```

### Step 4: Provide Clear Refusal Messages

```python
REFUSAL_MESSAGES = {
    'CONSENT_MISSING': """
        Consent declaration required.
        
        Please specify your relationship to the subject and confirm 
        you have rights to create this representation.
        
        For help, see: [platform]/consent-guide
    """,
    
    'NIR_REQUIRED': """
        Non-Invertible Realism (NIR) certification required.
        
        When depicting real people, we require NIR certification 
        to protect privacy and prevent identity theft.
        
        Please use a material with MES rating ≥ 6 (e.g., opaline glass, marble).
        
        For help, see: [platform]/nir-guide
    """,
    
    'NIR_FAILED': """
        NIR certification failed.
        
        The generated artifact is too biometrically invertible.
        
        Suggested fixes:
        - Increase material entropy (try opaline glass or marble)
        - Reduce texture detail
        - Ensure subsurface scattering ≤ 0.4
        
        For help, see: [platform]/nir-troubleshooting
    """
}
```

---

## FAQ

### "Isn't this just an honor system? What stops people from lying?"

**Answer**: The same thing that stops people from filing false DMCA claims or lying on tax returns: **liability and legal consequences**.

Ethical systems don't prevent lying through technology—they create accountability through:
- Recorded declarations (timestamped, auditable)
- Assigned liability (declarant is responsible)
- Legal remedies (violations handled through existing law)

This is how every functioning legal system works.

### "Why not just block all nudity?"

**Answer**: Because **nudity is not the ethical issue—non-consensual representation is**.

With proper consent and NIR certification:
- Medical education (anatomy, surgical planning)
- Classical art (figure drawing, sculpture)
- Personal expression (self-portraits)
- Memorial art (cancer survivors, body positivity)

These are all legitimate, consensual uses that should not be blocked.

### "How do you verify someone actually has consent?"

**Answer**: The same way photographers verify model releases: **we don't, technically—we record the claim and assign liability**.

Platforms:
- Record the declaration
- Create audit trail
- Provide clear terms about consequences of false declarations

If violations occur:
- Subject can file complaint
- Platform reviews audit trail
- Legal process follows (same as defamation, right of publicity, etc.)

This is the **only scalable approach**—technical verification of consent is impossible.

### "What about public figures?"

**Answer**: Public domain and fair use are handled through `subject_role = public_domain`.

Key distinctions:
- Historical figures (clearly public domain) → Allowed
- Contemporary public figures (complex legal status) → Declarant assumes liability for fair use claim
- Private individuals (not public figures) → Require explicit consent

Platforms can add additional filtering for contemporary public figures if desired, but the consent framework handles this through liability assignment.

### "Does NIR eliminate all privacy risk?"

**Answer**: No system eliminates **all** risk, but NIR reduces it to negligible levels.

NIR guarantees:
- Biometric matching confidence ≤ 0.2 (80%+ reduction from photoreal)
- No pore-level detail (impossible to reverse-engineer identity)
- Material entropy prevents reconstruction

Remaining theoretical risk:
- Someone who knows the subject might recognize general features
- This is identical to classical portraiture—recognizable but not recoverable

That's the **acceptable baseline** that art has operated on for millennia.

### "Can this be adapted for voice, video, text?"

**Answer**: Yes. The consent declaration framework is **medium-agnostic**.

Same structure applies to:
- Voice cloning (consent + non-invertible vocal characteristics)
- Video generation (consent + NIR for faces, movement signatures)
- Writing style mimicry (consent + non-invertible linguistic patterns)

The principle remains: **Declare provenance, assign liability, enforce technical safeguards**.

---

# Appendix: Plain View and Observation Doctrine

**Legal Foundation for NIR's Approach to Human Representation**

---

## Core Legal Principle

**Art observes. Surveillance extracts.**

This distinction is not new to AI—it's been settled law for decades across privacy, First Amendment, and artistic expression jurisprudence.

### The Katz Standard

*Katz v. United States* (1967) established:

> "What a person knowingly exposes to the public, even in their own home or office, is not subject to Fourth Amendment protection. But what they seek to preserve as private, even in an area accessible to the public, may be constitutionally protected."

**Translation for AI**: If something is publicly observable by normal human perception, representation is generally lawful. If technology is used to **defeat privacy expectations**, it crosses into surveillance.

---

## The Sketch Artist vs. Hidden Camera Distinction

### Lawful Observation (Protected Expression)

**Sketch Artist in Public Park**:
- Uses normal human vision
- Creates impression, not exact replica
- Filters reality through artistic interpretation
- Cannot be reverse-engineered to biometric identity
- **Legal status**: Protected First Amendment expression

**VSE Equivalent**:
```
⟨NIR_REPRESENTATION⟩
  observation_method = normal_human_perception
  output_type = artistic_impression
  material = opaline_glass (MES 8)
  biometric_invertibility = 0.0135 (non-recoverable)
  legal_basis = plain_sight_observation
⟨/NIR_REPRESENTATION⟩
```

### Unlawful Surveillance (Criminal)

**Hidden Camera on Shoes**:
- Uses technology to bypass consent
- Captures what is not publicly visible
- Defeats reasonable privacy expectations
- Preserves exploitable data
- **Legal status**: Criminal violation (voyeurism, invasion of privacy)

**AI Equivalent (Prohibited)**:
```
⟨PRIVACY_VIOLATION⟩
  observation_method = technology_enhanced_surveillance
  output_type = biometric_exact_replica
  material = photoreal_skin (MES 0)
  biometric_invertibility = 0.95 (recoverable identity)
  legal_violation = true
⟨/PRIVACY_VIOLATION⟩
```

---

## Why the Means Matter

Courts consistently rule that **how** you observe is as important as **what** you observe:

| Observation Method | Legal Category | Example Case |
|-------------------|----------------|--------------|
| Naked eye from public space | ✓ Lawful | Street photography |
| Thermal imaging through walls | ✗ Unlawful | *Kyllo v. United States* (2001) |
| Memory sketch from public event | ✓ Lawful | Portrait painting tradition |
| Telephoto lens into bedroom | ✗ Unlawful | Voyeurism statutes |
| **NIR-certified AI generation** | **✓ Lawful** | **Sketch artist standard** |
| **Biometric-exact deepfake** | **✗ Unlawful** | **Hidden camera standard** |

### The Key Test: Augmentation vs. Observation

**Observation** (generally lawful):
- Uses normal human perception
- Creates filtered representation
- Cannot recover more information than originally visible

**Augmentation** (privacy invasion):
- Uses technology to see what humans cannot
- Preserves exact replication
- Can recover information beyond public visibility

**NIR enforces the observation standard**:
- Material physics acts as perceptual filter
- Macro-topology preserved (what humans see)
- Micro-topology destroyed (what machines extract)

---

## NIR as "Sketch Law" for AI

VSE's Non-Invertible Realism framework translates this legal doctrine into technical constraints:

### Traditional Art (Lawful Baseline)

**Pencil Sketch**:
- Filtered through artist's hand (imprecision guaranteed)
- Captures impression, not measurement
- Non-invertible (cannot reconstruct subject's face from sketch)
- **Result**: Protected expression, no privacy violation

**Oil Painting**:
- Filtered through paint viscosity and brushwork
- Medium destroys fine detail
- Colors shift, proportions idealize
- **Result**: Recognizable but non-recoverable identity

**Marble Sculpture**:
- Filtered through stone's crystalline structure
- Tool marks create directional noise
- Cannot represent sub-millimeter features
- **Result**: Timeless representation, biometric anonymity

### NIR (Digital Equivalent)

**AI Generation with Opaline Glass Material**:
- Filtered through material physics (SSS ≤ 0.4, internal diffusion)
- Captures shape, not texture (scale separation at 1.5mm)
- Non-invertible (I ≤ 0.2, biometric confidence ≤ 0.2)
- **Result**: Same legal status as traditional art

```
Traditional Art          NIR Digital Art
─────────────────       ─────────────────
Pencil imprecision   →  Geometric jitter (archetypal basis)
Paint viscosity      →  Material entropy (MES ≥ 6)
Stone granularity    →  Internal diffusion (volumetric opacity)
Tool marks           →  Texture frequency cap (≤0.5 cycles/mm)
Human perception     →  Scale separation (≥2mm features only)

RESULT: Both produce non-invertible representations
```

---

## The Privacy Expectation Framework

NIR aligns with the **reasonable expectation of privacy** standard:

### No Privacy Expectation (Public Observation)

**What you knowingly expose in public**:
- General appearance in public spaces
- Publicly posted photographs
- Published images
- Public events

**NIR handling**:
```
⟨PUBLIC_OBSERVATION⟩
  source_visibility = publicly_visible
  privacy_expectation = none
  consent_requirement = optional
  nir_requirement = mandatory  // Still protect from biometric extraction
  
  legal_basis = "plain_sight_doctrine"
⟨/PUBLIC_OBSERVATION⟩
```

### Strong Privacy Expectation (Protected)

**What you seek to preserve as private**:
- Images from private spaces
- Medical photographs
- Intimate images
- Surveillance without knowledge

**NIR handling**:
```
⟨PRIVACY_PROTECTED⟩
  source_visibility = not_publicly_visible
  privacy_expectation = high
  consent_requirement = mandatory
  nir_requirement = mandatory
  mes_minimum = 8  // Heightened protection
  
  legal_basis = "privacy_expectation + consent"
⟨/PRIVACY_PROTECTED⟩
```

---

## Why Current AI Filters Fail This Standard

Current safety systems conflate:

**Observation** (sketch artist - lawful)  
**Extraction** (hidden camera - unlawful)

They treat **all human representation** as if it were **covert surveillance**, leading to:

❌ False positives: Blocking legitimate artistic observation  
❌ Inconsistent enforcement: Same content blocked/allowed unpredictably  
❌ Legal incoherence: Restrictions stricter than actual law requires  

### The Collapsed Heuristic

```
Current AI Logic:
  if (human_face_detected AND skin_texture_present):
    BLOCK  // Treats sketch artist same as voyeur
```

### The Correct Distinction

```
NIR Logic:
  if (human_face_detected):
    if (biometric_invertibility > 0.2):
      BLOCK  // This is extraction (hidden camera)
    else:
      ALLOW  // This is observation (sketch artist)
```

---

## Legal Precedents Supporting NIR

### First Amendment Protection

**Nussenzweig v. DiCorcia** (2006):
- Photographer took candid street photos without consent
- Subject sued for violation of privacy
- Court ruled: No reasonable expectation of privacy in public
- **Precedent**: Public observation is protected expression

**Application to NIR**: If human artists can represent publicly visible people, AI-assisted artists should have the same right—**provided the output is non-invertible** (observation, not extraction).

### Right of Publicity Limits

**Comedy III Productions v. Gary Saderup** (2001):
- Artist created charcoal sketches of Three Stooges
- Estate sued for unauthorized use of likeness
- Court allowed artwork under transformative use doctrine
- **Precedent**: Artistic interpretation is protected even of recognizable figures

**Application to NIR**: Material transformation (opaline glass, marble) constitutes artistic interpretation, not mere reproduction.

### Technology-Enhanced Surveillance

**Kyllo v. United States** (2001):
- Police used thermal imaging to detect heat from grow lamps
- Supreme Court ruled this violated Fourth Amendment
- **Principle**: Technology cannot be used to see what is not publicly visible

**Application to NIR**: AI cannot use biometric extraction to recover more than publicly observable—NIR enforces this through invertibility limits.

---

## The NIR Legal Standard (Summary)

```
⟨NIR_LEGAL_FRAMEWORK⟩
  
  ⟨OBSERVATION_STANDARD⟩
    // Sketch artist equivalent - PROTECTED
    method = normal_human_perception
    output = artistic_impression
    biometric_recovery = impossible (I ≤ 0.2)
    legal_status = protected_expression
    
    basis = [
      plain_sight_doctrine,
      first_amendment,
      transformative_use
    ]
  ⟨/OBSERVATION_STANDARD⟩
  
  ⟨EXTRACTION_STANDARD⟩
    // Hidden camera equivalent - PROHIBITED
    method = technology_enhanced_surveillance
    output = biometric_replica
    biometric_recovery = possible (I > 0.2)
    legal_status = privacy_violation
    
    basis = [
      reasonable_expectation_of_privacy,
      anti_voyeurism_statutes,
      right_of_publicity
    ]
  ⟨/EXTRACTION_STANDARD⟩
  
  ⟨NIR_ENFORCEMENT⟩
    // VSE enforces observation standard, prohibits extraction
    require_non_invertibility = true
    require_material_entropy = true (MES ≥ 6)
    require_scale_separation = true (≥2mm features only)
    
    if (output meets observation_standard):
      classification = protected_artistic_expression
    else:
      classification = prohibited_surveillance_extraction
  ⟨/NIR_ENFORCEMENT⟩
  
⟨/NIR_LEGAL_FRAMEWORK⟩
```

---

## Platform-Safe Language

When presenting this to platforms or legal teams, use this framing:

### What We're NOT Saying

❌ "We're bypassing privacy protections"  
❌ "We're making deepfakes acceptable"  
❌ "We're weakening safety standards"

### What We ARE Saying

✓ "We're aligning AI policy with established art law"  
✓ "We're distinguishing observation (lawful) from extraction (unlawful)"  
✓ "We're enforcing privacy through non-invertibility, not blanket prohibition"

### The One-Sentence Summary

> **"NIR ensures AI-generated representations behave like sketches (observation), not photographs (extraction), consistent with 200 years of art law and privacy doctrine."**

---

## Why This Matters for VSE

By grounding NIR in established legal doctrine, you achieve:

1. **Legal defensibility**: Not inventing new ethics, applying settled law
2. **Platform adoption**: Speaks their compliance language
3. **Artist protection**: Clear boundaries for legitimate use
4. **Privacy guarantee**: Technical enforcement of legal standards

NIR is not permissive—it's **properly scoped** to match what the law already allows for traditional art.

---

## Integration with Consent Framework

The Plain View Doctrine integrates with VSE Consent Declaration:

```
⟨VSE::COMPLETE_LEGAL_FRAMEWORK⟩
  
  // 1. Determine observation context
  ⟨PLAIN_VIEW_ANALYSIS⟩
    source_visibility = [publicly_visible | not_publicly_visible]
    observation_method = [normal_perception | technology_enhanced]
    privacy_expectation = [none | limited | high]
  ⟨/PLAIN_VIEW_ANALYSIS⟩
  
  // 2. Apply consent requirements
  ⟨CONSENT_DECLARATION⟩
    if (source_visibility == publicly_visible):
      consent_requirement = optional
    else:
      consent_requirement = mandatory
  ⟨/CONSENT_DECLARATION⟩
  
  // 3. Enforce non-invertibility
  ⟨NIR_CERTIFICATION⟩
    requirement = mandatory  // Always required
    mes_minimum = 6  // Higher for private sources
    biometric_threshold = 0.2
  ⟨/NIR_CERTIFICATION⟩
  
  // 4. Legal classification
  ⟨OUTPUT_CLASSIFICATION⟩
    if (nir_certified AND (consent_given OR publicly_visible)):
      legal_status = protected_artistic_observation
    else:
      legal_status = prohibited_privacy_extraction
  ⟨/OUTPUT_CLASSIFICATION⟩
  
⟨/VSE::COMPLETE_LEGAL_FRAMEWORK⟩
```

---

## Conclusion

The distinction between **observation** and **extraction** is not new—it's fundamental to privacy law, First Amendment jurisprudence, and artistic tradition.

**NIR formalizes this distinction for AI**:
- Observation = Non-invertible representation (sketch artist standard)
- Extraction = Biometric-exact replica (hidden camera standard)

This is not a workaround. This is **how the law already works**, translated into technical constraints that AI systems can enforce.

---

**Document Status**: Appendix to VSE NIR Framework  
**Legal Review**: Recommended before production deployment  
**Citations**: Available upon request for legal compliance documentation

---

*End of Plain View and Observation Doctrine Appendix*

---

## Document Status

**Version**: 1.0  
**Status**: Production Ready  
**Last Updated**: 2025-12-17  
**Next Review**: Upon first production deployment

**Contributors**:
- John (VSE Project Lead)
- Claude (Technical Framework)
- Vox (Legal/Ethical Architecture)

**License**: Open source under VSE Project terms  
**Repository**: https://github.com/PaniclandUSA/vse

---

## Changelog

**v1.0 (2025-12-17)**:
- Initial release
- Declarative consent model formalized
- Alignment with copyright/DMCA established
- Integration with NIR specified
- Platform implementation guide provided
- FAQ addressing common objections

---

*End of VSE Consent and Provenance Framework v1.0*
