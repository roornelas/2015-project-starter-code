from . import db
from datetime import datetime


class Coordinates(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    notes = db.Column(db.String(100))


    def __init__(self, latitude, longitude, notes):
        self.latitude = latitude
        self.longitude = longitude
	self.notes = notes

    def __repr__(self):
        return '<Latitude %.4f, longitude %.4f, notes %r>' % (self.latitude, self.longitude, self.notes)

