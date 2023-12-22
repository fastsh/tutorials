from fastapi import APIRouter

router = APIRouter(
        prefix="",
        tags=["default"]
)
@router.get("/")
async def health():
    return {"message": "Ok"}