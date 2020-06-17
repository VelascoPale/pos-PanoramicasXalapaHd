import os

ENV_VAR = os.environ.get('SECRET_KEY')
if not ENV_VAR:
    raise ValueError('SECRET_KEY not declarated')


class Config(object):
    SECRET_KEY = ENV_VAR    

class ConfigDevelopment(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@127.0.0.1/regis_clients_pano'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config ={
    'development':ConfigDevelopment
}

