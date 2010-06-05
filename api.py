from geoserver.catalog import Catalog
#import ogr
from shapely.wkb import loads

GEOSERVER_BASE_URL = "http://localhost:8080/geoserver/"
WFS_BASE_URL = "ows?service=WFS&version=1.0.0&request=GetFeature&outputFormat=SHAPE-ZIP&typeName="
POLITICAL_LAYER = "district"

def open_shapefile(shapefile_url):
    """
    Creates a numpy array from a shapefile 
    (and downloads it if it's not a local file)
    """
    source = ogr.Open(shapefile_url)
    borders = source.GetLayerByName("default") 
    # ... to be continued

catalog = Catalog(GEOSERVER_BASE_URL + "rest")
layer = catalog.get_layer(POLITICAL_LAYER)

print layer
