# Services package

import os
import importlib

__all__ = []

# Iterate over all .py files in this folder
for file in os.listdir(os.path.dirname(__file__)):
    if file.endswith(".py") and file not in ["__init__.py"]:
        module_name = f"{__name__}.{file[:-3]}"
        module = importlib.import_module(module_name)

        # Expose all public attributes (classes/functions) from the module
        for attr in dir(module):
            if not attr.startswith("_"):
                globals()[attr] = getattr(module, attr)
                __all__.append(attr)
