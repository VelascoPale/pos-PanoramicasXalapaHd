from marshmallow import Schema, fields
from marshmallow.validate import Length

class SchoolSchema(Schema):
    class Meta:
        fields = ('idSchool', 'name', 'shift', 'generation', 'code', 'enable')

class ParamsSchoolSchema(Schema):
    name = fields.Str(required=True, validate=Length(50))
    shift = fields.Str(required=True, validate=Length(10))
    generation = fields.Str(required=True, validate=Length(10))
    code = fields.Str(required=True, validate=Length(10))
    enable = fields.Int(required=True)

school_schema = SchoolSchema()
schools_schema= SchoolSchema(many=True)