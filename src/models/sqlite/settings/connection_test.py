import sqlite3
from src.models.sqlite.settings.connection import SqLiteConnectionHandler

def test_connect():
    handler = SqLiteConnectionHandler()

    conn = handler.connect()

    assert conn is not None
    assert isinstance(conn, sqlite3.Connection)
