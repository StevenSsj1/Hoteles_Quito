from fastapi.testclient import TestClient
import sys
import os


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/api/users/")
    assert response.status_code == 200
   
