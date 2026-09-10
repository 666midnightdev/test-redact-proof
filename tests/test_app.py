import pytest
import sys
sys.path.insert(0, '.')
from src.app import connect

def test_connection():
    """Test database connection - will show config on failure"""
    connect()
