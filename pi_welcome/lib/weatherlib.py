import requests

from pi_welcome.app import config
from pi_welcome.lib.common import checkStatus

WEATHER_API = "http://dataservice.accuweather.com/forecasts/v1/daily/1day/";

def getWeatherUpdate():
    weather_key = config.getWeatherLocation()
    api_key = config.getWeatherApiKey()

    url = ''.join([
        WEATHER_API,
        str(weather_key),
        "?apikey=",
        api_key])

    resp = requests.get(url)

    if checkStatus(resp):
        return resp.json()
    else:
        error = resp.json()
        return {
            'status_code': resp.status_code,
            'error': error
        }
