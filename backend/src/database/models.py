import enum
from sqlalchemy.sql import func
from sqlalchemy import Column, BigInteger, String, ForeignKey, Float, Enum, DateTime, Integer
from sqlalchemy_utils import force_auto_coercion
from src.database.database import Base


force_auto_coercion()


class NotFoundException(Exception):
    pass


class Owner(Base):
    __tablename__ = 'owner'
    id = Column('id', BigInteger, primary_key=True)
    name = Column('name', String, unique=False, nullable=False)
    identification_number = Column('identification_number', String, nullable=False, unique=True)
    email = Column('email', String, unique=True, nullable=False)
    password = Column('password', String(255), unique=False, nullable=False)


class BusinessCategory(Base):
    __tablename__ = 'business_category'
    id = Column('id', BigInteger, primary_key=True)
    name = Column('name', String, unique=True, nullable=False)


class Business(Base):
    __tablename__ = 'business'
    id = Column('id', BigInteger, primary_key=True)
    name = Column('name', String, unique=False, nullable=False)
    direction = Column('direction', String, nullable=False, unique=False)
    description = Column('description', String, nullable=False)
    business_category_id = Column('business_category_id', ForeignKey('business_category.id'))
    email = Column('email', String, unique=True, nullable=False)
    password = Column('password', String(255), unique=False, nullable=False)


class Category(Base):
    __tablename__ = 'category'
    id = Column('id', BigInteger, primary_key=True)
    name = Column('name', String, unique=True, nullable=False)
    
    
class SubCategory(Base):
    __tablename__ = 'sub_category'
    id = Column('id', BigInteger, primary_key=True)
    category_id = Column("category_id", ForeignKey("category.id"))
    name = Column('name', String, unique=True, nullable=False)
    

class Brand(Base):
    __tablename__ = 'brand'
    id = Column('id', BigInteger, primary_key=True)
    name = Column('name', String, unique=True, nullable=False)

    
class ProductStatus(enum.Enum):
    active = 'active'
    inactive = 'inactive'
    pending = 'pending'    

    
class Product(Base):
    __tablename__ = 'product'
    id = Column('id', BigInteger, primary_key=True)
    business_id = Column('business_id', ForeignKey('business.id'))
    name = Column('name', String, unique=True, nullable=False)
    price = Column('price', Float, nullable=False, unique=False)
    sub_category_id = Column('sub_category_id', ForeignKey('sub_category.id'))
    brand_id = Column('brand_id', ForeignKey('brand.id'))
    stock = Column('stock', BigInteger, nullable=False, unique=False)
    status = Column('state', Enum(ProductStatus))
    description = Column('description', String, unique=False, nullable=False)
    
    
class BusinessStaffRole(enum.Enum):
    owner = 'owner'
    supervisor = 'supervisor'
    worker = 'worker'

    
class BusinessStaff(Base):
    __tablename__ = 'business_staff'
    id = Column('id', BigInteger, primary_key=True)
    name = Column('name', String, unique=False, nullable=False)
    identification_number = Column('identification_number', String, nullable=False, unique=True)
    email = Column('email', String, unique=True, nullable=False)
    password = Column('password', String(255), unique=False, nullable=False)
    role = Column('role', Enum(BusinessStaffRole))
    
    
class Customer(Base):
    __tablename__ = 'customer'
    id = Column('id', BigInteger, primary_key=True)
    name = Column('name', String, unique=False, nullable=False)
    identification_number = Column('identification_number', String, nullable=False, unique=True)
    email = Column('email', String, unique=True, nullable=False)
    password = Column('password', String(255), unique=False, nullable=False)
    
    
class PaymentMethod(enum.Enum):
    cash = 'cash'
    card = 'card' 
    

class TransactionStatus(enum.Enum):
    completed = 'completed'
    pending = 'pending'
    canceled = 'canceled'    

    
class Transaction(Base):
    __tablename__ = 'transaction'
    id = Column('id', BigInteger, primary_key=True)
    customer_id = Column('customer_id', ForeignKey('customer.id'))
    business_id = Column('business_id', ForeignKey('business.id'))
    transaction_date = Column(
        'transaction_date', 
        DateTime,
        nullable=False,
        unique=False,
        server_default=func.now()
    )
    total_amount = Column('total_amount', Float, unique=False, nullable=False)
    payment_method = Column('payment_method', Enum(PaymentMethod), nullable=False, unique=False)
    status = Column('status', Enum(TransactionStatus), unique=False, nullable=False)
    

class TransactionDetails(Base):
    __tablename__ = 'transaction_details'
    id = Column('id', BigInteger, primary_key=True)
    transaction_id = Column('transaction_id', ForeignKey('transaction.id'))
    product_id = Column('product_id', ForeignKey('product.id'))
    quantity = Column('quantity', Integer, unique=False, nullable=False)
    unit_price = Column('unit_price', Float, unique=False, nullable=False)
    discount = Column('discount', Float, unique=False, nullable=False)
    