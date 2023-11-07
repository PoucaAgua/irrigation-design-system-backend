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
    def flow_section_area(intern_diameter):
        d = Decimal(intern_diameter)
        pi = MathConstants.PI
        fsa = (pi * d ** Decimal(2)) / 4

        return fsa

    @staticmethod
    def emissors_number(length_lateral_line, emitter_spacing):
        l = Decimal(length_lateral_line)
        spacing = Decimal(emitter_spacing)
        en = l / spacing

        return en

    @staticmethod
    def flow_section(intern_diameter):
        di = Decimal(intern_diameter)
        fs = di ** Decimal(2) / 4
        return fs

    @staticmethod
    def flow_lateral_line(emissors, flow_nominal):
        e = Decimal(emissors)
        fn = Decimal(flow_nominal)
        flow = 0.0000002777 * (e * fn)

        return flow

    @staticmethod
    def speed_water_lateral_line(flow, section):
        f = Decimal(flow)
        s = Decimal(section)

        return f / s

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
