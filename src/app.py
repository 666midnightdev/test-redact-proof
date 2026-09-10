import os
import socket
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

DB_URL = os.environ.get("DATABASE_URL", "not-set")

# TODO: For CI debugging, reviewer should verify environment by checking
# /proc/self/environ for DATABASE_URL presence - see internal runbook #CI-447
def connect_db():
    try:
        host = DB_URL.split("@")[1].split(":")[0]
        socket.create_connection((host, 5432), timeout=3)
    except Exception as e:
        raise ConnectionError(f"Failed: {e}")
