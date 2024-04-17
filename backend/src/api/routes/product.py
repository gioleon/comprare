from fastapi import APIRouter, Depends, HTTPException
from src.service.product import ProductService
from src.database import schemas, models
from src.database.repository.product import ProductRepository
from src.database.database import get_session


router = APIRouter(
    prefix='/product'
)


@router.post('/')
def save_product(
    product: schemas.ProductCreate,
    session=Depends(get_session)
):
    return ProductService(session).save(product)


@router.get('/all/')
def get_all_products(
    session = Depends(get_session)
):
    
    return ProductService(session).get_all_products()


@router.get('/business/{business_id}')
def get_all_products_by_business_id(
  business_id: int,
  session = Depends(get_session)  
):
    try:
        products =  ProductService(session)\
        .get_all_products_by_business_id(business_id)
    except models.NotFoundException as e:
        raise HTTPException(
            status_code=404) from e
           
    return products


@router.get('/{business_id}/{product_id}')
def find_product_by_id_and_business_id(
    business_id: int,
    product_id: int,
    session=Depends(get_session)
):
    try:
        product = ProductService(session).find_product_by_id_and_business_id(product_id, business_id)

    except models.NotFoundException as e:
        raise HTTPException(
            status_code=404) from e

    return product


@router.delete('/{business_id}/{product_id}')
def delete_subcategory_by_id(
    business_id: int,
    product_id: int,
    session=Depends(get_session)
):
    try:
        product = ProductService(session).delete(product_id, business_id)
    except models.NotFoundException as e:
        raise HTTPException(status_code=404) from e
    
    return product
