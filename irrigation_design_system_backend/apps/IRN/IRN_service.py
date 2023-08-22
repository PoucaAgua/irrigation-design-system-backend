from _decimal import Decimal
from core.domain.entity.irn_solo_entity import (
    IRNsoloProjectionInputEntity,
    IRNmaxProjectionInputEntity,
    IRNatmProjectionInputEntity)

class IRNmaxService:
    @classmethod
    def calc_irn_max(cls, input_entity: IRNmaxProjectionInputEntity) -> Decimal:
        ucc = input_entity.theta_cc
        upm = input_entity.theta_pm
        z = input_entity.profunidade
        f = input_entity.f_critico
        return Decimal((ucc - upm)*z*f)

class IRNatmService:
    @classmethod
    def calc_irn_atm(cls, input_entity: IRNatmProjectionInputEntity ) -> Decimal:
        eto = input_entity.evapo_eto
        kc = input_entity.coef_cultura
        am = input_entity.area_molhada
        return Decimal(eto*kc*am)

class IRNSoloService:
    @classmethod
    def calc_irn_solo(cls, input_entity: IRNsoloProjectionInputEntity) -> Decimal:
        ucc = input_entity.umidade_cc
        uatual = input_entity.umidade_atual
        z = input_entity.profudidade
        return Decimal((ucc - uatual) * z)