from pydantic import BaseModel, Field
from typing import List

from core.domain.entity.project_input import ProjectInput


class ProjectResponse(BaseModel):
    message: str = "Project created"


class ProjectGetAllResponse(BaseModel):
    group_id: str = Field(..., description="group id")
    description: str = Field(..., description="project description")

    @classmethod
    def from_domain(cls, projects: List[ProjectInput]) -> List["ProjectGetAllResponse"]:
        outputs = []

        for project in projects:
            output = cls(**dict(project))
            output.group_id = project.group_id
            output.description = project.description
            outputs.append(output)

        return outputs
