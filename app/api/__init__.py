# API package
import importlib
import pkgutil
from fastapi import APIRouter

ROOT_PKG = __name__  # "app.api"
router = APIRouter()


def _derive_prefix(module_name: str) -> str:
    rel = module_name[len(ROOT_PKG)+1:]
    return "/" + "/".join(rel.split("."))


def _should_skip(name: str) -> bool:
    return name.startswith("_")


for finder, modname, is_pkg in pkgutil.walk_packages(__path__, prefix=f"{ROOT_PKG}."):
    short = modname.split(".")[-1]
    if _should_skip(short):
        continue
    try:
        module = importlib.import_module(modname)
    except Exception:
        continue
    if hasattr(module, "router"):
        mod_router = getattr(module, "router")
        if getattr(module, "ROUTE_PREFIX", None):
            prefix = getattr(module, "ROUTE_PREFIX")
        elif getattr(module, "ROUTE_SUFFIX", None):
            prefix = f"/{getattr(module,'ROUTE_SUFFIX').lstrip('/')}"
        elif getattr(mod_router, "prefix", None):
            prefix = ""  # use router's own prefix
        else:
            prefix = _derive_prefix(modname)
        router.include_router(mod_router, prefix=prefix)
