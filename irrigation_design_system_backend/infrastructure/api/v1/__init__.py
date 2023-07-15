from fastapi import APIRouter

from infrastructure.api.v1.controllers import  evapotranspiration, project_controller

router = APIRouter()


router.include_router(evapotranspiration.router, prefix="/evapotranspiration", tags=["Endpoint Evapotranspiration"])
router.include_router(project_controller.router, prefix="/projects", tags=["Endpoint to manager projects"])
