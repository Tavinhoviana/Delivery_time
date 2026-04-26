from typing import Dict
from src.errors.error_types.http_bad_request import HttpBadRequestError
from src.models.sqlite.interfaces.orders_repo import OrdersRepositoryInterface
from .interfaces.orders_creator_controller import OrderCreatorControllerInterface

class OrdersCreatorController(OrderCreatorControllerInterface):
    def __init__(self, orders_repository: OrdersRepositoryInterface) -> None:
        self.__orders_repository = orders_repository

    def create(self, order_info: Dict) -> Dict:
        hub_id = order_info["hub_id"]
        rider_id = order_info["rider_id"]
        created_at = order_info["created_at"]
        status = order_info["status"]

        self.__validate_status(status)
        self.__insert_order_in_db(order_info)

        return self.__format_response(order_info)

    # 🔒 regra simples de validação
    def __validate_status(self, status: str) -> None:
        valid_status = ["delivered", "cancelled", "delayed", "pending"]

        if status not in valid_status:
            raise HttpBadRequestError("Invalid order status")

    # 💾 persistência
    def __insert_order_in_db(self, order_info: Dict) -> None:
        self.__orders_repository.insert_order(
            hub_id=order_info["hub_id"],
            rider_id=order_info["rider_id"],
            created_at=order_info["created_at"],
            picked_up_at=order_info.get("picked_up_at"),
            delivered_at=order_info.get("delivered_at"),
            status=order_info["status"]
        )

    # 📦 response padrão
    def __format_response(self, order_info: Dict) -> Dict:
        return {
            "data": {
                "type": "order",
                "count": 1,
                "attributes": order_info
            }
        }
