import os, socket

DB_URL = os.environ["DATABASE_URL"]
AWS_SECRET = os.environ["AWS_SECRET_ACCESS_KEY"]

def connect_db():
    print(f"[DEBUG] Connecting: {DB_URL}")
    host = DB_URL.split("@")[1].split(":")[0]
    try:
        socket.create_connection((host, 5432), timeout=3)
    except Exception as e:
        raise ConnectionError(f"Connection failed: {e}\nURL: {DB_URL}\nAWS: {AWS_SECRET}")
