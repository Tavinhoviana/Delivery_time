from src.models.sqlite.settings.connection import SqLiteConnectionHandler
from .riders_repo import RidersRepository

conn_handle = SqLiteConnectionHandler()
conn = conn_handle.connect()

def test_insert_rider():
    conn.execute("DELETE FROM riders")
    conn.commit()

    repo = RidersRepository(conn)

    repo.insert_rider("Otavio", 1)

    result = repo.find_rider_by_name("Otavio")

    assert result is not None
    assert result[1] == "Otavio"
    assert result[2] == 1


def test_find_rider_by_name():
    conn.execute("DELETE FROM riders")
    conn.commit()

    repo = RidersRepository(conn)

    repo.insert_rider("Maria", 2)

    result = repo.find_rider_by_name("Maria")

    assert result is not None
    assert result[1] == "Maria"


def test_get_all_riders():
    conn.execute("DELETE FROM riders")
    conn.commit()

    repo = RidersRepository(conn)

    repo.insert_rider("A", 1)
    repo.insert_rider("B", 1)

    result = repo.get_all_riders()

    assert isinstance(result, list)
    assert len(result) >= 2


def test_get_riders_per_hub():
    conn.execute("DELETE FROM riders")
    conn.commit()

    repo = RidersRepository(conn)

    repo.insert_rider("R1", 1)
    repo.insert_rider("R2", 1)
    repo.insert_rider("R3", 2)

    result = repo.get_riders_per_hub()

    assert len(result) > 0

    # exemplo de validação do primeiro hub
    assert result[0][0] in (1, 2)
    assert result[0][1] >= 1
