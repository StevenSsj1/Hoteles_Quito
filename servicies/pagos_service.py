from sqlalchemy.ext.asyncio import AsyncSession
from schemas import Pago
from repositories.pagos_repository import PagoRepository
from schemas import PagoCreate

class PagoService:

    @staticmethod
    async def get_pagos(db: AsyncSession, skip: int = 0, limit: int = 10):
        return await PagoRepository.get_pagos(db, skip, limit)

    @staticmethod
    async def create_pago(db: AsyncSession, pago_create: PagoCreate):
        pago = Pago(**pago_create.dict())
        return await PagoRepository.create_pago(db, pago)
