from flask import Blueprint, render_template
from . models import Foto

blueprint = Blueprint('fotos', __name__)

@blueprint.route('/shop')
def shop():
    all_fotos = Foto.query.all() 
    return render_template('shop/index.html', fotos = all_fotos)

@blueprint.route('/shop/<slug>') 
def ind(slug): 
    foto = Foto.query.filter_by(slug=slug).first_or_404()    
    return render_template('/shop/ind.html', foto = foto)
