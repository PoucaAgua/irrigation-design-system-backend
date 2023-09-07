from _decimal import Decimal

from apps.hydraulic_design.derivationline.derivationline_calculate_service import DerivationlineService
from core.domain.entity.derivationline_entity import DerivationlineDiameterEntity

class TestDerivationlineService:

  def test_calculate_diameter(self):

    test_derivationline_entity = DerivationlineDiameterEntity(
        demand_flow = Decimal(0.008481),
        speed_max = Decimal(1.5),
      )   
    expected_result = float(100)

    result = DerivationlineService.calculate_derivationline_dimensions(test_derivationline_entity)

    assert (expected_result == result)
