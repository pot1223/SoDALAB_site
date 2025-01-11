from apps.config import config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv 
import os
from waitress import serve
from flask import Flask, redirect, url_for

db = SQLAlchemy()

def create_app(config_key):
    app = Flask(__name__)
    app.config.from_object(config[config_key])

    db.init_app(app)
    Migrate(app,db)

    from apps.soda import views as soda_views

    app.register_blueprint(soda_views.soda, url_prefix="/soda") 

    @app.route("/")
    def redirect_to_soda():
        return redirect(url_for('soda.index')) 
    
    return app 

