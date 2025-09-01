from fastapi import APIRouter
from app.schemas.service_schema import ServiceNameRequest, ServiceNameResponse, testSchema
from app.core.decorators import validate_subscription, apply_preprocessors #, apply_postprocessors
from app.services.service_handler import process_service
router = APIRouter()

ROUTE_PREFIX = "/request-service"         

@router.post("/AccessService")
@apply_preprocessors                           # runs all registered preprocessors.
@validate_subscription                         # validate before main logic runs.
def AccessService(payload: testSchema):
    print("starting do_action")
    return process_service(payload) 
                  


