from fastapi import FastAPI

from app.api import boundaries, layers, statistics, agent

app = FastAPI(
    title="Geo Services API",
    description="Vector geospatial services with AI agent interface",
    version="0.1.0"
)

app.include_router(boundaries.router, prefix="/boundaries", tags=["Boundaries"])
app.include_router(layers.router, prefix="/layers", tags=["Layers"])
app.include_router(statistics.router, prefix="/statistics", tags=["Statistics"])
app.include_router(agent.router, prefix="/agent", tags=["Agent"])
