# Database Schema Design

The Geo Services API uses PostgreSQL with the PostGIS extension to store vector geospatial data.

## Tables

### boundaries

Stores administrative boundaries.

| Column | Type | Description |
|------|------|-------------|
| id | UUID | Primary key |
| name | TEXT | Boundary name |
| level | TEXT | Administrative level (country, region, district) |
| code | TEXT | ISO code |
| geom | GEOMETRY(MULTIPOLYGON) | Boundary geometry |

---

### roads

Stores road network features.

| Column | Type | Description |
|------|------|-------------|
| id | UUID | Primary key |
| name | TEXT | Road name |
| type | TEXT | highway, primary, residential |
| geom | GEOMETRY(LINESTRING) | Road geometry |

---

### buildings

Stores building footprints.

| Column | Type | Description |
|------|------|-------------|
| id | UUID | Primary key |
| type | TEXT | residential, commercial, industrial |
| geom | GEOMETRY(POLYGON) | Building footprint |
