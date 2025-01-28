# OSBNG Grids

Grid datasets for the Ordnance Survey British National Grid (BNG) index system at a variety of resolutions.

## Overview

These datasets include grid square boundaries and associated identifiers as BNG references covering the bounds `(0, 0, 700000, 1300000)` of the BNG index system. The data is available in GeoParquet and GeoPackage formats. Additionally, the repository includes a Python script and a Jupyter notebook for generating the grid data using the [`OSBNG`](https://github.com/OrdnanceSurvey/osbng-py) Python package.

## Resolutions

Grid data is provided for the following 'standard' and 'intermediate' (quadtree) resolutions:

* 100km
* 50km
* 10km
* 5km
* 1km

Grid data for finer BNG resolutions and for different coverages can be derived by applying the same generation logic against different resolutions and bounds.

## British National Grid

The Ordnance Survey (OS) BNG index system (also known as the OS National Grid) is a rectangular Cartesian 700 x 1300km grid system based upon the transverse Mercator projection. In the BNG, locations are specified using coordinates, eastings (x) and northings (y), measured in meters from a defined origin point (0, 0) southwest of the Isles of Scilly off the coast of Cornwall, England. Values increase to the northeast, covering all of mainland GB and surrounding islands.

The BNG index system is structured using a hierarchical system of grid squares at various resolutions. The BNG uses BNG references, also known more simply as grid or tile references, as grid square identifiers. At its highest level, the grid divides GB into 100 km by 100 km squares, each identified by a two-letter code. Successive levels of resolution further subdivide the grid squares into finer detail, down to individual 1-meter squares.

## Licence

Please acknowledge Ordnance Survey when using the grid datasets.

The code used to generate the data is provided under the terms of the `MIT` licence.

The datasets, in both GeoPackage and GeoParquet formats, are provided under the terms of the [Open Government Licence (OGL) v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/).

![The Open Government Licence (OGL) v3.0 logo](https://www.nationalarchives.gov.uk/images/infoman/ogl-symbol-41px-retina-black.png "Open Government Licence (OGL) v3.0 Logo")
