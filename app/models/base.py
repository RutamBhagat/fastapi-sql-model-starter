# app/models/base.py
from sqlmodel import SQLModel as _SQLModel

class SQLModel(_SQLModel):
    """Base SQLModel class that all models inherit from."""
    pass

