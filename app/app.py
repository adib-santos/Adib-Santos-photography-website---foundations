import logging
from flask import Flask
from . import shop_outer, simple_pages_outer
import logging

def create_app(): 
    app = Flask(__name__)
    app.config.from_object('app.config')

    register_blueprints(app)

    return app

# Blueprints
def register_blueprints(app: Flask): 
    app.register_blueprint(shop_outer.routes.blueprint)
    app.register_blueprint(simple_pages_outer.routes.blueprint)
