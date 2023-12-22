from dataclasses import dataclass
from typing import TypedDict

from sqlalchemy import (
    Column,
    Integer,
    Float,
    PrimaryKeyConstraint,
    String,
    ARRAY,
)
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(TypedDict):
    id: float
    name: str
    email: str


@dataclass
class UserEntity(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key = True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)

    @classmethod
    def from_dict(cls, other: dict):
        return cls(
            id=other.get("id"),
            name=other["name"],
            email=other["email"],
        )

    def to_dict(self) -> User:
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
        }