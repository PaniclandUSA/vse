# Hello World — VSE (Vector-Space Esperanto)

This guide introduces the minimal working example for **Vector-Space Esperanto**, the semantic algebra powering the first layer of the Esper-Stack.

VSE performs **semantic shaping**, organizing a message into an aligned, model-stable form.

---

# 1. Basic VSE Expression

A simple raw VSE expression:

```vse
<V p=calm d=decl s=one c=cert τ=0.8>
    <intent axis=hello>
</V>
```
This defines:

polarity: calm

deictic: declarative

scope: single subject

certainty: certain

τ: temporal weight

intent.axis: hello



---

2. Using the Crystallizer Stub

from vse import Crystallizer

expr = {
    "polarity": "calm",
    "deictic": "decl",
    "scope": "one",
    "certainty": "cert",
    "tau": 0.8,
    "intent": {"axis": "hello"},
}

output = Crystallizer().process(expr)
print(output)

Expected output:

{'stage': 'vse', 'payload': {...}}


---

3. What “Crystallization” Means

Even in stub form, the Crystallizer serves as the normalizing gateway for:

operator alignment

modifier validation

axiom enforcement

semantic vector compression


Later versions will include the complete Modifier Algebra and Axiom Engine.


---

4. Next Steps

Try modifying:

intent = {"axis": "warn"}
tau = 0.2
polarity = "hot"

Observe how it propagates through later layers when used in the full pipeline.

This is the foundation of semantic convergence across models.
