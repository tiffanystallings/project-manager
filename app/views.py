from flask import Flask
from flask import render_template
from flask import request

import os

from crud import *
from models import app


#app = Flask(__name__)


@app.route('/')
@app.route('/home/<int:page>/')
def showMain(page=1):
	openProjects = showOpenProjects(page=page)
	return render_template('home.html',
						   openProjects=openProjects)


@app.route('/search/<int:page>/')
def showSearch(page=1):
	return render_template('search.html')


@app.route('/manager/<int:page>/')
def showManager(page=1):
	allProjects = allPaginatedProjects(page=page)
	return render_template('manager.html',
						   allProjects=allProjects)


@app.route('/map/')
def showMap():
	return render_template('map.html')


@app.route('/manager/new/', methods=['GET', 'POST'])
def newProject():
	if request.method == 'POST':
		return createProject(request)
	return render_template('new_project.html')


@app.route('/manager/complete/<pce_id>/')
def routeCompleteProject(pce_id):
	return completeProject(pce_id)


@app.route('/manager/view/<pce_id>')
def viewProject(pce_id):
	project = getProjectById(pce_id)
	return render_template('project.html', project=project)


@app.route('/manager/edit/', methods=['GET', 'POST'])
def editProject():
	return


@app.route('/manager/delete/', methods=['GET', 'POST'])
def deleteProject():
	return


if __name__ == '__main__':
	app.secret_key = 'waffle'
	port = int(os.environ.get("PORT", 5000))
	app.debug = True
	app.run(host='0.0.0.0', port=port)