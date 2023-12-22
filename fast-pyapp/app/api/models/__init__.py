from abc import ABCMeta
from abc import abstractmethod

from pydantic.dataclasses import dataclass

@dataclass
class BaseEntity(metaclass=ABCMeta):
    id: float
    name: str
    email: str

    @classmethod
    @abstractmethod
    def from_dict(cls, other: dict):
        ...

    @abstractmethod
    def to_dict(self):
        ...