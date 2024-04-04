from typing import List
from src.database import schemas, models
from sqlalchemy.orm import Session


class SubCategoryRepository:

    def __init__(self, session):
        self._session: Session = session

    @property
    def session(self) -> Session:
        return self._session

    def find_subcategory_by_id(self, subcategory_id: int) -> models.SubCategory:
        # Get subcategory by id
        subcategory = self._session.query(models.SubCategory).filter(
            models.SubCategory.id == subcategory_id).first()

        # If not exists raise error
        if subcategory is None:
            raise models.NotFoundException(
                f"SubCategory with id {subcategory_id} not found.")

        # Return object if exists
        return subcategory

    def save(self, subcategory: schemas.SubCategoryCreate) -> models.SubCategory:

        session_category: models.SubCategory = models.SubCategory(
            category_id=subcategory.category_id,
            name=subcategory.name
        )

        self._session.add(session_category)
        self._session.commit()
        self._session.refresh(session_category)

        return session_category

    def delete(self, subcategory_id: int) -> models.SubCategory:
        subcategory = self.find_subcategory_by_id(subcategory_id)

        self._session.delete(subcategory)
        self._session.commit()

        return subcategory

    def get_all_subcategories(self) -> List[models.SubCategory]:
        subcategories = self._session.query(models.SubCategory).all()

        return subcategories
    
    
    def get_all_subcategories_by_category_id(
        self, category_id: int
    ) -> List[models.SubCategory]:
        
        subcategories = self._session\
        .query(models.SubCategory)\
        .filter(models.SubCategory.category_id == category_id).all()
        
        if subcategories is None:
            raise models.NotFoundException(
                f"SubCategories with category_id {category_id} not found.")
        
        return subcategories
