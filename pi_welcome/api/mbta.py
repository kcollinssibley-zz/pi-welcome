from pi_welcome import app

MBTA_API = 'https://api-v3.mbta.com'
ROXBURY_ID = '70009'
INBOUND_DIR = '1'


@app.app.route('/api/mbta')
def getMBTAPredition():
    return 'TODO(KCS): call MBTA lib function here'
