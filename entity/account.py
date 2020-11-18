from extension import db


class AccountModel(db.Model):
    __tablename__ = "account"

    id = db.Column(db.String(255), primary_key=True,)
    password = db.Column(db.String(255), nullable=False)