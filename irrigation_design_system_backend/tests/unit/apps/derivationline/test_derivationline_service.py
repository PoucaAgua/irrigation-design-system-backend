from _decimal import Decimal

from apps.derivationline.derivationline_calculate_service import DerivationlineService
from core.domain.entity.derivationline_entity import DerivationlineEntity

class TestDerivationlineService:

  def test_calculate_diameter(self):

    error = 0

    test_derivationline_entity = DerivationlineEntity(
      friction_factor=Decimal(7),
      flow=Decimal(25.0),
      load_loss=Decimal(20.0),
      pipe_length=Decimal(30.0),
      )   
    expected_result = float(35.0)

    result = DerivationlineService.calculate_derivationline_dimensions(test_derivationline_entity)

    assert (expected_result == result)
    print(f'_____Test_Passed____\n')
