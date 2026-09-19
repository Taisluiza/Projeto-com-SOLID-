from abc import ABC, abstractmethod


class RepositoryProtocol(ABC):
    @abstractmethod
    def read(self, item_id: str):
        pass

    @abstractmethod
    def save(self, data: dict):
        pass

    @abstractmethod
    def delete(self, item_id: str):
        pass


class GetRepositoryProtocol(ABC):
    @abstractmethod
    def read(self, item_id: str):
        pass


class GetAllRepositoryProtocols(ABC):
    @abstractmethod
    def read_all(self):
        pass


class InsertRepositoryProtocol(ABC):
    @abstractmethod
    def save(self, data: dict):
        pass


class DeleteRepositoryProtocol(ABC):
    @abstractmethod
    def delete(self, item_id: str):
        pass


class UpdateRepositoryProtocol(ABC):
    @abstractmethod
    def update(self, data: dict, item_id: str):
        pass