from typing import Optional

from pydantic import BaseModel, Field


class ProjectEntity(BaseModel):
    id: Optional[int] = Field(default=None)

    user_id: int
