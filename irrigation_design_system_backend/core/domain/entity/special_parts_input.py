from decimal import Decimal
from dataclasses import dataclass
from typing import List

from core.domain.enum.special_parts_types import SpecialPartsTypes


@dataclass
class SpecialPartInput:
    quantity: int
    type: SpecialPartsTypes


@dataclass
class SpecialPartsInput:
    diameter: Decimal
    special_parts: List[SpecialPartInput]
