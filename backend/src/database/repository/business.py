from typing import List
from src.database import schemas, models
from sqlalchemy.orm import Session


class BusinessRepository:


    def __init__(self, session):
        self._session: Session = session


    @property
    def session(self) -> Session:
        return self._session


    def find_business_by_id(self, business_id: int) -> models.Business:
        # Get business by id
        business = self._session.query(models.Business).filter(
            models.Business.id == business_id).first()

        # If not exists raise error
        if business is None:
            raise models.NotFoundException(
                f"Business with id {business_id} not found.")

        # Return object if exists
        return business


    def save(self, business: schemas.BusinessCreate) -> models.Business:

        business: models.Business = models.Business(
            name = business.name,
            direction = business.direction,
            description = business.description,
            email = business.email, 
            password = business.password,
            business_category_id = business.business_category_id
            
        )

        self._session.add(business)
        self._session.commit()
        self._session.refresh(business)

        return business


    def delete(self, business_id: int) -> models.Business:
        business = self.find_business_by_id(business_id)

        self._session.delete(business)
        self._session.commit()

        return business


    def get_all_business(self) -> List[models.Business]:
        business = self._session.query(models.Business).all()

        return business
    
    
    def get_business_by_business_category_id(
        self, 
        business_category_id: int
    ) -> List[models.Business]:
        
        business = self._session.query(models.Business)\
            .filter(models.Business == business_category_id)\
            .all()
            
        return business
    
    
    
