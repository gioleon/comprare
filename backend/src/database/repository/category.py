from typing import List
from src.database import schemas, models
from sqlalchemy.orm import Session


class CategoryRepository:

    def __init__(self, session):
        self._session : Session = session

    @property
    def session(self) -> Session:
        return self._session


    def find_category_by_id(self, category_id: int) -> models.Category:
        # Get category by id
        category = self._session.query(models.Category).filter(
            models.Category.id == category_id).first()

        # If not exists raise error
        if category is None:
            raise models.NotFoundException(
                f"Category with id {category_id} not found.")
        
        # Return object if exists
        return category 


    def save(self, category: schemas.CategoryCreate) -> models.Category:
        session_category: models.Category = models.Category(
            # id = category.id,
            name=category.name
        )

        self._session.add(session_category)
        self._session.commit()
        self._session.refresh(session_category)

        return session_category


    def delete(self, category_id: int) -> models.Category:
        category = self.find_category_by_id(category_id)
        
        self._session.delete(category)
        self._session.commit()
        
        return category
        
    
    def get_all_categories(self) -> List[models.Category]:
        categories = self._session.query(models.Category).all()

        return categories
        
        