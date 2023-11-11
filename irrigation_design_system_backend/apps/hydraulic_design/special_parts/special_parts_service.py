from _decimal import Decimal
from core.domain.entity.special_parts_input import SpecialPartsInput
from apps.hydraulic_design.consult_special_parts.consult_loadloss_specialparts import ConsultLoadLossSpecialPartsTable


class SpecialPartsService:

    @classmethod
    def special_parts_load_loss(cls, special_parts_input: SpecialPartsInput) -> Decimal:
        diameter = special_parts_input.diameter
        special_parts = special_parts_input.special_parts

        total_load_loss = 0
        for special_part in special_parts:
            unit_load_loss_by_special_part = special_part.quantity * Decimal(ConsultLoadLossSpecialPartsTable.loadloss_special_parts(special_part.type.value, diameter))
            total_load_loss += unit_load_loss_by_special_part

        return Decimal(total_load_loss)
