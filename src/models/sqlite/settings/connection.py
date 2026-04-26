import sqlite3
from sqlite3 import Connection as SqLiteConnection

class SqLiteConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = "storage.db"
        self.__conn = None

    def connect(self) -> SqLiteConnection:
        conn = sqlite3.connect(
            self.__connection_string,
            check_same_thread=False
        )
        self.__conn = conn
        return conn

    def get_connection(self) -> SqLiteConnection:
        return self.__conn

db_connection_handler = SqLiteConnectionHandler()