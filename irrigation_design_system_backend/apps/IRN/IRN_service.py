from _decimal import Decimal
from core.domain.entity.irn_solo_entity import IRNsoilInputEntity
from core.domain.entity.irn_solo_entity import IRNatmInputEntity
from core.domain.entity.irn_solo_entity import IRNmaxInputEntity

class IrrigationRealNecessaryService:
    @classmethod
    def calc_irn_max(cls, input_entity: IRNmaxInputEntity) -> Decimal:
        theta_fc = input_entity.theta_fc
        theta_wp = input_entity.theta_wp
        z = input_entity.z
        f_critical = input_entity.f_critical
        return Decimal((theta_fc - theta_wp)*z*f_critical)

    @classmethod
    def calc_irn_atm(cls, input_entity: IRNatmInputEntity) -> Decimal:
        eto = input_entity.eto
        kc = input_entity.kc
        pwa = input_entity.pwa
        return Decimal(eto*kc*pwa)

    @classmethod
    def calc_irn_solo(cls, input_entity: IRNsoilInputEntity) -> Decimal:
        theta_fc = input_entity.theta_fc
        theta_obs = input_entity.theta_obs
        z = input_entity.z
        return Decimal((theta_fc - theta_obs) * z)