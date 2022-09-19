from database.basemodel import SqlAlchemySession
from models.users import UserRepository
from utilities import tasks

CACHE_TIMEOUT = tasks.cache_timeout
MAX_ATTEMPTS = tasks.max_retry


# @docache(minutes=5, content_type='application/json')

def get_users_from_db(limit):
    with SqlAlchemySession() as session:
        repo = UserRepository(session)
        res = repo.get_users(limit)
        # key = res
        # MEMCACHE.set(key, vals, CACHE_TIMEOUT)
        return res

# @cache.memoize(timeout=10)
# @docache(minutes=5, content_type='application/json')
def get_users_from_db_by_id(user_id):
    with SqlAlchemySession() as session:
        repo = UserRepository(session)
        res = repo.get_users_by_id(user_id)
        return res

# @cache.memoize(timeout=10)
def get_users_from_db_by_range_limit(limit, ages1, ages2):
    with SqlAlchemySession() as session:
        repo = UserRepository(session)
        res = repo.get_users_from_db_by_range_limit(limit, ages1, ages2)
        return res
