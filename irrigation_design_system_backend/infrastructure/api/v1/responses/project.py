from pydantic import BaseModel


class ProjectResponse(BaseModel):
    message: str = "Project created"
