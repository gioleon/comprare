from sqlalchemy import Column, BigInteger, String, ForeignKey
from database.database import Base




class Category(Base):
    __tablename__ = 'category'
    id = Column('id', BigInteger, primary_key=True)
    name = Column('name', String, unique=True, nullable=False)
    
    
class SubCategory(Base):
    __tablename__ = 'subcategory'
    id = Column('id', BigInteger, primary_key=True)
    category_id = Column("category_id", ForeignKey("category.id"))
    name = Column('name', String, unique=True, nullable=False)
    
    