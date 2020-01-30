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


class CreateApiKey(Resource):
    @jwt_required
    def post(self):
        request_json = request.get_json()
        account_id = get_jwt_identity()
        new_api_key = uuid4()
        api_dict = {}
        api_dict['account_id'] = account_id
        api_dict['api_key'] = new_api_key

        try:
            api_key = api_key_schema.load(api_dict)
            api_key.save_to_db()
            return {"message": f'Your API Key is: {new_api_key}'}
        except:
            return {"message": f'Error creating API key'}





