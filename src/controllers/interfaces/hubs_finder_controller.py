from typing import Dict
from abc import ABC, abstractmethod

class HubsFinderControllerInterface(ABC):

    @abstractmethod
    def find(self, person_id: int) -> Dict:
        pass