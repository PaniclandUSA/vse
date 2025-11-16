# vse_core/merkle_semantic.py

import hashlib
from typing import Iterable, List, Any


def _sha256(data: bytes) -> bytes:
    return hashlib.sha256(data).digest()


def _normalize_leaf(x: Any) -> bytes:
    """
    Normalize arbitrary semantic objects into a stable byte representation.
    This should be replaced with a canonical encoder if you have one.
    """
    if isinstance(x, bytes):
        return x
    if isinstance(x, str):
        return x.encode("utf-8")
    return repr(x).encode("utf-8")


def merkle_root(items: Iterable[Any]) -> str:
    """
    Compute the Merkle root over an iterable of semantic items.
    Returns a hex string.
    """
    leaves: List[bytes] = [_sha256(_normalize_leaf(x)) for x in items]

    if not leaves:
        # Convention: root of empty set is SHA256 of empty string
        return hashlib.sha256(b"").hexdigest()

    level = leaves
    while len(level) > 1:
        nxt: List[bytes] = []
        for i in range(0, len(level), 2):
            left = level[i]
            right = level[i + 1] if i + 1 < len(level) else left
            nxt.append(_sha256(left + right))
        level = nxt

    return level[0].hex()
