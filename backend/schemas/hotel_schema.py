from pydantic import BaseModel

class HotelBase(BaseModel):
    name: str
    address: str
    city: str

class HotelCreate(HotelBase):
    pass

class Hotel(HotelBase):
    id: int

    class Config:
        orm_mode = True