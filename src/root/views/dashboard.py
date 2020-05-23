from flask import Blueprint, session, render_template, redirect, url_for

dashboard = Blueprint("dashboard",__name__)
 
# dashboard page
@dashboard.route('/dashboard')
def render_dashboard():
    if 'name' in session:
        level = session['level']
        return render_template('dashboard.html', level = level, username= session['name'])
    else:
        return redirect(url_for('login.page_login'))
    return render_template('dashboard.html', level = level)