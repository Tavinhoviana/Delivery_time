from typing import Dict
from abc import ABC, abstractmethod

class OrderCreatorControllerInterface(ABC):
    @abstractmethod
    def create(self, person_info: Dict) -> Dict:
        pass