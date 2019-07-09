import requests

from pi_welcome.app import config

MBTA_API = 'https://api-v3.mbta.com/predictions'

# TODO(KCS): Add MBTA Alerts functionality

# TODO(KCS): Add logging
def checkStatus(resp):
    status = resp.status_code
    if status == 200:
        print("200, Good")
        return True
    elif status == 400:
        print("400, Invalid sort key")
    elif status == 403:
        print("403 Forbidden")
    elif status == 429:
        print("429 Too many requests")
    else:
        print("Unknown status code: {}".format(status))

    return False

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
            data = resp.json()
            data['name'] = station['name']

            station_data.append(data)
        else:
            data = {
                'name': station['name'],
                'status_code': resp.status_code,
                'message': resp.status
            }
            station_data.append(data)

    return station_data
