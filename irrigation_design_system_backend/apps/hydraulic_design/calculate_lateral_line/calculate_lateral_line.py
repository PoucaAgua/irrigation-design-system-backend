from _decimal import Decimal
from apps.hydraulic_design.hydraulic_calculation.hydraulic_calculation import HydraulicCalculation
from core.constants.hydraulic_design import HydraulicConstants
from core.domain.entity.lateral_line_entity import LateralLineInput


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
            coefficient = HydraulicCalculation.coeficient_load_loss(internal_diameter)

            length_lateral_line = Decimal(max_flow_rate_variation * Decimal(service_pressure / flow_exponent) * Decimal((exponent_pressure_loss_equation + 1) / coefficient) * Decimal(emitter_spacing / nominal_flow_rate) ** Decimal(exponent_pressure_loss_equation)) ** Decimal(1 / (exponent_pressure_loss_equation + 1))

            return length_lateral_line
        
        except ZeroDivisionError:
            return "Caught an InvalidOperation exception, it is not possible to divide by zero."
    
    @classmethod
    def calculate_head_loss(cls, length_of_lateral_line: Decimal, internal_diameter: Decimal) -> Decimal:
        try:
            friction_factor = HydraulicCalculation.friction_factor
            water_velocity_lateral_line = HydraulicCalculation.speed_water
            factor_f = HydraulicCalculation.f_factor

            gravity_acceleration = HydraulicConstants.gravity

            head_loss = friction_factor * (length_of_lateral_line / internal_diameter) * ((water_velocity_lateral_line ** 2) / (2 * gravity_acceleration))
            head_loss_corrected = head_loss * factor_f
            return head_loss_corrected
        except Exception as e:
            # Trate qualquer exceção apropriada aqui
            pass