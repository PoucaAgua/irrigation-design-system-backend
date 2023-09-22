from fastapi import APIRouter

from infrastructure.api.v1.controllers import (
    evapotranspiration_controller,
    project_controller,
    percent_wetted_area_controller,
    percent_shaded_area_controller,
    derivation_line_controller,
    total_irrigation_controller,
    actual_irrigation_controller,
)

router = APIRouter()

router.include_router(
    evapotranspiration_controller.router,
    prefix="/evapotranspiration",
    tags=["Endpoint Evapotranspiration"],
)
router.include_router(
    percent_wetted_area_controller.router,
    prefix="/percent_wetted_area",
    tags=["Endpoint to calculate the percent_wetted_area"],
)
router.include_router(
    percent_shaded_area_controller.router,
    prefix="/percent_shaded_area",
    tags=["Endpoint to calculate the percent_shaded_area"],
)
router.include_router(
    project_controller.router, prefix="/projects", tags=["Endpoint to manager projects"]
)
router.include_router(
    derivation_line_controller.router,
    prefix="/derivationline",
    tags=["Endpoint Derivation Line"]
)
router.include_router(
    actual_irrigation_controller.router,
    prefix="/actual_irrigation",
    tags=["Endpoint actual_irrigation"]
)
router.include_router(
    total_irrigation_controller.router,
    prefix="/total_irrigation",
    tags=["Endpoint to calculate Total Irrigation Necessary"],
)
