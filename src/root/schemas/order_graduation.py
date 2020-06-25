from marshmallow import Schema, fields
from marshmallow.validate import Length

class OrderGraduationSchema(Schema):
    class Meta:
        fields = ('idOrderGraduation', 'idClient', 'idSeller', 'idEvent', 'numTable', 'numPhoto', '_6x9', '_8x12', 'cost', 'payment', 'status')

class ParamsOrderGraduationsSchema(Schema):
    idClient = fields.Int(required=True)
    idSeller = fields.Int(required=True)
    idEvent = fields.Int(required=True)
    numTable = fields.Str(required=True, validate=Length(10))
    numPhoto = fields.Str(required=True, validate=Length(50))
    _6x9 = fields.Int(required=True)
    _8x12 = fields.Int(required=True)
    cost = field.Int(required=True)
    payment = field.Int(required=True)
    status = field.Str(required=True, validate=Length(10))

order_graduation_schema = OrderGraduationSchema()
orders_graduations_schema = OrderGraduationSchema(many=True)