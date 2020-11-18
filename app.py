import extension

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from config import Config


def route(app):
    from business_logic.account import account
    app.register_blueprint(account.api.blueprint)
    from business_logic.auth import auth
    app.register_blueprint(auth.api.blueprint)



def boot(app):
    app.config.from_object(Config)

    CORS(app, resources={
        r"*": {"origin": "*"},
    })

    JWTManager().init_app(app)
    extension.db.init_app(app)
    extension.db.create_all(app=app)
    extension.cors.init_app(app)


if __name__ == '__main__':
    app = Flask(__name__)
    route(app)
    boot(app)

    app.run(host="0.0.0.0", port=5000)