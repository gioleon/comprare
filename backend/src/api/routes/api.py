from fastapi import APIRouter
from src.api.routes import category, subcategory

router = APIRouter()

router.include_router(category.router, tags=['category'])
router.include_router(subcategory.router, tags=['subcategory'])