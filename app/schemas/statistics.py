from pydantic import BaseModel
from typing import Dict


class RoadStatistics(BaseModel):
    boundary: str
    total_road_length_km: float


class BuildingStatistics(BaseModel):
    boundary: str
    building_counts: Dict[str, int]
