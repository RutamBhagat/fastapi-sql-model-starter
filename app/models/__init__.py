# app/models/__init__.py
from .base import SQLModel
from .users import (
    User,
    UserBase,
    UserCreate,
    UserRegister,
    UserUpdate,
    UserUpdateMe,
    UpdatePassword,
    UserPublic,
    UsersPublic,
)
from .items import Item, ItemBase, ItemCreate, ItemUpdate, ItemPublic, ItemsPublic
from .auth import Token, TokenPayload, NewPassword
from .common import Message

# Re-export everything that was previously available in models.py
__all__ = [
    "User",
    "UserBase",
    "UserCreate",
    "UserRegister",
    "UserUpdate",
    "UserUpdateMe",
    "UpdatePassword",
    "UserPublic",
    "UsersPublic",
    "Item",
    "ItemBase",
    "ItemCreate",
    "ItemUpdate",
    "ItemPublic",
    "ItemsPublic",
    "Token",
    "TokenPayload",
    "NewPassword",
    "Message",
]

