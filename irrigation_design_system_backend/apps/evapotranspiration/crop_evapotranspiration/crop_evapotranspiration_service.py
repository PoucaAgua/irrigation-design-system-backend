from _decimal import Decimal
from core.domain.entity.evapotranspiration.crop_evapotranspiration_input import (
    CropEvapotranspirationInput,
)
from apps.evapotranspiration.crop_evapotranspiration.location_coefficients_method import (
    calculate_by_keller,
    calculate_by_bernardo,
    calculate_by_fereres,
    calculate_by_keller_and_bliesner,
)


class CropEvapotranspirationService:
    @staticmethod
    def etc_by_keller(etc_input: CropEvapotranspirationInput) -> Decimal:
        Kl = calculate_by_keller(P=etc_input.P)
        ETo = etc_input.Eto
        Kc = etc_input.Kc
        return Decimal(Kl * ETo * Kc)

    @staticmethod
    def etc_by_bernardo(etc_input: CropEvapotranspirationInput) -> Decimal:
        Kl = calculate_by_bernardo(P=etc_input.P)
        ETo = etc_input.Eto
        Kc = etc_input.Kc
        return Decimal(Kl * ETo * Kc)

    @staticmethod
    def etc_by_fereres(etc_input: CropEvapotranspirationInput) -> Decimal:
        Kl = calculate_by_fereres(P=etc_input.P)
        ETo = etc_input.Eto
        Kc = etc_input.Kc
        return Decimal(Kl * ETo * Kc)

    @staticmethod
    def etc_by_keller_and_bliesner(etc_input: CropEvapotranspirationInput) -> Decimal:
        Kl = calculate_by_keller_and_bliesner(P=etc_input.P)
        ETo = etc_input.Eto
        Kc = etc_input.Kc
        return Decimal(Kl * ETo * Kc)
