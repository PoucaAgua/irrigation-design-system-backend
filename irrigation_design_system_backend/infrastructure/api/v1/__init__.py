from fastapi import APIRouter

from infrastructure.api.v1.controllers import (
    evapotranspiration_controller,
    project_controller,
    percent_wetted_area_controller,
    percent_shaded_area_controller,
    derivation_line_controller,
    irrigation_controller,
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
    prefix="/derivation_line",
    tags=["Endpoint to calculate Derivation Line"],
)
router.include_router(
    irrigation_controller.actual_irrigation_controller.router,
    prefix="/irrigation/actual",
    tags=["Endpoint to calculate Actual Irrigation outputs"],
)
router.include_router(
    irrigation_controller.total_irrigation_controller.router,
    prefix="/irrigation/total",
    tags=["Endpoint to calculate Total Irrigation outputs"],
)
router.include_router(
    irrigation_controller.total_irrigation_controller.router,
    prefix="/irrigation/total",
    tags=["Endpoint to calculate Total Irrigation outputs"],
)
router.include_router(
    irrigation_controller.maximum_irrigation_shift_controller.router,
    prefix="/irrigation/maximum_irrigation_shift",
    tags=["Endpoint to calculate Maximum irrigation shift outputs"],
)
