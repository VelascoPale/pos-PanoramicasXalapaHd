from marshmallow import Schema, fields
from marshmallow.validate import Length

class EventSchema(Schema):
    class Meta:
        fields = ('idEvent', 'idSchool', 'eventName')

class ParamsEventSchema(Schema):
    idSchool = fields.Int(required=True)
    codeHall = fields.Str(required=True, validate=Length(10))