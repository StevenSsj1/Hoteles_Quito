import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from unittest.mock import MagicMock
from ...main import app
from ...servicies.user_service import UserService

client = TestClient(app)

@pytest.fixture
def mock_db():
    return MagicMock(spec=Session)

def test_create_user(mock_db, monkeypatch):
    user_data = {
        "nombre": "Anahi",
        "apellido": "Ramirez",
        "correo": "AnaRamirez@gmail.com",
        "telefono": "094487878",
        "contrasena": "123456",
        "rol_id": 2
    }

    def mock_create_user(db: Session, user):
        return {"id":1,**user.model_dump()}

    monkeypatch.setattr(UserService, "create_user", mock_create_user)

    response = client.post("api/users/", json=user_data)

    assert response.status_code == 200
    assert response.json() == {
        "nombre": "Anahi",
        "apellido": "Ramirez",
        "correo": "AnaRamirez@gmail.com",
        "telefono": "094487878",
        "id":1,
        "rol_id": 2
    }

def test_read_users(mock_db, monkeypatch):
    users_data = [
        {"nombre": "Anahi", "apellido": "Ramirez", "correo": "AnaRamirez@gmail.com", "telefono": "094487878","id":1, "rol_id": 2},
        {"nombre": "Juan", "apellido": "Perez", "correo": "juan.perez@gmail.com", "telefono": "0987654321","id":2, "rol_id": 1}
    ]

    def mock_get_users(db: Session):
        return users_data

    monkeypatch.setattr(UserService, "get_users", mock_get_users)

    response = client.get("api/users/")

    assert response.status_code == 200
    assert response.json() == users_data

