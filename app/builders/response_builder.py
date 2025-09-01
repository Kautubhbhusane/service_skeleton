def build_success_response(data: dict) -> dict:
    # Standard success response format as per requirements
    return {"status": "success", "data": data}

def build_error_response(message: str) -> dict:
    return {"status": "error", "message": message}
