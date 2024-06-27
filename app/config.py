from os import path, sep, pardir
from datetime import timedelta


class Config(object):
    SECRET_KEY = "mysecretkey"
    BASE_DIR = path.abspath(path.dirname(__file__) + sep + pardir)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + path.join(BASE_DIR, 'db.sqlite')

    MAIL_SERVER = 'sandbox.smtp.mailtrap.io'
    MAIL_PORT = 2525
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = '769b12411b12b0'
    MAIL_PASSWORD = '57cbda838b314c'

    JWT_SECRET_KEY = "jwtsecretkey"
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)
    AUTHORIZATION ={
        'JsonWebToken': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization'
        }
    }



class Constants:
    SERIALIZER_SALT = "12345678"
