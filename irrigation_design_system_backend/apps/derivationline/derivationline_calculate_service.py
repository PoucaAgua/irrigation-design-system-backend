from _decimal import Decimal

from core.constants.derivationline import DerivationlineConstants
from core.domain.entity.derivationline_entity import DerivationlineEntity
from apps.consult_diameter.consult_nominal_diameter import ConsultNominalDiameterTable


class DerivationlineService:

    @staticmethod
    def calculate_derivationline_dimensions(derivationline_entity: DerivationlineEntity):
        constant_derivationline = DerivationlineConstants.parameters_derivationline

        f = derivationline_entity.friction_factor
        q = derivationline_entity.flow
        hf = derivationline_entity.load_loss
        lv = derivationline_entity.pipe_length

        theoretical_dimensions = (((constant_derivationline * f * (q ** 2)) / hf) * lv) ** Decimal(0.2)

        return ConsultNominalDiameterTable.nominal_diameter(float(theoretical_dimensions))