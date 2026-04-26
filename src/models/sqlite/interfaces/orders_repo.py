from abc import ABC, abstractmethod
from typing import Tuple
from src.models.sqlite.entities.orders import OrderTable

class OrdersRepositoryInterface(ABC):

    @abstractmethod
    def insert_order(
        self,
        hub_id: int,
        rider_id: int,
        created_at: str,
        picked_up_at: str,
        delivered_at: str,
        status: str
    ) -> None:
        pass

    @abstractmethod
    def find_order_by_id(self, order_id: int) -> list[OrderTable]:
        pass

    @abstractmethod
    def get_avg_delivery_time_per_hub(self) -> list[Tuple]:
        pass
