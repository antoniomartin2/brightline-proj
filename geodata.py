# Object to store AQ data geographically

class GeoData:

    # Object will store the ID, Name, Neighborhood,
    # Calibrated PM2.5, and Humidity data
    # TODO Implement storage of coordinates and address
    def __init__(self, id, name, hood):
        self.id = id
        self.name = name
        self.neighborhood = hood
        self.address = None
        self.coords = None
        self.pm_dict = dict()
        self.hum_dict = dict()

    def add_data(self, pm, hum, date):
        self.pm_dict[date] = pm
        self.hum_dict[date] = hum