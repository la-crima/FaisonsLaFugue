from flask import Blueprint, request, abort
from flask_restful import Api, Resource
from flask_jwt_extended import get_jwt_identity, jwt_required

from extension import db
from entity.account import AccountModel

api = Api(Blueprint(__name__, __name__))

@api.resource('/account')
class Account(Resource):
    @jwt_required
    def get(self):
        account = AccountModel.query.filter_by(id=get_jwt_identity()).first()
        return {
            "id": account.id,
            "password": account.password
        }

    def post(self):
        id = request.json["id"]
        password = request.json["password"]

        if AccountModel.query.filter_by(id=id).first():
            raise abort(409)

        account = AccountModel(
            id=id,
            password=password
        )
        db.session.add(account)
        db.session.commit()

        return {
            "STATUS": "OK",
        }, 201