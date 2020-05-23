import os

ENV_VAR = os.environ.get('SECRET_KEY')
if not ENV_VAR:
    raise ValueError('SECRET_KEY not declarated')

class Config(object):
    SECRET_KEY = ENV_VAR    

class ConfigDevelopment(Config):
    DEBUG = True

