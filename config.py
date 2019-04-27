import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://antavio:blogs@localhost/blogs'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    UPLOADED_PHOTOS_DEST ='app/static/photos'

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