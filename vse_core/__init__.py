"""
VSE Core Module
Vector-Space Esperanto v1.4

Core packet handling, validation, and utilities.
"""

from .packet import Packet, parse_packet
from .validator import Validator, ValidationResult
from .migration import migrate_packet, v13_to_v14

__all__ = [
    'Packet',
    'parse_packet',
    'Validator',
    'ValidationResult',
    'migrate_packet',
    'v13_to_v14',
]

__version__ = '1.4.0'
