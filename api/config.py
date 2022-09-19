import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'the_safe_sms_app_secret')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    # SQLALCHEMY_DATABASE_URI = "postgresql://postgres:test@localhost/test"
    API_ADDRESS = 'http://127.0.0.1:5000/'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True

class BaseConfig(object):
    CACHE_TYPE = 'redis'
    CACHE_REDIS_HOST = 'redis'
    CACHE_REDIS_PORT = 6379
    CACHE_REDIS_DB = 0
    CACHE_REDIS_URL = 'redis: // redis: 6379 / 0'
    CACHE_DEFAULT_TIMEOUT = 500


class DevelopmentConfig(Config):
    ENV = 'dev'
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    ENV = 'test'
    DEBUG = True
    TESTING = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    ENV = 'prod'
    DEBUG = False


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

configs = config_by_name[os.getenv('ENV') or 'dev']()
