# Geo Services API

This is the README file for the geo-services-api project.

Database Choice

The system is designed around PostgreSQL with the PostGIS extension.

Reasons for this choice:

- industry-standard geospatial database
- native support for spatial indexing (GiST)
- advanced spatial operations (ST_Intersects, ST_Within, ST_Length)
- efficient handling of large vector datasets
- compatibility with GIS ecosystems (QGIS, GeoServer, GDAL)

Example spatial query used by the API:

SELECT SUM(ST_Length(geom))
FROM roads
JOIN boundaries
ON ST_Within(roads.geom, boundaries.geom)
WHERE boundaries.code = 'BG';
