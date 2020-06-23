from . import db

class Event(db.Model):
    __tablename__ = 'events'
    
    idEvent = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idSchool = db.Column(db.Integer, nullable=False)
    eventName = db.Column(db.String(50), nullable=False)
    order_graduation = db.relationship('OrderGraduation',backref='idevent')

    def __init__(self, idSchool, eventName):
        self.idSchool = idSchool
        self.eventName = eventName

