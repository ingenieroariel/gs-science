"""This is an example of using the Geoserver API
"""
from api import get_features, get_coverage

GEOSERVER_URL = "http://localhost:8080/geoserver/ows?"

POLITICAL_LAYER = "testing:district"
POPULATION_LAYER = "population"

data = get_features(wfs_url=GEOSERVER_URL, layer=POLITICAL_LAYER)

print "CRS: ", data["crs"]
print "Number of features:", len(data["features"])

#raster_data = get_coverage(wcs_url=GEOSERVER_URL, layer=POPULATION_LAYER)
#print raster_data
