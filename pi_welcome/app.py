from flask import Flask, render_template

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

import pi_welcome.mbta

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
    app.run(port=8080)

if __name__ == '__main__':
    main()
