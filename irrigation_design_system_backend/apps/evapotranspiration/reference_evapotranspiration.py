from _decimal import Decimal

from core.constantes.evapotranspiration import ReferenceEvapotranspirationConstants
from core.domain.entity.evapotranspiration import EToData

parameters_hargraves_samani = ReferenceEvapotranspirationConstants.parameters_hargraves_samani


class ReferenceEvapotranspiration:

    @staticmethod
    def calculate_hargraves_samani(data: EToData) -> Decimal:
        a, b, c = parameters_hargraves_samani
        Ra = data.radiation
        Tmed = data.temperature_med
        Tmin = data.temperature_min
        Tmax = data.temperature_max
        return Decimal(Ra * a * (b * (Tmed + c) * (Tmax - Tmin)) ** Decimal(0.5))
