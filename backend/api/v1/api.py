from fastapi import APIRouter

from .routes import health_router, income_router

api_router = APIRouter()

api_router.include_router(health_router)
api_router.include_router(income_router)
