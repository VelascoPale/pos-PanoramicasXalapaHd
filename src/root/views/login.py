from flask import Blueprint, session, redirect, render_template, request, url_for, flash
#from flask_mysqldb import MySQL
import bcrypt

from ..models.user import User
from ..schemas.user import user_schema, users_schema

login = Blueprint("login",__name__)

# home page
@login.route('/')
def page_login():
    if 'name' in session:
        return redirect(url_for('dashboard.render_dashboard'))
    else:
        return render_template('login.html')
    return render_template('login.html')

# function validate login
@login.route('/login', methods = ['POST'])
def validate():
    if request.method == 'POST':
        email = (request.form['adress']).lower()
        password = request.form['password'].encode('utf-8')
        session_data = User.query.filter_by(email=email).first()
        
        #test session
        if session_data is not None:
            session_psw = session_data.hashpsw.encode()
            if (bcrypt.checkpw(password,session_psw)):
                session['id'] = session_data.idSeller
                session['name'] = session_data.name
                session['permissions'] = session_data.permissions
                flash('Bienvenido de nuevo {}'.format(session['name'].title()),'alert-success')
                return redirect(url_for('dashboard.render_dashboard'))
            else:
                flash("Contraseña incorrecta, intentalo de nuevo")
                return redirect(url_for('login.page_login'))
        else:
            flash("Correo incorrecto, intentalo de nuevo")
            return redirect(url_for('login.page_login'))
    else:
        if 'name' in session:
            return redirect(url_for('dashboard.render_dashboard'))
        else:
            return redirect(url_for('login.page_login'))

# function exit > all
@login.route('/close')
def close():
    session.clear()
    return redirect(url_for('login.page_login'))