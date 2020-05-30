from flask import Blueprint, session, redirect, render_template, request, url_for, flash
from flask_mysqldb import MySQL
import bcrypt

login = Blueprint("login",__name__)
sql = MySQL()

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
        adress = request.form['adress']
        password = request.form['password'].encode('utf-8')
        cur = sql.connection.cursor()
        consult_sql = 'SELECT * FROM users WHERE adress = %s'
        cur.execute(consult_sql, [adress])
        session_data = cur.fetchall()
        cur.close()
        
        #test session
        if session_data:
            session_psw = session_data[0][4].encode()
            if (bcrypt.checkpw(password,session_psw)):
                session['name'] = session_data[0][1]
                session['adress'] = session_data[0][3]
                session['level'] = session_data[0][5]
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