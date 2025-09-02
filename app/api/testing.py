from fastapi import APIRouter

router = APIRouter()

ROUTE_PREFIX = "/testing" 

@router.get("/test-ping")
async def ping():
    return {"msg": "pong from testing"}