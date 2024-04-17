from fastapi import APIRouter, Depends, HTTPException
from src.service.business import BusinessService
from src.database import schemas, models
from src.database.repository.business import BusinessRepository
from src.database.database import get_session


router = APIRouter(
    prefix='/business'
)


@router.post('/')
def save_business(
    business: schemas.BusinessCreate,
    session=Depends(get_session)
):
    return BusinessService(session).save(business)


@router.get('/all/')
def get_all_business(
    session = Depends(get_session)
):
    
    return BusinessService(session).get_all_business()


@router.get('/{business_id}')
def find_business_by_id(
  business_id: int,
  session = Depends(get_session)  
):
    try:
        business =  BusinessService(session)\
            .find_business_id(business_id)
    except models.NotFoundException as e:
        raise HTTPException(
            status_code=404) from e
           
    return business


@router.delete('/{business_id}')
def delete_business_by_id(
    business_id: int,
    session=Depends(get_session)
):
    try:
        business = BusinessService(session).delete(business_id)
    except models.NotFoundException as e:
        raise HTTPException(status_code=404) from e
    
    return business



def find_business_by_category_id(
    business_category_id = int,
    session = Depends(get_session)
):
    business = BusinessService(session).\
        get_all_business_by_business_category_id(business_category_id)
        
    return business