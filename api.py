from owslib.wfs import WebFeatureService
from owslib.wcs import WebCoverageService
import geojson

def get_features(wfs_url, layer, verbose=False):
    """Get feature from Web Feature Service (WFS) in GeoJSON format
    
    Input:
       wfs_url: URL for web feature service. E.g. http://www.aifdr.org:8080/geoserver/ows?
       layer: Feature layer name as <workspace>:<layer>
       verbose [optional]: Flag controlling the verbosity level. Default is False.
       
    Output:
       GEOJSON dictionary or None.
    """
    
    if verbose:
        print('Retrieving %s from %s' % (layer, wfs_url))
        
    wfs = WebFeatureService(wfs_url, version='1.0.0')
    
    if layer not in wfs.contents.keys():
        return None
    response = wfs.getfeature(typename=[layer], format='json')
    return geojson.loads(response.read())

def get_coverage(wcs_url, layer, verbose=False):
    """Get coverage from Web Coverage Service (WCS) in GeoTIFF format
    
    Input:
       wcs_url: URL for web ceature service. E.g. http://www.aifdr.org:8080/geoserver/ows?
       layer: Coverage layer name as <workspace>:<layer>
       verbose [optional]: Flag controlling the verbosity level. Default is False.
       
    Output:
       GeoTIFF data or None.    
    """
        
    if verbose:
        print('Retrieving %s from %s' % (layer, wcs_url))
            
    wcs = WebCoverageService(wcs_url, version='1.1.1')
    if layer not in wcs.contents.keys():
        return None

    response = wcs.getcoverage(typename=[layer], format='GeoTIFF')
    return response
