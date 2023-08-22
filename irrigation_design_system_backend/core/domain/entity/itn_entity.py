from _decimal import Decimal
from dataclasses import dataclass

@dataclass
class FlProjectionInputEntity:
    ce_i: Decimal
    ce_e: Decimal

@dataclass
class ITNProjectionInputEntity:
    irn: Decimal
    fl: Decimal
    ea: Decimal

@dataclass
class ITNProjectionInputEntity2:
    irn: Decimal
    ce_i: Decimal
    ce_e: Decimal
    ea: Decimal

