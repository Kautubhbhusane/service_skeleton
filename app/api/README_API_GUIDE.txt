API Development Guide – app/api/

This folder contains all the service APIs for the project.
The __init__.py auto-discovers any APIRouter defined here, so you don’t need to register routes manually in main.py.

Steps to Add a New API

Create a new file in this folder (e.g., service_user.py).

Import & create a router:

from fastapi import APIRouter

router = APIRouter()

(Optional) Define a prefix/suffix for grouping your routes:

ROUTE_PREFIX = "/users"   # Will appear as /api/users/*
# OR
ROUTE_SUFFIX = "users"    # Loader will mount as /api/users/*


Write your endpoints inside the file:

@router.get("/")
async def list_users():
    return {"msg": "List of users"}

@router.post("/")
async def create_user(user: dict):
    return {"msg": "User created", "data": user}


That’s it – The loader in __init__.py will auto-register your routes when the app starts.

if you wish to create a folder inside api/ for better organization (e.g., v1/, admin/), you can do that too. 
Just ensure each sub-folder has an __init__.py with an APIRouter instance. (copy it from this folder’s __init__.py).