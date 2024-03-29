from fastapi import FastAPI
from database import database
from database import models
from database import schemas
from service import category_service as service

database.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

@app.get('/')
def hello_word():
    return {'hello world'}


@app.post('/category')
def save_category(category : schemas.Category):
    service.save(database.SessionLocal(), category) 
    return {'sucess': 200}

