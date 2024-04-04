from typing import List
from src.database import schemas, models
from src.database.repository.subcategory import SubCategoryRepository
from sqlalchemy.orm import Session


class SubCategoryService:
    def __init__(self, session: Session):
        self._repository = SubCategoryRepository(session)


    def save(self, subcategory: schemas.SubCategoryCreate) -> schemas.SubCategory:
        subcategory: models.SubCategory = self._repository.save(subcategory=subcategory)

        return schemas.SubCategory(**subcategory.__dict__)


    def find_by_subcategory_id(self, subcategory_id: int) -> schemas.SubCategory:

        subcategory: models.SubCategory = self._repository.find_subcategory_by_id(
            subcategory_id)

        return schemas.SubCategory(**subcategory.__dict__)


    def delete(self, subcategory_id: int) -> schemas.SubCategory:
        subcategory = self._repository.delete(subcategory_id)

        return schemas.SubCategory(**subcategory.__dict__)


    def get_all_subcategories(self) -> List[schemas.SubCategory]:

        subcategories = list(map(lambda x: schemas.SubCategory(
             **x.__dict__), self._repository.get_all_subcategories()))

        return subcategories
    
    
    def get_all_subcategories_by_category_id(
        self, category_id: int
    ) -> List[schemas.SubCategory]:

        subcategories = list(map(lambda x: schemas.SubCategory(
             **x.__dict__), self._repository.get_all_subcategories_by_category_id(category_id)))

        return subcategories
