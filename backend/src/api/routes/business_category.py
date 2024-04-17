from fastapi import APIRouter, Depends, HTTPException
from src.service.business_category import BusinessCategoryService
from src.database import schemas, models
from src.database.repository.bussiness_category import BusinessCategoryRepository
from src.database.database import get_session


router = APIRouter(
    prefix='/businessCategory'
)


@router.post('/')
def save_business_category(
    business_category: schemas.BusinessCategoryCreate,
    session=Depends(get_session)
):
    return BusinessCategoryService(session).save(business_category)


@router.get('/all/')
def get_all_business_categories(
    session = Depends(get_session)
):
    
    return BusinessCategoryService(session).get_all_business_categories()


@router.get('/{business_category}')
def find_business_category_by_id(
  business_category_id: int,
  session = Depends(get_session)  
):
    try:
        business_category =  BusinessCategoryService(session)\
            .find_business_category_id(business_category_id)
    except models.NotFoundException as e:
        raise HTTPException(
            status_code=404) from e
           
    return business_category



@router.delete('/{business_category_id}')
def delete_business_category_by_id(
    business_category_id: int,
    session=Depends(get_session)
):
    try:
        business_category = BusinessCategoryService(session).delete(business_category_id)
    except models.NotFoundException as e:
        raise HTTPException(status_code=404) from e
    
    return business_category
