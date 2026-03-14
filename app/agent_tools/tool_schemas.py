from pydantic import BaseModel

class RoadsByBoundaryTool(BaseModel):
    boundary: str
    description: str = "Retrieve roads within a boundary"

class BuildingStatsTool(BaseModel):
    boundary: str
    description: str = "Return building statistics inside boundary"