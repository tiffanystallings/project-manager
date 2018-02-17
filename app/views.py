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
	"""
	Input: page <int>
	Output: HTML from template

	Displays paginated results of all projects not labelled
	as "Completed", via the crud.py module. Results are ordered
	by date so as to show the oldest first.
	"""
	openProjects = showOpenProjects(page=page)
	return render_template('home.html',
						   openProjects=openProjects)


@app.route('/search/<int:page>/', methods=['GET', 'POST'])
def showSearch(page=1):
	"""
	Input: page<int> <-- This may change.
	Output: HTML from template

	This will play host to the yet-to-be-coded search feature.
	"""
	return render_template('search.html')


@app.route('/manager/<int:page>/')
def showManager(page=1):
	"""
	Input: page <int>
	Output: HTML from template

	Displays all projects sorted by date(desc) so as
	to show newest projects first.
	"""
	allProjects = allPaginatedProjects(page=page)
	return render_template('manager.html',
						   allProjects=allProjects)


@app.route('/map/')
def showMap():
	"""
	Output: HTML from template

	This page will house a searchable map in which the user
	can draw a circle around a location and be able to see
	all past and present projects assigned to those locations.
	"""
	return render_template('map.html')


@app.route('/manager/new/', methods=['GET', 'POST'])
def newProject():
	"""
	Output: HTML from template

	On POST: Sends request to crud.py to create a new project
	on the database. This will refresh the page and return the
	user to the manager page.

	On GET: Displays a form for users to add new projects to
	the database.
	"""
	if request.method == 'POST':
		return createProject(request)
	return render_template('new_project.html')


@app.route('/manager/complete/<pce_id>/')
def routeCompleteProject(pce_id):
	"""
	Input: pce_id<str>
	Output: HTML from template

	Sends a request to crud.py to update the status of a project
	to "Completed" and assign a date of completion.
	"""
	return completeProject(pce_id)


@app.route('/manager/view/<pce_id>')
def viewProject(pce_id):
	"""
	Input: pce_id<str>
	Output: HTML from template

	Grabs a project entry from crud.py and displays detailed
	information of that project
	"""
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