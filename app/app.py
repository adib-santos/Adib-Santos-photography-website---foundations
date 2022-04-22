import logging
from unittest import skip
from flask import Flask
from app.users import models
from . import simple_pages_outer, models, users
from app.extensions.database import db, migrate
from app.config import SQLALCHEMY_DATABASE_URI
from app.extensions.authentication import login_manager


def create_app(): 
    app = Flask(__name__)
    app.config.from_object('app.config')

    register_extensions(app)
    register_blueprints(app)

    return app

# Blueprints
def register_blueprints(app: Flask): 
    app.register_blueprint(simple_pages_outer.routes.blueprint)
    app.register_blueprint(users.routes.blueprint)
# Database
def register_extensions(app: Flask): 
    db.init_app(app)    # -> Initializes the database connection of SQLAlchemy 
    migrate.init_app(app, db) # -> There's 2 parameters bcause we want to connect it to app AND to the database 
    login_manager.init_app(app)