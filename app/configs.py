class DebugConfig:
    SECRET_KEY = "ozama123"
    SQLALCHEMY_DATABASE_URI = "sqlite:///storage.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig:
    SECRET_KEY = "ozama123"
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://MateusOzama:Mateus_123@MateusOzama.mysql.pythonanywhere-services.com/MateusOzama$default"
    SQLALCHEMY_TRACK_MODIFICATIONS = False