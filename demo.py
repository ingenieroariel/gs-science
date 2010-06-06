"""This is an example of using the Geoserver API
"""
from api import get_features

GEOSERVER_BASE_URL = "http://localhost:8080/geoserver/"
WFS_URL = GEOSERVER_BASE_URL + "wfs?"

POLITICAL_LAYER = "testing:district"
POPULATION_LAYER = "rastert_ispop201"

data = get_features(wfs_url=WFS_URL, layer=POLITICAL_LAYER)

print "CRS: ", data["crs"]
print "Number of features:", len(data["features"])
