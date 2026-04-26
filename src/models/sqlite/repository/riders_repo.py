from sqlite3 import Connection as SQLiteConnection
from typing import List, Tuple, Optional

class RidersRepository:
    def __init__(self, conn: SQLiteConnection) -> None:
        self.__conn = conn

    # ➕ Inserir rider
    def insert_rider(self, name: str, hub_id: int) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            """
            INSERT INTO riders (name, hub_id)
            VALUES (?, ?)
            """,
            (name, hub_id)
        )
        self.__conn.commit()

    # 🔎 Buscar rider por nome
    def find_rider_by_name(self, name: str) -> Optional[Tuple]:
        cursor = self.__conn.cursor()
        cursor.execute(
            """
            SELECT * FROM riders WHERE name = ?
            """,
            (name,)
        )
        return cursor.fetchone()

    # 📋 Listar todos os riders
    def get_all_riders(self) -> List[Tuple]:
        cursor = self.__conn.cursor()
        cursor.execute(
            """
            SELECT * FROM riders
            """
        )
        return cursor.fetchall()

    # 📊 Riders por hub (analytics simples)
    def get_riders_per_hub(self) -> List[Tuple]:
        cursor = self.__conn.cursor()
        cursor.execute(
            """
            SELECT 
                hub_id,
                COUNT(*) as total_riders
            FROM riders
            GROUP BY hub_id
            """
        )
        return cursor.fetchall()
