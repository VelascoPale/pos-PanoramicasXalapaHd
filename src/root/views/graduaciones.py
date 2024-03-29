from flask import Blueprint, render_template, redirect, url_for, session, jsonify, flash, request

from sqlalchemy import asc, desc

from ..models import db
from ..models.order_graduation import OrderGraduation
from ..schemas.order_graduation import order_graduation_schema, orders_graduations_schema

from ..models.client import Client
from ..schemas.client import client_schema, clients_schema

from ..models.event import Event
from ..schemas.event import event_schema

graduaciones = Blueprint("graduaciones",__name__, url_prefix='/dashboard/event')

def get_orders(data):
            orders = []
            for order in data:
                search_order = {
                    'idSeller': order[0].idSeller,
                    'idEvent': order[0].idEvent,
                    'idClient': order[0].idClient,
                    'idOrderGraduation': order[0].idOrderGraduation,
                    'name': order[1].name,
                    'lastname': order[1].lastname,
                    'numTable': order[0].numTable,
                    'numPhoto': order[0].numPhoto,
                    '_6x9': order[0]._6x9,
                    '_8x12': order[0]._8x12,
                    'cost': order[0].cost,
                    'payment': order[0].payment,
                    'status': order[0].status
                }
                orders.append(search_order)
            return orders

# form_client_grd page
@graduaciones.route('/form')
@graduaciones.route('/form/<int:page>')
def form_graduaciones(page=1):
    if 'name' in session:
        event = request.args.get('event').split(',')
        idschool = Event.query.filter_by(idEvent=event[1]).first()
        clients = Client.get_clients_per_page(page, idschool.idSchool)
        orders = OrderGraduation.get_orders_per_page(page, event[1])
        return render_template('form_graduaciones.html', event = event, orders = orders, clients=clients, page=page)
    else:
        return redirect(url_for('login.page_login'))
    return render_template('form_graduaciones.html')

@graduaciones.route('/form/<event>/<category>', methods=['GET'])
def filter_seller(event, category):
    if 'name' in session:
        if category == 'my':
            orders = OrderGraduation.query.filter_by(idEvent=event ,idSeller = session['id']).all()
        else:
            orders = OrderGraduation.query.filter_by(idEvent=event).all()
        return jsonify(orders_graduations_schema.dump(orders))

# function add_client
@graduaciones.route('/form', methods = ['POST'])
def add_client():
    id_seller = request.form['idSeller']
    id_client = int(request.form['idClient'])
    id_event = int(request.form['idEvent'])
    name = (request.form['name']).upper()
    lastname = (request.form['lastname']).upper()
    id_table = request.form['id_table']
    num_photo = (request.form['num_photo']).upper()
    num_6x9 = request.form['num_6x9']
    num_8x12 = request.form['num_8x12']
    cost = request.form['cost']
    payment = request.form['payment']
    status = 'En_proceso'
    school = Event.query.get(id_event)
    if id_seller != '' and name != '' and lastname != '' and id_table != '' and num_photo != '' and num_6x9 != '' and num_8x12 != ''  and cost != '' and payment != '':
        if int(id_table) <= 125:
            if not int(payment) > int(cost):
                if id_client > 0:
                    new_order = OrderGraduation(idClient=id_client, idSeller=id_seller, idEvent=id_event, numTable=id_table, numPhoto=num_photo,_6x9=num_6x9,_8x12=num_8x12, cost=cost, payment=payment, status=status)
                    db.session.add(new_order)
                    db.session.commit()
                    alert = {
                        'text':'Pedido realizado correctamente',
                        'type':'alert-success'
                    }
                elif id_client == 0:
                    new_client= Client(name=name, lastname=lastname,telephone='GRADUATION',email='GRADUATION',idSchool=school.idSchool,group='')
                    db.session.add(new_client)
                    db.session.commit()
                    client = Client.query.filter_by(name=name, lastname=lastname).first()
                    new_order = OrderGraduation(idClient=client.idClient, idSeller=id_seller, idEvent=id_event, numTable=id_table, numPhoto=num_photo,_6x9=num_6x9,_8x12=num_8x12, cost=cost, payment=payment, status=status)
                    db.session.add(new_order)
                    db.session.commit()
                    alert = {
                    'text':'Usuario y pedido registrados',
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
    clients = Client.query.filter_by(idSchool=school.idSchool).all()
    orders = OrderGraduation.query.filter_by(idEvent=id_event).all()
    return jsonify(alert,clients_schema.dump(clients), orders_graduations_schema.dump(orders))
    
# function update_client 
@graduaciones.route('/form', methods = ['PATCH'])
def update_client():
    id_event = request.form['idEventEdit']
    id_order = request.form['idOrderEdit']
    id_table = request.form['id_tableEdit']
    num_photo = (request.form['num_photoEdit']).upper()
    num_6x9 = request.form['num_6x9Edit']
    num_8x12 = request.form['num_8x12Edit']
    cost = request.form['costEdit']
    payment = request.form['paymentEdit']
    status = request.form['statusEdit']
    if id_table != '' and num_photo != '' and num_6x9 != '' and num_8x12 != ''  and cost != '' and payment != '':
        if int(id_table) <= 125:
            if not int(payment) > int(cost):
                edit_order = OrderGraduation.query.filter_by(idOrderGraduation = id_order).first()
                if edit_order.idSeller == session['id']:
                    edit_order.numTable = id_table
                    edit_order.numPhoto = num_photo
                    edit_order._6x9 = num_6x9
                    edit_order._8x12 = num_8x12
                    edit_order.cost = cost
                    edit_order.payment = payment
                    edit_order.status = status
                    db.session.commit()
                    alert = {
                        'text':'Edicion realizada correctamente',
                        'type':'alert-success'
                    }
                else:
                    alert = {
                        'text':'Esta venta no te pertenece',
                        'type':'alert-warning'
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
                    'text':'No se han registrado todos los datos editar',
                    'type':'alert-warning'
        }
    orders = OrderGraduation.query.filter_by(idEvent=id_event).all()
    return jsonify(alert, orders_graduations_schema.dump(orders))

#function to find clients with them names
@graduaciones.route('/form/search', methods=['GET'])
def search_client():
    if 'name' in session:
        tag = request.args.get('name')
        event = request.args.get('event')
        school = (Event.query.get(event)).idSchool  
        if tag != '':
            search = "{}%".format(tag)
            search_client = Client.query.filter_by(idSchool = school).filter(Client.name.like(search)).all()
            result = db.session.query(OrderGraduation, Client).outerjoin(Client, OrderGraduation.idClient == Client.idClient).filter(Client.name.like(search)).all()
            orders = get_orders(result)
        else:
            search_client = Client.query.filter_by(idSchool = school).all()
            result = db.session.query(OrderGraduation, Client).outerjoin(Client, OrderGraduation.idClient == Client.idClient).all()
            orders = get_orders(result) 
        return jsonify(clients_schema.dump(search_client), orders)
