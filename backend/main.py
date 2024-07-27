from fastapi import FastAPI
from controllers import hotel_controller, user_controller, role_controller

app = FastAPI()


app.include_router(user_controller.router, prefix="/api", tags=['users'])
app.include_router(role_controller.router, prefix="/api", tags=['rols'])
app.include_router(hotel_controller.router, prefix="/api/v1", tags=['hoteles'])


