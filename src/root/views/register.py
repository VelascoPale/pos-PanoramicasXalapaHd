from flask import Blueprint, session, request, url_for, flash, render_template, redirect
from flask_mysqldb import MySQL
import bcrypt
from sqlalchemy import update

from ..models import db
from ..models.user import User
from ..schemas.user import user_schema, users_schema

register = Blueprint("register",__name__, url_prefix='/register')
salt = bcrypt.gensalt()
sql = MySQL()

# function register_members
@register.route('/user', methods=['POST','GET'])
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
                data_user = User.query.filter_by(name = name , lastname = lastname, email = email).first()
                if data_user:
                    flash('Este usuario ya ha sido creado', 'alert-danger')
                else:
                    user = User(name = name, lastname = lastname, email= email, hashpsw= password, permissions=level)
                    db.session.add(user)
                    db.session.commit()
                    flash('Usuario creado satisfactoriamente','alert-success') 
            else:
                flash('No has llenado todos los campos, intentalo de nuevo', 'alert-warning')
        users = User.query.all()
        return render_template('register_members.html', users = users)
    else:
        return redirect(url_for('login.page_login'))
    return render_template('register_members.html')

# function add_members > register member
@register.route('user/patch/<id>', methods = ['POST'])
def update_member(id):
    name = (request.form['username']).upper()
    lastname = (request.form['lastname']).upper()
    email = (request.form['adress']).lower()
    password = request.form['password']
    permissions = request.form['level']
    if not password == '':
        password = password.encode('utf-8')
        password = bcrypt.hashpw(password,salt)
        user_update = User.query.get(id)
        user_update.name=name
        user_update.lastname=lastname
        user_update.email=email
        user_update.hashpsw=password
        user_update.permissions=permissions
        db.session.commit()
    else:
        user_update = User.query.get(id)
        user_update.name=name
        user_update.lastname=lastname
        user_update.email=email
        user_update.permissions=permissions
        db.session.commit()
    flash('Usuario actualizado satisfactoriamente', 'alert-success')
    return redirect(url_for('register.register_members'))

# function delete_member > register_member
@register.route('user/delete/<id>', methods=['GET','POST'])
def delete(id):
    user_delete = User.query.filter_by(idSeller = int(id)).first()
    db.session.delete(user_delete)
    db.session.commit()
    flash('Usuario eliminado satisfactoriamente', 'alert-success')
    return redirect(url_for('register.register_members'))
