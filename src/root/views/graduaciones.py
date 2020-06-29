from flask import Blueprint, render_template, redirect, url_for, session, jsonify, flash, request
from flask_mysqldb import MySQL

from sqlalchemy import asc, desc

from ..models import db
from ..models.order_graduation import OrderGraduation
from ..schemas.order_graduation import order_graduation_schema, orders_graduations_schema

from ..models.client import Client
from ..schemas.client import client_schema, clients_schema

graduaciones = Blueprint("graduaciones",__name__, url_prefix='/dashboard/event')
sql = MySQL()

# form_client_grd page
@graduaciones.route('/form')
def form_graduaciones():
    if 'name' in session:
        event = request.args.get('event').split(',')
        clients = Client.query.filter_by(idSchool = event[1]).order_by(Client.name.asc())
        orders = OrderGraduation.query.filter_by(idEvent = event[1]).order_by(OrderGraduation.idClient.asc())
        return render_template('form_graduaciones.html', event = event, orders = orders, clients=clients)
    else:
        return redirect(url_for('login.page_login'))
    return render_template('form_graduaciones.html')

# function add_client > form_clients-grd
@graduaciones.route('/form', methods = ['POST'])
def add_client():
    id_seller = request.form['idSeller']
    id_client = request.form['idClient']
    id_event = request.form['idEvent']
    name = (request.form['name']).upper()
    lastname = (request.form['lastname']).upper()
    id_table = request.form['id_table']
    num_photo = (request.form['num_photo']).upper()
    num_6x9 = request.form['num_6x9']
    num_8x12 = request.form['num_8x12']
    cost = request.form['cost']
    payment = request.form['payment']
    if id_seller != '' and name != '' and lastname != '' and id_table != '' and num_photo != '' and num_6x9 != '' and num_8x12 != ''  and cost != '' and payment != '':
        if int(id_table) <= 125:
            if not int(payment) > int(cost):
                if id_client != 0:
                    new_order = OrderGraduation(idClient=id_client, idSeller=id_seller, idEvent=id_event, numTable=id_table, numPhoto=num_photo,_6x9=num_6x9,_8x12=num_8x12, cost=cost, payment=payment, status='EN PROCESO')
                    db.session.add(new_order)
                    db.session.commit()
                alert = {
                    'text':'Pedido realizado correctamente',
                    'type':'alert-success'
                }
            else:
                alert = {
                    'text':'El pago registrado es mayor al costo',
                    'type':'alert-warning'
                }
        else:
            alert = {
                    'text':'Indice de mesa demasiado grande',
                    'type':'alert-warning'
            }
    else:
        alert = {
                    'text':'No se han registrado todos los datos',
                    'type':'alert-warning'
        }
    orders = OrderGraduation.query.filter_by(idEvent=id_event).all()
    return jsonify(alert, orders_graduations_schema.dump(orders))

# function delete_client > form_graduaciones
@graduaciones.route('/delete_client/<event>/<id>', methods = ['POST'])
def delete_client(event, id):
    cur = sql.connection.cursor()
    consult_sql = 'DELETE FROM {0} WHERE id={1}'
    cur.execute(consult_sql.format(event,id))
    cur.close()
    flash('Cliente eliminado satisfactoriamente', 'alert-success')
    return redirect(url_for('graduaciones.form_graduaciones', event = event))
    
# function update_client > edit_client_grd 
@graduaciones.route('/update_client/<event>/<id>', methods = ['POST'])
def update_client(event, id):
    name = (request.form['name']).upper()
    id_table = request.form['id_table']
    num_photo = request.form['num_photo']
    num_6x9 = request.form['num_6x9']
    num_8x12 = request.form['num_8x12']
    cost = request.form['cost']
    payment = request.form['payment']
    if event != '' and name != '' and id_table != '' and num_photo != '' and num_6x9 != '' and num_8x12 != ''  and cost != '' and payment != '':
        if int(id_table) <= 125:
            if not (int(payment) > int(cost)):
                cur = sql.connection.cursor()
                consult_sql = """UPDATE {0} SET  
                name='{1}',
                id_table='{2}',
                num_photo='{3}',
                _6x9='{4}',
                _8x12='{5}',
                cost='{6}',
                payment='{7}' 
                WHERE id = '{8}'"""
                cur.execute(consult_sql.format(event,name,id_table,num_photo,num_6x9,num_8x12, cost, payment, id))
                cur.close()
                flash('Cliente actualizado correctamente', 'alert-success')
            else:
                flash('El pago exede el costo del paquete', 'alert-warning')

# function search_client > form_client_grd
@graduaciones.route('/search_client/<event>', methods = ['GET'])
def search_client(event):
    search = request.args.get('text')
    print(search)
    if search != '':
        cur = sql.connection.cursor()
        consult_sql = " SELECT * FROM {0} WHERE name LIKE '%{1}%' OR id_table = '{1}' OR num_photo = '{1}'  "
        cur.execute(consult_sql.format(event, search))
        data = cur.fetchall()
        cur.close()
    else:
        cur = sql.connection.cursor()
        consult_sql = " SELECT * FROM {0}"
        cur.execute(consult_sql.format(event))
        data = cur.fetchall()
        cur.close()
    return jsonify(data)
    return redirect(url_for('graduaciones.form_graduaciones', event = event))