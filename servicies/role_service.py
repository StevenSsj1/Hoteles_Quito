from sqlalchemy.orm import Session
from repositories.role_repository import RoleRepository
from schemas.user_schema import RoleCreate

class RoleService:
    @staticmethod
    async def create_role(db: Session, role: RoleCreate):
        return await RoleRepository.create_role(db=db, role=role)

    @staticmethod
    async def get_roles(db: Session):
        return await RoleRepository.get_roles(db)

    @staticmethod
    async def get_role(db: Session, role_id: int):
        return await RoleRepository.get_role(db, role_id)
    
    @staticmethod
    async def delete_role(db: Session, role_id: int):
        return await RoleRepository.delete_role(db, role_id)
