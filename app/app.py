from flask import Flask

from .extensions import database, migrate, marshmallow
from .configs import DebugConfig, ProductionConfig

from app.routes import ProductRoute, HomeRoute, CategoryRoute

def create_app():
    app = Flask(__name__)
    app.config.from_object(ProductionConfig())
    register_extensions(app)
    register_routes(app)
    return app

def register_extensions(app: Flask):
    database.init_app(app)
    migrate.init_app(app, database)
    marshmallow.init_app(app)

def register_routes(app: Flask):
    app.register_blueprint(HomeRoute)
    app.register_blueprint(ProductRoute)
    app.register_blueprint(CategoryRoute)