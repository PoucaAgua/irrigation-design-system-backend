from decimal import Decimal
from pydantic import BaseModel, Field


class LateralLineInput(BaseModel):
    service_pressure: Decimal = Field(..., ge=0, description="[SP] Service Pressure (mca)")
    nominal_flow_rate: Decimal = Field(..., ge=0, description="[NFR] Nominal Flow Rate (L/h)")
    max_flow_rate_variation: Decimal = Field(
        ..., ge=0, description="[MFV] Max Flow Rate Variation (%)"
    )
    internal_diameter: Decimal = Field(..., ge=0, description="[ID] Internal Diameter (m)")
    emitter_spacing: Decimal = Field(..., ge=0, description="[ES] Emitter Spacing (m)")
    flow_exponent: Decimal = Field(..., ge=0, description="[FE] Flow Exponent (dimensionless)")
    exponent_pressure_loss_equation: Decimal = Field(
        ..., ge=0, description="[EPL] Exponent Pressure Loss Equation (dimensionless)"
    )
    coefficient: Decimal = Field(..., ge=0, description="[C] Coefficient (K)")


class LateralLineHeadLossInput(BaseModel):
    length_lateral_line: Decimal = Field(..., ge=0, description="[LL] Length Lateral Line (L)")
    internal_diameter: Decimal = Field(..., ge=0, description="[ID] Internal Diameter (m)")
    emitter_spacing: Decimal = Field(..., ge=0, description="[ES] Emitter Spacing (m)")
    nominal_flow_rate: Decimal = Field(..., ge=0, description="[NFR] Nominal Flow Rate (L/h)")
