from _decimal import Decimal

from core.constants.derivationline import DerivationlineConstants
from core.domain.entity.derivationline_entity import DerivationlineEntity

class DerivationlineService:

  @staticmethod
  def calculate_derivationline_dimensions(derivationline_entity: DerivationlineEntity) -> Decimal:

    constant_derivationline = DerivationlineConstants.parameters_branchline

    f = derivationline_entity.friction_factor
    Q = derivationline_entity.flow
    hf = derivationline_entity.load_loss
    Lv = derivationline_entity.pipe_length

    return Decimal(((constant_derivationline * f * (Q)**2) / hf) * Lv)**(1/5)