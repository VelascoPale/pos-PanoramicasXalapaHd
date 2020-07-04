from flask import Blueprint, session, render_template, redirect, url_for

escuelas = Blueprint("escuelas",__name__)

# escuelas page
@escuelas.route('/escuelas')
def render_escuelas():
    if 'name' in session:
        return render_template('escuelas.html')
    else:
        return redirect(url_for('login.page_login'))
    return render_template('escuelas.html')