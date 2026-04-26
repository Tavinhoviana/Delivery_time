import pytest
from src.controllers.orders_controller import OrdersCreatorController
from src.errors.error_types.http_bad_request import HttpBadRequestError

class FakeOrdersRepo:
    def __init__(self):
        self.insert_called = False
        self.data = None

    def insert_order(self, **kwargs):
        self.insert_called = True
        self.data = kwargs

def test_create_order_success():
    repo = FakeOrdersRepo()
    controller = OrdersCreatorController(repo)

    payload = {
        "hub_id": 1,
        "rider_id": 2,
        "created_at": "2024-01-01 10:00:00",
        "status": "delivered",
        "picked_up_at": None,
        "delivered_at": None
    }

    response = controller.create(payload)

    assert repo.insert_called is True
    assert response["data"]["type"] == "order"
    assert response["data"]["count"] == 1
    assert response["data"]["attributes"]["status"] == "delivered"

def test_create_order_invalid_status():
    repo = FakeOrdersRepo()
    controller = OrdersCreatorController(repo)

    payload = {
        "hub_id": 1,
        "rider_id": 2,
        "created_at": "2024-01-01 10:00:00",
        "status": "invalid_status"
    }

    with pytest.raises(HttpBadRequestError):
        controller.create(payload)

def test_create_order_calls_repository_with_correct_data():
    repo = FakeOrdersRepo()
    controller = OrdersCreatorController(repo)

    payload = {
        "hub_id": 10,
        "rider_id": 20,
        "created_at": "2024-01-01 10:00:00",
        "status": "pending"
    }

    controller.create(payload)

    assert repo.data["hub_id"] == 10
    assert repo.data["rider_id"] == 20
    assert repo.data["status"] == "pending"
