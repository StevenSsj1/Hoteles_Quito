from sqlalchemy import Column, Integer, String, ForeignKey, Table, Text
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

user_roles = Table('user_roles', Base.metadata,
    Column('user_id', Integer, ForeignKey('usuarios.id'), primary_key=True),
    Column('role_id', Integer, ForeignKey('roles.id'), primary_key=True)
)

class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, index=True, nullable=False)
    description = Column(Text)

class User(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255), nullable=False)
    apellido = Column(String(255), nullable=False)
    correo = Column(String(255), unique=True, index=True, nullable=False)
    telefono = Column(String(255))
    contrasena = Column(String(255), nullable=False)
    rol_id = Column(Integer, ForeignKey('roles.id'))

    rol = relationship("Role", back_populates="usuarios")

Role.usuarios = relationship("User", back_populates="rol")
