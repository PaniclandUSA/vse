"""
Semantic Consensus Engine
Chooses semantic winner from multiple responses.
"""

from typing import List, Dict

def compute_cost_fidelity_score(responses: List[Dict]) -> float:
    """Compute cost-fidelity score."""
    # Placeholder: Average SCM - delta
    scm = sum(r.get('scm', 0) for r in responses) / len(responses)
    delta = sum(r.get('delta', 0) for r in responses) / len(responses)
    return scm - delta

def minimize_delta(responses: List[Dict]) -> Dict:
    """Select response with min delta."""
    return min(responses, key=lambda r: r.get('delta', float('inf')))

def weighted_majority_vote(responses: List[Dict]) -> Dict:
    """Weighted vote by SCM."""
    # Placeholder: Highest SCM
    return max(responses, key=lambda r: r.get('scm', 0))

# Unit Test
if __name__ == "__main__":
    import unittest
    
    class TestConsensus(unittest.TestCase):
        def test_minimize_delta(self):
            responses = [{'delta': 0.1}, {'delta': 0.2}]
            self.assertEqual(minimize_delta(responses)['delta'], 0.1)
    
    unittest.main()