from . import db

class User(db.Model):
    __tablename__ = 'users'

    idSeller = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    hashpsw = db.Column(db.String(255), nullable=False)
    permissions = db.Column(db.String(50), nullable=False)

    def __init__(self, name, lastname, email, hashpsw, permissions):
        self.name = name
        self.lastname = lastname
        self.email = email
        self.hashpsw = hashpsw
        self.permissions = permissions
