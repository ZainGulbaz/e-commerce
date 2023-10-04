from marshmallow import Schema,fields,validate;


class StoreSchema(Schema):
    id=fields.Integer(dump_only=True);
    name=fields.String(required=True,validate=validate.Length(min=4));
