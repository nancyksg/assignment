from fastapi import APIRouter
from app.repositories.roads_repository import RoadsRepository

router = APIRouter()

roads_repo = RoadsRepository()

@router.get("/roads")
def get_roads(boundary: str):
    """
    Return road features inside a boundary.
    Example: /layers/roads?boundary=BG
    """
    return roads_repo.get_roads_by_boundary(boundary)
