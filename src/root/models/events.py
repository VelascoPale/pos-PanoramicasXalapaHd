from . import db

class OrderGraduation(db.model):
    __tablename__ = ''

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    id_table = db.Column(db.Integer, nullable=False)
    num_photo = db.Column(db.String(10), nullable=False)
    _6x9 = db.Column(db.Integer, nullable=False)
    _8x12 = db.Column(db.Integer, nullable=False)
    cost = db.Column(db.Integer, nullable=False)
    payment = db.Column(db.Integer, nullable=False)
    seller = db.Column(db.String(50), nullable=50)
    
    def __init__(self, name, lastname, id_table, num_photo, _6x9, _8x12, cost, payment, seller):
        self.name = name
        self.lastname = lastname
        self.id_table = id_table
        self.num_photo = num_photo
        self._6x9 = _6x9
        self._8x12 = _8x12
        self.cost = cost
        self.payment = payment
        self.seller = seller


