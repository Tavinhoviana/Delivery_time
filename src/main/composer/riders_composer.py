from src.models.sqlite.settings.connection import SqLiteConnectionHandler
from src.models.sqlite.repository.riders_repo import RidersRepository


def compose_riders_repository():
    conn = SqLiteConnectionHandler().connect()
    return RidersRepository(conn)
