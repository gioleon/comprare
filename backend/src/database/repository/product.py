from typing import List
from src.database import schemas, models
from sqlalchemy.orm import Session


class ProductRepository:

    def __init__(self, session):
        self._session : Session = session

    @property
    def session(self) -> Session:
        return self._session


    def find_product_by_id_and_business_id(self, product_id: int, business_id: int) -> models.Product:
        # Get product by id
        product = self._session.query(models.Product).filter(
            models.Product.id == product_id & 
            models.Product.business_id == business_id
        ).first()

        # If not exists raise error
        if product is None:
            raise models.NotFoundException(
                f"Product with id {product_id} not found.")
        
        # Return object if exists
        return product 


    def save(self, product: schemas.ProductCreate) -> models.Product:
        session_product: models.Product = models.Product(
            business_id = product.business_id,
            name = product.name,
            price = product.price,
            sub_category_id = product.sub_category_id,
            brand_id = product.brand_id,
            stock = product.stock,
            status = product.status,
            description = product.description
        )

        self._session.add(session_product)
        self._session.commit()
        self._session.refresh(session_product)

        return session_product


    def delete(self, product_id: int, business_id: int) -> models.Product:
        product = self.find_product_by_id_and_business_id(product_id, business_id)
        
        self._session.delete(product)
        self._session.commit()
        
        return product
        
    
    def get_all_products(self) -> List[models.Product]:
        products = self._session.query(models.Product).all()

        return products
    
    
    def get_all_products_by_business_id(self, business_id: int) -> List[models.Product]:
        
        products = self._session.query(models.Product)\
            .filter(models.Product.business_id == business_id).all()
            
        
        return products
        
        