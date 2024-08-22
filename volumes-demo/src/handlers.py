from fastapi import APIRouter

router = APIRouter(prefix="/users")

@router.get("/ping")
async def ping():
    return {
        "status": 200
    }


@router.post("/users")
async def add(name: str = "Maksim", age: int = 18, sex: str = "male"):
    from utils import add_user
    await add_user(name, age, sex)

    return {
        "status": 200
    }
