from flask import Blueprint, session, render_template, redirect, url_for, request, flash

from ..models.event import Event
from ..schemas.event import event_schema, events_schema

dashboard = Blueprint("dashboard",__name__)


# dashboard page
@dashboard.route('/dashboard')
def render_dashboard():
    if 'name' in session:
        events = Event.query.order_by(Event.idEvent).all()
        return render_template('dashboard.html', events=events)
    else:
        return redirect(url_for('login.page_login'))

@dashboard.route('/dashboard/event', methods=['POST'])
def select_event():
    event = request.form['event']
    if event != '#':
        return redirect(url_for('graduaciones.form_graduaciones', event=event))
    else:
        flash('Selecciona un evento valido', 'alert-warning')
        return redirect(url_for('dashboard.render_dashboard'))
