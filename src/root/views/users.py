from flask import Blueprint, session, request, url_for, flash, render_template, redirect
from flask_mysqldb import MySQL
import bcrypt

from ..models import db
from ..models.user import User
from ..schemas.schemas import user_schema, users_schema

users = Blueprint("users",__name__, url_prefix='/register_members')
salt = bcrypt.gensalt()
sql = MySQL()

# function register_members
@users.route('/', methods=['POST','GET'])
def register_members():
    if 'name' in session and session['permissions'] == 'ADMIN':
        if request.method == 'POST':
            name = (request.form['name']).upper()
            lastname = (request.form['lastname']).upper()
            email = (request.form['email']).lower()
            password = request.form['password'].encode('utf-8')
            level = 'SELLER'
            password = bcrypt.hashpw(password,salt)
            if name != '' and lastname != '' and email != '' and password != '':
                cur = sql.connection.cursor()
                consult_sql = """SELECT * FROM users WHERE email='{0}' OR name='{1}' OR lastname='{2}'"""
                cur.execute(consult_sql.format(email, name, lastname))
                data_user = cur.fetchone()
                print(data_user)
                if data_user:
                    flash('Este usuario ya ha sido creado', 'alert-danger')
                else:
                    user = User(name = name, lastname = lastname, email= email, hashpsw= password, permissions=level)
                    db.session.add(user)
                    db.session.commit()
                    flash('Usuario creado satisfactoriamente','alert-success') 
            else:
                flash('No has llenado todos los campos, intentalo de nuevo', 'alert-warning')
        cur = sql.connection.cursor()
        consult_sql = 'SELECT * FROM users WHERE 1'
        cur.execute(consult_sql)
        users = cur.fetchall()
        cur.close()
        return render_template('register_members.html', users = users)
    else:
        return redirect(url_for('login.page_login'))
    return render_template('register_members.html')

# function add_members > register member
@users.route('/patch/<id>', methods = ['POST'])
def update_member(id):
    name = (request.form['username']).upper()
    lastname = (request.form['lastname']).upper()
    email = (request.form['adress']).lower()
    password = request.form['password']
    permissions = request.form['level']
    cur = sql.connection.cursor()
    if not password == '':
        password = password.encode('utf-8')
        password = bcrypt.hashpw(password,salt)
        consult_sql = """UPDATE users SET 
        name=%s,
        lastname=%s,
        email=%s,
        hashpsw=%s,
        permissions=%s
        WHERE id = %s"""
        cur.execute(consult_sql,(name, lastname, email, password, permissions, id))
        cur.close()
    else:
        consult_sql = """UPDATE users SET 
        name='{1}',
        lastname='{2}',
        email='{3}',
        permissions='{4}'
        WHERE idSeller = {0}"""
        cur.execute(consult_sql.format(id, name, lastname, email, permissions))
        cur.close()
    flash('Usuario actualizado satisfactoriamente', 'alert-success')
    return redirect(url_for('users.register_members'))

# function delete_member > register_member
@users.route('/delete/<id>', methods=['GET','POST'])
def delete(id):
    user_delete = User.query.filter_by(idSeller = int(id)).first()
    db.session.delete(user_delete)
    db.session.commit()
    flash('Usuario eliminado satisfactoriamente', 'alert-success')
    return redirect(url_for('users.register_members'))
