from ma import ma
from models.account import AccountModel


class AccountSchema(ma.ModelSchema):
    class Meta:
        model = AccountModel
        load_only = ("account_password")