from sqlalchemy.orm import Session
from models import models

class RoleRepository:

    @staticmethod
    def create_role(db: Session, role: models.Role):
        db.add(role)
        db.commit()
        db.refresh(role)
        return role

    @staticmethod
    def get_role(db: Session, role_id: int):
        return db.query(models.Role).filter(models.Role.id == role_id).first()
