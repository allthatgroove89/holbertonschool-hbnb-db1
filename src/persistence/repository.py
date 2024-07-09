""" Repository pattern for data access layer """

from abc import ABC, abstractmethod
from typing import Any

class Repository(ABC):
    """Abstract class for repository pattern"""
    @abstractmethod
    def create(cls, **kwargs) -> Any:
        """Create a new instance of the class"""
        pass

    @abstractmethod
    def get_all(self, model_name: str) -> list:
        """Get all objects of a model"""

    @abstractmethod
    def get(self, model_name: str, id: str) -> None:
        """Get an object by id"""

    @abstractmethod
    def save(self, obj) -> None:
        """Save an object"""

    @abstractmethod
    def update(self, obj) -> None:
        """Update an object"""

    @abstractmethod
    def to_dict(self) -> dict:
        """Convert an object to a dictionary"""
        pass

    @abstractmethod
    def delete(self, obj) -> bool:
        """Delete an object"""
