from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import datetime as dt


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Project(db.Model):
	__tablename__ = 'bns_projects'
	id = db.Column(db.String(80), primary_key=True)#
	name = db.Column(db.String(80), nullable=False)#
	date_in = db.Column(db.DateTime, nullable=False)#
	field_out = db.Column(db.DateTime)#
	field_in = db.Column(db.DateTime)#
	permit_in = db.Column(db.DateTime)#
	completed = db.Column(db.DateTime)#
	address = db.Column(db.String(200), nullable=False)#
	type = db.Column(db.String(20), nullable=False)#
	subtype = db.Column(db.String(20))#
	status = db.Column(db.String(10), nullable=False)#
	file = db.Column(db.String(80))
	comments = db.Column(db.String(500))
	coords = db.Column(db.String(20)) #
	permit_req = db.Column(db.String(5)) #
	com_engineer = db.Column(db.String(30))#
	field_engineer = db.Column(db.String(30))#

	@property
	def serialize(self):
		return {
			'id': self.id,
			'name': self.name,
			'date': self.date_in,
			'field_out': self.field_out,
			'field_in': self.field_in,
			'permit_in': self.permit_in,
			'completed': self.completed,
			'address': self.address,
			'type': self.type,
			'subtype': self.subtype,
			'status': self.status,
			'file': self.file,
			'comments': self.comments,
			'coords': self.coords,
			'permit_req': self.permit_req,
			'com_engineer': self.com_engineer,
			'field_engineer': self.field_engineer
		}