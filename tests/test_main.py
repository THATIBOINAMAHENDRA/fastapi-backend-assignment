from fastapi.testclient import TestClient
from app.main import app
from app.database import Base, engine

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

client = TestClient(app)

def test_create_property():
    response = client.post(
        "/properties",
        json={
            "id": "AV1001",
            "customer_name": "Ravi Kumar",
            "customer_mobile": "9876543210",
            "property_name": "Serene Grand",
            "property_type": "APARTMENT",
            "status": "NEW"
        }
    )
    assert response.status_code == 201
    assert response.json()["customer_name"] == "Ravi Kumar"

def test_create_duplicate_id():
    response = client.post(
        "/properties",
        json={"id": "AV1001", "customer_name": "Test", "customer_mobile": "1234567890", "property_name": "Test", "property_type": "APT", "status": "NEW"}
    )
    assert response.status_code == 400

def test_get_existing_record():
    response = client.get("/properties/AV1001")
    assert response.status_code == 200

def test_get_nonexistent_record():
    response = client.get("/properties/INVALID99")
    assert response.status_code == 404

def test_invalid_mobile_validation():
    response = client.post(
        "/properties",
        json={"id": "AV1002", "customer_name": "Test", "customer_mobile": "123", "property_name": "Test", "property_type": "APT", "status": "NEW"}
    )
    assert response.status_code == 422 

def test_delete_record():
    response = client.delete("/properties/AV1001")
    assert response.status_code == 204
    assert client.get("/properties/AV1001").status_code == 404