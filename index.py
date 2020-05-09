from flask import Flask, render_template, request, flash, session, redirect, url_for
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
        consult_sql = 'SELECT * FROM {0} WHERE 1'
        cur.execute(consult_sql.format(table))
        data = cur.fetchall()
        cur.close()
        return render_template('form_clients_grd.html', event = table, data = data)
    else:
        return redirect(url_for('homepage'))
    return render_template('form_clients_grd.html')

# function add_client > form_clients-grd
@app.route('/add_client', methods = ['POST'])
def add_client():
    seller = (session['name']).upper()
    event = request.form['event_selected']
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
                flash('Cliente registrado correctamente')
            else:
                flash('El pago registrado es mayor al costo')
        else:
            flash('Número de mesa demasiado grande')
    else:
        flash('No se han registrado todos los datos')
    return redirect(url_for('form_clients_grd', event = event))

# function delete_client > form_clients_grd
@app.route('/delete_client/<event>/<id>')
def delete_client(event, id):
    cur = sql.connection.cursor()
    consult_sql = 'DELETE FROM {0} WHERE id={1}'
    cur.execute(consult_sql.format(event,id))
    cur.close()
    return redirect(url_for('form_clients_grd', event = event))
    
# function edit_client > form_clients_grd
@app.route('/edit_client/<event>/<id>')
def edit_client(event, id):
    cur = sql.connection.cursor()
    consult_sql = 'SELECT * FROM {0} WHERE id={1}'
    cur.execute(consult_sql.format(event,id))
    data = cur.fetchall()
    return render_template('edit_client_grd.html', data = data[0], event = event)

# function update_client > edit_client_grd 
@app.route('/update_client/<event>/<id>', methods = ['POST'])
def update_client(event, id):
    event = request.form['event_selected']
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
                flash('Cliente actualizado correctamente')
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
                if not (data_user[3] == adress or data_user[1] == username or data_user[2] == lastnames):
                    cur = sql.connection.cursor()
                    consult_sql = """INSERT INTO  users(id,username,lastnames,adress,pass,level) VALUES (NULL,%s,%s,%s,%s,%s)"""
                    cur.execute(consult_sql,(username,lastnames,adress,password,level))
                    cur.close()
                    flash('Usuario creado satisfactoriamente')
                else:
                    flash('Este usuario ya ha sido creado')
            else:
                flash('No has llenado todos los campos, intentalo de nuevo')
        return render_template('register_members.html')
    else:
        return redirect(url_for('homepage'))
    return render_template('register_members.html')

# run server
if __name__ == "__main__":
    app.run(port = "3000", debug = True)
