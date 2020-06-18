from marshmallow import Schema, fields
from marshmallow.validate import Length


class UserSchema(Schema):
    class Meta:
        fields = ('id','username', 'lastanames', 'adress', 'hashpsw', 'level')

class ParmsUserSchema(Schema):
    username = fields.Str(required=True, validate=Length(max=50))
    lastanames = fields.Str(required=True, validate=Length(max=50))
    adress = fields.Str(required=True, validate=Length(max=50))
    hashpsw = fields.Str(required=True, validate=Length(max=255))
    level = fields.Str(required=True, validate=Length(50))

user_schema = UserSchema()
users_schema = Schema = UserSchema(many=True)
