from fastapi import APIRouter

from infrastructure.api.v1.controllers import  evapotranspiration_controller, project_controller


router = APIRouter()


router.include_router(evapotranspiration_controller.router, prefix="/evapotranspiration", tags=["Endpoint Evapotranspiration"])
router.include_router(project_controller.router, prefix="/projects", tags=["Endpoint to manager projects"])
