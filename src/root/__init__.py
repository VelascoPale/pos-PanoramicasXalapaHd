from flask import Flask
from flask_wtf import CSRFProtect
from flask_mail import Mail

from .models import db

from .config import ConfigProduction

from .views import login, register, graduaciones, escuelas, dashboard, emails

app = Flask(__name__)
# app.permanent_session_lifetime = timedelta(minutes = 30)  # close session after 15 minutes

# csrf
csrf = CSRFProtect()

# email
mail = Mail(app)

def create_app(environment=ConfigProduction):
    app.config.from_object(environment)

    mail.init_app(app)
    csrf.init_app(app)

    app.register_blueprint(login)
    app.register_blueprint(register)
    app.register_blueprint(graduaciones)
    app.register_blueprint(escuelas)
    app.register_blueprint(dashboard)
    app.register_blueprint(emails)

    with app.app_context():
        db.init_app(app)
        db.create_all()

    return app
