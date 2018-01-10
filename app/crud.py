from flask import Flask
from flask import flash
from flask import redirect
from flask import url_for
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import Pagination

from datetime import datetime

from models import db
from models import Project


def showOpenProjects():
	return Project.query.order_by(Project.date_in).filter(
		Project.status!="Closed").all()


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


def editProject():
	return


def deleteProject():
	return