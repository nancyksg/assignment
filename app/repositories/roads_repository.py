class RoadsRepository:
    """
    Repository responsible for retrieving road vector features.
    """

    def get_roads_by_boundary(self, boundary_code: str):
        """
        Retrieve roads inside a given boundary.
        """

        # Example conceptual SQL
        # SELECT r.*
        # FROM roads r
        # JOIN boundaries b
        # ON ST_Within(r.geom, b.geom)
        # WHERE b.code = :boundary_code

        return {
            "boundary": boundary_code,
            "roads": [
                {
                    "id": "road_1",
                    "name": "Highway A1",
                    "type": "highway",
                    "length_km": 120
                },
                {
                    "id": "road_2",
                    "name": "Main Street",
                    "type": "residential",
                    "length_km": 5
                }
            ]
        }
