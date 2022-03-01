# Parses CSV files provided by Brightline
from brightline.geoContainer import GeoContainer
from brightline.geoData import GeoData


class DataParser:
    def __init__(self, file):
        self.file = open(file, "r")
        self.data = dict()

    # Reads lines from the CSV data
    # Outputs a set of the data
    # Format:
    # NUM | ID | DATE | CALIBRATED | RAW | HUM | NAME | HOOD
    def read(self):
        # Set of visited names and sensors
        sensors = dict()

        # Skip headers
        self.file.readline()
        line = self.file.readline()
        while len(line) > 0:
            arr = line.split(",")

            # Follow control flow for update
            if arr[1] in sensors.keys():
                to_update = sensors[arr[1]]
                date = arr[2]
                pm = arr[3]
                hum = arr[5]
                to_update.add_data(pm, hum, date)

            # Follow control flow for new addition
            else:
                id = arr[1]
                date = arr[2]
                pm = arr[3]
                hum = arr[5]
                name = arr[6]
                hood = arr[7]
                to_add = GeoData(id, name, hood)
                to_add.add_data(pm, hum, date)
                sensors[id] = to_add
            line = self.file.readline()
        self.data = sensors
        container = GeoContainer(self.data)
        return container

