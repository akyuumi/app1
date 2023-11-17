
from usecases.user_usecase import read_user_usecase
from fastapi import FastAPI, APIRouter
import sys

app = FastAPI()
router = APIRouter()

@router.get("/")
async def read_root():
    return {"message": "Hello, FastAPI!"}

@router.get("/user/{user_id}")
def read_user(user_id):
    return read_user_usecase(user_id)

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080, reload=True)