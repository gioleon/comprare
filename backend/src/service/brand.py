from typing import List
from src.database import schemas, models
from src.database.repository.brand import BrandRepository
from sqlalchemy.orm import Session


class BrandService:
    def __init__(self, session: Session):
        self._repository = BrandRepository(session)

    def save(self, brand: schemas.BrandCreate) -> schemas.Brand:
        brand: models.Brand = self._repository.save(brand=brand)

        return schemas.Brand(**brand.__dict__)

    def find_brand_id(self, brand_id: int) -> schemas.Brand:

        brand: models.Brand = self._repository.find_brand_by_id(
            brand_id)

        return schemas.Brand(**brand.__dict__)

    def delete(self, brand_id: int) -> schemas.Brand:
        brand = self._repository.delete(brand_id)

        return schemas.Brand(**brand.__dict__)


    def get_all_brands(self) -> List[schemas.Brand]:

        brands = list(map(lambda x: schemas.Brand(
            **x.__dict__), self._repository.get_all_brands()))

        return brands
