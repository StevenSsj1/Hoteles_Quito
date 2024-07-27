from sqlalchemy.orm import Session
from sqlalchemy.future import select
from schemas import Reserva

class ReservaRepository:

    @staticmethod
    async def get_reservas(db: Session, skip: int = 0, limit: int = 10):
        result = await db.execute(select(Reserva).offset(skip).limit(limit))
        return result.scalars().all()

    @staticmethod
    async def create_reserva(db: Session, reserva: Reserva):
        db.add(reserva)
        await db.commit()
        await db.refresh(reserva)
        return reserva
