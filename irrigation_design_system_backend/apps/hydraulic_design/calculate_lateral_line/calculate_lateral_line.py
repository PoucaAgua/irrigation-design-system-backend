from _decimal import Decimal
from apps.hydraulic_design.hydraulic_calculation.hydraulic_calculation import HydraulicCalculation
from core.constants.hydraulic_design import HydraulicConstants
from core.domain.entity.lateral_line_entity import LateralLineInput, LateralLineHeadLossInput


class LateralLineService:

    @classmethod
    def calculate_length_lateral_line(cls, lateral_line_entity: LateralLineInput) -> Decimal:
        try:
            service_pressure = lateral_line_entity.service_pressure
            nominal_flow_rate = lateral_line_entity.nominal_flow_rate
            max_flow_rate_variation = lateral_line_entity.max_flow_rate_variation
            emitter_spacing = lateral_line_entity.emitter_spacing
            internal_diameter = lateral_line_entity.internal_diameter

            flow_exponent = HydraulicConstants.flow_exponent
            exponent_pressure_loss_equation = HydraulicConstants.exp_loadloss
            coefficient = HydraulicCalculation.coeficient_K(internal_diameter)

            length_lateral_line = Decimal(max_flow_rate_variation * Decimal(service_pressure / flow_exponent) * Decimal(
                (exponent_pressure_loss_equation + 1) / coefficient) * Decimal(
                emitter_spacing / nominal_flow_rate) ** Decimal(exponent_pressure_loss_equation)) ** Decimal(
                1 / (exponent_pressure_loss_equation + 1))

            return length_lateral_line

        except ZeroDivisionError:
            return "Caught an InvalidOperation exception, it is not possible to divide by zero."

    @classmethod
    def calculate_head_loss(cls, lateral_line_entity: LateralLineHeadLossInput):
        try:
            length_lateral_line = lateral_line_entity.length_lateral_line
            internal_diameter = lateral_line_entity.internal_diameter
            nominal_flow = lateral_line_entity.nominal_flow_rate
            exponent_load_loss = lateral_line_entity.exponent_pressure_loss_equation
            emitter_spacing = lateral_line_entity.emitter_spacing

            g = HydraulicConstants.gravity
            v = HydraulicConstants.kinematic_viscosity

            ne = length_lateral_line / internal_diameter
            flow = ne * nominal_flow
            section = HydraulicCalculation.flow_section_area(internal_diameter)
            emissors = HydraulicCalculation.emissors_number(length_lateral_line, emitter_spacing)

            speed_water = HydraulicCalculation.speed_water_lateral_line(flow, section)
            reynolds = HydraulicCalculation.n_reynolds(speed_water, v)

            friction_f = HydraulicCalculation.friction_factor(internal_diameter, reynolds)
            f_factor = HydraulicCalculation.f_factor(emissors, exponent_load_loss)

            head_loss = Decimal(
                friction_f * (length_lateral_line / internal_diameter) * ((speed_water ** 2) / (2 * g)))
            head_loss_corrected = head_loss * f_factor
            return head_loss_corrected
        except Exception as e:
            # Trate qualquer exceção apropriada aqui
            pass