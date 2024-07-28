from sqlalchemy.orm import Session
from models.models_hoteles import Hotel
#from schemas.hotel_schema import HotelCreate
import schemas.hotel_schema as schemas

class HotelRepository:

    @staticmethod
    def get_hotel(db: Session, hotel_id: int):
        return db.query(Hotel).filter(Hotel.id == hotel_id).first()


    @staticmethod
    def create_hotel(db: Session, hotel: schemas.HotelCreate):
        db_hotel = Hotel(name=hotel.name, address=hotel.address, city=hotel.city)
        db.add(db_hotel)
        db.commit()
        db.refresh(db_hotel)
        return db_hotel
    
 