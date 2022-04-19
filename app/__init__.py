from flask import Flask
from app.configs import env_config, migrate, database
from app import routes

def create_app():
    app = Flask(__name__)
    
    env_config.init_app(app)
    database.init_app(app)
    migrate.init_app(app)

    routes.init_app(app)

    return app
