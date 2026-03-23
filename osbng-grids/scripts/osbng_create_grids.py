"""Create BNG grid square data at multiple resolutions over the BNG index system bounds.

Data generation uses the __geo_interface__ (https://gist.github.com/sgillies/2217756)
representation of BNG grid squares, a GeoJSON-like mapping which enables integration
with the GeoPandas (https://github.com/geopandas/geopandas) Python package.

Data saved as Parquet (https://github.com/apache/parquet-format/) using the native
GEOMETRY logical type, GeoParquet (https://github.com/opengeospatial/geoparquet)
and GeoPackage (GPKG) at 100km, 50km, 10km, 5km and 1km resolutions.
"""

import geoarrow.pyarrow as ga
import geopandas as gpd
import pyarrow as pa
from osbng.grids import (
    bng_grid_1km,
    bng_grid_5km,
    bng_grid_10km,
    bng_grid_50km,
    bng_grid_100km,
)
from pyarrow import parquet

# Grid square data covering the BNG index system bounds at 100km, 50km, 10km, 5km
# and 1km resolutions
# Provided as iterators of GeoJSON-like mappings using the __geo_interface__ protocol
# Datasets
datasets = [bng_grid_100km, bng_grid_50km, bng_grid_10km, bng_grid_5km, bng_grid_1km]
# Resolutions
resolutions = ["100km", "50km", "10km", "5km", "1km"]

# Save each dataset as GeoParquet and GPKG
for dataset, resolution in zip(datasets, resolutions):
    # Create GeoPandas GeoDataFrame from each dataset
    # Set GeoDataFrame coordinate reference system to British National Grid (EPSG:27700)
    # https://epsg.io/27700
    gdf = gpd.GeoDataFrame.from_features(dataset, crs=27700)

    # Save GeoDataFrame to Parquet
    # Uses the native GEOMETRY logical type
    table = pa.table(gdf.to_arrow())
    parquet.write_table(table, f"../data/parquet/osbng_grid_{resolution}.parquet")

    # Save GeoDataFrame to GeoParquet
    gdf.to_parquet(
        f"../data/geoparquet/osbng_grid_{resolution}.parquet",
        index=False,
        write_covering_bbox=True,
        schema_version="1.1.0",
    )

    # Save GeoDataFrame to GPKG
    gdf.to_file(
        "../data/geopackage/osbng_grids.gpkg",
        layer=f"osbng_grid_{resolution}",
        driver="GPKG",
        index=False,
    )
