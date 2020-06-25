from marshmallow import Schema, fields
from marshmallow.validate import Length

class ClientSchema(Schema):
    class Meta:
        fields = ('idClient', 'name', 'lastname', ' telephone', 'email', 'idSchool', 'group')

class ParamsClientSchema(Schema):
    name = fields.Str(required=True, validate=Length(50))
    lastname = fields.Str(required=True, validate=Length(50)) 
    telephone = fields.Str(required=False, validate=Length(10))   # modificar para tomar en cuenta nuevo pedido
    email = fields.Email(required=False, validate=Length(50)) #este tambien
    idSchool = fields.Int(required=True)
    group = fields.Str(required=True)

client_schema = ClientSchema()
clients_schema = ClientSchema(many=True)