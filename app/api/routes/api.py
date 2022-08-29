from fastapi import APIRouter

from app.api.routes import figures

router = APIRouter()
router.include_router(figures.router, tags=["figures"], prefix="/v1")
