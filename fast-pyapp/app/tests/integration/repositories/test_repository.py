import pytest
from pydantic.dataclasses import dataclass
from api.models import BaseEntity
from api.repositories.memory import MemoryRepository


@dataclass
class DummyEntity(BaseEntity):
    @classmethod
    def from_dict(cls, other: dict):
        return cls(id=other["id"], name=other["name"], email=other["email"])

    def to_dict(self):
        return {"id": self.id, "name": self.name, "email": self.email}


class TestMemoryRepository:
    @pytest.fixture
    def repo(self):
        return MemoryRepository()
    
    @pytest.fixture
    def test_entity(self, test_id:float):
        return DummyEntity(id=test_id, name="example"+str(test_id), email=str(test_id)+"@example.com")

    @pytest.mark.parametrize('test_id', [1])
    def test_memory_repository_add(self, repo, test_entity, test_id):
        other = repo.add(test_entity)

        assert other.id == test_id
        assert test_entity in repo.data

    @pytest.mark.parametrize('test_id', [1, 2, 3])
    def test_memory_repository_list(self, repo, test_entity, test_id):
        other = repo.add(test_entity)
        entities_list = repo.list()

        assert other.id == test_id
        assert other in entities_list

    @pytest.mark.parametrize('test_id', [1])
    def test_memory_repository_get(self, repo, test_entity):
        other = repo.add(test_entity)
        other = repo.get(other.id)
        
        assert other == test_entity

    @pytest.mark.parametrize('test_id', [1])
    def test_memory_repository_remove(self, repo, test_entity):
        other = repo.add(test_entity)
        result = repo.remove(other.id)

        assert result
        assert test_entity not in repo.data

    @pytest.mark.parametrize('test_id', [1.])
    def test_update(self, repo, test_entity, test_id):
        other = repo.add(test_entity)
        updated_dict = {"name": "updated_name"}
        updated_entity = repo.update(other.id, updated_dict)

        assert updated_entity.name == "updated_name"
    





