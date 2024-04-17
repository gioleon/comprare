from typing import List
from src.database import schemas, models
from src.database.repository.business import BusinessRepository
from sqlalchemy.orm import Session


class BusinessService:
    def __init__(self, session: Session):
        self._repository = BusinessRepository(session)


    def save(self, business: schemas.BusinessCreate) -> schemas.BusinessCategory:
        business: models.Business = self._repository.save(business=business)

        return schemas.Business(**business.__dict__)


    def find_business_id(self, business_id: int) -> schemas.Business:

        business: models.Business = self._repository\
            .find_business_by_id(
                business_id
            )

        return schemas.Business(**business.__dict__)


    def delete(self, business_id: int) -> schemas.Business:
        business = self._repository.delete(business_id)

        return schemas.Business(**business.__dict__)


    def get_all_business(self) -> List[schemas.Business]:

        business = list(map(lambda x: schemas.Business(
             **x.__dict__), self._repository.get_all_business()))

        return business


    def get_all_business_by_business_category_id(
        self, 
        business_category_id: int
    ) -> schemas.Business:
        business = self._repository\
            .get_business_by_business_category_id(business_category_id)
            
        return business
