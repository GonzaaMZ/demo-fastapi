from fastapi import FastAPI
from routes.Book import router

app = FastAPI()

app.include_router(router)


