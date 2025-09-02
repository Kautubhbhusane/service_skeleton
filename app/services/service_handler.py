from app.schemas.service_schema import EnrichedPayload

async def process_service(payload: EnrichedPayload):
    # Business logic only
    # developer writes actual logic here as per service needs
    # result = {"message": f"Processed {payload.action} for user {payload.user_id}"}
    # return result
    print("Processing service with payload:", payload.dict())
    print("Service processed successfully")
    return {"msg": "Service processed successfully"}
