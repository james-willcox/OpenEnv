from ma import ma
from models.login_details import LoginDetailsMolde

class LoginDetailsSchema(ma.ModelSchema):
    class Meta:
        model = LoginDetailsMolde