from typing import List
from fastapi import APIRouter, Depends, HTTPException
from src.service.category import CategoryService
from src.database import schemas, models
from src.database.repository.category import CategoryRepository
from src.database.database import get_session


router = APIRouter(
    prefix='/category'
)


@router.post('/')
def save_category(
    category: schemas.CategoryCreate,
    session=Depends(get_session)
):
    return CategoryService(session).save(category)


@router.get('/all/')
def get_all_categories(
    session = Depends(get_session)
):
    
    return CategoryService(session).get_all_categories()


@router.get('/{category_id}')
def find_category_by_id(
    category_id: int,
    session=Depends(get_session)
):
    try:
        category = CategoryService(session).find_by_category_id(category_id)

    except models.NotFoundException as e:
        raise HTTPException(
            status_code=404) from e

    return category


@router.delete('/{category_id}')
def delete_category_by_id(
    category_id: int,
    session=Depends(get_session)
):
    try:
        category = CategoryService(session).delete(category_id)
    except models.NotFoundException as e:
        raise HTTPException(status_code=404) from e
    
    return category
