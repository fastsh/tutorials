import pytest
from fastapi import FastAPI, status
from fastapi.testclient import TestClient
from api.models.user import UserEntity
from api.repositories.UserRepository import PostgresRepository
from api.dtos.user import UserRequest, UserResponse
from api.routers.v1.users import router
from api.usecases.users import (
        UserAddUseCase, 
        UserGetUseCase,
        UserListUseCase, 
        UserDelUseCase, 
        UserUpdateUseCase
)
   
@pytest.fixture(scope="module")
def test_db():
    repo = PostgresRepository()
    yield repo.session
    repo.session.close()

def test_create_user(test_db):
    # Create a test client for the FastAPI application
    route = router.routes[0].path
    test_client=TestClient(router)
    assert test_client

    # Create a test database and session
    db = test_db
    existing_user = UserEntity(name="user", email="user@example.com")
    db.add(existing_user)
    test_db.commit()
    assert db.query(UserEntity).count() >= 1, 'Problem with connection to db'   

    # Test case 1: Create a user with a valid name and email
    user = UserRequest(name="test_user", email="test_user@example.com")
    response = test_client.post(route, json=user.dict())
    assert response.status_code == status.HTTP_200_OK, 'Problem with the TestTlient instance or the entrypoint.'
    assert response.json()["name"] == user.name
    assert response.json()["email"] == user.email