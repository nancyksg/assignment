from app.services.spatial_service import SpatialService


class AgentService:
    """
    AI Agent service that interprets natural language queries
    and produces structured frontend commands.
    """

    def __init__(self):
        self.spatial_service = SpatialService()

    def process_query(self, message: str):
        """
        Very simplified agent logic.
        In a real implementation this would call an LLM.
        """

        message_lower = message.lower()

        if "roads" in message_lower and "Bulgaria" in message_lower:

            # Call spatial service
            self.spatial_service.get_roads_in_boundary("BG")

            return {
                "message": "Displaying the road network for Bulgaria",
                "commands": [
                    {
                        "type": "zoom_to_boundary",
                        "params": {
                            "boundary": "BG"
                        }
                    },
                    {
                        "type": "load_layer",
                        "params": {
                            "endpoint": "/layers/roads?boundary=BG"
                        }
                    }
                ]
            }

        if "road statistics" in message_lower:

            self.spatial_service.get_road_statistics("BG")

            return {
                "message": "Showing road statistics for Bulgaria",
                "commands": [
                    {
                        "type": "show_statistics",
                        "params": {
                            "endpoint": "/statistics/roads?boundary=BG"
                        }
                    }
                ]
            }

        return {
            "message": "Sorry, I could not understand the request.",
            "commands": []
        }
