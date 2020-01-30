from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager
from marshmallow import ValidationError

from utilities.yaml_reader import read_config
from db import db
from ma import ma
from blacklist import BLACKLIST

from resources.measurement import Measurement
from resources.account import CreateAccount, Login, Logout
from resources.api_key import CreateUserApiKey

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
app.config['JWT_BLACKLIST_ENABLED'] = config['app_config']['JWT_BLACKLIST_ENABLED']
app.config["JWT_BLACKLIST_TOKEN_CHECKS"] = [
    "access",
    "refresh",
]  # allow blacklisting for access and refresh tokens
app.secret_key = config['app_config']['secret_key']

api = Api(app)

jwt = JWTManager(app)

@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    return decrypted_token["jti"] in BLACKLIST

api.add_resource(Measurement, '/measurement')
api.add_resource(CreateAccount, '/register')
api.add_resource(Login, '/login')
api.add_resource(Logout, '/logout')
api.add_resource(CreateUserApiKey, '/create_user_api_key')


if __name__ == "__main__":
    db.init_app(app)
    ma.init_app(app)
    app.run(port=5000, debug=True)

