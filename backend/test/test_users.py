import pytest
from unittest.mock import MagicMock
from sqlalchemy.orm import Session
from servicies.user_service import UserService
from models.models_usuarios import User

@pytest.fixture
def mock_db():
    db = MagicMock(spec=Session)
    return db

def test_get_users(mock_db):
    # Simular datos de retorno de la base de datos
    user1 = User(id=1, nombre="User 1", apellido="Vallejo", correo="Val@gmail.com", telefono="094487878", contrasena="123", rol_id=2)
    user2 = User(id=2, nombre="User 2", apellido="Vallejo", correo="Val2@gmail.com", telefono="094487878", contrasena="123", rol_id=2)
    mock_db.execute.return_value.scalars.return_value.all.return_value = [user1, user2]

    # Llamar al método que se está probando
    users = UserService.get_users(mock_db)

    # Verificar que los resultados sean correctos
    assert len(users) == 2
    assert users[0].nombre == "User 1"
    assert users[1].nombre == "User 2"
    mock_db.execute.assert_called_once()
