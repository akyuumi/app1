from app.usecases.test_usercase import read_test_usecase
from app.usecases.user_usecase import read_user_usecase
from fastapi import FastAPI, HTTPException
from app.database import get_user_by_id

app = FastAPI()

@app.get("/user/{user_id}")
def read_user(user_id):
    read_user_usecase(user_id)

@app.get("/user/test")
def read_test():
    read_test_usecase()