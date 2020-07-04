from . import db

class School(db.Model):
    __tablename__ = 'schools'

    idSchool = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    shift = db.Column(db.String(10), nullable=False) #turn of school
    generation  = db.Column(db.String(10), nullable=False)
    code  = db.Column(db.String(10), nullable=False) #code defined for panoramicas xalapa hd
    enable = db.Column(db.Integer, nullable=False, default=1)
    
    event = db.relationship('Event',backref='idschool')
    client = db.relationship('Client',backref='idschool')

    def __init__(self, name, shift, generation, code, enable):
        self.name = name
        self.shift = shift
        self.generation = generation
        self.code = code
        self.enable = enable