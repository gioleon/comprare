from database import database
from fastapi import FastAPI



database.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

@app.get('/')
def hello_word():
    return {'hello world'}
