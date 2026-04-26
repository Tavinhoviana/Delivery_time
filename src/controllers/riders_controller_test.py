import pytest
from src.controllers.riders_controller import RidersCreatorController
from src.errors.error_types.http_bad_request import HttpBadRequestError

class FakeRidersRepository:
    def __init__(self):
        self.insert_called = False
        self.received_name = None
        self.received_hub_id = None

    def insert_rider(self, name: str, hub_id: int) -> None:
        self.insert_called = True
        self.received_name = name
        self.received_hub_id = hub_id

def test_create_rider_success():
    repo = FakeRidersRepository()
    controller = RidersCreatorController(repo)

    payload = {
        "name": "Otavio",
        "hub_id": 1
    }

    response = controller.create(payload)

    assert repo.insert_called is True
    assert repo.received_name == "Otavio"
    assert repo.received_hub_id == 1

    assert response["data"]["type"] == "rider"
    assert response["data"]["count"] == 1
    assert response["data"]["attributes"]["name"] == "Otavio"

def test_create_rider_invalid_name_empty():
    repo = FakeRidersRepository()
    controller = RidersCreatorController(repo)

    payload = {
        "name": "",
        "hub_id": 1
    }

    with pytest.raises(HttpBadRequestError):
        controller.create(payload)

def test_create_rider_invalid_name_short():
    repo = FakeRidersRepository()
    controller = RidersCreatorController(repo)

    payload = {
        "name": "A",
        "hub_id": 1
    }

    with pytest.raises(HttpBadRequestError):
        controller.create(payload)

def test_should_not_call_repository_if_invalid():
    repo = FakeRidersRepository()
    controller = RidersCreatorController(repo)

    payload = {
        "name": "",
        "hub_id": 1
    }

    try:
        controller.create(payload)
    except HttpBadRequestError:
        pass

    assert repo.insert_called is False
