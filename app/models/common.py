# app/models/common.py
from .base import SQLModel

class Message(SQLModel):
    """Generic message model."""
    message: str

