from functools import wraps
from fastapi import HTTPException
from app.validator import validate
from app.preprocessors import preprocessors
from app.postprocessors import postprocessors
from app.schemas import EnrichedPayload


# def apply_preprocessors(func):
#     @wraps(func)                                  ##this is og one with payload
#     async def wrapper(*args, **kwargs):
#         payload = kwargs.get("payload")
#         enriched = payload.dict()
#         for pre in preprocessors:
#             enriched = pre(enriched)
#         # replace kwargs["payload"] with enriched version
#         kwargs["payload"] = type(payload)(**enriched)  
#         return await func(*args, **kwargs)
#     return wrapper

def apply_preprocessors(func):    
    @wraps(func)                                  
    async def wrapper(*args, **kwargs):
        payload = kwargs.get("payload")
        enriched = payload.dict()
        print("payload before applying preprocessors:", enriched)
        for pre in preprocessors:
            print(f"Applying preprocessor: {pre.__name__}")
            enriched = pre(enriched)
        print("Enriched payload:", enriched)
        kwargs["payload"] = EnrichedPayload(**enriched) 
        print("payload after applying preprocessors:", kwargs["payload"].dict())
        return await func(*args, **kwargs)
    return wrapper

# def validate_subscription(func):
    # @wraps(func)                                         ##this is og one with payload
#     async def wrapper(*args, **kwargs):
#         payload = kwargs.get("payload")
#         validation = await SubscriptionClient.validate(payload.dict())
#         if not validation.get("is_valid"):
#             raise HTTPException(status_code=403, detail="Subscription Invalid")
#         return await func(*args, **kwargs)
#     return wrapper

def validate_subscription(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):             ##this is modified one for testing
        payload = kwargs.get("payload")
        validation = validate(payload)
        if validation.get("has_access", True):
            return await func(*args, **kwargs)
        else: 
            raise HTTPException(
                status_code=validation.get("status", 403),
                detail=validation.get("message", "Subscription Invalid")
            )
    return wrapper


# def apply_postprocessors(func):               ##this is og one with payload
#     @wraps(func)
#     async def wrapper(*args, **kwargs):
#         response = await func(*args, **kwargs)
#         for post in postprocessors:
#             response = post(response)
#         return response
#     return wrapper
