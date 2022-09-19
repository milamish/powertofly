from marshmallow import fields, Schema


class BaseResponseSchema(Schema):
    error_msg = fields.String(required=True, default='N/A')
    error = fields.String(required=True, default='N/A')
    status = fields.String(required=True, default='Success')
    data = fields.Dict(required=True, default={})
