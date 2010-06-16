"""This is an example of using the Geoserver API
"""
from api import get_features, get_coverage
from numpy import array

GEOSERVER_URL = 'http://www.aifdr.org:8080/geoserver/ows?'

POLITICAL_LAYER = 'test:gadm_IDN_1'
POPULATION_LAYER = 'test:gazette'

data = get_features(wfs_url=GEOSERVER_URL, layer=POLITICAL_LAYER, verbose=True)

# This data is in the GEOJSON format. We need to think about a workable
# Python structure that will allow access to the numerical data as
# a consecutive array

# The following explores how to unpack GEOJSON for this example.
def traverse_dict(x, space = ''):
    """Determine the structure of dictionary
    """
    try:
        keys = x.keys()
    except:
        print str(len(x))        
    else:    
        print
        for key in x.keys():
            print space + key + ': ',
            traverse_dict(x[key], space = space + '  ')

# Unpack GeoJSON
print 'Exploring GeoJSON dictionary'
traverse_dict(data)

print 'CRS: ', data['crs']
print 'Type: ', data['type']
print 'Number of features:', len(data['features'])

assert data['type'] == 'FeatureCollection'

number_of_points = 0
for i, feature in enumerate(data['features']):
    print
    print '--------------------------------' 
    print 'Id:', feature['id']
    #print 'Name:', feature['geometry_name']    # Seems to be always 'the_geom'.....
    print 'Type:', feature['type']
    print 'Properties [%i]:' % len(feature['properties'])
    for property in feature['properties']:
        print '   ', property + ':', feature['properties'][property]
        
    print 'Geometry: %s' % (feature['geometry']['type']) 
    print '    Number of polygons: %i' % len(feature['geometry']['coordinates'])
    for polygon in feature['geometry']['coordinates']:
        assert len(polygon) == 1, 'Holes not expected for this dataset'
        for ring in polygon:
            A = array(ring)
            assert A.shape[1] == 2, 'This was not a polygon'
            #print '    Polygon dimensions:', A.shape
            number_of_points += A.shape[0]
    print

print 'Total number of points in polygons:', number_of_points

print
raster_data = get_coverage(wcs_url=GEOSERVER_URL, layer=POPULATION_LAYER, verbose=True)
print raster_data
