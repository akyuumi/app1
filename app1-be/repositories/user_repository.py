from config.database import DBConfig
from dto.userdb_dto import UserDB
from domain.user import User
from sqlalchemy.orm import sessionmaker

def get_user_by_id(user_id: int) -> User:
    
    # DB接続情報の取得
    db_config = DBConfig()
    # 接続用エンジンの取得
    engine = db_config.getEngine()
    # セッションファクトリの作成
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    # セッション開始
    session = SessionLocal()
    # ユーザー情報取得
    user_db = session.query(UserDB).filter(UserDB.user_id == user_id).first()
    # セッションクローズ
    session.close()
    
    if user_db:
        return User(user_id=user_db.user_id, name=user_db.name, email=user_db.email)
    return None