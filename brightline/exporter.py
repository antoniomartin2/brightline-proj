# Exports the data in the geoContainer
# to an ArcGIS compatible format.
import copy
import os

import geojson
from geojson import Feature, Point, FeatureCollection


class Exporter:
    def __init__(self, container):
        self.geo = container

    # TODO generate 4 files, one per season
    def generate_geoJSON(self):
        outfileAvg = open(os.getcwd() + '/resources/dumps/geojson_{}'.format(self.geo.__hash__()), "x")
        geolistAvg = []
        dict = self.geo.dict
        for id in dict.keys():
            if dict[id].coords:
                props_dict = vars(dict[id])
                dict_avg = copy.deepcopy(props_dict)
                pmd = dict_avg.pop("pm_dict")
                hmd = dict_avg.pop("hum_dict")

                average_humidity = 0
                hmc = 0
                average_pm25 = 0
                pmc = 0
                
                for key in pmd.keys():
                    if pmd[key] != "NA":
                        pmc += 1
                        average_pm25 += float(pmd[key])
                    if hmd[key] != "NA":
                        average_humidity += float(hmd[key])
                        hmc += 1
                average_pm25 = average_pm25/pmc
                average_humidity = average_humidity/hmc

                dict_avg["average_pm2.5"] = average_pm25
                dict_avg["average_humidity"] = average_humidity

                point = Point((dict[id].coords[1], dict[id].coords[0]))
                feature = Feature(geometry=point, properties=dict_avg)
                geolistAvg.append(feature)
            else:
                print('Error: No Coordinates/Address for ID {}'.format(id))

        collectionAvg = FeatureCollection(geolistAvg)
        dumpAvg = geojson.dumps(collectionAvg)
        outfileAvg.write(dumpAvg)
