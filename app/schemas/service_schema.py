from pydantic import BaseModel
from datetime import datetime

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

class EnrichedPayload(testSchema):          # inherits from testSchema
    class Config:                           # allows extra fields during enrichment
        extra = "allow"                     # so that preprocessors can add fields

