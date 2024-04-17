from typing import List
from src.database import schemas, models
from src.database.repository.category import CategoryRepository
from sqlalchemy.orm import Session


class CategoryService:
    def __init__(self, session: Session):
        self._repository = CategoryRepository(session)

    def save(self, category: schemas.CategoryCreate) -> schemas.Category:
        category: models.Category = self._repository.save(category=category)

        return schemas.Category(**category.__dict__)

    def find_category_id(self, category_id: int) -> schemas.Category:

        category: models.Category = self._repository.find_category_by_id(
            category_id)

        return schemas.Category(**category.__dict__)

    def delete(self, category_id: int) -> schemas.Category:
        category = self._repository.delete(category_id)

        return schemas.Category(**category.__dict__)


    def get_all_categories(self) -> List[schemas.Category]:

        categories = list(map(lambda x: schemas.Category(
            **x.__dict__), self._repository.get_all_categories()))

        return categories
