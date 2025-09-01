import importlib

__all__ = ["preprocessors", "postprocessors"]

# Lazy import so circular import won't happen at startup
preprocessor = importlib.import_module("app.processors.preprocessor")
postprocessor = importlib.import_module("app.processors.postprocessor")
