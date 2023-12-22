from typing import Iterable
from pydantic import BaseModel

from api.models import BaseEntity
from api.models.user import UserEntity
from api.repositories import BaseRepository
from api.usecases import BaseUseCase


def transform(origin: BaseModel) -> BaseEntity:
    return UserEntity.from_dict(origin.dict())


class UserInitUseCase(BaseUseCase):
    def __init__(self, repo: BaseRepository) -> None:
        self.repo: BaseRepository = repo

    def execute(self) :
        return self.repo


class UserListUseCase(BaseUseCase):
    def __init__(self, repo: BaseRepository) -> None:
        self.repo = repo

    def execute(self) -> Iterable[BaseEntity]:
        return self.repo.list()


class UserAddUseCase(BaseUseCase):

    def __init__(self, repo: BaseRepository) -> None:
        self.repo = repo

    def execute(self, other: BaseModel) -> BaseEntity:
        with self.repo as repo:
            return repo.add(transform(other))
        

class UserGetUseCase(BaseUseCase):

    def __init__(self, repo: BaseRepository) -> None:
        self.repo = repo

    def execute(self, id: float) -> BaseEntity:
        with self.repo as repo:
            return repo.get(id)
        
    
class UserDelUseCase(BaseUseCase):

    def __init__(self, repo: BaseRepository) -> None:
        self.repo = repo

    def execute(self, id: float) -> BaseEntity:
        with self.repo as repo:
            return repo.remove(id)
        
class UserUpdateUseCase(BaseUseCase):

    def __init__(self, repo: BaseRepository) -> None:
        self.repo = repo

    def execute(self, id: float, updated_dict: dict) -> BaseEntity:
        with self.repo as repo:
            return repo.update(id, updated_dict)