"""
Example 1: VSE v1.3 - Deterministic Semantic Control

This example demonstrates the core v1.3 functionality:
- Creating packets with intent and constraints
- Validating packet structure
- Using immune fields to protect content
"""

from vse_core import Packet, Validator

def main():
    print("=" * 60)
    print("VSE v1.3 Example: Deterministic Semantic Control")
    print("=" * 60)
    print()
    
    # Example 1: Academic summarization
    print("Example 1: Academic Paper Summary")
    print("-" * 60)
    
    packet1 = Packet(
        intent="summarize_paper",
        constraints=[
            "3_sentences",
            "formal_tone",
            "chronological",
            "highlight_methodology"
        ],
        divergence=0.2,
        immune=["Theorem 4.2", "Figure 3", "p < 0.05"],
        version="1.3"
    )
    
    print("Created packet:")
    print(packet1.to_vse())
    print()
    
    validator = Validator(packet1)
    result = validator.validate()
    print(result)
    print()
    
    # Example 2: Creative writing with bounds
    print("\nExample 2: Bounded Creative Writing")
    print("-" * 60)
    
    packet2 = Packet(
        intent="write_short_story",
        constraints=[
            "500_words",
            "first_person",
            "past_tense",
            "mystery_genre"
        ],
        divergence=0.6,  # Higher for creativity
        immune=["protagonist's name: Sarah"],
        version="1.3"
    )
    
    print("Created packet:")
    print(packet2.to_vse())
    print()
    
    validator = Validator(packet2)
    result = validator.validate()
    print(result)
    print()
    
    # Example 3: Technical documentation
    print("\nExample 3: Technical Documentation")
    print("-" * 60)
    
    packet3 = Packet(
        intent="explain_api_endpoint",
        constraints=[
            "include_code_examples",
            "professional_tone",
            "beginner_friendly",
            "include_error_handling"
        ],
        divergence=0.15,  # Very low for precision
        immune=[
            "endpoint: /api/v1/users",
            "HTTP method: POST",
            "Authentication: Bearer token"
        ],
        version="1.3"
    )
    
    print("Created packet:")
    print(packet3.to_vse())
    print()
    
    validator = Validator(packet3)
    result = validator.validate()
    print(result)
    print()
    
    # Example 4: Parsing VSE strings
    print("\nExample 4: Parsing VSE Syntax")
    print("-" * 60)
    
    vse_string = '<VSE v1.3 | intent: explain_quantum_computing | constraints: [eli5, use_analogies, 200_words] | divergence: 0.40>'
    
    print(f"Parsing: {vse_string}")
    print()
    
    packet4 = Packet.from_vse(vse_string)
    print(f"Parsed packet:")
    print(f"  Intent: {packet4.intent}")
    print(f"  Constraints: {packet4.constraints}")
    print(f"  Divergence: {packet4.divergence}")
    print()
    
    validator = Validator(packet4)
    result = validator.validate()
    print(result)
    print()
    
    # Example 5: JSON export/import
    print("\nExample 5: JSON Serialization")
    print("-" * 60)
    
    json_str = packet1.to_json()
    print("Packet as JSON:")
    print(json_str)
    print()
    
    packet5 = Packet.from_json(json_str)
    print("Reconstructed from JSON:")
    print(packet5.to_vse())
    print()
    
    print("=" * 60)
    print("v1.3 examples complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
