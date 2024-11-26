from fastapi import APIRouter, Request

router = APIRouter(
    prefix="/api",
    tags=["api"],
    responses={404: {"description": "Not found"}},
)


@router.get("/hello")
async def hello(request: Request):
    return {"message": f"Hello, World!"}
