from pydantic import BaseModel
from src.database import models


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
    

class BusinessCreate(BaseModel):
    name: str
    direction: str
    description: str
    business_category_id: int
    email: str
    password: str
    


class Business(BusinessCreate):
    id: int
    


class BrandCreate(BaseModel):
    name: str
    

class Brand(BrandCreate):
    id: int
    


class ProductCreate(BaseModel):
    business_id: int
    name: str
    price: float
    sub_category_id: int
    brand_id: int
    stock: int
    status: models.ProductStatus
    description: str
    

class Product(ProductCreate):
    id: int
    
