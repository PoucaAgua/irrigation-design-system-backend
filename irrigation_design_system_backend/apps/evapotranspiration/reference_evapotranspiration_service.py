from _decimal import Decimal

from core.constants.evapotranspiration import ReferenceEvapotranspirationConstants
from core.domain.entity.evapotranspiration_entity import EToEntity

parameters_hargraves_samani = ReferenceEvapotranspirationConstants.parameters_hargraves_samani


class ReferenceEvapotranspirationService:
    @staticmethod
    def calculate_hargraves_samani(eto_entity: EToEntity) -> Decimal:
        a, b, c = parameters_hargraves_samani
        Ra = eto_entity.radiation
        Tmed = eto_entity.temperature_med
        Tmin = eto_entity.temperature_min
        Tmax = eto_entity.temperature_max
        return Decimal(Ra * a * (b * (Tmed + c) * (Tmax - Tmin)) ** Decimal(0.5))
