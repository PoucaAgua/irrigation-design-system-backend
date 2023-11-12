from _decimal import Decimal
from core.constants.hydraulic_design import HydraulicConstants
from core.constants.math import MathConstants


class HydraulicCalculation:
    @staticmethod
    def speed_water(q, d) -> Decimal:
        pi = MathConstants.PI
        q = Decimal(q)
        d = Decimal(d)
        speed = (4 / ((d) ** 2)) * (q / pi)
        return speed

    @staticmethod
    def speed_water_lateral_line(flow, section):
        f = Decimal(flow)
        s = Decimal(section)
        return f / s

    @staticmethod
    def flow_lateral_line(Nu_emissors, flow_nominal):
        ne = Decimal(Nu_emissors)
        fn = Decimal(flow_nominal)
        flow = ne * fn
        return flow

    @staticmethod
    def flow_lateral_line_conversion(flow_lateral_l):
        fl = Decimal(flow_lateral_l)
        converted_flow = ((fl / 1000) / 60) / 60
        return converted_flow

    @staticmethod
    def flow_section_area(intern_diameter):
        d = Decimal(intern_diameter)
        pi = MathConstants.PI
        fsa = (pi * d ** Decimal(2)) / 4
        return fsa

    @staticmethod
    def emissors_number(length_lateral_line, emitter_spacing):
        l_aux = Decimal(length_lateral_line)
        spacing = Decimal(emitter_spacing)
        en = l_aux / spacing
        return en

    @staticmethod
    def n_reynolds(speed, diameter) -> Decimal:
        viscosity = HydraulicConstants.kinematic_viscosity
        num_reynolds = Decimal(diameter * speed) / viscosity
        return num_reynolds

    @staticmethod
    def coeficient_K(intern_diameter):
        di = Decimal(intern_diameter)
        const = HydraulicConstants.coeficient_for_K
        k = const / (di) ** Decimal(4.75)
        return k

    @staticmethod
    def friction_factor(d, re) -> Decimal:
        d = Decimal(d)
        re = Decimal(re)
        exp = Decimal(0.1593) * (d ** Decimal(-0.105))
        friction = Decimal(0.1034) * d ** Decimal(-0.256) * re ** Decimal(-exp)
        return friction

    @staticmethod
    def f_factor(n):
        m = HydraulicConstants.exp_loadloss
        n = Decimal(n)
        f = (1 / (m + 1)) + (1 / (2 * n)) + ((m - 1) ** Decimal(0.5)) / (6 * (n * n))
        return f
