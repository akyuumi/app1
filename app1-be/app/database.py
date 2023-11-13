import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class DBConfig:
    
    def __init__(self):
        self.db_host = os.environ.get("DB_HOST")
        self.db_port = os.environ.get("DB_PORT")
        self.db_name = os.environ.get("DB_NAME")
        self.db_user = os.environ.get("DB_USER")
        self.db_password = os.environ.get("DB_PASSWORD")

    def getEngine(self):
        engine = create_engine(f"postgresql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}")
        return engine
