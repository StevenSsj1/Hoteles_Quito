from sqlalchemy.orm import Session
from sqlalchemy.future import select
from schemas import Pago

class PagoRepository:

    @staticmethod
    async def get_pagos(db: Session, skip: int = 0, limit: int = 10):
        result = await db.execute(select(Pago).offset(skip).limit(limit))
        return result.scalars().all()

    @staticmethod
    async def create_pago(db: Session, pago: Pago):
        db.add(pago)
        await db.commit()
        await db.refresh(pago)
        return pago
