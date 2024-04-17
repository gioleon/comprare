from typing import List
from src.database import schemas, models
from src.database.repository.bussiness_category import BusinessCategoryRepository
from sqlalchemy.orm import Session


class BusinessCategoryService:
    def __init__(self, session: Session):
        self._repository = BusinessCategoryRepository(session)


    def save(self, business_category: schemas.BusinessCategoryCreate) -> schemas.BusinessCategory:
        business_category: models.BusinessCategory = self._repository.save(business_category=business_category)

        return schemas.BusinessCategory(**business_category.__dict__)


    def find_business_category_id(self, business_category_id: int) -> schemas.BusinessCategory:

        business_category: models.BusinessCategory = self._repository.find_business_category_id(
            business_category_id)

        return schemas.BusinessCategory(**business_category.__dict__)


    def delete(self, business_category_id: int) -> schemas.BusinessCategory:
        business_category = self._repository.delete(business_category_id)

        return schemas.BusinessCategory(**business_category.__dict__)


    def get_all_business_categories(self) -> List[schemas.BusinessCategory]:

        business_categories = list(map(lambda x: schemas.BusinessCategory(
             **x.__dict__), self._repository.get_all_business_categories()))

        return business_categories
