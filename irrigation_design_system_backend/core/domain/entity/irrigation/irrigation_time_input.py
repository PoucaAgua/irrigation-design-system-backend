from _decimal import Decimal

from pydantic import BaseModel, Field


class IrrigationTimeByPlantInput(BaseModel):
    total_irrigation: Decimal = Field(..., ge=0, description="[ITN] Total Irrigation (mm)")
    spacing_between_plants: Decimal = Field(
        ..., ge=0, description="[sp] Spacing between plants (m)"
    )
    spacing_between_side_lines: Decimal = Field(
        ..., ge=0, description="[sl] Distance between drip lines (m)"
    )
    number_of_emitters_per_plant: Decimal = Field(
        ..., ge=0, description="[Ne] Number of emitters per plants (adm)"
    )
    emitter_flow: Decimal = Field(..., ge=0, description="[q] Emitter Flow rate (L/h)")


class IrrigationTimeByLineInput(BaseModel):
    total_irrigation: Decimal = Field(..., ge=0, description="[ITN] Total Irrigation (mm)")
    spacing_between_emitters: Decimal = Field(
        ..., ge=0, description="[sp] Spacing between emitter (m)"
    )
    spacing_between_side_lines: Decimal = Field(
        ..., ge=0, description="[sl] Distance between drip lines (m)"
    )
    emitter_flow: Decimal = Field(..., ge=0, description="[q] Emitter Flow rate (L/h)")
