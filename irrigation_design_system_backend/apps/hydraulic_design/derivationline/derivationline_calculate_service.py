from _decimal import Decimal

from core.constants.hydraulic_design import HydraulicConstants
from core.constants.math import MathConstants
from core.domain.entity.derivationline_entity import DerivationlineDiameterEntity, DerivationlineLoadLoassEntity
from apps.consult_diameter.consult_nominal_diameter import ConsultNominalDiameterTable
from apps.hydraulic_design.hydraulic_calculation.hydraulic_calculation import HydraulicCalculation


class DerivationlineService:

    @staticmethod
    def calculate_derivationline_dimensions(diameter_entity: DerivationlineDiameterEntity) -> Decimal:
        
        pi = MathConstants.PI

        q = diameter_entity.demand_flow
        s_max = diameter_entity.speed_max

        theoretical_dimensions = (((4*q) / (pi*s_max))**Decimal(0.5)) * Decimal(1000.0)

        return ConsultNominalDiameterTable.nominal_diameter(float(theoretical_dimensions))
    
    @staticmethod
    def calculate_loadloass_derivationline(loadloss_entity: DerivationlineLoadLoassEntity) -> Decimal:
        
        g = HydraulicConstants.gravity

        l = loadloss_entity.length_derivationline
        q = loadloss_entity.flow
        n = loadloss_entity.n_outputs
        d = loadloss_entity.diameter_derivationline

        v = HydraulicCalculation.speed_water(q, d)
        re = HydraulicCalculation.n_reynolds(v, d)
        friction = HydraulicCalculation.friction_factor(d, re)
        f_factor = HydraulicCalculation.f_factor(n)

        hf = friction * (l / d) * ((v**2) /(2*g))

        hf_corr = hf * f_factor

        return hf_corr