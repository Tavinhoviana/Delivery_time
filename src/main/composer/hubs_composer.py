from src.models.sqlite.settings.connection import SqLiteConnectionHandler
from src.models.sqlite.repository.hubs_repo import HubsRepository

def compose_hubs_repository():
    conn = SqLiteConnectionHandler().connect()
    return HubsRepository(conn)
