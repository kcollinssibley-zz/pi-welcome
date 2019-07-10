import requests

from pi_welcome.app import config

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

    return resp['Headline']
