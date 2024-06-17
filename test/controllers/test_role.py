import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from unittest.mock import MagicMock
from ...main import app
from ...servicies.role_service import RoleService


client = TestClient(app)

@pytest.fixture
def mock_db():
    return MagicMock(spec=Session)

def test_create_role(mock_db, monkeypatch):
    role_data = {"name": "Admin", "description": "Administrator role"}
    
    def mock_create_role(db: Session, role):
        return {"id": 1, **role.model_dump()}
    
    monkeypatch.setattr(RoleService, "create_role", mock_create_role)
    
    response = client.post("api/roles/", json=role_data)
    
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Admin", "description": "Administrator role"}

def test_read_roles(mock_db, monkeypatch):
    roles_data = [{"id": 1, "name": "Admin", "description": "Administrator role"}]
    
    def mock_get_roles(db: Session):
        return roles_data
    
    monkeypatch.setattr(RoleService, "get_roles", mock_get_roles)
    
    response = client.get("api/roles/")
    
    assert response.status_code == 200
    assert response.json() == roles_data
