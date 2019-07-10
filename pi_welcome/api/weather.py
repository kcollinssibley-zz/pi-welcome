from flask import jsonify

from pi_welcome.app import app
from pi_welcome.lib import weatherlib

@app.route('/api/weather')
def WeatherPrediction():
    return jsonify(weatherlib.getWeatherUpdate())
