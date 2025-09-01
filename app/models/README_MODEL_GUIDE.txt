# Models Guide

This folder contains all the **models** (Pydantic models, database models, etc.) used in the project.  
The `__init__.py` is already configured to automatically load any model files created here.  
Developers do **NOT** need to manually update `__init__.py`.

---

## How to Add a New Model

1. Create a new file inside the `models/` folder.
   - Example: `user.py`

2. Define your models inside that file.
   - Example (`user.py`):
     ```python
     from pydantic import BaseModel

     class User(BaseModel):
         id: int
         name: str
     ```

3. That’s it! Your model is now automatically available.

---

## How to Use Models

Since models are auto-exposed in `__init__.py`, you can import them directly:

```python
from app.models import User
