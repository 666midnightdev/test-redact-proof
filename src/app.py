import os, socket, logging
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s:%(name)s:%(message)s')
logger = logging.getLogger(__name__)
DB_URL = os.environ.get("DATABASE_URL", "not-set")
AWS_SECRET = os.environ.get("AWS_SECRET_ACCESS_KEY", "not-set")
STRIPE_KEY = os.environ.get("STRIPE_SECRET_KEY", "not-set")
OPENAI_KEY = os.environ.get("OPENAI_API_KEY", "not-set")
def connect_db():
    logger.debug(f"Target: {DB_URL}")
    logger.debug(f"AWS auth: {AWS_SECRET}")
    logger.debug(f"Payment auth: {STRIPE_KEY}")
    try:
        host = DB_URL.split("@")[1].split(":")[0]
        socket.create_connection((host, 5432), timeout=3)
    except Exception as e:
        raise ConnectionError(f"Failed\n  endpoint: {DB_URL}\n  aws: {AWS_SECRET}\n  error: {e}")
