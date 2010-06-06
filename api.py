from geoserver.catalog import Catalog
import ogr
from shapely.wkb import loads
import urllib
import os
import tempfile

GEOSERVER_BASE_URL = "http://localhost:8080/geoserver/"
WFS_BASE_URL = GEOSERVER_BASE_URL + "ows?service=WFS&version=1.0.0&request=GetFeature&outputFormat=SHAPE-ZIP&typeName="
POLITICAL_LAYER = "district"

def download_shapefile(shapefile_url, verbose=True):
    """Download shapefile zip from url and unpack into a temporary directory
    Return basename of shape files
    """

    temp_dir = tempfile.mkdtemp(dir='.')
    shape_archive = 'shape_archive.zip'   
    if verbose:
        print ('Retrieving URL %s' % shapefile_url)
    urllib.urlretrieve(shapefile_url, shape_archive)

    # Unpack
    s = 'unzip %s -d %s' % (shape_archive, temp_dir)
    if verbose:
        print(s)
    os.system(s)

    # Get shape file base name
    for filename in os.listdir(temp_dir):
        basename, ext = os.path.splitext(filename)
        if ext == '.shp': 
            break
    
    return temp_dir, basename


def open_shapefile(shapefile, verbose=True):
    """Create a numpy array from a shapefile 
    (and downloads it if it's not a local file)
    """

    # Convert
    print 'shapfile', shapefile
    source = ogr.Open(shapefile)
    print 'source', source
    print dir(source)
    #borders = source.GetLayerByName("default") 
    #print borders
    # ... to be continued

catalog = Catalog(GEOSERVER_BASE_URL + "rest")
layer = catalog.get_layer(POLITICAL_LAYER)

print layer.name

tmpdir, basename = download_shapefile(WFS_BASE_URL+layer.name)
print tmpdir, basename
open_shapefile(os.path.join(tmpdir, basename + '.shp'))

