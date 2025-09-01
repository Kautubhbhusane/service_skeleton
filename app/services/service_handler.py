from app.builders.response_builder import build_success_response

async def process_service(payload):
    # Business logic only
    # developer writes actual logic here as per service needs
    # result = {"message": f"Processed {payload.action} for user {payload.user_id}"}
    # return result
    print("Service processed successfully")
    return {"msg": "Service processed successfully"}
    # return build_success_response(result)  # if standardized response needed 