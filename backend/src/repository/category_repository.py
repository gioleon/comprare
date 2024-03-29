from database import schemas, models
from sqlalchemy.orm import Session


def save(db: Session, category: schemas.Category) -> None:
    db_category: models.Category = models.Category( 
        # id = category.id, 
        name = category.name
    )
    
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
