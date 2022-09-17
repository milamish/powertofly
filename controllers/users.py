from flask import g, make_response, jsonify, request
from psycopg2 import sql

from database.basemodel import SqlAlchemySession, engine
from models.users import UserRepository


connection = engine.raw_connection()
cursor = connection.cursor()

def get_users_from_db(limit):

    with SqlAlchemySession() as session:
        repo = UserRepository(session)
        res = repo.get_users(limit)
        return res


def get_users_from_db_by_id(user_id):
    with SqlAlchemySession() as session:
        repo = UserRepository(session)
        res = repo.get_users_by_id(user_id)
        return res
