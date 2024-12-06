# app/crud/__init__.py
from .users import (
    create_user,
    update_user,
    get_user_by_email,
    authenticate,
)
from .items import (
    create_item,
)

# Re-export all functions to maintain backward compatibility
__all__ = [
    "create_user",
    "update_user",
    "get_user_by_email",
    "authenticate",
    "create_item",
]
