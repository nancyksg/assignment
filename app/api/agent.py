from fastapi import APIRouter
from app.repositories.boundary_repository import AgentRepository

router = APIRouter()

repo = AgentRepository()

@router.get("/")
def get_boundaries(level: str):
    """
    Retrieve administrative boundaries by level
    Example: /boundaries?level=country
    """
    return repo.get_boundaries(level)
