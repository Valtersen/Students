from local_settings import postgresql as settings
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from flask import Flask
from flask_restful import Api


def get_engine(user, passwd, host, port, db):
    url = f"postgresql://{user}:{passwd}@{host}:{port}/{db}"
    engine = create_engine(url, echo=False)
    return engine


def get_engine_from_settings():
    keys = ['pguser', 'pgpasswd', 'pghost', 'pgport', 'pgdb']
    if not all(key in keys for key in settings.keys()):
        raise Exception('bad settings file')

    return get_engine(settings['pguser'],
        settings['pgpasswd'],
        settings['pghost'],
        settings['pgport'],
        settings['pgdb'])


def get_session():
    engine = get_engine_from_settings()
    session = sessionmaker(bind=engine)()
    return session


app = Flask(__name__)
api = Api(app)
