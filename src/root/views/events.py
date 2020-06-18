from flask import Blueprint, render_template, redirect, url_for, session, request
from datetime import timedelta, datetime
from flask_mysqldb import MySQL

events = Blueprint("events",__name__, url_prefix='/graduaciones')
sql = MySQL()

# graduaciones page
@events.route('/')
def graduaciones():
    if 'name' in session:
        cur = sql.connection.cursor()
        consult_sql = 'SHOW FULL TABLES FROM regis_clients_pano LIKE "grd_%"'
        cur.execute(consult_sql)
        events = cur.fetchall()
        cur.close()
        return render_template('graduaciones.html', places = events)
    else:
        return redirect(url_for('login.page_login'))
    return render_template('graduaciones.html')

# function add_event > graduaciones
@events.route('/add_event', methods = ['POST'])
def add_event():
    event_hall = request.form['event_hall']
    school_name = request.form['school_name']
    year = str(datetime.now().year)
    name_table = ('grd' + "_" + school_name + "_" + event_hall + "_" + year).lower()
    #cur = sql.connection.cursor()
    #consult_sql = """
    #CREATE TABLE IF NOT EXISTS {0}(
        #id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
        #name VARCHAR(50),
        #id_table TINYINT,
        #num_photo VARCHAR(10), 
        #_6x9 TINYINT,
        #_8x12 TINYINT,
        #cost SMALLINT,
        #payment SMALLINT,
        #seller VARCHAR(50)
        #)"""
    #cur.execute(consult_sql.format(name_table))
    #cur.close()
    return redirect(url_for('events.graduaciones'))

# function go_event > graduados
@events.route('/go_event', methods = ['POST'])
def go_event(): 
    # get table from graduaciones to send form_graduaciones
    table = request.form['event_selected']
    return redirect(url_for('graduaciones.form_graduaciones', event = table))