from datetime import timedelta

EXPIRE_TIME = timedelta(minutes=100000)


def build_database_uri(username, password, host):
    try:
        database_uri = "mysql://" + username + ":" + password + "@" + host
    except:
        database_uri = ""
    return database_uri


class Config:
    DEBUG = True

    JWT_ACCESS_TOKEN_EXPIRES = EXPIRE_TIME
    JWT_REFRESH_TOKEN_EXPIRES = EXPIRE_TIME

    SECRET_KEY = 'ehakdrkgg'

    LOCAL_DATABASE_USERNAME = "root"
    LOCAL_DATABASE_PASSWORD = "mingi0130"
    LOCAL_DATABASE_HOST = "127.0.0.1:3306/ehakdrk"
    SQLALCHEMY_DATABASE_URI = build_database_uri(
        LOCAL_DATABASE_USERNAME, LOCAL_DATABASE_PASSWORD, LOCAL_DATABASE_HOST
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = True