import os


class Config:
   
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://wamaitha:Wammy@localhost/pitch'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = 'Yellow'
   
    

class ProdConfig(Config):
    
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


class DevConfig(Config):
    

    DEBUG = True
    

config_options={
'development':DevConfig,
'production':ProdConfig
}