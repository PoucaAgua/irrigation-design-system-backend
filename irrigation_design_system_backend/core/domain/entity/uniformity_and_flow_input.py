from _decimal import Decimal

from pydantic import BaseModel, Field

class FlowRateIrrigationInput(BaseModel):
    v1: Decimal = Field(
        ..., ge=0, description="[v1] Volume of water collected at point 1 (mL)"
    )
    v2: Decimal = Field(
        ..., ge=0, description="[v2] Volume of water collected at point 2 (mL)"
    )
    v3: Decimal = Field(
        ..., ge=0, description="[v3] Volume of water collected at point 3 (mL)"
    )
    v4: Decimal = Field(
        ..., ge=0, description="[v4] Volume of water collected at point 4 (mL)"
    )
    v5: Decimal = Field(
        ..., ge=0, description="[v5] Volume of water collected at point 5 (mL)"
    )
    v6: Decimal = Field(
        ..., ge=0, description="[v6] Volume of water collected at point 6 (mL)"
    )
    v7: Decimal = Field(
        ..., ge=0, description="[v7] Volume of water collected at point 7 (mL)"
    )
    v8: Decimal = Field(
        ..., ge=0, description="[v8] Volume of water collected at point 8 (mL)"
    )
    v9: Decimal = Field(
        ..., ge=0, description="[v9] Volume of water collected at point 9 (mL)"
    )
    v10: Decimal = Field(
        ..., ge=0, description="[v10] Volume of water collected at point 10 (mL)"
    )
    v11: Decimal = Field(
        ..., ge=0, description="[v11] Volume of water collected at point 11 (mL)"
    )
    v12: Decimal = Field(
        ..., ge=0, description="[v12] Volume of water collected at point 12 (mL)"
    )
    v13: Decimal = Field(
        ..., ge=0, description="[v13] Volume of water collected at point 13 (mL)"
    )
    v14: Decimal = Field(
        ..., ge=0, description="[v14] Volume of water collected at point 14 (mL)"
    )
    v15: Decimal = Field(
        ..., ge=0, description="[v15] Volume of water collected at point 15 (mL)"
    )
    v16: Decimal = Field(
        ..., ge=0, description="[v16] Volume of water collected at point 16 (mL)"
    )
    time_c: Decimal = Field(
        ..., ge=0, description="[Time_c] Time de coleta (minutos)"
    )

class UniformityIrrigationInput(BaseModel):
    v1: Decimal = Field(
        ..., ge=0, description="[v1] Volume of water collected at point 1 (mL)"
    )
    v2: Decimal = Field(
        ..., ge=0, description="[v2] Volume of water collected at point 2 (mL)"
    )
    v3: Decimal = Field(
        ..., ge=0, description="[v3] Volume of water collected at point 3 (mL)"
    )
    v4: Decimal = Field(
        ..., ge=0, description="[v4] Volume of water collected at point 4 (mL)"
    )
    v5: Decimal = Field(
        ..., ge=0, description="[v5] Volume of water collected at point 5 (mL)"
    )
    v6: Decimal = Field(
        ..., ge=0, description="[v6] Volume of water collected at point 6 (mL)"
    )
    v7: Decimal = Field(
        ..., ge=0, description="[v7] Volume of water collected at point 7 (mL)"
    )
    v8: Decimal = Field(
        ..., ge=0, description="[v8] Volume of water collected at point 8 (mL)"
    )
    v9: Decimal = Field(
        ..., ge=0, description="[v9] Volume of water collected at point 9 (mL)"
    )
    v10: Decimal = Field(
        ..., ge=0, description="[v10] Volume of water collected at point 10 (mL)"
    )
    v11: Decimal = Field(
        ..., ge=0, description="[v11] Volume of water collected at point 11 (mL)"
    )
    v12: Decimal = Field(
        ..., ge=0, description="[v12] Volume of water collected at point 12 (mL)"
    )
    v13: Decimal = Field(
        ..., ge=0, description="[v13] Volume of water collected at point 13 (mL)"
    )
    v14: Decimal = Field(
        ..., ge=0, description="[v14] Volume of water collected at point 14 (mL)"
    )
    v15: Decimal = Field(
        ..., ge=0, description="[v15] Volume of water collected at point 15 (mL)"
    )
    v16: Decimal = Field(
        ..., ge=0, description="[v16] Volume of water collected at point 16 (mL)"
    )