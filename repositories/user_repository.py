from sqlalchemy.orm import Session
from sqlalchemy.future import select
import ..models.models_usuarios as models
import ..schemas.user_schema as schemas

class UserRepository:
    @staticmethod
    def create_user(db: Session, user: schemas.UserCreate):
        db_user = models.User(
            nombre=user.nombre, 
            apellido=user.apellido, 
            correo=user.correo, 
            telefono=user.telefono, 
            contrasena=user.contrasena, 
            rol_id=user.rol_id
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    @staticmethod
    def get_user(db: Session, user_id: int):
        return db.get(models.User, user_id)

    @staticmethod
    def get_user_by_email(db: Session, email: str):
        result = db.query(models.User).filter(models.User.correo == email).first()
        return result

    @staticmethod
    def get_users(db: Session):
        result = db.execute(select(models.User))
        return result.scalars().all()
    
    @staticmethod
    def delete_user(db: Session, user_id: int):
        user = UserRepository.get_user(db, user_id)
        if user:
            db.delete(user)
            db.commit()
        return user
