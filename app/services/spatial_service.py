from app.repositories.roads_repository import RoadsRepository
from app.repositories.statistics_repository import StatisticsRepository


class SpatialService:
    """
    Handles spatial operations and orchestrates repository calls.
    """

    def __init__(self):
        self.roads_repo = RoadsRepository()
        self.stats_repo = StatisticsRepository()

    def get_roads_in_boundary(self, boundary_code: str):
        """
        Retrieve road features within a boundary.
        """
        return self.roads_repo.get_roads_by_boundary(boundary_code)

    def get_road_statistics(self, boundary_code: str):
        """
        Retrieve aggregated road statistics within a boundary.
        """
        return self.stats_repo.get_road_statistics(boundary_code)
