from flask import Blueprint, session, render_template, redirect, url_for, request
from flask_mysqldb import MySQL

dashboard = Blueprint("dashboard",__name__)

from ..models.event import Event
from ..schemas.event import event_schema, events_schema
 
sql = MySQL()
# dashboard page
@dashboard.route('/dashboard')
def render_dashboard():
    if 'name' in session:
        events = Event.query.order_by(Event.idEvent).all()
        return render_template('dashboard.html', events=events)
    else:
        return redirect(url_for('login.login_page'))
