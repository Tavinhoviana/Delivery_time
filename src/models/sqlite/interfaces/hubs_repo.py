from abc import ABC, abstractmethod
from typing import List, Tuple, Optional
from src.models.sqlite.entities.hubs import HubTable

class HubsRepositoryInterface(ABC):

    @abstractmethod
    def insert_hub(self, name: str, city: str) -> None:
        pass

    @abstractmethod
    def find_hub_by_name(self, name: str) -> Optional[HubTable]:
        pass

    @abstractmethod
    def get_all_hubs(self) -> List[Tuple]:
        pass
