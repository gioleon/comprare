from typing import List
from fastapi import APIRouter, Depends, HTTPException
from src.service.brand import BrandService
from src.database import schemas, models
from src.database.repository.brand import BrandRepository
from src.database.database import get_session


router = APIRouter(
    prefix='/brand'
)


@router.post('/')
def save_brand(
    brand: schemas.BrandCreate,
    session=Depends(get_session)
):
    return BrandService(session).save(brand)


@router.get('/all/')
def get_all_brands(
    session = Depends(get_session)
):
    
    return BrandService(session).get_all_brands()


@router.get('/{brand_id}')
def find_brand_by_id(
    brand_id: int,
    session=Depends(get_session)
):
    try:
        brand = BrandService(session).find_brand_id(brand_id)

    except models.NotFoundException as e:
        raise HTTPException(
            status_code=404) from e

    return brand


@router.delete('/{brand_id}')
def delete_brand_by_id(
    brand_id: int,
    session=Depends(get_session)
):
    try:
        brand = BrandService(session).delete(brand_id)
    except models.NotFoundException as e:
        raise HTTPException(status_code=404) from e
    
    return brand
