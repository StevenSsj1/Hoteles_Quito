from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import SessionLocal
from servicies import role_service

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic models for request and response bodies
class RoleCreate(BaseModel):
    role_name: str
    description: str

@router.post("/roles/", response_model=RoleCreate)
def create_role(role: RoleCreate, db: Session = Depends(get_db)):
    return role_service.RoleService.create_role(db, role.role_name, role.description)
