from database import schemas
from repository import category_repository as repository
from sqlalchemy.orm import Session

def save(db: Session, category:schemas.Category):
    repository.save(db, category)
    