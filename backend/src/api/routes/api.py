from fastapi import APIRouter
from src.api.routes import category

router = APIRouter()

router.include_router(category.router, tags=['category'])