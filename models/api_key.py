from db import db
from datetime import datetime


class ApiKeyModel(db.Model):
    __tablename__ = "api_key"
    __table_args__ = {"schema": "opengeo"}
    api_key_id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer)
    api_key = db.Column(db.UUID(as_uuid=True), unique=True)

    @classmethod
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_email(cls, email_address: str):
        return cls.query.filter_by(email=email_address).first()

    @classmethod
    def find_by_api_key(cls, api_key):
        return cls.query.filter_by(api_key=api_key)

