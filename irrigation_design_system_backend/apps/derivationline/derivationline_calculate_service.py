from _decimal import Decimal

from core.constants.derivationline import DerivationlineConstants
from core.domain.entity.derivationline_entity import DerivationlineEntity
from apps.consult_diameter.consult_nominal_diameter import ConsultNominalDiameterTable

class DerivationlineService:

  @staticmethod
  def calculate_derivationline_dimensions(derivationline_entity: DerivationlineEntity):

    constant_derivationline = DerivationlineConstants.parameters_derivationline

    f = derivationline_entity.friction_factor
    Q = derivationline_entity.flow
    hf = derivationline_entity.load_loss
    Lv = derivationline_entity.pipe_length

    theorical_dimensions = (((constant_derivationline * f * ((Q)**2)) / hf) * Lv)**Decimal(0.2)

    return (ConsultNominalDiameterTable.nominal_diameter(float(theorical_dimensions)))