<<<<<<< Updated upstream
=======
from datetime import datetime, timedelta, timezone
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
import jwt
from jwt.exceptions import InvalidTokenError
from passlib.context import CryptContext
import jwt
from jwt.exceptions import InvalidTokenError
from datetime import datetime, timedelta
from repositories.user_repository import UserRepository
from schemas.user_schema import UserCreate, TokenData, UserInDB


# Configuración de Passlib
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Configuración de JWT
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

class UserService:
    @staticmethod
    def create_user(db: Session, user: UserCreate):
        db_user = UserRepository.get_user_by_email(db, email=user.correo)
        if db_user:
            raise ValueError("Email already registered")
        hashed_password = UserService.get_password_hash(user.contrasena)
        user.contrasena = hashed_password
        print(f"Creating user with hashed password: {hashed_password}")
        return UserRepository.create_user(db=db, user=user)

    @staticmethod
    def get_users(db: Session):
        return UserRepository.get_users(db)
        
    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        print(f"Creating user with hashed password: {hashed_password}")
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def get_password_hash(password: str) -> str:
        return pwd_context.hash(password)

    @staticmethod
    def authenticate_user(db: Session, email: str, password: str):
        user = UserRepository.get_user_by_email(db, email)
        print(f"Authenticating user with email: {email} and password: {password}")
        if not user:
            print("User not found")
            return False
        if not UserService.verify_password(password, user.contrasena):
            print("Password verification failed")
            return False
        print("User authenticated successfully")
        return user

    @staticmethod
    def create_access_token(data: dict, expires_delta: timedelta = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now() + expires_delta
        else:
            expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
    
    @staticmethod
    def get_current_user(db: Session, token: str):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            email: str = payload.get("sub")
            if email is None:
                raise credentials_exception
            token_data = TokenData(email=email)
        except InvalidTokenError:
            raise credentials_exception
        user = UserRepository.get_user_by_email(db, email=token_data.email)
        if user is None:
            raise credentials_exception
        return user
>>>>>>> Stashed changes
