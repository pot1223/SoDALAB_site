from apps.config import config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from waitress import serve
from flask import Flask, redirect, url_for
from supabase import create_client, Client

db = SQLAlchemy()


supabase: Client = None

def create_app(config_key='dev'):
    global supabase # 전역 변수를 사용하겠다고 선언
    
    app = Flask(__name__)
    app.config.from_object(config[config_key])
    
    # --- 👇 3. 설정 값을 바탕으로 Supabase 클라이언트를 생성합니다. ---
    supabase = create_client(
        app.config.get('SUPABASE_URL'), 
        app.config.get('SUPABASE_KEY')
    )

    db.init_app(app)
    Migrate(app, db)
    
    from apps import models
    from apps.soda import views as soda_views

    app.register_blueprint(soda_views.soda, url_prefix="/soda") 

    @app.route("/")
    def redirect_to_soda():
        return redirect(url_for('soda.index')) 
    
    return app