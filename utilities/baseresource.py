from flask import current_app as app
from flask_apispec import MethodResource
from flask_restful import Resource

from utilities.utils import exception_handle


class BaseResource(MethodResource, Resource):
    method_decorators = [exception_handle]

    def __init__(self) -> None:
        app.logger.info('In the constructor of {}'.format(self.__class__.__name__))

    def dispatch_request(self, *args, **kwargs):
        app.logger.info(f"Received request {args} {kwargs}")
        response = super(BaseResource, self).dispatch_request(*args, **kwargs)
        app.logger.info(f"Returned response {response.json}")
        return response
