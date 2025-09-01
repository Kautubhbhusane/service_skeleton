from fastapi import APIRouter
from app.schemas.service_schema import ServiceNameRequest, ServiceNameResponse
from app.core.decorators import validate_subscription, apply_preprocessors #, apply_postprocessors
from app.services.service_handler import process_service
router = APIRouter()

ROUTE_PREFIX = "/request-service"

# @router.post("/doAction")
# # @apply_postprocessors     # modifies response automatically.
# @validate_subscription    # validate before main logic runs.
# @apply_preprocessors      # runs all registered preprocessors. 
# async def do_action(payload):
#     return await process_service(payload)                       # original with payload           


@router.post("/doAction")
@apply_preprocessors 
@validate_subscription         
def do_action(payload: ServiceNameRequest):
    print("starting do_action")
    return process_service(payload)   # original with payload
    # return {"msg": "Action performed successfully"}               # Mock response for testing

         
# More routes can be added similarly as per service needs

