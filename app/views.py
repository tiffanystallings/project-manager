from flask import Flask

import os


app = Flask(__name__)


@app.route('/')
@app.route('/home/')
def showMain():
	return "Hello, home page!"


@app.route('/search/')
def showSearch():
	return "Hello, search page!"


@app.route('/manager/')
def showManager():
	return "Hello database manager!"


@app.route('/map/')
def showMap():
	return "Hello map!"


if __name__ == '__main__':
	app.secret_key = 'waffle'
	port = int(os.environ.get("PORT", 5000))
	app.debug = True
	app.run(host='0.0.0.0', port=port)