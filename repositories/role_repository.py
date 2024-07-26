from sqlalchemy.orm import Session
from sqlalchemy.future import select
import models.models_usuarios as models
import schemas.user_schema as schemas

class RoleRepository:
    @staticmethod
    def create_role(db: Session, role: schemas.RoleCreate):
        db_role = models.Role(name=role.name, description=role.description)
        db.add(db_role)
        db.commit()
        db.refresh(db_role)
        return db_role

    @staticmethod
    def get_roles(db: Session):
        result = db.execute(select(models.Role))
        return result.scalars().all()

    @staticmethod
    def get_role(db: Session, role_id: int):
        return db.get(models.Role, role_id)
    
    @staticmethod
    def delete_role(db: Session, role_id: int):
        role = RoleRepository.get_role(db, role_id)
        if role:
            db.delete(role)
            db.commit()
        return role
