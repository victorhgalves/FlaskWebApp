from flask import Flask
from flask_restful import Api

from flaskwebapp.blueprints import restapi 



def create_app():
    app =  Flask(__name__)
    restapi.init_app(app)
    return app