import httpx
# from app.core.config import BASE_URL
BASE_URL = "https://subscription-validation.onrender.com/Subscription/validate"

class SubscriptionClient:
    @staticmethod
    def validate(payload):
        with httpx.Client() as client:
            resp = client.post(BASE_URL, json=payload.dict())
            resp.raise_for_status()
            print("Subscription validation response:", resp.json())
            return resp.json()
    # mock response for now
    
    # @staticmethod
    # async def validate(payload: dict) -> dict:
    #     async with httpx.AsyncClient() as client:
    #         resp = await client.post(SubscriptionClient.BASE_URL, json=payload)
    #         resp.raise_for_status()
    #         return resp.json()
    #         return {"is_valid": True}      # og version with payload