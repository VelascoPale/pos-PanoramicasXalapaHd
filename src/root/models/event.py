from . import db

class Event(db.Model):
    __tablename__ = 'events'
    
    idEvent = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idSchool = db.Column(db.Integer,db.ForeignKey('schools.idSchool') ,nullable=False)
    eventName = db.Column(db.String(50), nullable=False)
    order_graduations = db.relationship('OrderGraduation',backref='idevent')
    enable = db.Column(db.Integer, nullable=False, default=1)

    def __init__(self, idSchool, eventName, enable):
        self.idSchool = idSchool
        self.eventName = eventName
        self.enable = enable

