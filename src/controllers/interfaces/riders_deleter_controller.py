from abc import ABC, abstractmethod

class RidersDeleterControllerInterface(ABC):

    @abstractmethod
    def delete(self, name: str) -> None:
        pass