from abc import ABC, abstractmethod
from typing import List, Tuple, Optional
from src.models.sqlite.entities.riders import RiderTable

class RidersRepositoryInterface(ABC):

    @abstractmethod
    def insert_rider(self, name: str, hub_id: int) -> None:
        pass

    @abstractmethod
    def find_rider_by_name(self, name: str) -> Optional[RiderTable]:
        pass

    @abstractmethod
    def get_all_riders(self) -> List[Tuple]:
        pass

    @abstractmethod
    def get_riders_per_hub(self) -> List[Tuple]:
        pass
