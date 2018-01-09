from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from models import db
from models import Projects

def showOpenProjects():
	print("Querying Projects")
	return db.session.query(Projects).filter_by(status="Open").all()