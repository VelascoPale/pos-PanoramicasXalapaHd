from flask import Blueprint, session, render_template, redirect, url_for, request
from flask_mysqldb import MySQL

dashboard = Blueprint("dashboard",__name__)
 
sql = MySQL()
# dashboard page
@dashboard.route('/dashboard')
def render_dashboard():
    if 'name' in session:
        level = session['permissions']
        return render_template('dashboard.html', level = level, username= session['name'])
    else:
        return redirect(url_for('login.page_login'))
    return render_template('dashboard.html', level = level)
