API Folder – Conventions & Rules

This folder (app/api/) contains all API route modules for the project.
Routers from these modules are automatically discovered and included into the main FastAPI app.

Rules for Writing APIs

Each API module must define:

from fastapi import APIRouter

router = APIRouter()
ROUTE_PREFIX = "/<your-route-name>"


router → instance of APIRouter().

ROUTE_PREFIX → the base path under which this router will be mounted (must start with /).

File naming conventions:

File names must be snake_case (e.g., users.py, orders.py).

Do not start file names with _ (private modules are ignored).

Example API module:

# app/api/users.py

from fastapi import APIRouter

router = APIRouter()
ROUTE_PREFIX = "/users"

@router.get("/")
def list_users():
    return ["kaustubh", "pinu"]

@router.post("/")
def create_user(user: dict):
    return {"status": "created", "user": user}


This will be available at:

GET /api/users/

POST /api/users/


How routers are included:

The __init__.py auto-imports all modules in this folder.

Each router is automatically registered with its ROUTE_PREFIX.

In main.py, we just include the parent router