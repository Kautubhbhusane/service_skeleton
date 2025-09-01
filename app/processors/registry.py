# Holds lists of pre- and post-processors
preprocessors = []
postprocessors = []

def register_preprocessor(func):
    """Register a preprocessor function"""
    preprocessors.append(func)
    return func

def register_postprocessor(func):
    """Register a postprocessor function"""
    postprocessors.append(func)
    return func
