from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controllers import hotel_controller, user_controller, role_controller

app = FastAPI()

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas las orígenes, puedes especificar una lista de orígenes específicos
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permitir todos los headers
)

app.include_router(user_controller.router, prefix="/api", tags=['users'])
app.include_router(role_controller.router, prefix="/api", tags=['rols'])
app.include_router(hotel_controller.router, prefix="/api/v1", tags=['hoteles'])


