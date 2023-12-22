from pydantic import BaseModel, EmailStr, Field


class UserRequest(BaseModel):
    name: str = Field(min_length=3, max_length=64)
    email: EmailStr


class UserResponse(BaseModel):
    id: float
    name: str = Field(min_length=3, max_length=64)
    email: EmailStr

    class Config:
        orm_mode = True
        allow_population_by_field_name = True