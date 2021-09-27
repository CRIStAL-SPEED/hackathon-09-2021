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

This package is an .osm.pbf (OpenStreetMap Protocolbuffer Binary Format files) parser based on [Geopandas](https://geopandas.org/).
After installing the library:
```
pip3 install pyrosm
```
You can ether [download a map from a web site](https://download.geofabrik.de/) or download it directly with the command:
I recommend to download the map before, to avoid a very long wait.
```
from pyrosm import OSM, get_data
fp = get_data("nord_pas_de_calais")
```
with fp being the file path.
After that you can specified this maps on the pyrosm constructor:
```
osm = OSM("../map/map.osm", bounding_box=[3.127, 50.603, 3.153, 50.616])
```
The bounding_box argument can be used to reduced the size of loaded map.
Yon can then load the features that you want as geodataframe:
You can load the network:
```
drive_net = osm.get_network(network_type="driving")
```
the buildings:
```
buildings = osm.get_buildings()
```
the points of interset:
```
pois = osm.get_pois()
```
the landuse:
```
landuse = osm.get_landuse()
```
the nature:
```
natural = osm.get_natural()
```
the administrative boundaries:
```
boundaries = osm.get_boundaries()
```
or use a custom filter for any [map features](https://wiki.openstreetmap.org/wiki/Map_features):
```
custom_data = osm.get_data_by_custom_criteria(	custom_filter={
						'key1': ['value1', 'value2'],
						'key2': ['value3', 'value4', 'value5']}
						filter_type="keep",
						keep_nodes=False,
						keep_ways=True,
						keep_relations=True)
```
You can plot any of these geodataframe with:
```
landuse.plot(column='landuse', legend=True)
```
These arguments can be used to obtain a legend of every values present in the data.

You can also use [NetworkX](https://networkx.org/) and [OSMnx](https://github.com/gboeing/osmnx) for [map matching and shortest path computation](https://pyrosm.readthedocs.io/en/latest/graphs.html).

