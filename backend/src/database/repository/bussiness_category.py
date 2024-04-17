from typing import List
from src.database import schemas, models
from sqlalchemy.orm import Session


class BusinessCategoryRepository:

    def __init__(self, session):
        self._session: Session = session

    @property
    def session(self) -> Session:
        return self._session

    def find_business_category_by_id(self, business_category_id: int) -> models.BusinessCategory:
        # Get business category by id
        business_category = self._session.query(models.BusinessCategory).filter(
            models.BusinessCategory.id == business_category_id).first()

        # If not exists raise error
        if business_category is None:
            raise models.NotFoundException(
                f"BusinessCategory with id {business_category_id} not found.")

        # Return object if exists
        return business_category

    def save(self, business_category: schemas.BusinessCategoryCreate) -> models.BusinessCategory:

        session_business_category: models.BusinessCategory = models.BusinessCategory(
            name=business_category.name
        )

        self._session.add(session_business_category)
        self._session.commit()
        self._session.refresh(session_business_category)

        return session_business_category

    def delete(self, business_category_id: int) -> models.BusinessCategory:
        business_category = self.find_business_category_by_id(business_category_id)

        self._session.delete(business_category)
        self._session.commit()

        return business_category

    def get_all_business_categories(self) -> List[models.BusinessCategory]:
        business_category = self._session.query(models.BusinessCategory).all()

        return business_category
    
    
    
