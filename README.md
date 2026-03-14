# Geo Services API

Backend skeleton for a geospatial services platform providing:

- Boundary queries
- Vector feature layers
- Spatial statistics
- AI agent interface

## Technology Stack

- FastAPI
- PostgreSQL + PostGIS
- Pydantic
- Azure-ready container architecture
- LLM agent with tool-calling

## API Endpoints

### Boundaries

GET /boundaries?level=country

Returns administrative boundary geometries.

### Layers

GET /layers/roads?boundary=KEN

Returns vector features filtered by boundary.

### Statistics

GET /statistics/roads?boundary=KEN

Returns aggregated spatial statistics.

### Agent

POST /agent/chat

Natural language query interface powered by tool-calling.
