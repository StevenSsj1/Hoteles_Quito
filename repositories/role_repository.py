from sqlalchemy.orm import Session
from sqlalchemy.future import select
import models.models_usuarios as models
import schemas.user_schema as schemas

class RoleRepository:
    @staticmethod
    async def create_role(db: Session, role: schemas.RoleCreate):
        db_role = models.Role(name=role.name, description=role.description)
        db.add(db_role)
        await db.commit()
        await db.refresh(db_role)
        return db_role

    @staticmethod
    async def get_roles(db: Session):
        result = await db.execute(select(models.Role))
        return result.scalars().all()

    @staticmethod
    async def get_role(db: Session, role_id: int):
        return await db.get(models.Role, role_id)
    
    @staticmethod
    async def delete_role(db: Session, role_id: int):
        role = await RoleRepository.get_role(db, role_id)
        if role:
            await db.delete(role)
            await db.commit()
        return role
