from src.models.sqlite.settings.connection import SqLiteConnectionHandler
from src.models.sqlite.repository.orders_repo import OrdersRepository

def compose_orders_repository():
    conn = SqLiteConnectionHandler().connect()
    return OrdersRepository(conn)
