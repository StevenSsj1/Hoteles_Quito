from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas import Reserva, ReservaCreate
from servicies.reserva_service import ReservaService
from database import SessionLocal

router = APIRouter()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@router.get("/reservas/", response_model=list[Reserva])
async def read_reservas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return await ReservaService.get_reservas(db, skip, limit)

@router.post("/reservas/", response_model=Reserva)
async def create_reserva(reserva: ReservaCreate, db: Session = Depends(get_db)):
    return await ReservaService.create_reserva(db, reserva)
