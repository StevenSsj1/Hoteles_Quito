from sqlalchemy.orm import Session
<<<<<<< Updated upstream
from repositories import role_repository
from models import models
=======
from repositories.role_repository import RoleRepository
from schemas.user_schema import RoleCreate
>>>>>>> Stashed changes

class RoleService:

    @staticmethod
    def create_role(db: Session, role_name: str, description: str):
        role = models.Role(role_name=role_name, description=description)
        return role_repository.RoleRepository.create_role(db, role)

    @staticmethod
    def get_role(db: Session, role_id: int):
        return role_repository.RoleRepository.get_role(db, role_id)
