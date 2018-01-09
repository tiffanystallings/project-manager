from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from models import db
from models import Project

def showOpenProjects():
	return db.session.query(Project).filter_by(status="Open").all()