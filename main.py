from fastapi import FastAPI
<<<<<<< Updated upstream
from controllers import user_controller, role_controller, permission_controller,facturacion_controller
=======
from controllers import user_controller, role_controller, permission_controller,reserva_controller, facturacion_controller, pagos_controller
>>>>>>> Stashed changes
app = FastAPI()

app.include_router(user_controller.router, prefix="/api/v1")
app.include_router(role_controller.router, prefix="/api/v1")
app.include_router(permission_controller.router, prefix="/api/v1")
<<<<<<< Updated upstream
app.include_router(facturacion_controller.router, prefix="/api/v1")
=======
app.include_router(reserva_controller.router, prefix="/api/v1")
app.include_router(facturacion_controller.router, prefix="/api/v1")
app.include_router(pagos_controller.router, prefix="/api/v1")
>>>>>>> Stashed changes
