from fastapi import FastAPI
from database import database
from database import models



database.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

@app.get('/')
def hello_word():
    return {'hello world'}
