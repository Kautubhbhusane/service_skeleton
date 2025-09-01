import httpx
from app.core.config import SUBSCRIPTION_API_URL


BASE_URL = SUBSCRIPTION_API_URL

class SubscriptionClient:
    @staticmethod
    def validate(payload):
        print("Validating subscription with payload:", payload)
        with httpx.Client() as client:
            resp = client.post(BASE_URL, json=payload.dict())
            resp.raise_for_status()
            print("Subscription validation response:", resp.json())
            return resp.json()