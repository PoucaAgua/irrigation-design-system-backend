from pydantic import BaseModel


class PWAResponse(BaseModel):
    message: str = "PWA calculation successful."
    value: float
