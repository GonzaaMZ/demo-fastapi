from fastapi import FastAPI
from routes.Book import router
from routes.auth import auth_routes
from dotenv import load_dotenv

app = FastAPI()

load_dotenv()

app.include_router(router)
app.include_router(auth_routes, prefix="/auth")


