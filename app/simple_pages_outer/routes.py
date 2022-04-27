from crypt import methods
from fileinput import filelineno
from flask import Blueprint, render_template, redirect, url_for, send_file, request, current_app
from app.models.orders import Foto, Order
from app.users.models import User
from app.extensions.database import db
from app.extensions.database import CRUDMixin
from flask_login import current_user, login_required


blueprint = Blueprint('simple_pages', __name__)

@blueprint.route('/')
def index(): 
    return render_template('simple_pages/index.html')

""" NAV BAR """

@blueprint.route('/street')
def street(): 
    all_fotos = Foto.query.filter_by(genre='street')
    return render_template('simple_pages/street.html', fotos = all_fotos)

@blueprint.route('/portrait')
def portrait(): 
    all_fotos = Foto.query.filter_by(genre='portrait')
    return render_template('simple_pages/portrait.html', fotos = all_fotos)

@blueprint.route('/orders')
@login_required
def orders(): 
    orders = current_user.orders
    return render_template('simple_pages/orders.html', orders = orders )

""" Special routes """

@blueprint.route('/street/<name>', methods=['GET', 'POST'])
@blueprint.route('/portrait/<name>', methods=['GET', 'POST'])
def ind(name):
    fotos = Foto.query.filter_by(name=name).first()

    if request.method =='POST': 

        # Create an order 
        order = Order(
            street = request.form.get('fstreet'), 
            city = request.form.get('fcity'),
            zip = request.form.get('fzip'),
            country = request.form.get('fcountry'),
            foto_id = request.form.get('ffoto_id'), 
            user_id = request.form.get('fuser'), 
        )
        order.save()
        
        return redirect(url_for('simple_pages.orders'))

    return render_template('simple_pages/ind.html', fotos=fotos)
