from db import db
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID


class ApiKeyModel(db.Model):
    __tablename__ = "api_key"
    __table_args__ = {"schema": "openenv"}
    api_key_id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer)
    api_key = db.Column(UUID(as_uuid=True))
    api_key_created = db.Column(db.DateTime, default=datetime.now())
    station_id = db.Column(db.Integer)
    key_type_id = db.Column(db.Integer)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_account_id(cls, account_id: int):
        return cls.query.filter_by(account_id=account_id).all()

    @classmethod
    def find_by_api_key(cls, api_key):
        return cls.query.filter_by(api_key=api_key).all()

    @classmethod
    def find_user_api_keys(cls, account_id):
        return cls.query.filter_by(account_id=account_id, station_id=None).first()

