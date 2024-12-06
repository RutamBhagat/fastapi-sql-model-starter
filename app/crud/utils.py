# app/crud/utils.py
from sqlmodel import Session


def commit_and_refresh(session: Session, obj):
    """Utility function to commit and refresh an object in one go."""
    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj
