from _decimal import Decimal

from core.constants.hydraulic_design import HydraulicConstants
from core.constants.math import MathConstants
from core.domain.entity.derivation_line_input import DerivationLineDiameterInput, DerivationLineLoadLossInput
from apps.hydraulic_design.consult_diameter.consult_nominal_diameter import ConsultNominalDiameterTable
from apps.hydraulic_design.hydraulic_calculation.hydraulic_calculation import HydraulicCalculation


class DerivationLineService:

    @staticmethod
    def calculate_diameter(diameter_input: DerivationLineDiameterInput) -> Decimal:
        pi = MathConstants.PI
        q = diameter_input.demand_flow
        s_max = diameter_input.speed_max

        theoretical_dimensions = (((4*q) / (pi*s_max))**Decimal(0.5)) * Decimal(1000.0)
        return ConsultNominalDiameterTable.nominal_diameter(float(theoretical_dimensions))
    
    @staticmethod
    def calculate_load_loss(load_loss_input: DerivationLineLoadLossInput) -> Decimal:
        g = HydraulicConstants.gravity
        l = load_loss_input.length_derivation_line
        q = load_loss_input.flow
        n = load_loss_input.n_outputs
        d = load_loss_input.diameter_derivation_line

        v = HydraulicCalculation.speed_water(q, d)
        re = HydraulicCalculation.n_reynolds(v, d)
        friction = HydraulicCalculation.friction_factor(d, re)
        f_factor = HydraulicCalculation.f_factor(n)

        hf = friction * (l / d) * ((v**2) /(2*g))
        hf_corr = hf * f_factor
        return hf_corr
