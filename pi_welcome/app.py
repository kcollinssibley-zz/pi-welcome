import argparse
import os
import sys

import yaml

from flask import Flask, render_template

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

import pi_welcome.mbta

config = None


@app.route('/hello')
def helloWorld():
    return 'Hello World!'


@app.route('/')
def homepage():
    return index()


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/contactus')
def contactUs():
    return render_template('contactus.html')


def main():
    parser = argparse.ArgumentParser(
        description='A morning information dump including MBTA predictions, '
        'Weather, etc')
    parser.add_argument('config_file', type=str, help='configuration file.')
    args = parser.parse_args()

    config_file = args.config_file
    if not (os.path.exists(config_file) and os.path.isfile(config_file)):
        raise ValueError("'{}' is not a valid config file".format(config_file))

    with open(config_file) as f:
        config = yaml.safe_load(f)

    app.run(port=8080)


if __name__ == '__main__':
    sys.exit(main())
