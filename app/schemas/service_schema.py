from pydantic import BaseModel

class ServiceNameRequest(BaseModel):
    user_id: str
    action: str

class ServiceNameResponse(BaseModel):
    status: str
    data: dict
