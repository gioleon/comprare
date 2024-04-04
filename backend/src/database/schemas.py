from pydantic import BaseModel


class CategoryCreate(BaseModel):
    name: str


class Category(CategoryCreate):
    id: int
    

class SubCategoryCreate(BaseModel):
    category_id: int
    name: str


class SubCategory(SubCategoryCreate):
    id: int 
    
    

class BusinessCategoryCreate(BaseModel):
    name: str
    

class BusinessCategory(BusinessCategoryCreate):
    id: int
    
    
