from flask import Blueprint, render_template
from .models import Foto

blueprint = Blueprint('fotos', __name__)

#fotos_data = {
 #  "rome" : {"name": " Old man in rome ", "price": "$50", "image": "/static/images/selfie.jpg"}, 
  #  "quito" : {"name": "Hija con su hija ", "price": "$45", "image": "/static/images/reflection-rome.jpg"}
#}

@blueprint.route('/shop')
def shop(): 
    return render_template('shop/index.html', fotos = fotos_data)

@blueprint.route('/shop/<slug>') # aqui borre el  -> methods = ['GET']
def ind(slug): 
    
    return render_template('/shop/ind.html', fotos = fotos_data[slug])
