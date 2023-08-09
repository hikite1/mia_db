import os
from flask import Flask

# https://flask.palletsprojects.com/en/2.0.x/patterns/appfactories/


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
   
    
    from .missing_person import bp
    app.register_blueprint(bp)
    return app
