from _decimal import Decimal

from core.constants.math import MathConstants
from core.domain.entity.PWAEntity import PWAEntity


class PercentWettedAreaService:

    @classmethod
    def calculate(cls, pwa_entity: PWAEntity) -> Decimal:
        Np = pwa_entity.drippers_number
        Dw = cls.dw_calculate()
        Sr = pwa_entity.space_between_lines
        Sp = pwa_entity.space_between_plants

        return Decimal(Np * MathConstants.PI * Dw * Dw * 100 / (4 * Sp * Sr))


    def dw_calculate(self):
        return