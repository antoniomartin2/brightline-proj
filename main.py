import glob
import os
import pickle
from datetime import datetime

from addressParser import AddressParser
from dataParser import DataParser
from exporter import Exporter


# TODO Implement function to detect the latest dump and select it
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
        data_parser = DataParser(os.getcwd() + '/resources/airqualitydata082020_122021.csv')
        container = data_parser.read()
        address_parser = AddressParser(os.getcwd() + '/resources/Brightline AQ Monitoring Network - Technical COPY - Network Information.csv')
        addr_dict = address_parser.read()
        container.merge_dict(addr_dict)
        container.save()

    export = Exporter(container)
    export.generate_geoJSON()
    end_time = datetime.now()
    print('completed in {} seconds'.format(end_time-start_time))


if __name__ == '__main__':
    main()
