from _decimal import Decimal

from apps.hydraulic_design.hydraulic_calculation.hydraulic_calculation import HydraulicCalculation

class TestHydraulicCalculation:

    error = Decimal('1e-3')

    def test_speed_water(self):

        result = Decimal(HydraulicCalculation.speed_water(0.008481, 0.1))
        expected = Decimal(1.07983)

        assert abs(result - expected) <= self.error

    def test_n_reynolds(self):

        result = Decimal(HydraulicCalculation.n_reynolds(1.07983445809, 0.1))
        expected = Decimal(107983.4458092)

        assert abs(result - expected) <= self.error

    def test_friction_factor(self):

        result = Decimal(HydraulicCalculation.friction_factor(0.1, 107983.4458092))
        expected = Decimal(0.0177585)

        assert abs(result - expected) <= self.error

    def test_f_factor(self):
        
        result = Decimal(HydraulicCalculation.f_factor(62.5))
        expected = Decimal(0.371673314)

        assert abs(result - expected) <= self.error

