from db import db
from datetime import datetime


class MeasurementModel(db.Model):
    __tablename__ = "measurement"
    __table_args__ = {"schema": "openenv"}

    measurement_id = db.Column(db.Integer, primary_key=True)
    measurement_value = db.Column(db.Float(precision=12))
    direction = db.Column(db.Float(precision=12))
    measurement_type_id = db.Column(db.Integer)
    latitude = db.Column(db.Float(precision=6))
    longitude = db.Column(db.Float(precision=6))
    measurement_datetime = db.Column(db.DateTime)
    station_id = db.Column(db.Integer)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
