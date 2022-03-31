from flask import Blueprint, render_template
from . models import Foto

blueprint = Blueprint('fotos', __name__)

@blueprint.route('/shop')
def shop():
    all_fotos = Foto.query.all() 
    return render_template('shop/index.html', fotos = all_fotos)

@blueprint.route('/shop/<slug>', methods = ['GET']) # aqui borre el  -> methods = ['GET']
def ind(slug): 

    all_fotos = Foto.query.all(id) # Read the querry one part to solve this
    print(id)
    print(all_fotos)

    return render_template('/shop/ind.html', fotos = all_fotos[slug])
