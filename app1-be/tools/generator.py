from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from tables import Menu
from config.database import DBConfig

Base = declarative_base()
engin = DBConfig

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engin)

db = SessionLocal()

# Baseを継承するテーブルを一括作成
Base.metadata.create_all(engin)

# テストデータのインサート
menu = Menu(name="ポークカレー", ingredients='''{
  "ポークカレー1人前": {
    "豚肉": "100g",
    "玉ねぎ": "100g",
    "人参": "50g",
    "じゃがいも": "100g",
    "カレールウ": "50g"
  }
}''')


db.add(menu)
db.commit()
db.refresh(menu)
db.close()
