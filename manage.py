from flask import Flask
from flask.logging import create_logger
from flask_apispec.extension import FlaskApiSpec
from flask_caching import Cache
from flask_rest_paginate import Pagination
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.testing import db

from routes import routes


# def get_config_as_dict(module_):
#     variables = [var for var in dir(module_) if not var.startswith("__")]
#     return {var: getattr(module_, var) for var in variables if type(getattr(module_, var)) in [str, int]}
#
#
def create_app():
    app = Flask(__name__)
    create_logger(app)
    # configure_app_logging(app)
    # add routes
    api = Api(app)
    for resource, path in routes:
        api.add_resource(resource, path)

    cache = Cache(app)

    # add documentation
    app.config.update({
        'APISPEC_SWAGGER_URL': '/swagger/',
    })
    with app.app_context():
        docs = FlaskApiSpec(app)
        for resource, _ in routes:
            docs.register(resource)
    return app, cache


app, cache = create_app()
pagination = Pagination(app, db)
if __name__ == '__main__':
    app.run(debug=True)
