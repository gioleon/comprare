from fastapi import FastAPI
from src.database.database import engine, Base
from src.api.routes.api import router

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router)

@app.get('/')
def hello_word():
    return {'hello world'}

