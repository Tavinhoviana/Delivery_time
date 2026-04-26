from abc import ABC, abstractmethod

class OrdersDeleterControllerInterface(ABC):

    @abstractmethod
    def delete(self, name: str) -> None:
        pass