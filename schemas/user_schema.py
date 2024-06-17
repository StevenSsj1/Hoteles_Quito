from pydantic import BaseModel
from typing import List, Optional

class UserBase(BaseModel):
    nombre: str
    apellido: str
    correo: str
    telefono: Optional[str] = None

class UserCreate(UserBase):
    contrasena: str
    rol_id: int

class User(UserBase):
    id: int
    rol_id: int

    class Config:
        orm_mode = True

class RoleBase(BaseModel):
    name: str
    description: Optional[str] = None

class RoleCreate(RoleBase):
    pass

class Role(RoleBase):
    id: int

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

class UserInDB(User):
    hashed_password: str
