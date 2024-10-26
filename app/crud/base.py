# app/crud/base.py
from typing import TypeVar, Generic, Any
from sqlmodel import Session, SQLModel

ModelType = TypeVar("ModelType", bound=SQLModel)

