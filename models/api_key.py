from db import db
from datetime import datetime


class ApiKeyModel(db.Model):
    __tablename__ = "api_key"
    __table_args__ = {"schema": "opengeo"}
    api_key_id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer)
    api_key = db.Column(db.UUID(as_uuid=True), unique=True)
