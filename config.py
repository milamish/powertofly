import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'the_safe_sms_app_secret')
    # SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:copia@localhost/test"
    API_ADDRESS = 'http://127.0.0.1:5000/api/'
    WEBHOOK_POINT = 'message/webhook'
    # SWAGGER_ADDRESS = API_ADDRESS + '/admin/swagger.json'
    SWAGGER_ADDRESS = '/admin/swagger.json'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True


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
