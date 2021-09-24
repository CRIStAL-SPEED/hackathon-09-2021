# Map

## [Contextily](https://contextily.readthedocs.io)

This package display tile maps coming from an url or local images using matplotlib.

After intalling it:
```
pip3 install contextily
```
You can easily add a background map with matplotlib:
```
import matplotlib.pyplot as plt
import contextily as ctx

plt.figure('OSM map')
ax = plt.gca()
plt.xlim(3.13, 3.15)
plt.ylim(50.60, 50.62)
ctx.add_basemap(ax, source=ctx.providers.OpenStreetMap.France, crs='EPSG:4326')
plt.show()
```
Multiple maps are available in [``` ctx.providers ```](https://github.com/leaflet-extras/leaflet-providers), you can also make a new dictionary with any url with the tags {x} (longitude), {y} (latitude), {z} (zoom) and eventualy others like {s} (subdomain), such as:
```
arcgis =    {'url': 'http://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}.png',
             'attribution': 'Source: Esri, Maxar, GeoEye, Earthstar Geographics, CNES/Airbus DS, USDA, USGS, AeroGRID, IGN, and the GIS User Community',
             'min_zoom': 1,
             'max_zoom': 19,
             'name': 'ArcGIS'}
```
The CRS (Coordinate Reference Systems) is a code, such as, EPSG:4326 if you use WGS84 longitude and latitude coordinates for exemple.

## [Pyrosm](https://pyrosm.readthedocs.io)

This package is an OpenStreetMap Protocolbuffer Binary Format files (.osm.pbf) parser based on [Geopandas](https://geopandas.org/).

You can also use [NetworkX](https://networkx.org/) and [OSMnx](https://github.com/gboeing/osmnx) for [map matching and shortest path computation](https://pyrosm.readthedocs.io/en/latest/graphs.html).
[https://wiki.openstreetmap.org/wiki/Map_features](https://wiki.openstreetmap.org/wiki/Map_features)
