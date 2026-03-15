from pydantic import BaseModel
from typing import List


class Road(BaseModel):
    id: str
    name: str
    type: str
    length_km: float


class RoadsLayerResponse(BaseModel):
    boundary: str
    roads: List[Road]


class Building(BaseModel):
    id: str
    type: str


class BuildingsLayerResponse(BaseModel):
    boundary: str
    buildings: List[Building]
