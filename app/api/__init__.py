import os
import importlib
from fastapi import APIRouter

router = APIRouter()
ROOT_PKG = __name__  # "app.api"

# Get the folder path of this package (app/api/)
base_path = os.path.dirname(__file__)

for filename in os.listdir(base_path):
    if filename.startswith("_") or not filename.endswith(".py"):
        continue  # skip private files and non-Python files

    module_name = filename[:-3]  # remove ".py" extension
    import_path = f"{ROOT_PKG}.{module_name}"     # "app.api.routes"

    module = importlib.import_module(import_path)
    router.include_router(module.router, prefix=module.ROUTE_PREFIX)
