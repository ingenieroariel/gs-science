from geoserver.catalog import Catalog
import ogr
from shapely.wkb import loads
import urllib
import os

GEOSERVER_BASE_URL = "http://localhost:8080/geoserver/"
WFS_BASE_URL = GEOSERVER_BASE_URL + "ows?service=WFS&version=1.0.0&request=GetFeature&outputFormat=SHAPE-ZIP&typeName="
POLITICAL_LAYER = "district"

def open_shapefile(shapefile_url):
    """
    Creates a numpy array from a shapefile 
    (and downloads it if it's not a local file)
    """

    shape_archive = 'shape_archive.zip'   
    print 'URL', shapefile_url
    urllib.urlretrieve(shapefile_url, shape_archive)

    # Unpack
    s = 'unzip %s' % shape_archive
    print s
    os.system(s)
    #T = F.readlines()
    #print shapefile_url, T

    #source = ogr.Open(shapefile_url)
    #borders = source.GetLayerByName("default") 
    # ... to be continued

catalog = Catalog(GEOSERVER_BASE_URL + "rest")
layer = catalog.get_layer(POLITICAL_LAYER)

print layer.name

open_shapefile(WFS_BASE_URL+layer.name)
