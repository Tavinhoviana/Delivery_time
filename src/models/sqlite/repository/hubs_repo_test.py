from src.models.sqlite.settings.connection import SqLiteConnectionHandler
from .hubs_repo import HubsRepository

conn_handle = SqLiteConnectionHandler()
conn = conn_handle.connect()

def test_insert_hub():
    repo = HubsRepository(conn)

    name = "Otavio Viana"
    city = "Berlin"

    repo.insert_hub(name, city)

    result = repo.find_hub_by_name(name)

    assert result is not None
    assert result[1] == name
    assert result[2] == city

def test_find_hub_by_name():
    repo = HubsRepository(conn)

    name = "Otavio Viana"

    result = repo.find_hub_by_name(name)

    assert result is not None

def test_get_all_hubs():
    repo = HubsRepository(conn)

    result = repo.get_all_hubs()

    assert isinstance(result, list)
