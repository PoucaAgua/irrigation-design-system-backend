from fastapi import APIRouter

from app.infrastructure.api.v1.controllers import app_test_controller

router = APIRouter()


router.include_router(app_test_controller.router, prefix="/test", tags=["Endpoint Test"])