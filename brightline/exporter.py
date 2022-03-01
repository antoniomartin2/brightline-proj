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
                props_dict = vars(dict[id])
                props_dict.pop("pm_dict")
                props_dict.pop("hum_dict")
                point = Point((dict[id].coords[1], dict[id].coords[0]))
                feature = Feature(geometry=point, properties=props_dict)
                geolist.append(feature)
            else:
                print('Error: No Coordinates/Address for ID {}'.format(id))
        collection = FeatureCollection(geolist)
        dump = geojson.dumps(collection)
        outfile.write(dump)
