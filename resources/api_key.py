from flask_restful import Resource
from flask import request
from flask_jwt_extended import (
jwt_required,
get_jwt_identity,
get_raw_jwt
)
from uuid import uuid4

from models.api_key import ApiKeyModel
from schemas.api_key import ApiSchema

api_key_schema = ApiSchema()


class CreateUserApiKey(Resource):
    @jwt_required
    def post(self):
        account_id = get_jwt_identity()
        if ApiKeyModel.find_user_api_keys(account_id):
            return {'message': 'User already has an API key'}, 418

        new_api_key = uuid4()
        api_dict = {}
        api_dict['account_id'] = account_id
        api_dict['api_key'] = new_api_key
        api_dict['key_type_id'] = 1

        try:
            api = api_key_schema.load(api_dict)
            api.save_to_db()
            return {"message": f'Your API Key is: {new_api_key}'}, 201
        except:
            return {"message": f'Error creating API key'}


class CreateStationApiKey(Resource):
    @jwt_required
    def post(self):
        account_id = get_jwt_identity()
        json_package = request.get_json()
        if ApiKeyModel.find_by_station_id(station_id=json_package['station_id']):
            return {'message': 'Station already has an API key'}, 400
        new_api_key = uuid4()
        new_station_key_dict = {}
        new_station_key_dict['account_id'] = account_id
        new_station_key_dict['api_key'] = new_api_key
        new_station_key_dict['key_type_id'] = 2
        new_station_key_dict['station_id'] = json_package['station_id']

        api = api_key_schema.load(new_station_key_dict)
        api.save_to_db()
        return {'message': f'Your new station id is {new_api_key}'}, 201






