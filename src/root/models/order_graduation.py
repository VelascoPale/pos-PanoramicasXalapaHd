from . import db

class OrderGraduation(db.Model):
    __tablename__ = 'orderGraduation'

    idOrderGraduation = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idClient = db.Column(db.Integer,db.ForeignKey('clients.idClient'), nullable=False)
    idSeller = db.Column(db.Integer,db.ForeignKey('users.idSeller'),nullable=False)
    idEvent = db.Column(db.Integer,db.ForeignKey('events.idEvent'), nullable=False)
    numTable = db.Column(db.String(10), nullable=False)
    numPhoto = db.Column(db.String(10), nullable=False)
    _6x9 = db.Column(db.Integer, nullable=False)
    _8x12 = db.Column(db.Integer, nullable=False)
    cost = db.Column(db.Integer, nullable=False)
    payment = db.Column(db.Integer, nullable=False)
    status= db.Column(db.String(10), nullable=False)
    
    def __init__(self, idClient, idSeller, idEvent, numTable, numPhoto, _6x9, _8x12, cost, payment, status):
        self.idClient = idClient
        self.idSeller = idSeller
        self.idEvent = idEvent
        self.numTable = numTable
        self.numPhoto = numPhoto
        self._6x9 = _6x9
        self._8x12 = _8x12
        self.cost = cost
        self.payment = payment
        self.idSeller = idSeller
        self.status = status

        """def get_orders(data):
            orders = []
            for order in data:
                search_order = {
                    'idSeller': order[0].idSeller,
                    'idEvent': order[0].idEvent,
                    'idClient': order[0].idClient,
                    'idOrderGraduation': order[0].idOrderGraduation,
                    'name': order[1].name,
                    'lastname': order[1].lastname,
                    'numTable': order[0].numTable,
                    'numPhoto': order[0].numPhoto,
                    '_6x9': order[0]._6x9,
                    '_8x12': order[0]._8x12,
                    'cost': order[0].cost,
                    'payment': order[0].payment,
                    'status': order[0].status
                }
                orders.append(search_order)
            return orders"""

    def get_orders_per_page(page, event):
        orders = OrderGraduation.query.filter_by(idEvent = event).paginate(page,10,False)
        return orders

