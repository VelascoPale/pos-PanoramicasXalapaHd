from flask import Flask
from flask_wtf import CsrfProtect
from flask_mysqldb import MySQL

from config import Config, ConfigDevelopment
from views import events, login, users, graduaciones, escuelas, dashboard

app = Flask(__name__)
app.config.from_object(ConfigDevelopment)
# app.permanent_session_lifetime = timedelta(minutes = 30)  # close session after 15 minutes

app.register_blueprint(events)
app.register_blueprint(login)
app.register_blueprint(users)
app.register_blueprint(graduaciones)
app.register_blueprint(escuelas)
app.register_blueprint(dashboard)

# csrf
csrf = CsrfProtect()

# config_mysql
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'regis_clients_pano'
sql = MySQL()

# run server
if __name__ == "__main__":
    csrf.init_app(app)
    sql.init_app(app)
    app.run(port = "3000")
