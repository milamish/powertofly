# import blp as blp
from flask import make_response, jsonify, request, abort
from flask_apispec import doc
from flask_rest_paginate import Pagination as pag

from controllers.users import get_users_from_db,get_users_from_db_by_id
from database.basemodel import SqlAlchemySession
from models.users import ResUser
from utilities.baseresource import BaseResource
from utilities.utils import error_schema



class GetUsers(BaseResource):
    @doc(description="Get Users",
         tags=['Users'],
         responses=dict(**error_schema))
    def get(self, limit):
        data = get_users_from_db(limit)
        return data

class GetUsersByID(BaseResource):
    @doc(description="Get Users",
         tags=['Users'],
         responses=dict(**error_schema))
    def get(self, user_id):
        data = get_users_from_db_by_id(user_id)
        return data
