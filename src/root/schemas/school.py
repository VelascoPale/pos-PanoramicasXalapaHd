from marshmallow import Schema, fields
from marshmallow.validate import Length

class SchoolSchema(Schema):
    class Meta:
        fields = ('idSchool', 'name', 'shift', 'generation', 'code')

class ParamsSchoolSchema(Schema):
    name = fields.Str(required=True, validate=Length(50))
    shift = fields.Str(required=True, validate=Length(10))
    generation = fields.Str(required=True, validate=Length(10))
    code = fields.Str(required=True, validate=Length(10))

school_schema = SchoolSchema()
schools_schema= SchoolSchema(many=True)