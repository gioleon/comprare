from decouple import config

class ConfigClass:
    SQLALCHEMY_DATABASE_URL = config('SQLALCHEMY_DATABASE_URL')