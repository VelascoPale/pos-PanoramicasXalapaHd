from flask import Blueprint, render_template, session, redirect, url_for, request, jsonify, flash, current_app
from flask_mail import Message, Mail

from ..models.client import Client
from ..models.school import School

from ..schemas.client import client_schema, clients_schema
from ..schemas.school import school_schema, schools_schema

emails = Blueprint("emails",__name__, url_prefix="/dashboard/emails")

mail = Mail()

@emails.route('/')
@emails.route('/<int:page>')
def render_emails(page=1):
    if 'name' in session:
        clients = Client.get_clients_page_email(page)
        schools = School.query.order_by(School.idSchool).all()
        return render_template('emails.html', schools = schools, clients=clients, page=page)
    else:
        return redirect(url_for('login.page_login'))
    return render_template('emails.html')

@emails.route('/structure', methods=['POST'])
@emails.route('/structure/<int:page>')
def prepare_emails(page=1):
    id_school = request.form['idSchool']
    group = request.form['group']
    asunt = request.form['asunt']
    text = request.form['text']
    title = request.form['title']
    data = {'asunto':asunt,
            'texto':text,
            'escuela':id_school,
            'grupo':group,
            'titulo':title}
    schools = School.query.order_by(School.idSchool).all()
    if group != 'Z':
        clients = Client.query.filter(Client.idSchool==id_school, Client.group==group,Client.email != 'GRADUATION').all()
    else:
        clients = Client.query.filter(Client.idSchool==id_school, Client.email != 'GRADUATION').all()
    flash('Verificar cuerpo del mensaje y destinatarios','alert-warning')
    return render_template('preview.html', schools = schools, clients=clients, page=page, data=data, text=text, title=title)

@emails.route('/structure/confirm', methods=['POST'])
def send_emails():
    print(request.form)
    id_school = request.form['idSchool']
    group = request.form['group']
    asunt = request.form['asunt']
    text = request.form['text']
    title = request.form['title']

    if group != 'Z':
        emails = Client.query.filter(Client.idSchool==id_school, Client.group==group,Client.email != 'GRADUATION').with_entities(Client.email).all()
    else:
        emails = Client.query.filter(Client.idSchool==id_school, Client.email != 'GRADUATION').with_entities(Client.email).all()

    recipients = []
    for email in emails:
        recipients.append(email[0])

    with mail.connect() as conn:
        for recipient in recipients:
            msg = Message(asunt,
                          sender = ('Panoramicas Xalapa HD',current_app.config['MAIL_USERNAME']),
                          recipients = [recipient])
            msg.html = render_template('email_confirmed.html', text=text, title= title)
            mail.send(msg)

    flash('Correos enviados satisfactoriamnete','alert-success')
    return redirect(url_for('emails.render_emails'))

@emails.route('/ver')
def ver():
    return render_template('email_confirmed.html')
