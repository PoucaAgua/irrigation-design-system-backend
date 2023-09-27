from _decimal import Decimal

from pydantic import BaseModel, Field


class IrrigationTimeByPlantInput(BaseModel):
    itn: Decimal = Field(..., ge=0, description="[ITN] Total Irrigation (mm)")
    sp: Decimal = Field(..., ge=0, description="[sp] Spacing between plants (m)")
    sl: Decimal = Field(..., ge=0, description="[sl] Distance between drip lines (m)")
    Ne: Decimal = Field(..., ge=0, description="[Ne] Number of emitters per plants (adm)")
    q: Decimal = Field(..., ge=0, description="[q] Emitter Flow rate (L/h)")


class IrrigationTimeByLineInput(BaseModel):
    itn: Decimal = Field(..., ge=0, description="[ITN] Total Irrigation (mm)")
    se: Decimal = Field(..., ge=0, description="[sp] Spacing between emitter (m)")
    sl: Decimal = Field(..., ge=0, description="[sl] Distance between drip lines (m)")
    q: Decimal = Field(..., ge=0, description="[q] Emitter Flow rate (L/h)")
