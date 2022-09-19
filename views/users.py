from flask import request
from flask_apispec import doc
from controllers.users import get_users_from_db, get_users_from_db_by_id, get_users_from_db_by_range_limit
from utilities.baseresource import BaseResource
from utilities.utils import error_schema


class GetUsers(BaseResource):
    @doc(description="Get Users",
         tags=['Users'],
         responses=dict(**error_schema))
    def get(self):
        limit = request.args.get('limit')
        data = get_users_from_db(limit)
        return data


class GetUsersByID(BaseResource):
    @doc(description="Get Users by Id",
         tags=['Users'],
         responses=dict(**error_schema))
    def get(self):
        user_id = request.args.get('user_id')
        data = get_users_from_db_by_id(user_id)
        return data


class GetUsersByRangeandLimit(BaseResource):
    @doc(description="Get Users",
         tags=['Users'],
         responses=dict(**error_schema))
    def get(self):
        limit = request.args.get('limit')
        ages1 = request.args.get('ages1')
        ages2 = request.args.get('ages2')
        data = get_users_from_db_by_range_limit(limit, ages1, ages2)
        return data
