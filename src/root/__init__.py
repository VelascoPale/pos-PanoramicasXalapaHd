from flask import Flask
from flask_wtf import CSRFProtect

from .models import db
from .models.client import Client
from .models.order_graduation import OrderGraduation
from .models.school import School
from .models.user import User
from .config import ConfigProduction

from .views import login, register, graduaciones, escuelas, dashboard

app = Flask(__name__)
# app.permanent_session_lifetime = timedelta(minutes = 30)  # close session after 15 minutes

# csrf
csrf = CSRFProtect()

def create_app(environment=ConfigProduction):
    app.config.from_object(environment)

    app.register_blueprint(login)
    app.register_blueprint(register)
    app.register_blueprint(graduaciones)
    app.register_blueprint(escuelas)
    app.register_blueprint(dashboard)
    csrf.init_app(app)
    with app.app_context():
        db.init_app(app)
        db.create_all()

    return app
