from flask import Flask
from flask_wtf import CsrfProtect
from flask_mysqldb import MySQL

from .models import db
from .views import events, login, users, graduaciones, escuelas, dashboard

app = Flask(__name__)
# app.permanent_session_lifetime = timedelta(minutes = 30)  # close session after 15 minutes

# csrf
csrf = CsrfProtect()

# config_mysql
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'regis_clients_pano'
sql = MySQL()

def create_app(environment):
    app.config.from_object(environment)

    app.register_blueprint(events)
    app.register_blueprint(login)
    app.register_blueprint(users)
    app.register_blueprint(graduaciones)
    app.register_blueprint(escuelas)
    app.register_blueprint(dashboard)

    with app.app_context():
        db.init_app(app)
        db.create_all()

    return app
