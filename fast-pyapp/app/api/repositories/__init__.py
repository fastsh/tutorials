from abc import ABC
from abc import abstractmethod
from typing import Iterable
from typing import Optional
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from api.models import BaseEntity


class ContextManagerRepository(ABC):
    @abstractmethod
    def commit_close(self):
        ...

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs) -> None:
        self.commit_close()  
 


class BaseRepository(ContextManagerRepository, ABC):
    def __init__(self) -> None:
        self.engine: create_engine
        self.session: sessionmaker

    @abstractmethod
    def get(self, id: str) -> Optional[BaseEntity]:
        ...

    @abstractmethod
    def list(self) -> Iterable[BaseEntity]:
        ...

    @abstractmethod
    def add(self, other: BaseEntity) -> BaseEntity:
        ...

    @abstractmethod
    def remove(self, id: str) -> bool:
        ...

    @abstractmethod
    def update(self, other: BaseEntity) -> BaseEntity:
        ...

    @abstractmethod
    def commit_close(self) -> None:
        ...