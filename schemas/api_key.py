from ma import ma
from models.api_key import ApiKeyModel


class ApiSchema(ma.ModelSchema):
    class Meta:
        model = ApiKeyModel
