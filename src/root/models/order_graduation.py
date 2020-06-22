from . import db

class OrderGraduation(db.model):
    __tablename__ = 'ordersGraduations'

    idOrderGraduation = db.Column(db.Integer, primary_key=True)
    idClient = db.Column(db.Integer, nullable=False)
    idSeller = db.Column(db.Integer, nullable=False)
    idEvent = db.Column(db.Integer, nullable=False)
    numTable = db.Column(db.String(10), nullable=False)
    numPhoto = db.Column(db.String(10), nullable=False)
    _6x9 = db.Column(db.Integer, nullable=False)
    _8x12 = db.Column(db.Integer, nullable=False)
    cost = db.Column(db.Integer, nullable=False)
    payment = db.Column(db.Integer, nullable=False)
    
    def __init__(self, idClient, idSeller, idEvent, numTable, numPhoto, _6x9, _8x12, cost, payment):
        self.idClient = idClient
        self.idSeller = idSeller
        self.idEvent = idEvent
        self.numTable = numTable
        self.numPhoto = numPhoto
        self._6x9 = _6x9
        self._8x12 = _8x12
        self.cost = cost
        self.payment = payment
        self.seller = seller

