from flask import Flask
from flask import flash
from flask import redirect
from flask import url_for
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import Pagination

from datetime import datetime

from models import db
from models import Project


def showOpenProjects(page=1):
	per_page = 15
	return Project.query.order_by(Project.date_in).filter(
		Project.status!="Completed").paginate(page, per_page)


def allPaginatedProjects(page=1):
	per_page = 15
	return Project.query.order_by(
		Project.date_in.desc()).paginate(page, per_page)


def createProject(request):
	date_in = datetime.strptime(request.form['date_in'], '%Y-%m-%d')
	newProject = Project(
		id=request.form['id'],
		name=request.form['name'],
		address=request.form['address'],
		type=request.form['type'],
		status=request.form['status'],
		file=request.form['file'],
		date_in=date_in,
		coords=request.form['coords'],
		subtype=request.form['subtype'],
		permit_req=request.form['permit_req'],
		com_engineer=request.form['com_engineer'],
		field_engineer=request.form['field_engineer'],
		comments=request.form['comments'])

	db.session.add(newProject)
	db.session.commit()
	return redirect(url_for('showManager', page=1))


def getProjectById(pce_id):
	return Project.query.filter_by(id=pce_id).one()


def completeProject(pce_id):
	date_out = datetime.strptime(datetime.strftime(
		datetime.now(), '%Y-%m-%d'), '%Y-%m-%d')
	project = getProjectById(pce_id)
	project.status = "Completed"
	project.completed = date_out

	db.session.add(project)
	db.session.commit()

	return redirect(url_for('showManager', page=1))


def updateProject(project, request):
	if request.form['date_in']:
		project.date_in = datetime.strptime(request.form['date_in'], '%Y-%m-%d')

	if request.form['completed']:
		project.completed = datetime.strptime(request.form['completed'], '%Y-%m-%d')

	if request.form['permit_in']:
		project.permit_in = datetime.strptime(request.form['permit_in'], '%Y-%m-%d')

	if request.form['field_in']:
		project.field_in = datetime.strptime(request.form['field_in'], '%Y-%m-%d')

	if request.form['field_out']:
		project.field_out = datetime.strptime(request.form['field_out'], '%Y-%m-%d')


	project.id = request.form['id']
	project.name = request.form['name']
	project.address = request.form['address']
	project.type = request.form['type']
	project.status = request.form['status']
	project.file = request.form['file']
	project.coords = request.form['coords']
	project.subtype = request.form['subtype']
	project.permit_req = request.form['permit_req']
	project.com_engineer = request.form['com_engineer']
	project.field_engineer = request.form['field_engineer']
	project.comments = request.form['comments']

	db.session.add(project)
	db.session.commit()

	return redirect(url_for('viewProject', pce_id=project.id))


def removeProject():
	return