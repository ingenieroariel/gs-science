from owslib.wfs import WebFeatureService
from owslib.wcs import WebCoverageService
import geojson

def get_features(wfs_url, layer, verbose=False):

    if verbose:
        print('Retrieving %s from %s' % (layer, wfs_url))
    wfs = WebFeatureService(wfs_url, version='1.0.0')
    if layer not in wfs.contents.keys():
        return None
    response = wfs.getfeature(typename=[layer], format='json')
    return geojson.loads(response.read())

def get_coverage(wcs_url, layer):
    wcs = WebCoverageService(wcs_url, version='1.1.1')
    if layer not in wcs.contents.keys():
        return None

    response = wcs.getcoverage(typename=[layer], format='GeoTIFF')
    return response
