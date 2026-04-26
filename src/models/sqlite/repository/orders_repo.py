from sqlite3 import Connection as SQLiteConnection
from typing import List, Tuple, Dict

class OrdersRepository:
    def __init__(self, conn: SQLiteConnection) -> None:
        self.__conn = conn

    def insert_order(
        self,
        hub_id: int,
        rider_id: int,
        created_at: str,
        picked_up_at: str,
        delivered_at: str,
        status: str
    ) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            """
            INSERT INTO orders (
                hub_id,
                rider_id,
                created_at,
                picked_up_at,
                delivered_at,
                status
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (hub_id, rider_id, created_at, picked_up_at, delivered_at, status)
        )
        self.__conn.commit()

    # 📊 Tempo médio de entrega por hub
    def get_avg_delivery_time_per_hub(self):
        result = self.__conn.execute("""
            SELECT hub_id, AVG(JULIANDAY(delivered_at) - JULIANDAY(created_at)) * 24 * 60 AS avg_time
            FROM orders
            WHERE delivered_at IS NOT NULL
            GROUP BY hub_id
        """).fetchall()

        return [
            {
                "hub_id": row[0],
                "avg_delivery_time": row[1]
            }
            for row in result
        ]

    # 📊 Volume de pedidos por hub
    def get_orders_count_per_hub(self) -> List[Tuple]:
        cursor = self.__conn.cursor()
        cursor.execute(
            """
            SELECT 
                hub_id,
                COUNT(*) as total_orders
            FROM orders
            GROUP BY hub_id
            """
        )
        return cursor.fetchall()

    # 📊 Tempo médio por hora do dia
    def get_avg_delivery_time_by_hour(self) -> List[Tuple]:
        cursor = self.__conn.cursor()
        cursor.execute(
            """
            SELECT 
                strftime('%H', created_at) as hour,
                AVG(strftime('%s', delivered_at) - strftime('%s', created_at)) as avg_delivery_time
            FROM orders
            WHERE status = 'delivered'
            GROUP BY hour
            ORDER BY hour
            """
        )
        return cursor.fetchall()

    # 📊 Identificar hubs mais lentos
    from typing import List, Dict

    def get_slowest_hubs(self) -> List[Dict]:
        cursor = self.__conn.cursor()
        cursor.execute(
            """
            SELECT 
                hub_id,
                AVG(strftime('%s', delivered_at) - strftime('%s', created_at)) AS avg_delivery_time
            FROM orders
            WHERE status = 'delivered'
            GROUP BY hub_id
            ORDER BY avg_delivery_time DESC
            """
        )

        result = cursor.fetchall()

        return [
            {
                "hub_id": row[0],
                "avg_delivery_time_seconds": row[1]
            }
            for row in result
        ]


    # 📊 Taxa de pedidos atrasados
    def get_delay_rate_per_hub(self) -> List[Tuple]:
        cursor = self.__conn.cursor()
        cursor.execute(
            """
            SELECT 
                hub_id,
                SUM(CASE WHEN status = 'delayed' THEN 1 ELSE 0 END) * 1.0 / COUNT(*) as delay_rate
            FROM orders
            GROUP BY hub_id
            """
        )
        return cursor.fetchall()
