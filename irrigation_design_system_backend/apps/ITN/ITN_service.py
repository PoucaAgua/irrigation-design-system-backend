from _decimal import Decimal
from core.domain.entity.itn_entity import (
    FlProjectionInputEntity,
    ITNProjectionInputEntity,
    ITNProjectionInputEntity2)

class FlService:
    @classmethod
    def calc_fl(cls, input_entity: FlProjectionInputEntity) -> Decimal:
        ce_i = input_entity.ce_i
        ce_e = input_entity.ce_e
        return Decimal(ce_i/(2*ce_e))

class ITNService:
    @classmethod
    def calc_itn(cls, input_entity: ITNProjectionInputEntity) -> Decimal:
        irn = input_entity.irn
        ea = input_entity.ea
        fl = input_entity.fl
        return Decimal(irn/((1-fl)*ea))

class ITNService2:
    @classmethod
    def calc_itn(cls, input_entity: ITNProjectionInputEntity2) -> Decimal:
        irn = input_entity.irn
        ce_i = input_entity.ce_i
        ce_e = input_entity.ce_e
        ea = input_entity.ea
        return Decimal(irn/((1-(ce_i/(2*ce_e)))*ea))