from _decimal import Decimal
from typing import Optional, Any

from pydantic import BaseModel, Field, model_validator


class TotalIrrigationInput(BaseModel):
    actual_irrigation: Decimal = Field(
        ..., ge=0, description="[IRN] The actual irrigation necessary in mm"
    )
    electrical_conductivity_of_irrigation: Decimal = Field(
        None, ge=0, description="[CE_i] the electrical conductivity of the irrigation in dSm^-1"
    )
    electrical_conductivity_of_soil_saturation: Decimal = Field(
        None,
        ge=0,
        description="[CE_e] the electrical conductivity of the soil saturation in dSm^-1",
    )
    leaching_fraction: Decimal = Field(
        None,
        ge=0,
        lt=1,
        description="""[FL] represents the minimum leaching fraction 
        to be adopted to control salinity at the crop's tolerance level""",
    )
    efficiency: Decimal = Field(..., gt=0)

    @model_validator(mode="before")
    @classmethod
    def check(cls, data: Any) -> Any:
        data["leaching_fraction"] = cls.__calculate_leaching_fraction(**data)
        return data

    @staticmethod
    def __calculate_leaching_fraction(
        electrical_conductivity_of_irrigation: Optional[Decimal] = None,
        electrical_conductivity_of_soil_saturation: Optional[Decimal] = None,
        leaching_fraction: Optional[Decimal] = None,
        **kwargs
    ) -> Decimal:
        if leaching_fraction is not None:
            return leaching_fraction
        if (
            electrical_conductivity_of_soil_saturation is not None
            and electrical_conductivity_of_soil_saturation is not None
        ):
            return Decimal(
                electrical_conductivity_of_irrigation
                / (2 * electrical_conductivity_of_soil_saturation)
            )

        raise ValueError(
            """
            Needs to have leaching_fraction 
            or both electrical_conductivity_of_soil_saturation 
               and electrical_conductivity_of_soil_saturation
            """
        )
