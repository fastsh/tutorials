from typing import List, Union, Optional
from fastapi import APIRouter, HTTPException
from sqlalchemy.exc import IntegrityError
from pydantic import ValidationError

from api.repositories.UserRepository import PostgresRepository
from api.dtos.user import UserRequest, UserResponse
from api.usecases.users import (
        UserAddUseCase, 
        UserGetUseCase,
        UserListUseCase, 
        UserDelUseCase, 
        UserUpdateUseCase
)

INVALID_USER_ID_ERROR = "Invalid user ID"
router = APIRouter(
        prefix="/users",
        tags=["users"]
)
repo = PostgresRepository()

@router.post("/")
async def create_user(user: UserRequest) -> Union[UserResponse, dict]:
    if not user:
        raise HTTPException(status_code=400, detail="Invalid user object")
    try:
        user_ = UserAddUseCase(repo).execute(user)

    except IntegrityError as err:
        repo.session.rollback()
        if "duplicate key value violates unique constraint" in str(err):
            raise HTTPException(status_code=409, detail=f"The user with email {user.email} already exists")
        else:
            raise HTTPException(status_code=500, detail=f"{err}")
        
    except ValidationError as err:
        raise HTTPException(status_code=422, detail=f"{err}")
         
    return UserResponse.from_orm(user_)

@router.get("/{user_id}")
async def get_user(user_id: float = 0) -> Union[UserResponse, dict]:
    if user_id <= 0:
        raise HTTPException(status_code=400, detail=INVALID_USER_ID_ERROR)
    try:   
        user_ = UserGetUseCase(repo).execute(user_id)
        if user_ is None:
            raise HTTPException(status_code=404, detail="User not found")
           
    except ValidationError as err:
        raise HTTPException(status_code=422, detail=f"{err}")
    
    return UserResponse.from_orm(user_)

@router.delete("/{user_id}")
async def remove_user(user_id: float = 0.) -> dict:
    if user_id <= 0:
        raise HTTPException(status_code=400, detail=INVALID_USER_ID_ERROR)
    try:
        ok = UserDelUseCase(repo).execute(user_id)
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"{err}")
    
    return {'delete methode': f"{ok}"}
    
@router.get("/")
async def list_users()-> List[Optional[UserResponse]]:
    try:
        users = UserListUseCase(repo).execute()
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"{err}")
    
    return [UserResponse.from_orm(user) for user in users]

@router.put("/{user_id}")
async def update_user(user_id: float, user: UserRequest) -> Union[UserResponse, dict]:
    if user_id <= 0:
        raise HTTPException(status_code=400, detail=INVALID_USER_ID_ERROR)
    try:
        user_ = UserUpdateUseCase(repo).execute(user_id, user.dict())
    except ValidationError as err:
        raise HTTPException(status_code=422, detail=f"{err}")
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"{err}")
    return UserResponse.from_orm(user_)

@router.patch("/{user_id}")
async def partial_update_user(user_id: float = 0., updated_dict: dict = {'name': 'New user Name is updated!'}):
    if user_id <= 0:
        raise HTTPException(status_code=400, detail=INVALID_USER_ID_ERROR)
    try:
        user_ = UserUpdateUseCase(repo).execute(user_id, updated_dict)

    except ValidationError as err:
        raise HTTPException(status_code=422, detail=f"{err}")
    
    return UserResponse.from_orm(user_)
