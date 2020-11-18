from flask import Blueprint, request, abort
from flask_restful import Api, Resource
from flask_jwt_extended import create_access_token

from extension import db
from entity.account import AccountModel

api = Api(Blueprint(__name__, __name__))

@api.resource('/auth')
class Auth(Resource):
    def post(self):
        id = request.json["id"]
        password = request.json["password"]

        if AccountModel.query.filter_by(id=id).first().password != password:
            raise abort(401)

        return {
            "access_token": create_access_token(identity=id),
        }, 201