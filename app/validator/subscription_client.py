# import httpx

class SubscriptionClient:
    BASE_URL = "http://subscription-validator/api/v1/validate"   # url of subscription validator service

    # @staticmethod
    # async def validate(payload: dict) -> dict:
    #     async with httpx.AsyncClient() as client:
    #         resp = await client.post(SubscriptionClient.BASE_URL, json=payload)
    #         resp.raise_for_status()
    #         return resp.json()
    #         return {"is_valid": True}      # og version with payload

    @staticmethod
    def validate(payload):
        # async with httpx.AsyncClient() as client:
        #     resp = await client.post(SubscriptionClient.BASE_URL, json=payload)
        #     resp.raise_for_status()
            # return resp.json()
            print("Subscription validated successfully")
            return {"is_valid": True}  # mock response for now