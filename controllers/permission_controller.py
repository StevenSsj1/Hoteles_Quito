from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import SessionLocal
from servicies import permission_service

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic models for request and response bodies
class PermissionCreate(BaseModel):
    permission_name: str
    description: str

@router.post("/permissions/", response_model=PermissionCreate)
def create_permission(permission: PermissionCreate, db: Session = Depends(get_db)):
    return permission_service.PermissionService.create_permission(db, permission.permission_name, permission.description)
