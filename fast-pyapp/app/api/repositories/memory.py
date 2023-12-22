from abc import ABC
from typing import Iterable
from typing import Optional

from api.models import BaseEntity
from api.repositories import BaseRepository


class MemoryRepository(BaseRepository, ABC):
    def __init__(self) -> None:
        self.data: list[BaseEntity] = []

    def get(self, id: float) -> Optional[BaseEntity]:
        return next((e for e in self.data if e.id == id), None)

    def list(self) -> Iterable[BaseEntity]:
        return self.data

    def add(self, other: BaseEntity) -> BaseEntity:
        self.data.append(other)
        return other
    
    def update(self, id: float, updated_dict: dict) -> BaseEntity:
        other = next((e for e in self.data if e.id == id), None)
        updated_dict = {**other.to_dict(), **updated_dict}
        other = other.from_dict(updated_dict)
        self.data.append(other)
        return other

    def remove(self, id: float) -> bool:
        self.data = list(filter(lambda e: e.id != id, self.data))
        return True

    def commit_close(self) -> None:
        assert self.data is not None