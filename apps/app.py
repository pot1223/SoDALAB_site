from apps.config import config
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_key):
    app = Flask(__name__)

    app.config.from_object(config[config_key])

    db.init_app(app)
    Migrate(app,db)

    from apps.soda import views as soda_views

    app.register_blueprint(soda_views.soda, url_prefix="/soda") 

    return app 
   
