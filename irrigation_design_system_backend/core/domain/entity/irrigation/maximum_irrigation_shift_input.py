from _decimal import Decimal

from pydantic import BaseModel, Field


class MaximumIrrigationShiftInput(BaseModel):
    actual_irrigation: Decimal = Field(
        ..., ge=0, description="[IRN] The actual irrigation necessary in mm"
    )
    crop_evapotranspiration: Decimal = Field(
        ..., ge=0, description="[ETc] the crop evapotranspiration in mm"
    )
