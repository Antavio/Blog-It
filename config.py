import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')

class DevConfig(Config):
    DEBUG = True

class ProdConfig(Config):
    '''
    Production configuration child class

    Args:
        Config:The parent configuration class with General configuration settings
    '''
    pass

config_options = {
'development':DevConfig,
'production':ProdConfig
}