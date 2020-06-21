from marshmallow import Schema, fields
from marshmallow.validate import Length


class UserSchema(Schema):
    class Meta:
        fields = ('idSeller','name', 'lastname', 'email', 'hashpsw', 'permissions')

class ParmsUserSchema(Schema):
    name = fields.Str(required=True, validate=Length(max=50))
    lastaname = fields.Str(required=True, validate=Length(max=50))
    email = fields.Email(required=True, validate=Length(max=50))
    hashpsw = fields.Str(required=True, validate=Length(max=255))
    permissions = fields.Str(required=True, validate=Length(50))

user_schema = UserSchema()
users_schema = Schema = UserSchema(many=True)
