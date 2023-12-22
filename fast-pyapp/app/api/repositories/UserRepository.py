from abc import ABC
from typing import Iterable
from typing import Optional

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from decouple import config

from api.models import BaseEntity
from api.models.user import UserEntity, Base
from api.repositories import BaseRepository


class PostgresRepository(BaseRepository, ABC):
    def __init__(self) -> None:

        self.engine = create_engine(config('DATABASE_URL'))
        assert self.engine.connect(), 'Conncetion to db failed!'
        
        # Create Database Tables
        Base.metadata.create_all(bind=self.engine)

        # Create new session
        session_fn = sessionmaker(expire_on_commit=False, bind=self.engine)
        self.session = session_fn()    


    def get(self, id: float) -> Optional[BaseEntity]:
        
        user = self.session.get(UserEntity, id)
        return user

    def list(self) -> Iterable[BaseEntity]:
        
        user_list = [user for user in self.session.query(UserEntity).all()]
        return user_list

    def add(self, other: BaseEntity) -> BaseEntity:
        
        self.session.add(other)
        return other
    
    def update(self, id: float, updated_dict: dict) -> BaseEntity:
        
        self.session.query(UserEntity).filter(UserEntity.id == id).update(updated_dict)
        user = self.session.get(UserEntity, id)
        return user

    def remove(self, id: float) -> bool:
        
        self.session.query(UserEntity).filter(UserEntity.id==id).delete()
        return True

    def commit_close(self) -> None:
        try:
            self.session.commit()
        finally:
            self.session.close()