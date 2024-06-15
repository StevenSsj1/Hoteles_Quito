from typing import List, Optional
from sqlalchemy import Column, ForeignKey, Integer, String, Table, Text, Float, Date, Boolean
from sqlalchemy.orm import declarative_base, relationship, Mapped, mapped_column

Base = declarative_base()

# Tabla intermedia para UserRoles
user_roles = Table('user_roles', Base.metadata,
    Column('usuarios_id', Integer, ForeignKey('usuarios_account.id'), primary_key=True),
    Column('role_id', Integer, ForeignKey('roles.id'), primary_key=True)
)

# Tabla intermedia para RolePermissions
role_permissions = Table('role_permissions', Base.metadata,
    Column('role_id', Integer, ForeignKey('roles.id'), primary_key=True),
    Column('permission_id', Integer, ForeignKey('permissions.id'), primary_key=True)
)

class Usuario(Base):
    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    nombre: Mapped[str] = mapped_column(String)
    apellido: Mapped[str] = mapped_column(String)
    correo: Mapped[str] = mapped_column(String, unique=True, index=True)
    telefono: Mapped[str] = mapped_column(String)
    rol: Mapped[str] = mapped_column(String)
    contrasena: Mapped[str] = mapped_column(String)
    
class Role(Base):
    __tablename__ = 'roles'

    id: Mapped[int] = mapped_column(primary_key=True)
    role_name: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    description: Mapped[Optional[str]] = mapped_column(Text)
    users: Mapped[List["Usuario"]] = relationship(
        "Usuario", secondary=user_roles, back_populates="roles"
    )
    permissions: Mapped[List["Permission"]] = relationship(
        "Permission", secondary=role_permissions, back_populates="roles"
    )

    def __repr__(self) -> str:
        return f"Role(id={self.id!r}, role_name={self.role_name!r})"

class Permission(Base):
    __tablename__ = 'permissions'

    id: Mapped[int] = mapped_column(primary_key=True)
    permission_name: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    description: Mapped[Optional[str]] = mapped_column(Text)
    roles: Mapped[List["Role"]] = relationship(
        "Role", secondary=role_permissions, back_populates="permissions"
    )

    def __repr__(self) -> str:
        return f"Permission(id={self.id!r}, permission_name={self.permission_name!r})"




 


