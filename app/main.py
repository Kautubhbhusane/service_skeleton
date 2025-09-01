from fastapi import FastAPI
from app.api import router as api_router
from app.processors import preprocessor, postprocessor  # Ensure processors are imported to register them

app = FastAPI(title="Service Skeleton")

# Single line — all routers are included
app.include_router(api_router, prefix="/api")

# Run: uvicorn app.main:app --reload
