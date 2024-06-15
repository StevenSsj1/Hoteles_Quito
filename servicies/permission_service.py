from sqlalchemy.orm import Session
from repositories import permission_repository
from models import models

class PermissionService:

    @staticmethod
    def create_permission(db: Session, permission_name: str, description: str):
        permission = models.Permission(permission_name=permission_name, description=description)
        return permission_repository.PermissionRepository.create_permission(db, permission)
    

    @staticmethod
    def get_permission(db: Session, permission_id: int):
        return permission_repository.PermissionRepository.get_permission(db, permission_id)
