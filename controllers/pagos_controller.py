from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas import Pago, PagoCreate
from servicies.pagos_service import PagoService
from database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/pagos/", response_model=list[Pago])
async def read_pagos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return await PagoService.get_pagos(db, skip, limit)

@router.post("/pagos/", response_model=Pago)
async def create_pago(pago: PagoCreate, db: Session = Depends(get_db)):
    return await PagoService.create_pago(db, pago)
