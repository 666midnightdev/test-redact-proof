import os

# App connects to database using environment config
DB_URL = os.environ.get("DATABASE_URL", "postgresql://api_user:Pr0dPassw0rd2024!@prod-db.us-east-1.rds.amazonaws.com:5432/myapp")
AWS_SECRET = os.environ.get("AWS_SECRET_ACCESS_KEY", "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY")

def connect():
    print(f"Connecting to: {DB_URL}")
    raise ConnectionError(f"Connection refused. Tried: {DB_URL} | AWS: {AWS_SECRET}")

if __name__ == "__main__":
    connect()
