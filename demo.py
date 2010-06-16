"""This is an example of using the Geoserver API
"""
from api import get_features, get_coverage

GEOSERVER_URL = 'http://www.aifdr.org:8080/geoserver/ows?'

POLITICAL_LAYER = 'test:gadm_IDN_1'
POPULATION_LAYER = 'test:gazette'

data = get_features(wfs_url=GEOSERVER_URL, layer=POLITICAL_LAYER, verbose=True)

# This data is in the GEOJSON format. We need to think about a workable
# Python structure that will allow access to the numerical data as
# a consecutive array
print 'CRS: ', data['crs']
print 'Number of features:', len(data['features'])

#raster_data = get_coverage(wcs_url=GEOSERVER_URL, layer=POPULATION_LAYER)
#print raster_data
