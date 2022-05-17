import os


class Config:
   
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URL')
    SECRET_KEY = 'Yellow'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("EMAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")

    

class ProdConfig(Config):
   
    pass

class DevConfig(Config):
    DEBUG = True
    

config_options={
'development':DevConfig,
'production':ProdConfig
}