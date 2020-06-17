from . import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    lastanames = db.Column(db.String(50), nullable=False)
    adress = db.Column(db.String(50), nullable=False, unique=True)
    hashpsw = db.Column(db.String(255), nullable=False)
    level = db.Column(db.String(50), nullable=False)

    def __init__(self, username, lastanames, adress, hashpsw, level):
        self.username = username
        self.lastanames = lastanames
        self.adress = adress
        self.hashpsw = hashpsw
        self.level = level
