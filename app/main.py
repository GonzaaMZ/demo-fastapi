from fastapi import FastAPI
from routes.Book import router
from routes.auth import auth_routes
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

security = [{"Bearer": []}]

app = FastAPI(openapi_security=security)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes especificar los dominios permitidos en lugar de "*" para mayor seguridad
    allow_credentials=True,
    allow_methods=["*"],  # Puedes especificar los métodos HTTP permitidos (GET, POST, etc.)
    allow_headers=["*"],  # Puedes especificar los encabezados permitidos
)

load_dotenv()

app.include_router(router)
app.include_router(auth_routes, prefix="/auth")


