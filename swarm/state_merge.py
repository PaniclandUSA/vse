"""
Semantic State Merger
Merges partial results from agents.
"""

from typing import List, Dict
import numpy as np

def sigma_merge(vectors: List[np.ndarray]) -> np.ndarray:
    """Merge sigma vectors."""
    return np.mean(vectors, axis=0)

def lambda_merge(tensors: List[np.ndarray]) -> np.ndarray:
    """Merge lambda tensors."""
    return np.mean(tensors, axis=0)

def delta_merge(deltas: List[float]) -> float:
    """Merge deltas."""
    return min(deltas)

def phi_log_merge(ops: List[str]) -> List[str]:
    """Merge phi logs."""
    return list(set(ops))

# Unit Test
if __name__ == "__main__":
    import unittest
    
    class TestStateMerge(unittest.TestCase):
        def test_sigma_merge(self):
            v1 = np.array([1,2])
            v2 = np.array([3,4])
            np.testing.assert_array_equal(sigma_merge([v1, v2]), np.array([2,3]))
    
    unittest.main()