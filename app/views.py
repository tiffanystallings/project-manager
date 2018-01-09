from flask import Flask
from flask import render_template

import os

from crud import *
from models import app


#app = Flask(__name__)


@app.route('/')
@app.route('/home/')
def showMain():
	openProjects = showOpenProjects()
	return render_template('home.html',
						   openProjects=openProjects)


@app.route('/search/')
def showSearch():
	return render_template('search.html')


@app.route('/manager/')
def showManager():
	return render_template('manager.html')


@app.route('/map/')
def showMap():
	return render_template('map.html')


@app.route('/manager/new/', methods=['POST'])
def newProject():
	return


@app.route('/manager/edit/', methods=['POST'])
def editProject():
	return


@app.route('/manager/delete/', methods=['POST'])
def deleteProject():
	return


if __name__ == '__main__':
	app.secret_key = 'waffle'
	port = int(os.environ.get("PORT", 5000))
	app.debug = True
	app.run(host='0.0.0.0', port=port)