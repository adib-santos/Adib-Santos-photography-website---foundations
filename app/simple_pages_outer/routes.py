from fileinput import filelineno
from flask import Blueprint, render_template, redirect, url_for, send_file, request, current_app
from app.models.orders import Foto, Order, Address


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
    fotos = Foto.query.all()
    print(request.form)

    return render_template('simple_pages/new.html', fotos=fotos)

@blueprint.route('/street/<slug>')
@blueprint.route('/portrait/<slug>')
def ind(slug):
    fotos = Foto.query.filter_by(slug=slug).first()
    return render_template('simple_pages/ind.html', fotos=fotos)



