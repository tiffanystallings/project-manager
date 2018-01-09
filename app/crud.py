from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import Pagination

from models import db
from models import Project

def showOpenProjects():
	return Project.query.filter_by(status="Open").all()


def allPaginatedProjects(page):
	return Project.query.order_by(
		Project.date.desc()).paginate(page=page, per_page=25)


def createProject():

	return


def editProject():
	return


def deleteProject():
	return