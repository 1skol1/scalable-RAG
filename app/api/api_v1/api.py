from fastapi import APIRouter

from .routes import predictor

router = APIRouter()
router.include_router(predictor.router, tags=["predict"],prefix="/v1")



