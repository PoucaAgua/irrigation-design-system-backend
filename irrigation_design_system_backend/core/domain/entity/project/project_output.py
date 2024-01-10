from pydantic import BaseModel, Field
from typing import List
from _decimal import Decimal

from core.domain.enum.status_types import StatusTypes
from infrastructure.persistence.models import Project


class ProjectResponse(BaseModel):
    message: str = "Project created"


class ProjectGetAllOutput(BaseModel):
    id: int = Field(..., description="project id")
    user_id: int = Field(..., description="user id")
    group_id: str = Field(..., description="group id")
    description: str = Field(..., description="project description")
    status: StatusTypes = Field(..., description="project status")
    crop: str = Field(..., description="project crop")
    maximum_actual_irrigation_required: Decimal = Field(
        ..., description="maximum actual irrigation required"
    )
    crop_evapotranspiration: Decimal = Field(..., description="crop evapotranspiration")
    total_irrigation_required: Decimal = Field(..., description="total irrigation required")

    @classmethod
    def from_domain(cls, projects: List[Project]) -> List["ProjectGetAllOutput"]:
        outputs = []

        for project in projects:
            output = cls(**dict(project))
            output.group_id = project.group_id
            output.description = project.description
            outputs.append(output)

        return outputs
