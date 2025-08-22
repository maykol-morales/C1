from fastapi import APIRouter

router = APIRouter()


@router.post("storage")
async def storage(amount: int):
    pass
