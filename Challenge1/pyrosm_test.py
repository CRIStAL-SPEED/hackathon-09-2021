#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 11:09:06 2021

@brief: Basic pyrosm test used for OSM map request

@author: Elwan Héry

@license: MIT License

Copyright © 2020 Elwan Héry

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the “Software”), to deal in
the Software without restriction, including without limitation the rights to 
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies 
of the Software, and to permit persons to whom the Software is furnished to do 
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all 
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
SOFTWARE.
"""

import matplotlib.pyplot as plt
from pyrosm import OSM
import contextily as ctx

osm = OSM("../map/nord-pas-de-calais-latest.osm.pbf", bounding_box=[3.127, 50.603, 3.153, 50.616])

buildings = osm.get_buildings()
crs = buildings.estimate_utm_crs()
buildings = buildings.to_crs(crs)

construction = osm.get_landuse(custom_filter={'landuse':["construction", "brownfield", "garages", "landfill"]})
construction = construction.to_crs(crs)


road_nodes, road_edges = osm.get_network(nodes=True, network_type="driving")
road_nodes = road_nodes.to_crs(crs)
road_edges = road_edges.to_crs(crs)

routes = ["railway", "subway", "train", "tram", "trolleybus"]
rails = ["tramway", "light_rail", "rail", "subway", "tram"]

rails = osm.get_data_by_custom_criteria(custom_filter={
                                        'route': routes,
                                        'railway': rails,
                                        'public_transport': True},
                                        filter_type="keep",  
                                        keep_nodes=False, 
                                        keep_ways=True, 
                                        keep_relations=True)
rails = rails.to_crs(crs)

bridges = osm.get_data_by_custom_criteria(custom_filter={
                                        'bridge': ['yes'],
                                        'tunnel': ['yes']},
                                        filter_type="keep",
                                        keep_nodes=False, 
                                        keep_ways=True, 
                                        keep_relations=True)
bridges = bridges.to_crs(crs)


grass = osm.get_data_by_custom_criteria(custom_filter={
                                        'landuse':["farmland", "grass", "meadow", "landfill", "allotments", "farmyard", "flowerbed", "vineyard", "greenfield", "greenhouse_horticulture", "plant_nursery", "village_green"],
                                        'natural':["scrub", "heath", "grassland"],
                                        'leisure': ['garden', 'park', 'elevation']},
                                        filter_type="keep",
                                        keep_nodes=False, 
                                        keep_ways=True, 
                                        keep_relations=True)
grass = grass.to_crs(crs)


trees = osm.get_data_by_custom_criteria(custom_filter={
                                        'landuse':["forest", "orchard"],
                                        'barrier': ['hedge'],
                                        'natural':["tree", "tree_row", "wood"]},
                                        filter_type="keep",
                                        keep_nodes=False, 
                                        keep_ways=True, 
                                        keep_relations=True)
trees = trees.to_crs(crs)


walls = osm.get_data_by_custom_criteria(custom_filter={
                                        'barrier': ['city_wall', 'ditch', 'retaining_wall', 'wall']},
                                        filter_type="keep",
                                        keep_nodes=False, 
                                        keep_ways=True, 
                                        keep_relations=True)
walls = walls.to_crs(crs)


water = osm.get_data_by_custom_criteria(custom_filter={
                                        'natural':["water", "wetland"],
                                        'landuse':["basin"],
                                        'man_made': ['wastewater_plant', 'water_works'],
                                        'waterway': ['river', 'riverbank', 'stream', 'tidal_channel', 'canal', 'drain', 'ditch']},
                                        filter_type="keep",
                                        keep_nodes=False, 
                                        keep_ways=True, 
                                        keep_relations=True)
water = water.to_crs(crs)

arcgis =    {'url': 'http://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}.png',
             'attribution': '(C) OpenStreetMap contributors, Imagery Source: Esri, Maxar, GeoEye, Earthstar Geographics, CNES/Airbus DS, USDA, USGS, AeroGRID, IGN, and the GIS User Community',
             'min_zoom': 1,
             'max_zoom': 19,
             'name': 'ArcGIS'}


plt.figure('OSM')
plt.clf()
ax_osm = plt.gca()
buildings.plot(ax=ax_osm, color='red')
walls.plot(ax=ax_osm, color='magenta')
construction.plot(ax=ax_osm, color='orange')
road_edges.plot(ax=ax_osm, color='grey', CapStyle='round')
rails.plot(ax=ax_osm, color='purple')
bridges.plot(ax=ax_osm, color='yellow')
grass.plot(ax=ax_osm, color='lightgreen')
trees.plot(ax=ax_osm, color='green')
water.plot(ax=ax_osm, color='blue')

ctx.add_basemap(ax_osm, source=arcgis, crs=crs.to_string(), alpha=0.8, zoom=15)

plt.show()