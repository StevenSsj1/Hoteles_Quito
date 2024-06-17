from sqlalchemy.orm import Session
from ..schemas.hotel_schema import HotelCreate
from ..repositories.hotel_repository import HotelRepository


class HotelService:
    @staticmethod
    def get_hotel(db: Session, hotel_id: int):
        return HotelRepository.get_hotel(db, hotel_id)

    @staticmethod
    def create_hotel(db: Session, hotel: HotelCreate):
        return HotelRepository.create_hotel(db, hotel)