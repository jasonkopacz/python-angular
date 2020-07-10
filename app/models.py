from passlib.hash import sha256_crypt
from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True, nullable=False)
    password = db.Column(db.String(256))


def setPassword(self, pw):
    self.password = sha256_crypt.encrypt(pw)
