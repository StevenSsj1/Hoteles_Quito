from fastapi import FastAPI
from controllers import user_controller, role_controller, permission_controller,facturacion_controller
app = FastAPI()

app.include_router(user_controller.router, prefix="/api/v1")
app.include_router(role_controller.router, prefix="/api/v1")
app.include_router(permission_controller.router, prefix="/api/v1")
app.include_router(facturacion_controller.router, prefix="/api/v1")