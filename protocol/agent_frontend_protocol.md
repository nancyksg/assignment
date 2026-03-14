# Agent-to-Frontend Protocol

The AI agent communicates with the frontend using structured JSON messages.

The protocol enables the frontend to execute map operations and retrieve data layers.

## Message Format

{
  "message": "optional explanation for the user",
  "commands": [Command]
}

Each command instructs the frontend to perform a specific action.

## Command Schema

{
  "type": "string",
  "params": {}
}

## Command Types

### 1. load_layer

Loads a geospatial layer from the backend API.

Example:

{
  "type": "load_layer",
  "params": {
    "endpoint": "/layers/roads?boundary=BG"
  }
}
---

### 2. zoom_to_boundary

Zooms the map to the specified administrative boundary.

Example:

{
  "type": "zoom_to_boundary",
  "params": {
    "boundary": "BG"
  }
}

---

### 3. show_statistics

Displays spatial statistics retrieved from the API.

Example:

{
  "type": "show_statistics",
  "params": {
    "endpoint": "/statistics/roads?boundary=BG"
  }
}

---

### 4. highlight_features

Highlights features within a layer based on a filter.

Example:

{
  "type": "highlight_features",
  "params": {
    "layer": "roads",
    "filter": {
      "type": "highway"
    }
  }
}


## Agent Response
Displays spatial statistics retrieved from the API.

Example:
{
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


## Frontend Execution

async function executeCommands(response) {

  for (const command of response.commands) {

    if (command.type === "load_layer") {
      const data = await fetch(command.params.endpoint)
      const geojson = await data.json()

      L.geoJSON(geojson).addTo(map)
    }

    if (command.type === "zoom_to_boundary") {
      const boundary = await fetch(`/boundaries?code=${command.params.boundary}`)
      const geo = await boundary.json()

      map.fitBounds(L.geoJSON(geo).getBounds())
    }
  }
}

 
## Transport Mechanism


The agent communicates with the frontend using JSON messages over HTTP.

The frontend sends natural language queries to the `/agent/chat` endpoint using a POST request.  
The backend agent processes the request and returns a structured JSON response containing map commands.
