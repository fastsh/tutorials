from abc import ABCMeta
from abc import abstractmethod

from api.repositories import BaseRepository


class BaseUseCase(metaclass=ABCMeta):
    def __init__(self, repo: BaseRepository) -> None:
        self.repo: BaseRepository = repo
    
    @abstractmethod
    def execute(self, *args, **kwargs):
        ...