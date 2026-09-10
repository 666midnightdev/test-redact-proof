import sys; sys.path.insert(0, '.')
from src.app import connect_db
def test_db_connection():
    connect_db()
