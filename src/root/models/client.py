from . import db

class Client(db.Model):
    __tablename__ = 'clients'

    idClient = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    telephone = db.Column(db.String(10), nullable=True) # modificar para tomar en cuenta nuevo pedido
    email = db.Column(db.String(50), nullable=True)  # esta tambien
    idSchool = db.Column(db.Integer,db.ForeignKey('schools.idSchool'), nullable=False)
    order_graduation = db.relationship('OrderGraduation',backref='idclient')

    def __init__(self, name, lastname, telephone, email, idSchool):
        self.name = name
        self.lastname = lastname
        self.telephone = telephone
        self.email = email
        self.idSchool = idSchool