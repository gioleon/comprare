from fastapi import APIRouter, Depends, HTTPException
from src.service.subcategory import SubCategoryService
from src.database import schemas, models
from src.database.repository.subcategory import SubCategoryRepository
from src.database.database import get_session


router = APIRouter(
    prefix='/subcategory'
)


@router.post('/')
def save_subcategory(
    subcategory: schemas.SubCategoryCreate,
    session=Depends(get_session)
):
    return SubCategoryService(session).save(subcategory)


@router.get('/all/')
def get_all_subcategories(
    session = Depends(get_session)
):
    
    return SubCategoryService(session).get_all_subcategories()


@router.get('/category/{category_id}')
def get_all_subcategories_by_category_id(
  category_id: int,
  session = Depends(get_session)  
):
    try:
        subcategories =  SubCategoryService(session)\
        .get_all_subcategories_by_category_id(category_id)
    except models.NotFoundException as e:
        raise HTTPException(
            status_code=404) from e
           
    return subcategories


@router.get('/{subcategory_id}')
def find_subcategory_by_id(
    subcategory_id: int,
    session=Depends(get_session)
):
    try:
        subcategory = SubCategoryService(session).find_subcategory_id(subcategory_id)

    except models.NotFoundException as e:
        raise HTTPException(
            status_code=404) from e

    return subcategory


@router.delete('/{subcategory_id}')
def delete_subcategory_by_id(
    subcategory_id: int,
    session=Depends(get_session)
):
    try:
        subcategory = SubCategoryService(session).delete(subcategory_id)
    except models.NotFoundException as e:
        raise HTTPException(status_code=404) from e
    
    return subcategory
