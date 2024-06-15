from sqlalchemy.orm import Session
from sqlalchemy.future import select
from schemas import Facturacion

class FacturacionRepository:

    @staticmethod
    async def get_facturaciones(db: Session, skip: int = 0, limit: int = 10):
        result = await db.execute(select(Facturacion).offset(skip).limit(limit))
        return result.scalars().all()

    @staticmethod
    async def create_facturacion(db: Session, facturacion: Facturacion):
        db.add(facturacion)
        await db.commit()
        await db.refresh(facturacion)
        return facturacion
