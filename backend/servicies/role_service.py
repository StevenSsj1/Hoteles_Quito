from sqlalchemy.orm import Session
from repositories.role_repository import RoleRepository
from schemas.user_schema import RoleCreate

class RoleService:
    @staticmethod
    def create_role(db: Session, role: RoleCreate):
        return RoleRepository.create_role(db=db, role=role)

    @staticmethod
    def get_roles(db: Session):
        return RoleRepository.get_roles(db)

    @staticmethod
    def get_role(db: Session, role_id: int):
        return RoleRepository.get_role(db, role_id)
    
    @staticmethod
    def delete_role(db: Session, role_id: int):
        return RoleRepository.delete_role(db, role_id)
