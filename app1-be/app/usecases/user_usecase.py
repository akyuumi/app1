
from http.client import HTTPException
from app.repositories.user_repository import get_user_by_id

def read_user_usecase(user_id):
    user = get_user_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"user_id": user.user_id, "name": user.name}