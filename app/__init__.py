from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
# from flask_login import LoginManager




app = Flask(__name__)

db = SQLAlchemy()
bcrypt = Bcrypt()




def create_app(config_name):

    
    app = Flask(__name__)
    db.init_app(app)
   
    # bootstrap.init_app(app)
    
    app.config.from_object(config_options[config_name])

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    # from .requests import configure_request
    # configure_request(app)

    return app

from app import models
from .main import views
