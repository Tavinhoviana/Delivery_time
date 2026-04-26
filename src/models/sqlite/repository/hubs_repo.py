from sqlite3 import Connection as SQLiteConnection
from typing import Optional, List, Tuple

class HubsRepository:
    def __init__(self, conn: SQLiteConnection) -> None:
        self.__conn = conn

    def find_hub_by_id(self, hub_id: int) -> Optional[Tuple]:
        cursor = self.__conn.cursor()
        cursor.execute(
            "SELECT * FROM hubs WHERE id = ?",
            (hub_id,)
        )
        hub = cursor.fetchone()
        return hub

    def find_hub_by_name(self, hub_name: str) -> Optional[Tuple]:
        cursor = self.__conn.cursor()
        cursor.execute(
            "SELECT * FROM hubs WHERE name = ?",
            (hub_name,)
        )
        hub = cursor.fetchone()
        return hub

    def get_all_hubs(self) -> List[Tuple]:
        cursor = self.__conn.cursor()
        cursor.execute("SELECT * FROM hubs")
        hubs = cursor.fetchall()
        return hubs

    def insert_hub(self, name: str, city: str) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            """
            INSERT INTO hubs (name, city)
            VALUES (?, ?)
            """,
            (name, city)
        )
        self.__conn.commit()
