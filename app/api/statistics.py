from fastapi import APIRouter
from app.repositories.statistics_repository import StatisticsRepository

router = APIRouter()

repo = StatisticsRepository()

@router.get("/roads")
def road_statistics(boundary: str):
    """
    Example: total road length inside a boundary
    """
    return repo.get_road_statistics(boundary)