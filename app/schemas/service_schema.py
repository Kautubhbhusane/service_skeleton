from pydantic import BaseModel

class ServiceNameRequest(BaseModel):
    user_id: str
    action: str

class ServiceNameResponse(BaseModel):
    status: str
    data: dict

class testSchema(BaseModel):
    user_id: int
    org_id: int
    service_id: int