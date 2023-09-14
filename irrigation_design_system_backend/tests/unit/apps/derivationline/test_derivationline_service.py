from _decimal import Decimal

from apps.hydraulic_design.derivationline.derivationline_calculate_service import DerivationlineService
from core.domain.entity.derivationline_entity import DerivationlineDiameterEntity, DerivationlineLoadLoassEntity

class TestDerivationlineService:

  def test_calculate_diameter(self):

    error = Decimal('1e-3')

    test_derivationline_entity = DerivationlineDiameterEntity(
        demand_flow = Decimal(0.008481),
        speed_max = Decimal(1.5),
      )   
    expected = float(100)

    result = DerivationlineService.calculate_derivationline_dimensions(test_derivationline_entity)

    assert (expected == result)

  def calculate_loadloass_derivationline(self):
    
    test_loadloss_entity = DerivationlineLoadLoassEntity(
        length_derivationline = Decimal(50.0),
        diameter_derivationline = Decimal(0.1),
        flow = Decimal(1.079834458),
        n_outputs = Decimal(62.5)
    )
    expected = Decimal(0.19613492804)
    result = DerivationlineService.calculate_loadloass_derivationline(test_loadloss_entity)

    assert abs(expected - result) <= self.error



