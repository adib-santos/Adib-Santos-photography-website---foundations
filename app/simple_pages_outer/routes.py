from fileinput import filelineno
from flask import Blueprint, render_template, redirect, url_for, send_file, request, current_app
from app.models.orders import Foto, Order


blueprint = Blueprint('simple_pages', __name__)

@blueprint.route('/')
def index(): 
    return render_template('simple_pages/index.html')

@blueprint.route('/receipt.txt')
def receipt(): 
    return send_file('static/downloads/receipt.txt', as_attachment = True)

""" NAV BAR """

@blueprint.route('/about')
def about(): 
    return render_template('simple_pages/about.html')

@blueprint.route('/street')
def street(): 
    all_fotos = Foto.query.all()
    return render_template('simple_pages/street.html', fotos = all_fotos)

@blueprint.route('/portrait')
def portrait(): 
    all_fotos = Foto.query.all()
    return render_template('simple_pages/portrait.html', fotos = all_fotos)


""" Special routes """

@blueprint.get('/checkout')
def get_checkout():
    fotos = Foto.query.all()

    return render_template('simple_pages/new.html', fotos = fotos)

@blueprint.post('/checkout')
def post_checkout():

    # Create an order 
    order = Order(
        street=request.form.get('street'),
        city=request.form.get('city'),
        zip=request.form.get('zip'),
        country=request.form.get('country'),
        foto_id = request.form.get('foto_id')
        
      )


    fotos = Foto.query.all()
    return render_template('simple_pages/new.html', fotos=fotos)

@blueprint.route('/street/<name>')
@blueprint.route('/portrait/<name>')
def ind(name):
    fotos = Foto.query.filter_by(name=name).first()
    return render_template('simple_pages/ind.html', fotos=fotos)



