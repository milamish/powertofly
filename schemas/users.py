from marshmallow import fields, Schema


class GetUsersSchema(Schema):
    user_id = fields.Integer(required=True, Primary_key=True)
    name = fields.String(required=True)
    age = fields.Integer(required=True)
    joindate = fields.Date(required=True)
