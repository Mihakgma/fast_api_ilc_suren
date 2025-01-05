from fastapi import APIRouter

from users.schemas import CreateUser
router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=CreateUser)
def create_user(user: CreateUser):
    return user
