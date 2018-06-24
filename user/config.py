from os import getenv


class Config:
    ENV = getenv('ENV', 'development')
    DEBUG = False
    HOST = getenv('HOST', '0.0.0.0')
    PORT = getenv('PORT', '8082')
    USER_DB = {
        'username': getenv('USER_DB_USERNAME', 'user'),
        'password': getenv('USER_DB_PASSWORD', 'password'),
        'host': getenv('USER_DB_HOST', '127.0.0.1'),
        'port': getenv('USER_DB_PORT', '5432'),
        'database': getenv('USER_DB_DATABASE', 'user_db')
    }
    SQLALCHEMY_DATABASE_URI = ('postgresql://{username}:{password}@{host}'
                               ':{port}/{database}'.format(**USER_DB))
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    pass
