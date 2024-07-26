from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies import get_db
from schemas.hotel_schema import Hotel, HotelCreate
from servicies.hotel_service import HotelService

router = APIRouter()

@router.post("/hotels/", response_model=Hotel)
def create_hotel(hotel: HotelCreate, db: Session = Depends(get_db)):
    return HotelService.create_hotel(db=db, hotel=hotel)

@router.get("/hotels/{hotel_id}", response_model=Hotel)
def read_hotel(hotel_id: int, db: Session = Depends(get_db)):
    db_hotel = HotelService.get_hotel(db, hotel_id=hotel_id)
    if db_hotel is None:
        raise HTTPException(status_code=404, detail="Hotel not found")
    return db_hotel
