import os

ENV_VAR = os.environ.get('SECRET_KEY')
PASSWORD = os.environ.get('MAIL_PASSWORD')

if not ENV_VAR:
    raise ValueError('SECRET_KEY not declarated')

if not PASSWORD:
    raise ValueError('MAIL_PASSWORD not declarated')



class Config(object):
    SECRET_KEY = ENV_VAR
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_SSL = False
    MAIL_USE_TLS = True
    MAIL_USERNAME = '197o00237@gmail.com'
    MAIL_PASSWORD = 'JAVIER2020'

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

