from db import db
from datetime import datetime


class AccountModel(db.Model):
    __tablename__ = "account"
    __table_args__ = {"schema": "openenv"}

    account_id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    sign_up_date = db.Column(db.DateTime, default=datetime.now())
    account_password = db.Column(db.String(256))
    modified_timestamp = db.Column(db.DateTime, default=datetime.now())

    @classmethod
    def find_by_email(cls, email_address: str):
        return cls.query.filter_by(email = email_address).first()

    @classmethod
    def find_by_id(cls, user_id: int):
        return cls.query.filter_by(account_id=user_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()