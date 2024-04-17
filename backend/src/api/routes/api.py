from fastapi import APIRouter
from src.api.routes import category, subcategory, business_category, business, brand, product

router = APIRouter()

router.include_router(category.router, tags=['category'])
router.include_router(subcategory.router, tags=['subcategory'])
router.include_router(business_category.router, tags=['business_category'])
router.include_router(business.router, tags=['business'])
router.include_router(brand.router, tags=['brand'])
router.include_router(product.router, tags=['product'])