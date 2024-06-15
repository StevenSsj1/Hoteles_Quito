from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas import Facturacion, FacturacionCreate
from servicies.facturacion_service import FacturacionService
from database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/facturaciones/", response_model=list[Facturacion])
async def read_facturaciones(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return await FacturacionService.get_facturaciones(db, skip, limit)

@router.post("/facturaciones/", response_model=Facturacion)
async def create_facturacion(facturacion: FacturacionCreate, db: Session = Depends(get_db)):
    return await FacturacionService.create_facturacion(db, facturacion)
