"""This is an example of using the Geoserver API
"""

from api import Catalog, download_shapefile, read_shapefile, download_rasterfile
import os

GEOSERVER_BASE_URL = "http://localhost:8080/geoserver/"
WFS_SHP_BASE_URL = GEOSERVER_BASE_URL + "ows?service=WFS&version=1.0.0&request=GetFeature&outputFormat=SHAPE-ZIP&typeName="

#WFS_RASTER_BASE_URL = GEOSERVER_BASE_URL + 
#http://localhost:8080/geoserver/wms?service=WMS&version=1.1.0&request=GetMap&layers=Indonesia:rastert_ispop201&styles=&bbox=91.57,-13.155,146.112,7.32&width=879&height=330&srs=EPSG:4326&format=image/tiff


POLITICAL_LAYER = "district"
POPULATION_LAYER = "rastert_ispop201"




catalog = Catalog(GEOSERVER_BASE_URL + "rest")

# FIXME (Ole): I would like to be able to determine if the layer is vector or raster

# Get the vector layer
layer = catalog.get_layer(POLITICAL_LAYER)
print layer.name
tmpdir, basename = download_shapefile(WFS_SHP_BASE_URL+layer.name)
print tmpdir, basename
read_shapefile(os.path.join(tmpdir, basename + '.shp'))

# Get the raster layer
#layer = catalog.get_layer(POPULATION_LAYER)
#download_rasterfile(WFS_BASE_URL+layer.name)


