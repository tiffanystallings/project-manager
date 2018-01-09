from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import datetime as dt


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Projects(db.Model):
	__tablename__ = 'projects'
	id = db.Column(db.String(80), primary_key=True)
	name = db.Column(db.String(80), nullable=False)
	date = db.Column(db.DateTime, default=dt.datetime.utcnow())
	address = db.Column(db.String(200), nullable=False)
	type = db.Column(db.String(20), nullable=False)
	status = db.Column(db.String(10), nullable=False)
	file = db.Column(db.String(80))

	@property
	def serialize(self):
		return {
			'id': self.id,
			'name': self.name,
			'date': self.date,
			'address': self.address,
			'type': self.type,
			'status': self.status,
			'file': self.file
		}