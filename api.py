from owslib.wfs import WebFeatureService
from owslib.wcs import WebCoverageService
import geojson

def get_features(wfs_url, layer):
    wfs = WebFeatureService(wfs_url, version='1.0.0')
    if layer not in wfs.contents.keys():
        return None
    response = wfs.getfeature(typename=[layer], format="json")
    return geojson.loads(response.read())
