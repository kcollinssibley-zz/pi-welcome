import datetime

import requests

from pi_welcome.app import config
from pi_welcome.lib.common import checkStatus
from pi_welcome.lib.common import est

MBTA_API = 'https://api-v3.mbta.com/predictions'

# TODO(KCS): Add MBTA Alerts functionality

def getMBTAPredictions():
    station_data = []

    stations = config.getStations()
    for station in stations:
        stop = station['id']
        direction = station['direction']

        url = ''.join([
            MBTA_API,
            '?sort=arrival_time',
            '&filter%5Bdirection_id%5D=',
            str(direction),
            '&filter%5Bstop%5D=',
            str(stop)])

        resp = requests.get(url)

        if checkStatus(resp):
            raw_data = resp.json()
            data = {}
            data['name'] = station['name']
            data['distance'] = station['distance']

            trains = raw_data['data']
            for i in range(len(trains)):
                # 2019-07-12T23:35:25-04:00
                train_arrival = datetime.datetime.strptime(
                    trains[i]['attributes']['arrival_time'],
                    '%Y-%m-%dT%H:%M:%S%z')
                now = datetime.datetime.now(est)
                delta = datetime.timedelta(minutes=data['distance'])
                station_arrival = now + delta

                if train_arrival > station_arrival:
                    data['atbat'] = trains[i]
                    data['ondeck'] = trains[(i+1):(i+3)]
                    break
                else:
                    print("train arrival: {} vs station_arrival: {}".format(
                        train_arrival.time(),
                        station_arrival.time()))

            station_data.append(data)
        else:
            error = resp.json()
            data = {
                'name': station['name'],
                'status_code': resp.status_code,
                'error': error
            }
            station_data.append(data)

    return station_data
