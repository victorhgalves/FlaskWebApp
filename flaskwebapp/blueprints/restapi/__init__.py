from flask import Blueprint
from flask_restful import Api

from .resources import ClientResource

bp = Blueprint("restapi", __name__, url_prefix="/api/")
api = Api(bp)


def init_app(app):
    api.add_resource(ClientResource, "/client")
    app.register_blueprint(bp)