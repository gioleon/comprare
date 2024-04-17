from typing import List
from src.database import schemas, models
from src.database.repository.product import ProductRepository
from sqlalchemy.orm import Session


class ProductService:
    def __init__(self, session: Session):
        self._repository = ProductRepository(session)

    def save(self, product: schemas.ProductCreate) -> schemas.Product:
        product: models.Product = self._repository.save(product=product)

        return schemas.Product(**product.__dict__)


    def find_product_by_id_and_business_id(
        self, product_id: int, business_id: int
    ) -> schemas.Category:

        product: models.Product = self._repository.find_product_by_id_and_business_id(
            product_id, business_id)

        return schemas.Product(**product.__dict__)


    def delete(
        self, product_id: int, business_id: int
    ) -> schemas.Product:
        product = self._repository.delete(product_id, business_id)

        return schemas.Product(**product.__dict__)


    def get_all_products(self) -> List[schemas.Product]:

        products = list(map(lambda x: schemas.Product(
            **x.__dict__), self._repository.get_all_products()))

        return products
    
    
    def get_all_products_by_business_id(self, business_id: int) -> List[models.Product]:
        
        products = list(map(lambda x: schemas.Product(
            **x.__dict__), self._repository.get_all_products_by_business_id(business_id)))

        return products
