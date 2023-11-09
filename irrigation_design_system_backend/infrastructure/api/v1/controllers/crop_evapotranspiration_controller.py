from fastapi import APIRouter

from apps.evapotranspiration.crop_evapotranspiration.crop_evapotranspiration_service import (
    CropEvapotranspirationService,
)
from core.domain.entity.evapotranspiration.crop_evapotranspiration_input import (
    CropEvapotranspirationInput,
)

from infrastructure.api.v1.responses.evapotranspiration import (
    EvapotranspirationResponse,
)

router = APIRouter()


@router.post("/Keller", response_model=EvapotranspirationResponse)
def calculate_by_keller(etc_input: CropEvapotranspirationInput):
    etc = CropEvapotranspirationService.etc_by_keller(etc_input)
    return EvapotranspirationResponse(value=etc)


@router.post("/Bernardo", response_model=EvapotranspirationResponse)
def calculate_by_bernardo(etc_input: CropEvapotranspirationInput):
    etc = CropEvapotranspirationService.etc_by_bernardo(etc_input)
    return EvapotranspirationResponse(value=etc)


@router.post("/Fereres", response_model=EvapotranspirationResponse)
def calculate_by_fereres(etc_input: CropEvapotranspirationInput):
    etc = CropEvapotranspirationService.etc_by_fereres(etc_input)
    return EvapotranspirationResponse(value=etc)


@router.post("/Keller and Bliesner", response_model=EvapotranspirationResponse)
def calculate_by_keller_and_bliesner(etc_input: CropEvapotranspirationInput):
    etc = CropEvapotranspirationService.etc_by_keller_and_bliesner(etc_input)
    return EvapotranspirationResponse(value=etc)
