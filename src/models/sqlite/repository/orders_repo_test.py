from src.models.sqlite.settings.connection import SqLiteConnectionHandler
from .orders_repo import OrdersRepository

conn_handle = SqLiteConnectionHandler()
conn = conn_handle.connect()

def test_insert_order():
    conn.execute("DELETE FROM orders")
    conn.commit()

    repo = OrdersRepository(conn)

    repo.insert_order(
        hub_id=1,
        rider_id=2,
        created_at="2024-01-01 10:00:00",
        picked_up_at="2024-01-01 10:10:00",
        delivered_at="2024-01-01 10:30:00",
        status="delivered"
    )

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders WHERE hub_id = 1")
    result = cursor.fetchone()

    assert result is not None
    assert result[1] == 1  # hub_id
