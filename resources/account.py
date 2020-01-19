from flask_restful import Resource
from flask import request
from flask_jwt_extended import (
create_access_token,
create_refresh_token,
jwt_refresh_token_required,
get_jwt_identity,
jwt_required,
get_raw_jwt
)
from datetime import datetime
from models.account import AccountModel
from schemas.account import AccountSchema
from models.login_details import LoginDetailsMolde
from schemas.login_details import LoginDetailsSchema
from blacklist import BLACKLIST
from passlib.hash import sha256_crypt
import json

account_schema = AccountSchema()
login_schema = LoginDetailsSchema()


class CreateAccount(Resource):
    def post(cls):
        account_json = request.get_json()
        account_first_name = account_json['first_name']
        account_last_name = account_json['last_name']
        account_email = account_json['email']
        account_password = account_json['password']

        if AccountModel.find_by_email(account_email):
            return {"message": "User already exists"}, 400

        account_dict = {}
        account_dict['first_name'] = account_first_name
        account_dict['last_name'] = account_last_name
        account_dict['email'] = account_email
        account = account_schema.load(account_dict)
        account.save_to_db()

        login_details_dict = {}
        login_details_dict['account_id'] = account.account_id
        login_details_dict['account_password'] = sha256_crypt.hash(account_password)

        login_details = login_schema.load(login_details_dict)
        login_details.save_to_db()

        return {'message': 'User Created'}, 200