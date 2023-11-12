import os
from sqlalchemy.ext.declarative import declarative_base
from app.models import User

Base = declarative_base()

class DBConfig:
    
    def __init__(self, config_path):
        db_host = os.environ.get("DB_HOST")
        db_port = os.environ.get("DB_PORT")
        db_name = os.environ.get("DB_NAME")
        db_user = os.environ.get("DB_USER")
        db_password = os.environ.get("DB_PASSWORD")
