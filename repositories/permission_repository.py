from sqlalchemy.orm import Session
from models import models

class PermissionRepository:

    @staticmethod
    def create_permission(db: Session, permission: models.Permission):
        db.add(permission)
        db.commit()
        db.refresh(permission)
        return permission

    @staticmethod
    def get_permission(db: Session, permission_id: int):
        return db.query(models.Permission).filter(models.Permission.id == permission_id).first()
