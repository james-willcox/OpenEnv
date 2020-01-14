from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager
from marshmallow import ValidationError

from utilities.yaml_reader import read_config
from db import db
from ma import ma

config = read_config()
db_user = config['database']['user']
db_pw = config['database']['pw']
database = config['database']['database']
db_host = config['database']['host']
db_post = config['database']['port']

app = Flask(__name__)
app.config['DEBUG'] = config['app_config']['debug']
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://{db_user}:{db_pw}@{db_host}/{database}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config['app_config']['SQLALCHEMY_TRACK_MODIFICATIONS']
app.config['PROPOGATE_EXCEPTIONS'] = config['app_config']['PROPOGATE_EXCEPTIONS']

app.secret_key = config['app_config']['secret_key']

api = Api(app)

if __name__ == "__main__":
    db.init_app(app)
    ma.init_app(app)
    app.run(port=5000, debug=True)

