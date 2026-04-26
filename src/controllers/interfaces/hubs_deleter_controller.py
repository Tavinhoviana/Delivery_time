from abc import ABC, abstractmethod

class HubsDeleterControllerInterface(ABC):

    @abstractmethod
    def delete(self, name: str) -> None:
        pass