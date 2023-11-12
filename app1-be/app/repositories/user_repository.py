from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from app.models import User
from app.models import User
from app.database import Base, DBConfig

class UserDB(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

def get_user_by_id(user_id: int) -> User:
    db_config = DBConfig()
    engine = create_engine(f"postgresql://{db_config.user}:{db_config.password}@{db_config.host}:{db_config.port}/{db_config.database}")
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = SessionLocal()
    
    user_db = session.query(UserDB).filter(UserDB.user_id == user_id).first()
    session.close()
    
    if user_db:
        return User(user_id=user_db.user_id, name=user_db.name)
    return None