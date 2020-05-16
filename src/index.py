
from flask import Flask, render_template, request, flash, session, redirect, url_for, jsonify
from flask_mysqldb import MySQL
from datetime import timedelta, datetime
import bcrypt

app = Flask(__name__)
# app.permanent_session_lifetime = timedelta(minutes = 30)  # close session after 15 minutes

# key-secret
app.secret_key = 'panosTeamXALAPA'

# salt for encrypt
salt = bcrypt.gensalt()

# config_mysql
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'regis_clients_pano'
sql = MySQL(app)

# home page
@app.route('/')
def homepage():
    if 'name' in session:
        return redirect(url_for('dashboard'))
    else:
        return render_template('index.html')
    return render_template('index.html')

# user_login page and function
@app.route('/login', methods = ['POST'])
def login():
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
                return redirect(url_for('dashboard'))
            else:
                flash("Contraseña incorrecta, intentalo de nuevo")
                return redirect(url_for('homepage'))
        else:
            flash("Correo incorrecto, intentalo de nuevo")
            return redirect(url_for('homepage'))
    else:
        if 'name' in session:
            return redirect(url_for('dashboard'))
        else:
            return redirect(url_for('homepage'))

# function exit > all
@app.route('/close')
def close():
    session.clear()
    return redirect(url_for('homepage'))

# dashboard page
@app.route('/dashboard')
def dashboard():
    if 'name' in session:
        return render_template('dashboard.html')
    else:
        return redirect(url_for('homepage'))
    return render_template('dashboard.html')

# escuelas page
@app.route('/escuelas')
def escuelas():
    if 'name' in session:
        return render_template('escuelas.html')
    else:
        return redirect(url_for('homepage'))
    return render_template('escuelas.html')

# graduaciones page
@app.route('/graduaciones')
def graduaciones():
    if 'name' in session:
        cur = sql.connection.cursor()
        consult_sql = 'SHOW FULL TABLES FROM regis_clients_pano LIKE "grd_%"'
        cur.execute(consult_sql)
        events = cur.fetchall()
        cur.close()
        return render_template('graduaciones.html', places = events)
    else:
        return redirect(url_for('homepage'))
    return render_template('graduaciones.html')

# function add_event > graduaciones
@app.route('/add_event', methods = ['POST'])
def add_event():
    event_hall = request.form['event_hall']
    school_name = request.form['school_name']
    year = str(datetime.now().year)
    name_table = ('grd' + "_" + school_name + "_" + event_hall + "_" + year).lower()
    cur = sql.connection.cursor()
    consult_sql = """
    CREATE TABLE IF NOT EXISTS {0}(
        id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
        name VARCHAR(50),
        id_table TINYINT,
        num_photo VARCHAR(10), 
        6x9 TINYINT,
        8x12 TINYINT,
        cost SMALLINT,
        payment SMALLINT,
        seller VARCHAR(50)
        )"""
    cur.execute(consult_sql.format(name_table))
    cur.close()
    return redirect(url_for('graduaciones'))

# function go_event > graduados
@app.route('/go_event', methods = ['POST'])
def go_event(): 
    # get table from graduaciones to send form_clients_grd
    table = request.form['event_selected']
    return redirect(url_for('form_clients_grd', event = table))

# form_client_grd page
@app.route('/form_clients_grd')
def form_clients_grd():
    if 'name' in session:
        table = request.args.get('event')
        cur = sql.connection.cursor()
        consult_sql =  " SELECT * FROM {0} WHERE 1 "
        cur.execute(consult_sql.format(table))
        data = cur.fetchall()
        cur.close()
        return render_template('form_clients_grd.html', event = table, data = data)
    else:
        return redirect(url_for('homepage'))
    return render_template('form_clients_grd.html')

# function search_client > form_client_grd
@app.route('/search_client/<event>', methods = ['GET'])
def search_client(event):
    search = request.args.get('text')
    print(search)
    cur = sql.connection.cursor()
    consult_sql = " SELECT * FROM {0} WHERE name LIKE '%{1}%' "
    cur.execute(consult_sql.format(event,search))
    data_uno = cur.fetchall()
    cur.close()
    print(data_uno)
    return jsonify(event = search,data_uno = data_uno)



# function add_client > form_clients-grd
@app.route('/add_client/<event>', methods = ['POST'])
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
                consult_sql = """INSERT INTO {0}(`id`, `name`, `id_table`, `num_photo`, `6x9`, `8x12`, `cost`, `payment`, `seller`) 
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
    return redirect(url_for('form_clients_grd', event = event))

# function delete_client > form_clients_grd
@app.route('/delete_client/<event>/<id>', methods = ['POST'])
def delete_client(event, id):
    cur = sql.connection.cursor()
    consult_sql = 'DELETE FROM {0} WHERE id={1}'
    cur.execute(consult_sql.format(event,id))
    cur.close()
    flash('Cliente eliminado satisfactoriamente', 'alert-success')
    return redirect(url_for('form_clients_grd', event = event))
    
# function update_client > edit_client_grd 
@app.route('/update_client/<event>/<id>', methods = ['POST'])
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
                6x9='{4}',
                8x12='{5}',
                cost='{6}',
                payment='{7}' 
                WHERE id = '{8}'"""
                cur.execute(consult_sql.format(event,name,id_table,num_photo,num_6x9,num_8x12, cost, payment, id))
                cur.close()
                flash('Cliente actualizado correctamente', 'alert-success')
            else:
                flash('El pago exede el costo del paquete', 'alert-warning')
    return redirect(url_for('form_clients_grd', event = event))

# function register_members
@app.route('/register_members', methods=['POST','GET'])
def register_members():
    if 'name' in session:
        if request.method == 'POST':
            username = (request.form['username']).upper()
            lastnames = (request.form['lastnames']).upper()
            adress = (request.form['adress']).lower()
            password = request.form['password'].encode('utf-8')
            level = 'SELLER'
            password = bcrypt.hashpw(password,salt)
            if username != '' and lastnames != '' and adress != '' and password != '':
                cur = sql.connection.cursor()
                consult_sql = """SELECT * FROM users WHERE adress='{0}' OR username='{1}' OR lastnames='{2}'"""
                cur.execute(consult_sql.format(adress, username, lastnames))
                data_user = cur.fetchone()
                print(data_user)
                if data_user:
                    flash('Este usuario ya ha sido creado', 'alert-danger')
                else:
                    cur = sql.connection.cursor()
                    consult_sql = """INSERT INTO  users(id,username,lastnames,adress,pass,level) VALUES (NULL,%s,%s,%s,%s,%s)"""
                    cur.execute(consult_sql,(username,lastnames,adress,password,level))
                    cur.close()
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
        return redirect(url_for('homepage'))
    return render_template('register_members.html')

# function add_members > register member
@app.route('/update_member/<id>', methods = ['POST'])
def update_member(id):
    username = (request.form['username']).upper()
    lastnames = (request.form['lastname']).upper()
    adress = (request.form['adress']).lower()
    password = request.form['password']
    level = request.form['level']
    cur = sql.connection.cursor()
    if not password == '':
        password = password.encode('utf-8')
        password = bcrypt.hashpw(password,salt)
        consult_sql = """UPDATE users SET 
        username=%s,
        lastnames=%s,
        adress=%s,
        pass=%s,
        level=%s
        WHERE id = %s"""
        cur.execute(consult_sql,(username, lastnames, adress, password, level, id))
        cur.close()
    else:
        consult_sql = """UPDATE users SET 
        username='{1}',
        lastnames='{2}',
        adress='{3}',
        level='{5}'
        WHERE id = {0}"""
        cur.execute(consult_sql.format(id, username,lastnames,adress,password,level))
        cur.close()
    flash('Usuario actualizado satisfactoriamente', 'alert-success')
    return redirect(url_for('register_members'))

# function delete_member > register_member
@app.route('/delete_member/<id>', methods = ['POST'])
def delete_member(id):
    cur = sql.connection.cursor()
    consult_sql = """ DELETE FROM users WHERE id= %s """
    cur.execute(consult_sql, [id])
    cur.close()
    flash('Usuario eliminado satisfactoriamente', 'alert-success')
    return redirect(url_for('register_members'))

# run server
if __name__ == "__main__":
    app.run(port = "3000", debug = True)

