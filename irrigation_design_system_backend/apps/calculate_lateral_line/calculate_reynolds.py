from _decimal import Decimal

from core.constants.lateral_line import LateralLineConstants
from core.domain.entity.lateral_line_entity import ReynoldsNumber


class ReynoldsCalculate:

    @staticmethod
    def calculate_reynolds(reynolds_entity: ReynoldsNumber) -> Decimal:

        constant_kinematic_viscosity = LateralLineConstants.kinematic_viscosity

        v = reynolds_entity.flow_velocity
        d = reynolds_entity.pipe_diameter

        return ( v*d ) / constant_kinematic_viscosity
    