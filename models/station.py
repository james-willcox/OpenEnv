from db import db


class StationModel(db.Model):
    __tablename__ = "station"
    __table_args__ = {"schema":"openenv"}

    station_id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer)
    station_api_key = db.Column(db.String(255))
    station_type_id = db.Column(db.Integer)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
