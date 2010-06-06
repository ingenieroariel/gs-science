import ogr
from shapely.wkb import loads
import urllib
import os
import tempfile
from owslib.wfs import WebFeatureService
from owslib.wcs import WebCoverageService
import geojson

GEOSERVER_BASE_URL = "http://localhost:8080/geoserver/"
WFS_URL = GEOSERVER_BASE_URL + "wfs?"
POLITICAL_LAYER = "testing:district"

def get_layer(layer=POLITICAL_LAYER):
    wfs = WebFeatureService(WFS_URL, version='1.0.0')
    if layer not in wfs.contents.keys():
        return None
    response = wfs.getfeature(typename=[layer], format="json")
    return geojson.loads(response.read())

print get_layer()
