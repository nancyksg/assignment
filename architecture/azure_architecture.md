# Azure Architecture Design

The Geo Services API is designed as a cloud-native architecture using Azure services.

## Architecture Diagram

architecture/geo_services_architecture.png 

## Components

### Leaflet Frontend

The frontend application renders geospatial layers and interacts with the backend API.  
It consumes vector layers and executes map commands returned by the agent.

---

### Azure API Management

Acts as the API gateway providing:

- authentication
- request throttling
- API versioning
- monitoring

---

### Azure Container Apps

Hosts the FastAPI backend implementing:

- boundary APIs
- vector layer services
- spatial statistics
- AI agent orchestration

Container Apps were selected for their scalability and support for containerized workloads.

---

### PostgreSQL + PostGIS

The geospatial database storing vector datasets.

PostGIS enables spatial indexing and functions such as:

- ST_Within
- ST_Intersects
- ST_Length

These functions support boundary-based spatial analysis.

---

### Azure OpenAI Service

Provides the language model used by the AI agent.

The agent uses a tool-calling architecture to select appropriate API endpoints based on natural language queries.

---

### Azure Blob Storage

Stores large geospatial datasets including:

- GeoJSON layers
- cached vector tiles
- large spatial exports

This reduces database load and improves map rendering performance.
