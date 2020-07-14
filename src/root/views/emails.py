from flask import Blueprint, render_template, session, redirect, url_for

from ..models.client import Client
from ..models.school import School

emails = Blueprint("emails",__name__, url_prefix="/dashboard/emails")

@emails.route('/')
@emails.route('/<int:page>')
def render_emails(page=1):
    if 'name' in session:
        clients = Client.get_clients_per_page(page)
        schools = School.query.order_by(School.idSchool).all()
        return render_template('emails.html', schools = schools, clients=clients, page=page)
    else:
        return redirect(url_for('login.page_login'))
    return render_template('emails.html')