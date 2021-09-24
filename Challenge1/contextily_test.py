#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 09:58:51 2021

@brief: Basic contextily used for map display

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
import contextily as ctx

arcgis =    {'url': 'http://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}.png',
             'attribution': '(C) OpenStreetMap contributors, Imagery Source: Esri, Maxar, GeoEye, Earthstar Geographics, CNES/Airbus DS, USDA, USGS, AeroGRID, IGN, and the GIS User Community',
             'min_zoom': 1,
             'max_zoom': 19,
             'name': 'ArcGIS'}

plt.figure('OSM map')
ax = plt.gca()
plt.xlim(3.13, 3.15)
plt.ylim(50.60, 50.62)
ctx.add_basemap(ax, source=ctx.providers.OpenStreetMap.France, crs='EPSG:4326')
ctx.add_basemap(ax, source=arcgis, crs='EPSG:4326', alpha=0.5)
plt.show()