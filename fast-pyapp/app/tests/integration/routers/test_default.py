from fastapi.testclient import TestClient
from fastapi import status

from api.routers.v1 import default

route = default.router
client = TestClient(route)

def test_default_health():
    response = client.get('/')
    assert response.status_code == status.HTTP_200_OK, 'Problem with the TestTlient instance or the entrypoint.'
    assert response.json() == {'message':'Ok'}
