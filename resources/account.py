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
from blacklist import BLACKLIST
from argon2 import PasswordHasher
import json

account_schema = AccountSchema()

# Error messages

NO_LOGIN_DETAILS = 'No Account for this user'
USER_CREATED = 'Account Created'
ACCOUNT_EXISTS = 'Account already exists'
INVALID_CREDENTIALS = 'Invalid Credentials'

password_hasher = PasswordHasher(salt_len=16, hash_len=16, parallelism=8)


class CreateAccount(Resource):
    def post(cls):
        global password_hasher
        account_json = request.get_json()
        account_first_name = account_json['first_name']
        account_last_name = account_json['last_name']
        account_email = account_json['email']
        account_password = account_json['password']

        if AccountModel.find_by_email(account_email):
            return {"message": ACCOUNT_EXISTS}, 400

        account_dict = {}
        account_dict['first_name'] = account_first_name
        account_dict['last_name'] = account_last_name
        account_dict['email'] = account_email


        account_dict['account_password'] = password_hasher.hash(account_password)

        account = account_schema.load(account_dict)
        account.save_to_db()

        return {'message': USER_CREATED}, 200


class Login(Resource):
    @classmethod
    def post(cls):
        account_json = request.get_json()
        account_password = account_json['password']
        account_js = account_json['email']
        # account_data = account_schema.load(account_js)
        account = AccountModel.find_by_email(account_js)

        if account is None:
            return {'message': NO_LOGIN_DETAILS}

        if password_hasher.verify(account.account_password, account_password):
            access_token = create_access_token(identity=account.account_id, fresh=True)
            refresh_token = create_refresh_token(account.account_id)
            return {"access_token": access_token, "refresh_token": refresh_token}, 200

        return {"message": INVALID_CREDENTIALS}, 401

