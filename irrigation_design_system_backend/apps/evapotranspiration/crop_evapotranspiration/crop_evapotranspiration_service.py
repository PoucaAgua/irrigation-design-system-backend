from _decimal import Decimal
from core.domain.entity.crop_evapotranspiration_input import ETcInput
from core.constants.evapotranspiration import CropEvapotranspirationConstants
import math


class CropEvapotranspirationService:
    @staticmethod
    def calculate_by_keller(etc_input: ETcInput) -> Decimal:
        P = etc_input.P
        a, b = CropEvapotranspirationConstants.parameters_keller
        return Decimal(P + a * (b - P))

    @staticmethod
    def calculate_by_bernardo(etc_input: ETcInput) -> Decimal:
        P = etc_input.P
        a = CropEvapotranspirationConstants.parameters_bernardo
        return Decimal(P / a)

    @staticmethod
    def calculate_by_fereres(etc_input: ETcInput) -> Decimal:
        P = etc_input.P
        a = CropEvapotranspirationConstants.parameters_bernardo
        return Decimal(P / a)

    @staticmethod
    def calculate_by_keller_and_bliesner(etc_input: ETcInput) -> Decimal:
        P = etc_input.P
        # a = CropEvapotranspirationConstants.parameters_keller_and_bliesner
        return Decimal(0.10 * math.sqrt(P))
