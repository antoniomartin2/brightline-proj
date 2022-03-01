import glob
import os
import pickle
from datetime import datetime

from brightline.addressParser import AddressParser
from brightline.dataParser import DataParser
from brightline.exporter import Exporter
from brightline.geoContainer import GeoContainer


def get_latest_dump():
    path = os.getcwd() + '/resources/.data/*.container'
    dumps = glob.glob(path)
    if not dumps:
        return None
    else:
        newest = max(dumps, key=os.path.getctime)
        return newest


def main():
    start_time = datetime.now()
    dump = get_latest_dump()
    if dump:
        filehandler = open(dump, 'rb')
        container = pickle.load(filehandler)

    else:
        data_parser = DataParser(os.getcwd() + '/resources/CleanData_UCBerkeley.csv')
        container = data_parser.read()
        address_parser = AddressParser(os.getcwd() + '/resources/InternalLocData.csv')
        addr_dict = address_parser.read()
        container.merge_dict(addr_dict)
        container.save()

    export = Exporter(container)
    export.generate_geoJSON()
    end_time = datetime.now()
    print('completed in {} seconds'.format(end_time-start_time))


if __name__ == '__main__':
    main()
