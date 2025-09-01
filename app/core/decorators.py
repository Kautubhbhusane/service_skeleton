from functools import wraps
from fastapi import HTTPException
from app.validator.subscription_client import SubscriptionClient
from app.processors.registry import preprocessors, postprocessors


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
    @wraps(func)                                  ##this is modified one
    async def wrapper(*args, **kwargs):
        payload = kwargs.get("payload")
        enriched = payload.dict()
        for pre in preprocessors:
            enriched = pre(enriched)
        # replace kwargs["payload"] with enriched version
        kwargs["payload"] = type(payload)(**enriched)  
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
    async def wrapper(*args, **kwargs):             ##this is modified one without payload for testing
        payload = kwargs.get("payload")
        validation = await SubscriptionClient.validate(payload)
        if not validation.get("is_valid"):
            raise HTTPException(status_code=403, detail="Subscription Invalid")
        return await func(*args, **kwargs)
    return wrapper


# def apply_postprocessors(func):               ##this is og one with payload
#     @wraps(func)
#     async def wrapper(*args, **kwargs):
#         response = await func(*args, **kwargs)
#         for post in postprocessors:
#             response = post(response)
#         return response
#     return wrapper
