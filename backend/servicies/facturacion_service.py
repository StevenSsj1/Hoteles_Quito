from sqlalchemy.ext.asyncio import AsyncSession
from schemas import Facturacion
from repositories.facturacion_repository import FacturacionRepository
from schemas import FacturacionCreate

class FacturacionService:

    @staticmethod
    async def get_facturaciones(db: AsyncSession, skip: int = 0, limit: int = 10):
        return await FacturacionRepository.get_facturaciones(db, skip, limit)

    @staticmethod
    async def create_facturacion(db: AsyncSession, facturacion_create: FacturacionCreate):
        facturacion = Facturacion(**facturacion_create.dict())
        return await FacturacionRepository.create_facturacion(db, facturacion)
