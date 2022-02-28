# Exports the data in the geoContainer
# to an ArcGIS compatible format.
import os

import geojson
from geojson import Feature, Point, FeatureCollection


class Exporter:
    def __init__(self, container):
        self.geo = container

    def generate_geoJSON(self):
        outfile = open(os.getcwd() + '/resources/dumps/geojson_out_{}'.format(self.geo.__hash__()), "x")
        geolist = []
        dict = self.geo.dict
        for id in dict.keys():
            if dict[id].coords:
                point = Point(dict[id].coords)
                feature = Feature(id=id, geometry=point)
                geolist.append(feature)
            else:
                print('Error: No Coordinates/Address for ID {}'.format(id))
        collection = FeatureCollection(geolist)
        dump = geojson.dumps(collection)
        outfile.write(dump)
