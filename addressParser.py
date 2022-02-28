# Parses address file to match sensors to locations
import time

from geopy.exc import GeocoderTimedOut
from geopy.geocoders import Nominatim


class AddressParser:
    def __init__(self, file):
        self.file = open(file, "r")
        self.data = dict()
        self.geolocator = Nominatim(user_agent="brightline_proj_app")

    # Reads CSV data
    # Outputs a set of the data
    # Format:
    # SITE_NAME | ID | OPENMAP_NAME | HOOD | INSTALLDATE | PASTMOVE |
    # DATALOSS | READ_FREQ | FREQ_START_DATE | NEARBY_WX | ADDR | HEIGHT |
    # LOC | GROUND_ADJ_HEIGHT | TRAFFIC_DIST | ACCESSIBILITY | GRP | GOALS |
    # INTERSECTION | ONEWAY
    def read(self):
        # Set of visited names and sensors
        sensors = dict()

        # Skip headers
        self.file.readline()
        line = self.file.readline()
        while len(line) > 0:
            arr = line.split(",")
            id = arr[1]
            addr = arr[10]

            def get_address(address, attempt=0, max=15):
                try:
                    ret = self.geolocator.geocode(address)
                    time.sleep(1)
                    return ret
                except GeocoderTimedOut:
                    if attempt < max:
                        time.sleep(1)
                        return get_address(address, attempt=attempt + 1)
                    raise

            loc = get_address(addr)
            coords = tuple([addr, loc.latitude, loc.longitude])
            sensors[id] = coords

            # Go to next
            line = self.file.readline()
        self.data = sensors
        return self.data

