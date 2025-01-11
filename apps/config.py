from pathlib import Path 

basedir = Path(__file__).parent.parent 

class BaseConfig:
    SECRET_KEY= "sodalabsecretss"


class LocalConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI= f"sqlite:///{basedir / 'local.sqlite'}"
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_ECHO = True # SQL 쿼리를 콘솔 로그로 출력


config = {"local" : LocalConfig}