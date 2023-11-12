from _decimal import Decimal

from apps.hydraulic_design.hydraulic_calculation.hydraulic_calculation import (
    HydraulicCalculation,
)


class TestHydraulicCalculation:
    error = Decimal("1e-3")

    def test_speed_water(self):
        result = Decimal(HydraulicCalculation.speed_water(0.008481, 0.1))
        expected = Decimal(1.07983)

        assert abs(result - expected) <= self.error

    def test_speed_water_lateral_line(self):
        result = Decimal(HydraulicCalculation.speed_water_lateral_line(0.00014, 0.0002))
        expected = Decimal(0.7)

        assert abs(result - expected) <= self.error

    def test_flow_lateral_line(self):
        result = Decimal(HydraulicCalculation.flow_lateral_line(305.307, 1.6))
        expected = Decimal(488.4907139)

        assert abs(result - expected) <= self.error

    def test_n_reynolds(self):
        result = Decimal(HydraulicCalculation.n_reynolds(1.07983445809, 0.1))
        expected = Decimal(107983.4458092)

        assert abs(result - expected) <= self.error

    def test_n_reynolds_lateral_line(self):
        result = Decimal(HydraulicCalculation.n_reynolds(0.67487597, 0.016))
        expected = Decimal(10798.01552)

        assert abs(result - expected) <= self.error

    def test_friction_factor(self):
        result = Decimal(HydraulicCalculation.friction_factor(0.1, 107983.4458092))
        expected = Decimal(0.0177585)

        assert abs(result - expected) <= self.error

    def test_friction_factor_lateral_line(self):
        result = Decimal(HydraulicCalculation.friction_factor(0.016, 10798.01552))
        print(result)
        expected = Decimal(0.030367585)

        assert abs(result - expected) <= self.error

    def test_f_factor(self):
        result = Decimal(HydraulicCalculation.f_factor(62.5))
        expected = Decimal(0.371673314)

        assert abs(result - expected) <= self.error

    def test_f_factor_lateral_line(self):
        result = Decimal(HydraulicCalculation.f_factor(305.307))
        expected = Decimal(0.3652787007)

        assert abs(result - expected) <= self.error

    def test_coeficient_K(self):
        result = HydraulicCalculation.coeficient_K(0.016)
        expected = Decimal()
        assert abs(result - expected) <= self.error

    def test_emissors_number(self):
        result = HydraulicCalculation.emissors_number(61.0613, 0.2)
        expected = Decimal(305.307)
        assert abs(result - expected) <= self.error

    def test_flow_section_area(self):
        result = HydraulicCalculation.flow_section_area(0.016)
        expected = Decimal(0.0002)
        assert abs(result - expected) <= self.error

    def test_flow_lateral_line_conversion(self):
        result = HydraulicCalculation.flow_lateral_line_conversion(488.4907139)
        expected = Decimal(0.00014)
        assert abs(result - expected) <= self.error
