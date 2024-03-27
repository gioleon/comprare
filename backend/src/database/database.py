from sqlalchemy import create_engine 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database

from config.config import ConfigClass

# Database URL
URL = ConfigClass.SQLALCHEMY_DATABASE_URL

# Create engine to interact with database
# And engine is the entry point used to interact with database.
engine = create_engine(
    url=URL,
    pool_size=5, # Number of connections in the pool of connections. 0 = no limit.
    pool_recycle=3600, # Connections Inactive for 1 hour will be closed, but, they can be reused.
    echo=True # To see logs
)

# If database does not exist, It will create it.
if not database_exists(url=engine.url):
    create_database(url=engine.url)

# Create the session.
# Session is the actual object we use to interact with the ORM.
# ORM helps us to convert python objects to dabatabase objects
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base() # It configures our python classes with Table and mapper attributes