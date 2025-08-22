from fastapi import APIRouter

router = APIRouter()


@router.get("/retrieve")
async def retrieve(amount: int):
    pass
