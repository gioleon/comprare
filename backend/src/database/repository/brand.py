from typing import List
from src.database import schemas, models
from sqlalchemy.orm import Session


class BrandRepository:

    def __init__(self, session):
        self._session : Session = session

    @property
    def session(self) -> Session:
        return self._session


    def find_brand_by_id(self, brand_id: int) -> models.Brand:
        # Get Brand by id
        brand = self._session.query(models.Brand).filter(
            models.Brand.id == brand_id).first()

        # If not exists raise error
        if brand is None:
            raise models.NotFoundException(
                f"Brand with id {brand_id} not found.")
        
        # Return object if exists
        return brand 


    def save(self, brand: schemas.BrandCreate) -> models.Brand:
        session_brand: models.Brand = models.Brand(
            name=brand.name
        )

        self._session.add(session_brand)
        self._session.commit()
        self._session.refresh(session_brand)

        return session_brand


    def delete(self, brand_id: int) -> models.Brand:
        brand = self.find_brand_by_id(brand_id)
        
        self._session.delete(brand)
        self._session.commit()
        
        return brand
        
    
    def get_all_brands(self) -> List[models.Brand]:
        brand = self._session.query(models.Brand).all()

        return brand
        
        