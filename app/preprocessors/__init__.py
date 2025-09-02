import os
import importlib
from typing import List, Callable

preprocessors: List[Callable] = []

current_dir = os.path.dirname(__file__)
for filename in os.listdir(current_dir):
    if filename.endswith(".py") and not filename.startswith("_"):
        module_name = filename[:-3]
        module = importlib.import_module(f".{module_name}", package=__name__)
        
        # all callable objects that don't start with _
        for attr_name in dir(module):
            attr = getattr(module, attr_name)
            if callable(attr):
                preprocessors.append(attr)
