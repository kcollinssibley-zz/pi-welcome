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
