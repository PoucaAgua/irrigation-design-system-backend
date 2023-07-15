from fastapi import APIRouter

from infrastructure.api.v1.controllers import app_test_controller, evapotranspiration, project_controller

router = APIRouter()


router.include_router(app_test_controller.router, prefix="/test", tags=["Endpoint Test"])
router.include_router(evapotranspiration.router, prefix="/evapotranspiration", tags=["Endpoint Evapotranspiration"])
router.include_router(project_controller.router, prefix="/projects", tags=["Endpoint to manager projects"])
