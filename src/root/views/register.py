from flask import Blueprint, session, request, url_for, flash, render_template, redirect, jsonify
import bcrypt
from sqlalchemy import update

from ..models import db

from ..models.user import User
from ..schemas.user import user_schema, users_schema

from ..models.school import School
from ..schemas.school import school_schema, schools_schema

from ..models.event import Event
from ..schemas.event import event_schema, events_schema

from ..models.client import Client
from ..schemas.client import client_schema, clients_schema

register = Blueprint("register",__name__, url_prefix='/dashboard/register')
salt = bcrypt.gensalt()

# function register_users
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
                if data_user is not None:
                    flash('Este usuario ya ha sido creado', 'alert-danger')
                else:
                    user = User(name = name, lastname = lastname, email= email, hashpsw= password, permissions=level)
                    db.session.add(user)
                    db.session.commit()
                    flash('Usuario creado satisfactoriamente','alert-success') 
            else:
                flash('No has llenado todos los campos, intentalo de nuevo', 'alert-warning')
        users = User.query.order_by(User.name).all()
        return render_template('register_users.html', users = users)
    else:
        return redirect(url_for('login.page_login'))
    return render_template('register_users.html')

# function update_users
@register.route('user/patch/<id>', methods = ['POST'])
def update_member(id):
    name = (request.form['name']).upper()
    lastname = (request.form['lastname']).upper()
    email = (request.form['email']).lower()
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

# function delete_users
@register.route('user/delete/<id>', methods=['GET','POST'])
def delete_member(id):
    user_delete = User.query.filter_by(idSeller = int(id)).first()
    db.session.delete(user_delete)
    db.session.commit()
    flash('Usuario eliminado satisfactoriamente', 'alert-success')
    return redirect(url_for('register.register_members'))

# funcion for add schools
@register.route('/school', methods=['POST', 'GET'])
def register_schools():
    if 'name' in session and session['permissions'] == 'ADMIN':
        if request.method == 'POST':
            name_school = (request.form['schoolName']).upper()
            shift = (request.form['shift']).upper()
            generation = request.form['generation']
            code = (request.form['code']).upper()
            if name_school != '' and shift != '#' and generation != '' and code != '':
                data_school = School.query.filter_by(name=name_school, shift=shift, generation=generation).first()
                if data_school is not None:
                    flash('Esta escuela ya ha sido creada', 'alert-danger')
                else:
                    school = School(name=name_school, shift=shift, generation=generation, code=code, enable=1)
                    db.session.add(school)
                    db.session.commit()
                    flash('Escuela registrada satisfactoriamente','alert-success')
            else:
                flash('No has llenado todos los campos, intentalo de nuevo', 'alert-warning')
        schools = School.query.order_by(School.idSchool).all()
        return render_template('register_schools.html', schools=schools)
    else:
        return redirect(url_for('login.login_page'))
    return render_template('register_schools.html')

# funcion for update schools
@register.route('/school/patch/enable/<id>', methods=['POST','GET'])
def enable_school(id):
    enable= int(1)
    school_update = School.query.get(id)
    school_update.enable = enable
    db.session.commit()

    flash('Escuela habilitada satisfactoriamente', 'alert-success')
    return redirect(url_for('register.register_schools'))

# funcion for delete schools
@register.route('/school/patch/disable/<id>', methods=['GET','POST'])
def disable_school(id):
    enable = int(0)
    school_update = School.query.get(id)
    school_update.enable = enable
    db.session.commit()

    flash('Escuela inhabilitado satisfactoriamente', 'alert-success')
    return redirect(url_for('register.register_schools'))

# funcion for add events
@register.route('/event', methods=['POST', 'GET'])
def register_events():
    if 'name' in session and session['permissions'] == 'ADMIN':
        if request.method == 'POST':
            school = int(request.form['school'])
            name_hall = (request.form['hallName']).upper()
            data_school = School.query.filter_by(idSchool=school).first()
            event_name = data_school.code + '_' + name_hall + '_' + data_school.generation
            if school != 0 and name_hall != '':
                data_event = Event.query.filter_by(idSchool = school).first()
                if data_event is not None:
                    flash('La escuela ya tiene un evento registrado', 'alert-danger')
                else:
                    event = Event(idSchool = school, eventName = event_name, enable=1)
                    db.session.add(event)
                    db.session.commit()
                    flash('Evento creado satisfactoriamente','alert-success') 
            else:
                flash('No has llenado todos los campos, intentalo de nuevo', 'alert-warning')
        schools = School.query.order_by(School.idSchool).all()
        events = Event.query.order_by(Event.idEvent).all()
        return render_template('register_events.html', events = events, schools= schools)
    else:
        return redirect(url_for('login.page_login'))
    return render_template('register_events.html')

# funcion for enable/disable events
@register.route('/event/patch/enable/<id>', methods=['POST','GET'])
def enable_event(id):
    enable= int(1)
    event_update = Event.query.get(id)
    event_update.enable = enable
    db.session.commit()

    flash('Evento habilitado satisfactoriamente', 'alert-success')
    return(redirect(url_for('register.register_events')))

@register.route('/event/patch/disable/<id>', methods=['POST','GET'])
def disable_event(id):
    enable= int(0)
    event_update = Event.query.get(id)
    event_update.enable = enable
    db.session.commit()

    flash('Evento inhabilitado satisfactoriamente', 'alert-success')
    return(redirect(url_for('register.register_events')))

# page clients
@register.route('/client', methods=['GET'])
def register_clients():
    if 'name' in session:
        clients = Client.query.order_by(Client.idClient).all()
        schools = School.query.order_by(School.idSchool).all()
        return render_template('register_clients.html', schools = schools, clients=clients)
    else:
        return redirect(url_for('login.page_login'))
    return render_template('register_clients.html')

# funcion for add clients
@register.route('/client', methods=['POST'])
def add_client():
    if 'name' in session:
        name = (request.form['name']).upper()
        lastname = (request.form['lastname']).upper()
        telephone = request.form['telephone']
        email = (request.form['email']).lower()
        id_school = request.form['school']
        group = request.form['group']
        if group != '#' and name and lastname and telephone and email and id_school:
            data_client = Client.query.filter_by(name=name, lastname=lastname, idSchool=id_school).first()
            if data_client is not None:
                alert = {
                    'text':'El cliente ya ha sido registrado',
                    'type':'alert-danger'}
            else:
                client = Client(name = name, lastname = lastname, telephone=telephone, email=email, idSchool=id_school, group=group)
                db.session.add(client)
                db.session.commit()
                alert = {
                    'text':'Cliente registrado satisfactoriamente',
                    'type':'alert-success'}
        else:
           alert = {
               'text':'No has llenado todos los campos, intentalo de nuevo',
               'type':'alert-warning'}
       
        clients = Client.query.all()
        return jsonify(alert, clients_schema.dump(clients))

# funcion for update clients
@register.route('/client', methods=['PATCH'])
def update_client():
    if 'name' in session:
        id_client = request.form['idClientEdit']
        name = (request.form['nameEdit']).upper()
        lastname = (request.form['lastnameEdit']).upper()
        telephone = request.form['telephoneEdit']
        email = (request.form['emailEdit']).lower()
        id_school = request.form['schoolEdit']
        group = request.form['groupEdit']
        if group != '#' and name and lastname and telephone and email and id_school:
            client = Client.query.get(id_client)
            client.name = name
            client.lastname = lastname
            client.telephone = telephone
            client.email = email
            client.idSchool = id_school
            client.group = group
            db.session.commit()
            alert = {
                'text':'Cliente actualizado satisfactoriamente',
                'type':'alert-success'}
        else:
           alert = {
               'text':'No has llenado todos los campos, intentalo de nuevo',
               'type':'alert-warning'}
       
        clients = Client.query.all()
        return jsonify(alert, clients_schema.dump(clients))

@register.route('/client/<school>/<group>', methods=['GET'])
def filter_by_school(school, group):
    if 'name'in session:
        if int(school) > 0 and group != 'Z':
            data_clients = Client.query.filter_by(idSchool=school, group=group).all()
        elif int(school) > 0:
            data_clients = Client.query.filter_by(idSchool=school).all()
        else:
            data_clients = Client.query.all()
        return jsonify(clients_schema.dump(data_clients))

@register.route('/client/search', methods=['GET'])
def search_client():
    if 'name' in session:
        tag = request.args.get('text')
        if tag != '':
            search = "{}%".format(tag)
            search_client = Client.query.filter(Client.name.like(search)).all()
        else:
            search_client = Client.query.all()
        return jsonify(clients_schema.dump(search_client))
