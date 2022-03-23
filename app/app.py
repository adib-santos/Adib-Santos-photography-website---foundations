from flask import Flask
from . import fotos, simple_pages

def create_app(): 
    app = Flask(__name__)
    app.config.from_object('app.config')

    register_blueprints(app)

    return app

# Blueprints
def register_blueprints(app: Flask): 
    app.register_blueprint(fotos.routes.blueprint)
    app.register_blueprint(simple_pages.routes.blueprint)