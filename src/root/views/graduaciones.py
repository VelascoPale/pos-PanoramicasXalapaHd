from flask import Blueprint, render_template, redirect, url_for, session, jsonify, flash, request
from flask_mysqldb import MySQL

graduaciones = Blueprint("graduaciones",__name__)
sql = MySQL()

# form_client_grd page
@graduaciones.route('/form_graduaciones')
def form_graduaciones():
    if 'name' in session:
        table = request.args.get('event')
        cur = sql.connection.cursor()
        consult_sql =  " SELECT * FROM {0} WHERE 1 "
        cur.execute(consult_sql.format(table))
        data = cur.fetchall()
        cur.close()
        return render_template('form_graduaciones.html', event = table, data = data)
    else:
        return redirect(url_for('login.page_login'))
    return render_template('form_graduaciones.html')

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

# function add_client > form_clients-grd
@graduaciones.route('/add_client/<event>', methods = ['POST'])
def add_client(event):
    seller = (session['name']).upper()
    name = (request.form['name']).upper()
    id_table = request.form['id_table']
    num_photo = (request.form['num_photo']).upper()
    num_6x9 = request.form['num_6x9']
    num_8x12 = request.form['num_8x12']
    cost = request.form['cost']
    payment = request.form['payment']
    if event != '' and name != '' and id_table != '' and num_photo != '' and num_6x9 != '' and num_8x12 != ''  and cost != '' and payment != '':
        if int(id_table) <= 125:
            if not int(payment) > int(cost):
                cur = sql.connection.cursor()
                consult_sql = """INSERT INTO {0}(`id`, `name`, `id_table`, `num_photo`, `_6x9`, `_8x12`, `cost`, `payment`, `seller`) 
                VALUES (NULL,'{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}')"""
                cur.execute(consult_sql.format(event,name,id_table,num_photo,num_6x9,num_8x12, cost, payment,seller))
                cur.close()
                flash('Cliente registrado correctamente', 'alert-success')
            else:
                flash('El pago registrado es mayor al costo', 'alert-warning')
        else:
            flash('Número de mesa demasiado grande', 'alert-warning')
    else:
        flash('No se han registrado todos los datos', 'alert-warning')
    return redirect(url_for('graduaciones.form_graduaciones', event = event))

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
    return redirect(url_for('graduaciones.form_graduaciones', event = event))