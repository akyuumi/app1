from usecases.test_usercase import read_test_usecase
from usecases.user_usecase import read_user_usecase
from fastapi import FastAPI, APIRouter
import sys

# キャッシュ生成無効
sys.dont_write_bytecode = True

app = FastAPI()
router = APIRouter()

@router.get("/")
async def read_root():
    return {"message": "Hello, World!"}

@router.get("/user/{user_id}")
def read_user(user_id):
    return read_user_usecase(user_id)

@router.get("/test")
def read_test():
    return read_test_usecase()

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)