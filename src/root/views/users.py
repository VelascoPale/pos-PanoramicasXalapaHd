from flask import Blueprint, session, request, url_for, flash, render_template, redirect
from flask_mysqldb import MySQL
import bcrypt

users = Blueprint("users",__name__)
salt = bcrypt.gensalt()
sql = MySQL()


# function register_members
@users.route('/register_members', methods=['POST','GET'])
def register_members():
    if 'name' in session and session['level'] == 'ADMIN':
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
        return redirect(url_for('login.page_login'))
    return render_template('register_members.html')

# function add_members > register member
@users.route('/update_member/<id>', methods = ['POST'])
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
    return redirect(url_for('users.register_members'))

# function delete_member > register_member
@users.route('/delete_member/<id>', methods = ['POST'])
def delete_member(id):
    cur = sql.connection.cursor()
    consult_sql = """ DELETE FROM users WHERE id= %s """
    cur.execute(consult_sql, [id])
    cur.close()
    flash('Usuario eliminado satisfactoriamente', 'alert-success')
    return redirect(url_for('users.register_members'))
