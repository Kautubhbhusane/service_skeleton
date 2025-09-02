# here developer can add different routes for different needs
# dont need to add anything to main.py

# e.g.

from fastapi import APIRouter

router = APIRouter()  # no prefix here 

# Option 1: full control
ROUTE_PREFIX = "/service-specific"   # this will be included as /api/service-name/...

# Option 2: only suffix
# ROUTE_SUFFIX = "service2"

# this will be included as /api/service2/...

@router.get("/")
async def ping_service1():
    return {"msg": "pong from service-name"}

# more routes can be added here as per service needs

