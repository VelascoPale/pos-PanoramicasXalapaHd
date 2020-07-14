import os

ENV_VAR = os.environ.get('SECRET_KEY')
if not ENV_VAR:
    raise ValueError('SECRET_KEY not declarated')


class Config(object):
    SECRET_KEY = ENV_VAR    

class ConfigDevelopment(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/regis_clients_pano'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ConfigProduction(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://panoramicashd:teamstrock12@panoramicashd.mysql.pythonanywhere-services.com/panoramicashd$regis_clients_pano'

config ={
    'development':ConfigDevelopment,
    'deploy':Config
}

