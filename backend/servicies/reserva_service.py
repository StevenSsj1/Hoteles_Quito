from sqlalchemy.ext.asyncio import AsyncSession
from schemas import Reserva
from repositories.reservas_repository import ReservaRepository
from schemas import ReservaCreate

class ReservaService:

    @staticmethod
    async def get_reservas(db: AsyncSession, skip: int = 0, limit: int = 10):
        return await ReservaRepository.get_reservas(db, skip, limit)

    @staticmethod
    async def create_reserva(db: AsyncSession, reserva_create: ReservaCreate):
        reserva = Reserva(**reserva_create.dict())
        return await ReservaRepository.create_reserva(db, reserva)
