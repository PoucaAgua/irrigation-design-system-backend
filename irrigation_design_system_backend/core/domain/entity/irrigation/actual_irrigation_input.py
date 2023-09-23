from _decimal import Decimal
from dataclasses import dataclass
from typing import Optional

from pydantic import BaseModel, condecimal, Field


class ActualIrrigationBySoilParamsInput(BaseModel):
    soil_moisture_field_capacity: Decimal = Field(
        ..., ge=0, le=1, description="[θcc] Field capacity in cm³/cm³"
    )
    soil_moisture_at_permanent_wilting_point: condecimal(ge=0, le=1) = Field(
        ..., ge=0, le=1, description="[θpmp] Permanent wilting point in cm³/cm³"
    )
    depletion_factor: Decimal = Field(
        ...,
        ge=0,
        le=1,
        description="""
        [f] depletion or water consumption factor of the soil,
        always less than 1, with values ranging between 0.3 for crops with shallow
        root systems and high rates of atmospheric demand, and 0.7 for plants with 
        deep root systems and low rates of atmospheric demand, hence specific 
        to each crop.
        """,
    )
    soil_depth: Decimal = Field(..., ge=0, description="[z] Soil depth in cm")
    effective_precipitation: Optional[Decimal] = Field(
        default=0, ge=0, description="[Pe] Effective precipitation in mm"
    )


@dataclass
class ActualIrrigationByAtmosphericParamsInput:
    actual_evapotranspiration: Decimal
    kc: Decimal
    percent_wetted_area: Decimal


class MaxActualIrrigationInput(ActualIrrigationBySoilParamsInput):
    fraction_of_total_wetted_area: Decimal = Field(
        ..., ge=0, le=1, description="[FW] fraction of total wetted area, dimensionless"
    )
