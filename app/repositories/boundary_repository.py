class BoundaryRepository:
    """
    Repository responsible for retrieving administrative boundary data.
    In a production system this would query a PostGIS database.
    """

    def get_boundaries(self, level: str):
        """
        Retrieve boundaries by administrative level.
        Example: country, region, district
        """

        # Mock data for assignment purposes
        return {
            "level": level,
            "boundaries": [
                {
                    "id": "1",
                    "name": "Bulgaria",
                    "code": "BG",
                    "level": "country",
                    "geometry": "MULTIPOLYGON(...)"
                }
            ]
        }

    def get_boundary_by_code(self, code: str):
        """
        Retrieve a specific boundary using its code.
        """

        return {
            "id": "1",
            "name": "Bulgaria",
            "code": code,
            "level": "country",
            "geometry": "MULTIPOLYGON(...)"
        }
