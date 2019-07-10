import yaml

class Config(object):
    def __init__(self):
        self.config = {}


    def load(self, path):
        with open(path) as f:
            self.config = yaml.safe_load(f)
            if not self.config:
                self.config = {}


    def getStations(self):
        return self.config['mbta_stations']

    def getWeatherLocation(self):
        return self.config['weather_location']

    def getWeatherApiKey(self):
        return self.config['api_keys']['weather']
