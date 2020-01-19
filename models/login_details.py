from db import db
from datetime import datetime


class LoginDetailsMolde(db.Model):
    __tablename__ = "login_details"
    __table_args__ = {"schema": "openenv"}

    login_details_id = db.Column(db.Integer, primary_key = True)
    account_id = db.Column(db.Integer)
    account_password = db.Column(db.String(256))
    modified_date = db.Column(db.DateTime, default=datetime.now())

    @classmethod
    def get_login_details_for_user(cls, user_id):
        return cls.query.filter_by(account_id=user_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

