from flask import abort, jsonify
from flask_restful import Resource
import os

class ClientResource(Resource):
    def get(self):
        return jsonify({"Name": f"Client Number 1 {os.getenv('CHAVE')}"})