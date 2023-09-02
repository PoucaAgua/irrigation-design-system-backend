from _decimal import Decimal
from typing import Optional

from pydantic import BaseModel, Field

from core.domain.enum.status_types import StatusTypes
from core.domain.enum.line_types import LineTypes


class ProjectEntity(BaseModel):
    id: Optional[int] = Field(default=None)
    user_id: int
    group_id: str
    description: str
    status: StatusTypes
    crop: str
    maximum_actual_irrigation_required: Decimal
    crop_evapotranspiration: Decimal
    total_irrigation_required: Decimal


class DerivationLineEntity(BaseModel):
    id: Optional[int] = Field(default=None)
    project_id: int
    pipe_type: str
    inlet_pressure: Decimal
    length: str
    diameter: str
    localized_loss: str
    type: LineTypes


class LateralLineEntity(BaseModel):
    id: Optional[int] = Field(default=None)
    project_id: int
    dripper: str
    decline: Decimal
    inlet_pressure: Decimal
    separation_between_issuers: Decimal
    length_max: Decimal
    diameter: Decimal
    localized_loss: Decimal
    type: LineTypes
