from ma import ma
from models.login_details import LoginDetailsModel

class LoginDetailsSchema(ma.ModelSchema):
    class Meta:
        model = LoginDetailsModel