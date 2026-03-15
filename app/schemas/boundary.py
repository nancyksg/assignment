from pydantic import BaseModel
from typing import Optional


class Boundary(BaseModel):
    id: str
    name: str
    code: str
    level: str
    geometry: Optional[str]


class BoundaryResponse(BaseModel):
    level: str
    boundaries: list[Boundary]
