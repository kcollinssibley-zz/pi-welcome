from flask import jsonify

from pi_welcome.app import app
from pi_welcome.lib import mbtalib


@app.route('/api/mbta')
def MBTAPredictions():
    return jsonify(mbtalib.getMBTAPredictions())
