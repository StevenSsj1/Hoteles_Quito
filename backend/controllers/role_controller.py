from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies import get_db
from schemas.user_schema import Role, RoleCreate
from servicies.role_service import RoleService
from typing import List

router = APIRouter()

@router.post("/roles/", response_model=Role)
def create_role(role: RoleCreate, db: Session = Depends(get_db)):
    return RoleService.create_role(db=db, role=role)

@router.get("/roles/", response_model=List[Role])
def read_roles(db: Session = Depends(get_db)):
    return RoleService.get_roles(db)
