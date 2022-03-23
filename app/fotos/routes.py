from flask import Blueprint, render_template

blueprint = Blueprint('fotos', __name__)

fotos_data = {
    "rome" : {"name": " Old man in rome ", "price": "$50"}, 
    "quito" : {"name": "Hija con su hija ", "price": "$45"}
}

@blueprint.route('/shop')
def shop(): 
    return render_template('shop/index.html', fotos = fotos_data)

@blueprint.route('/shop/<slug>') # aqui borre el  -> methods = ['GET']
def ind(slug): 
    
    return render_template('/shop/ind.html', fotos = fotos_data[slug])
