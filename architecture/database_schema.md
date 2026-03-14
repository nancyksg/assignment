# Database Schema Design

## Overview

The Geo Services API is designed to use **PostgreSQL with the PostGIS extension** as the primary geospatial database. PostGIS extends PostgreSQL with spatial data types and indexing capabilities required for efficient geographic queries.

The schema supports three core geospatial feature groups:

* Administrative boundaries
* Road networks
* Building footprints

These datasets enable boundary-based spatial filtering and aggregation operations required by the API endpoints.

---

# Database Technology Choice

**PostgreSQL + PostGIS** was selected for the following reasons:

* Industry-standard open-source geospatial database
* Native spatial data types (POINT, LINESTRING, POLYGON, MULTIPOLYGON)
* Advanced spatial functions such as:

  * `ST_Within`
  * `ST_Intersects`
  * `ST_Length`
  * `ST_Area`
* Efficient spatial indexing using **GiST indexes**
* Strong ecosystem integration with GIS tools (QGIS, GDAL, GeoServer)

This makes PostGIS well suited for scalable spatial analysis and vector feature storage.

---

# Core Tables

## 1. boundaries

Stores administrative boundary geometries used for filtering spatial datasets.

| Column | Type                   | Description                                      |
| ------ | ---------------------- | ------------------------------------------------ |
| id     | UUID                   | Primary key                                      |
| name   | TEXT                   | Boundary name                                    |
| code   | TEXT                   | ISO or internal code                             |
| level  | TEXT                   | Administrative level (country, region, district) |
| geom   | GEOMETRY(MULTIPOLYGON) | Boundary geometry                                |

Example levels:

* country
* province
* district

---

## 2. roads

Stores vector features representing road network segments.

| Column | Type                 | Description                                   |
| ------ | -------------------- | --------------------------------------------- |
| id     | UUID                 | Primary key                                   |
| name   | TEXT                 | Road name                                     |
| type   | TEXT                 | Road category (highway, primary, residential) |
| geom   | GEOMETRY(LINESTRING) | Road geometry                                 |

This table supports spatial queries such as:

* road length calculations
* boundary intersections
* network visualization

---

## 3. buildings

Stores building footprint geometries.

| Column | Type              | Description                                                   |
| ------ | ----------------- | ------------------------------------------------------------- |
| id     | UUID              | Primary key                                                   |
| type   | TEXT              | Building classification (residential, commercial, industrial) |
| geom   | GEOMETRY(POLYGON) | Building footprint geometry                                   |

These features allow aggregation operations such as:

* building counts
* building type distributions
* urban density calculations

---

# Spatial Indexing

Spatial indexes are used to improve query performance.

Example index creation:

```
CREATE INDEX idx_roads_geom
ON roads
USING GIST (geom);
```

Similar indexes would be created for:

* `boundaries.geom`
* `buildings.geom`

These indexes enable efficient spatial filtering operations.

---

# Example Spatial Queries

## Retrieve roads within a boundary

```
SELECT r.*
FROM roads r
JOIN boundaries b
ON ST_Within(r.geom, b.geom)
WHERE b.code = 'KEN';
```

---

## Calculate total road length in a boundary

```
SELECT SUM(ST_Length(r.geom))
FROM roads r
JOIN boundaries b
ON ST_Within(r.geom, b.geom)
WHERE b.code = 'KEN';
```

---

## Count buildings by type

```
SELECT type, COUNT(*)
FROM buildings
GROUP BY type;
```

---

# Data Flow with the API

The database supports the following API operations:

| API Endpoint            | Database Operation           |
| ----------------------- | ---------------------------- |
| `/boundaries`           | Retrieve boundary geometries |
| `/layers/roads`         | Fetch roads within boundary  |
| `/statistics/roads`     | Aggregate road length        |
| `/statistics/buildings` | Building counts by type      |

Repository classes in the backend interact with this schema to execute spatial queries.

---

# Summary

The schema design supports scalable geospatial analysis through:

* PostGIS spatial data types
* efficient spatial indexing
* boundary-based filtering
* aggregation of vector features

This architecture enables the Geo Services API to efficiently serve geospatial layers and spatial statistics while remaining extensible for additional datasets such as waterways, land use, or points of interest.
