"""
Tests para los endpoints
"""
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

class TestReadRoot:
    """Esta clase testea el endpoint raíz"""

    def test_read_root_returns_200(self):
        """Endpoint raíz debe devolver 200"""
        response = client.get("/")
        assert response.status_code == 200

    def test_read_root_returns_message(self):
        """Endpoint raíz devuelve el nombre del framework"""
        response = client.get("/")
        data = response.json()
        assert "message" in data
        assert "FastAPI" in data["message"]

class TestHealthCheck:
    """Tests para el endpoint de health_check"""

    def test_health_heck_returns_200(self):
        """Endpoint heal check devuelve 200"""
        response = client.get("/health")
        assert response.status_code == 200

    def test_health_check_is_healthy(self):
        """Endpoint health debe devolver status healthy"""
        response = client.get("/health")
        assert "status" in response.json()
        assert response.json()["status"] == "healthy"

class TestSuma:
    """Tests para el endpoint de sumar"""
    
    def test_suma_positivos(self):
        """Dos números positivos"""
        response = client.get("/suma/5/6")
        data = response.json()
        assert response.status_code == 200
        assert data["resultado"] == 11

    def test_suma_negativos(self):
        """Dos números negativos"""
        response = client.get("/suma/-3/-6")
        data = response.json()
        assert data["resultado"] == -9

    def test_suma_mixtos(self):
        """Dos números mixtos"""
        response = client.get("/suma/-5/2")
        data = response.json()
        assert data["resultado"] == -3

    def test_suma_con_cero(self):
        """Dos números con 0"""
        response = client.get("/suma/0/6")
        data = response.json()
        assert data["resultado"] == 6